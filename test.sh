#!/bin/bash

for f in $(find . -type f -name "*_test.py"); do
    echo "find test file $f"
    python3 $f -v
done
