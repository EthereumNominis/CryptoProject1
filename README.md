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
├── cbcmac-tag.py        {# Question 2}
├── cbcmac-validate.py        {# Question 2}
├── dataFiles
│   ├── .......
├── requirements.txt
└── temp
    ├── keyFile1
    ├── keyFile2
    ├── testFile1
    ├── testFile2
    └── testFile3
```




## CBC

```bash
python3 cbc-enc.py -k temp/keyFile2 -i dataFiles/file200.txt -o dataFiles/ll_1
```

```bash
python3 cbc-dec.py -k temp/keyFile2 -i dataFiles/ll_1 -o dataFiles/new_ll_2
```

## CTR

```bash
python3 ctr-enc.py -k temp/keyFile1 -i dataFiles/file20Kb.txt -o dataFiles/nn_1
```

```bash
python3 ctr-dec.py -k temp/keyFile1 -i dataFiles/nn_1 -o dataFiles/new_nn_2
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
