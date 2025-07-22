#!/bin/bash

FILE="message.txt"

if [ ! -f "$FILE" ]; then
    zenity --error --text="File '$FILE' not found."
    exit 1
fi

RESULT=""

while IFS= read -r line || [ -n "$line" ]; do
    line=$(echo "$line" | tr -d ' \t\r\n')  

    if [[ "$line" =~ ^[0-9a-fA-F]+$ ]]; then
        mode="hextob64"
    else
        mode="b64tohex"
    fi
    convert=$(python3 converter_base64.py "$mode" "$line")

    RESULT+="Input: $line\nMode: $mode\nResult: $convert\n\n"
done < "$FILE"

zenity --info --title="Conversion results" --text="$RESULT"
