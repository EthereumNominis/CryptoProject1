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







# `cbc-enc.py`









```Python
python3 cbc-enc.py  -k temp/keyFile2 -i dataFiles/plain1.txt -o dataFiles/c_p1
Applying CBC Cipher (Encryption)......
Key file:        temp/keyFile2
Input File:      dataFiles/plain1.txt
Output File:     dataFiles/c_p1
 Successfully loaded key (Hex)    '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
 Successfully loaded plain text file      "A good old man, sir; he will be talking: as they\nsay, when the age is in, the wit is out: God help\nus! it is a world to see. Well said, i' faith,\nneighbour Verges: well, God's a good man; an two men\nride of a horse, one must ride behind. An honest\nsoul, i' faith, sir; by my troth he is, as ever\nbroke bread; but God is to be worshipped; all men\nare not alike; alas, good neighbour!"
 IV is                    f308fc428b8b8bf0c9b9b9dc4fbe5ed1
 Cipher->
 b2ad8fd84785882d1ce76bef3943ef76
.....
```





