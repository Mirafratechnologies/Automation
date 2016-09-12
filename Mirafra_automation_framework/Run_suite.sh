#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage:" $0 " Testcases_file output_file\n"
    exit
fi

if [ -z "$2" ]
  then
    echo "Usage:" $0 " Testcases_file output_file\n"
    exit
fi

./testsuite.py $1 |& tee $2
