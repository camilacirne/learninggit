#!/bin/bash

#echo "Arg '$1'"

if [[ -f "$1" && "$1" == *.txt ]]; then
        while IFS= read -r line; do
            if echo "$line" | grep -qE '^[0-9a-fA-F]+$'; then
                echo "$line"
                echo "Seems to be hex"
                python3 main.py 1 "$line"
            elif echo "$line" | grep -qE '^[A-Za-z0-9+/=]+$'; then
                echo "$line"
                echo "Seems to be base64"
                python3 main.py 2 "$line"
            fi
        done < $1      
else
    echo "Pass a file as an arg"
fi