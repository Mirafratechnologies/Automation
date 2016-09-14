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

export PYTHONPATH=$PYTHONPATH:$PWD

./testsuite.py $1 $3 |& tee $2
