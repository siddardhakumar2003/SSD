#!/bin/bash
# Simple tester for log.sh

expected_output="Aaditya   : 2 success, 0 fail
Rohan     : 0 success, 5 fail
Sneha     : 1 success, 0 fail"

student_output=$(bash log.sh 2>/dev/null)

if [[ "$student_output" == *"$expected_output"* ]]; then
    echo "Correct output!"
else
    echo " Incorrect output!"
fi
    echo
    echo "Expected:"
    echo "$expected_output"
    echo
    echo "Got:"
    echo "$student_output"

