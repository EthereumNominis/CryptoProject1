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
                        |        ²­ØG-çkï9Cïv
 879d915cefd68dca411fc4c550a39837
                        |        \ïÖÊAÄÅP£7
 cad41a5a4f9fa498df2d06dad3d7f5a8
                        |        ÊÔZO¤ß-═ÚÓ×õ¨
 0826c319c6e3d733c37d1ba478b85de8
                        |       &ÃÆã×3Ã}x¸]è
 9e44fcdff559695854dcdf7e02ab033a
                        |        DüßõYiXTÜß~╗«╚:
 6f6347afab60c1e9169d57c4a7362ca6
                        |        ocG¯«`ÁéWÄ§6,¦
 bf64adc64814ab13d0bf6eca1b4fecac
                        |        ¿d­ÆH«Ð¿nÊ¬
 7f3c5df4612fad9a86c242028331925b
                        |        <]ôa/­ÂB╗1[
 cf65d629293225a25fa3e7d46aecdef9
                        |        ÏeÖ))2%¢_£çÔjìÞù
 a8f4cf64a3a9aeddbfa0f27e9f70d522
                        |        ¨ôÏd£©®Ý¿ ò~pÕ"
 365c25d28acf317adc3b9b63f58628cc
                        |        6\%ÒÏ1zÜ;õ(Ì
 c9a8139f419118b38abb72cd6a922af4
^[[?1;0c                        |        É¨A³»rÍj*ô
 54ac30564929e5dc8dc19c59f5b8fdc7
                        |        T¬0VI)åÜÁYõ¸ýÇ
 983ed46ec583dead4e388e876693c166
                        |        >ÔnÅÞ­N8fÁf
 c04d9ff2d971e61ed269b810ee684fc9
                        |        ÀMòÙqæÒi¸îhOÉ
 f84da5d54bf68fed8a61e19db49fffc7
                        |        øM¥ÕKöíaá´ÿÇ
 fc5c158460c2bfcbcb6b4a7c9cc6c63a
                        |        ü\`Â¿ËËkJ|ÆÆ:
 adc6be600f246f74dff788b2d0dae1f0
                        |        ­Æ¾`$otß÷²ÐÚáð
 10f774d6f6bfd56174bab78e60262481
                        |        ÷tÖö¿Õatº·`&$
 d54db0df677280dd4b811b2b8d454953
                        |        ÕM°ßgrÝKEIS
 0a5e2fa08c5a3f78e06ac7c154d47521
                        |
^/ Z?xàjÇÁTÔu!
 0d48f77fdfb2b8449467470544ee6652
H÷ß²¸DgG║DîfR         |
 e178343c558bca03a5b4a698da2068df
                        |        áx4<UÊ╚¥´¦Ú hß
 d2b3001be4be9b1589e929507e6487ff
                        |        Ò³ ¾é)P~dÿ
                        Encryption Finished!
```



```bash
sha256sum dataFiles/plain1.txt
aba98e97ebbce403e3670f88b93fc99cc79af84c68aeddb2587073950f5dbe3a  dataFiles/plain1.txt
```





