#!/bin/bash

expected_3="    1 
  1 2 3 
1 2 3 4 5 "
expected_invalid="Invalid input"

# Test valid input
output=$(bash center_pyramid.sh 3)
if [[ "$output" == "$expected_3" ]]; then
    echo "Test 1 Passed (N=3)"
else
    echo "Test 1 Failed"
fi
    echo "Expected:"
    echo "$expected_3"
    echo "Got:"
    echo "$output"

# Test invalid input
output_invalid=$(bash center_pyramid.sh 0)
if [[ "$output_invalid" == "$expected_invalid" ]]; then
    echo "Test 2 Passed (Invalid Input)"
else
    echo "Test 2 Failed"
fi
    echo "Expected: $expected_invalid"
    echo "Got: $output_invalid"

