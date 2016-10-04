#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage:" $0 " Testcases_file output_file testcase_result_file"
    exit
fi

if [ -z "$2" ]
  then
    echo "Usage:" $0 " Testcases_file output_file testcase_result_file"
    exit
fi

if [ -z "$3" ]
  then
    echo "Usage:" $0 " Testcases_file output_file testcase_result_file"
    exit
fi

echo $1 $2 $3
MY_PATH="`dirname \"$0\"`"

ROOT_DIR="$PWD/$MY_PATH/"
mkdir -p "$ROOT_DIR/Results_$1"
LOG_PATH="$ROOT_DIR/Results_$1"
echo $ROOT_DIR
TestList="$ROOT_DIR/$1"
echo $TestList
LogFile="$LOG_PATH/$2"
echo $LogFile
ResultFile="$LOG_PATH/$3"
echo $ResultFile
TESTSUITE_DIR="$ROOT_DIR/Mirafra_automation_framework"
echo $TESTSUITE_DIR
cd "$TESTSUITE_DIR"
export PYTHONPATH=$PYTHONPATH:$PWD
stdbuf -oL ./testsuite.py "$TestList" "$ResultFile" |& tee "$LogFile"
cd -
