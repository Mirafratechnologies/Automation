import unittest
import subprocess
import time
import paramiko		# SSH Support
import os

user = "root"
password = ""
#user = "sunilpatlamane"
#password = "sunilPsharma"
ping = 120
HOST = "192.168.1.232"
port = 22
cmd = ""


class VerifyEth0(unittest.TestCase):
	def setUp(self):
		self.startTime = time.time()
		global ssh
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(HOST, port, user, password)

	def tearDown(self):
		t = time.time() - self.startTime
                print "%s: %.3f %d" % (self.id(), t, self.status)
                f = open("Result.txt", "a")
                f.write("%d\t\t\t %.3f\t\t %s\n" % (self.status, t, self.id()))
                f.close()
		ssh.close()

	def runTest(self):
		cwd = os.getcwd()
		run_script_path = cwd + "/LAN_Verifyeth0/verifyEth0.sh"
		print run_script_path
		fp = open(run_script_path, "r")
		for cmd in fp.readlines():
			print cmd
			stdin, stdout, stderr = ssh.exec_command(cmd)
			ping = stdout.readlines()
			resp=''.join(ping)
			self.status = stdout.channel.recv_exit_status()
	                self.assertEqual(stdout.channel.recv_exit_status(), 0, "Command execution failed")
			print(resp)
		fp.close()

