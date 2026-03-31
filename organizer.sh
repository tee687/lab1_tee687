#!/bin/bash
mkdir -p archive
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
if [ -f "grades.csv" ]; then
    cp grades.csv "archive/grades_$TIMESTAMP.csv"
    echo "Archived grades.csv"
fi
