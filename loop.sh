#!/bin/bash
DIRNAME="נודר נדר"
{
    until [ -e "$DIRNAME" ]; 
    do echo "please create the requested ${DIRNAME} file "
    sleep 8
    done 
    echo "כל הכבוד יערס"
} &


