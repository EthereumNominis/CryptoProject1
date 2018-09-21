# crypto1
DONT USE CBCenc.py, this file is old. Delete it if you want. Use Part1_encryption.py




## Structure

```json
.
├── Cipher_CBC.py
├── Cipher_CTR.py
├── README.md
├── baseCipher.py
├── cbc-dec.py        {# Question 1}
├── cbc-enc.py        {# Question 1}
├── ctr-dec.py        {# Question 1}
├── ctr-enc.py        {# Question 1}
├── dataFiles
│   ├── ctrO1
│   ├── ctrO2
│   ├── ffFF
│   ├── k2c
│   ├── l2.txt
│   ├── l3.txt
│   ├── l4.txt
│   ├── longPlainText.txt
│   ├── lyy
│   ├── myo
│   ├── myy
│   ├── nnnnnk2cplain.txt
│   ├── out
│   ├── plain1.txt
│   ├── plain2byENC.txt
│   ├── plainFULL.txt
│   └── plainFULLNULL.txt
├── requirements.txt
└── temp
    ├── keyFile1
    ├── keyFile2
    ├── testFile1
    ├── testFile2
    └── testFile3
```







# CBC-MAC

```bash
python3 cbcmac-tag.py -k temp/keyFile2 -m dataFiles/file20Kb.txt -t dataFiles/tag2
Key file:	 temp/keyFile2
Message file:	 dataFiles/file20Kb.txt
Tag file:	 dataFiles/tag2
 Successfully loaded key (Hex)	  '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
 Successfully loaded plain text file
 Successfully generated tag for the message	  28cdddb038b86d46301febbc412a72f3
```

```bash
python3 cbcmac-validate.py -k temp/keyFile2 -m dataFiles/file200.txt -t dataFiles/tag2
Key file:	 temp/keyFile2
Message file:	 dataFiles/file200.txt
Tag file:	 dataFiles/tag2
 Successfully loaded key (Hex)	  '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
 Successfully loaded message file
 Successfully loaded tag (Hex)	  28cdddb038b86d46301febbc412a72f3



			 ----------------------------------------


			  FALSE tag for the input message!


			 ----------------------------------------
```


```bash
python3 cbcmac-validate.py -k temp/keyFile2 -m dataFiles/file20Kb.txt -t dataFiles/tag2
Key file:	 temp/keyFile2
Message file:	 dataFiles/file20Kb.txt
Tag file:	 dataFiles/tag2
 Successfully loaded key (Hex)	  '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
 Successfully loaded message file
 Successfully loaded tag (Hex)	  28cdddb038b86d46301febbc412a72f3



			 ----------------------------------------


			  TRUR tag for the input message!


			 ----------------------------------------
```









