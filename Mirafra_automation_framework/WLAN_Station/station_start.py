import paramiko
import unittest
import re
import time
import commonData
import os

class StartStation(unittest.TestCase):
        def setUp(self):
		global ssh
		self.startTime = time.time()
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(commonData.Ipaddr, commonData.Port, commonData.User, commonData.Password)

	def tearDown(self):
		t = time.time() - self.startTime
		print "%s: %.3f %d" % (self.id(), t, self.status)
		f = open(commonData.TestcaseResult, "a")
		f.write("%d\t\t\t %.3f\t\t %s\n" % (self.status, t, self.id()))
		f.close()
                ssh.close()

	def runTest(self):
		cwd = os.getcwd()
		run_script_path = cwd + "/WLAN_Station/cli_start.sh"
		print run_script_path
		f = open(run_script_path)
		for line in f.readlines():
                        print line
			stdin,stdout,stderr=ssh.exec_command(line)
			time.sleep(2)
			outlines=stdout.readlines()
			resp=''.join(outlines)
			self.status = stdout.channel.recv_exit_status()
                        self.assertEqual(stdout.channel.recv_exit_status(), 0, "Command execution failed")

			if 'ps -w' in line:
			    if '/usr/sbin/wpa_supplicant' in resp:
				print 'Station is enabled\n'
			    else:
				print 'Station is not enabled'
				break

			if 'wpa_cli status' in line:
			    for str in resp.split('\n'):
				if 'bssid' in str:
				    bssid=re.match(r'bssid=(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))', str)
				elif 'ssid' in str:
				    ssid=re.match(r'ssid=(\w{0,})',str)
                                if 'wpa_state' in str:
				    if 'COMPLETED' in str:
				        print "Station connected to \"%s\" with MAC address: " % ssid.group(1),bssid.group(1)
				    else:
                                        print "Could not connect to AP ",wpa_state
					break
				if 'ip_address' in str:
				    station_ip=re.match(r'ip_address=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str)
				    print "IP address of Station: ",station_ip.group(1)
				    stdin,stdout,stderr=ssh.exec_command('cat /proc/net/arp')
				    outlines=stdout.readlines()
				    arp=''.join(outlines)
				    for str in arp.split('\n'):
					if bssid.group(1) in str:
					    arp_ip=re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',str)
				            if arp_ip:
				                print "IP address of AP: ",arp_ip.group(1)
				                cmd = "ping -c 5 " + arp_ip.group(1)
						print "Ping to AP...\n\n"
				   	        stdin,stdout,stderr=ssh.exec_command(cmd)
 				  	        outlines=stdout.readlines()
 				 	        resp=''.join(outlines)
		              			print(resp)
				 	        self.status = stdout.channel.recv_exit_status()
				 	        if self.status:
				                    print "Connection lost"
						    break
					    break
				
			if 'iwinfo' in line:
			    print "Client statistics:"
			    for str in resp.split('\n'):
				    if 'Channel:' in str:
				        print str
				    if 'Tx-Power:' in str:
				        print str
				    if 'Signal:' in str:
				        print str
				    if 'Bit Rate:' in str:
				        print str
				    if 'Encryption:' in str:
				        print str
				    if 'Type:' in str:
				        print str


		f.close()


