# vigenere
Home-made vigenere cipher project in python3. needs dependency ConfigParser. you can edit settings in config.ini.

Add text to be processed in input_text.txt, and it will be written to output_text.txt. You will be prompted for the encryption key for both.

### Example:

text:
>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce egestas fringilla interdum. In vitae sapien arcu. Nullam at iaculis mauris. Maecenas eu malesuada sapien. Quisque ut nibh ex. Phasellus ac nibh blandit, dapibus neque nec, pulvinar mi. Nunc luctus, nulla quis iaculis tempor, velit purus auctor libero, tempor laoreet leo metus id leo. Nullam egestas aliquet nulla efficitur pulvinar. Donec consequat consequat erat, vitae cursus libero tempus at. In sed est dictum, mattis sem sed, laoreet tellus.

key: 
`helloworld`

config:

```
PreserveFormatting = 0
WordLength = 4
RowLength = 15
Caps = 2
```


encrypt it with these parameters and you get:
```
SSCP AEDJ FPKS WZFO WKLP LXNZ BOST EHAY CLRE DZDF PRRP ZEHW FVJI PRSO HRDI
YMYR WHZR TQAI COII WEGL AEPD OLWV YDYG FYIH ZRXD AMLN IHWJ XDBV TDAW STPQ
HWPF AWZV DXHH LDOL WVYT BMDB IAIK YLIL PIDD OJPO SYDL QJWS SESE YOWP RRAL
IYDY SMIV YHJT FWJE BRCP PRFY QHIT EXZR FWZW ELTV PENF ZEGK PPWS CGSH WKAX
YYDL IYHF COPF PCCP SDAR YPLZ FASK WHVQ PEIO WUWH VRFW ZWAV RHZX LDOH WHFH
ARFW ZWSW QLJM EFFL ICGL UECO CJST NRUW PBIW HTZQ ZIBF OPSI LWCM ELSY IIDX
ZPTM SNCK PPWY DLHE BJPG LWEO WYHL XPHX ETGO SDDH KPLZ FASK EHSP FD 

```

decrypt it with the same key, and you will get:
```
LORE MIPS UMDO LORS ITAM ETCO NSEC TETU RADI PISC INGE LITF USCE EGES TASF
RING ILLA INTE RDUM INVI TAES APIE NARC UNUL LAMA TIAC ULIS MAUR ISMA ECEN
ASEU MALE SUAD ASAP IENQ UISQ UEUT NIBH EXPH ASEL LUSA CNIB HBLA NDIT DAPI
BUSN EQUE NECP ULVI NARM INUN CLUC TUSN ULLA QUIS IACU LIST EMPO RVEL ITPU
RUSA UCTO RLIB EROT EMPO RLAO REET LEOM ETUS IDLE ONUL LAME GEST ASAL IQUE
TNUL LAEF FICI TURP ULVI NARD ONEC CONS EQUA TCON SEQU ATER ATVI TAEC URSU
SLIB EROT EMPU SATI NSED ESTD ICTU MMAT TISS EMSE DLAO REET TELL US 

```
