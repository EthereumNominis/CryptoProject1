#!/bin/bash

FILENAME=sherlock_holmes.txt
FILESIZE=$(stat -f%z "$FILENAME")
i=$(echo "obase=16; $FILESIZE" | bc)
printf -v j "%016x" 0x$i
echo $j


openssl enc -e -aes-256-cbc -K 603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4 -iv $j < testdata.txt | tail -c 32 | od

