# vigenere
Home-made vigenere cipher project in python3. needs dependency ConfigParser. you can edit settings in config.ini.

Add text to be processed in input_text.txt, and it will be written to output_text.txt. You will be prompted for the encryption key for both.

Here's an example.

text:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce egestas fringilla interdum. In vitae sapien arcu. Nullam at iaculis mauris. Maecenas eu malesuada sapien. Quisque ut nibh ex. Phasellus ac nibh blandit, dapibus neque nec, pulvinar mi. Nunc luctus, nulla quis iaculis tempor, velit purus auctor libero, tempor laoreet leo metus id leo. Nullam egestas aliquet nulla efficitur pulvinar. Donec consequat consequat erat, vitae cursus libero tempus at. In sed est dictum, mattis sem sed, laoreet tellus.

key:

`helloworld`

config:

`PreserveFormatting = 0
WordLength = 4
RowLength = 15
Caps = 2`

run it with these parameters and you get:

`
SSCP AWGD XTOZ ZKFD LALX SPNR UWPN HAHL CHHT AWOQ ZYJI WTHW FVJI PUAG KLVJ
CTBC WCWD MYES NRLX MYJE HRPZ EATS JRCF BYIH ZRXH XTOY ICTV QLFF EGPH INPB
WGPX QLWS OIRO DWLA WABT BMDB IALE UMMS ALSO EDPZ HIJD JYTP DSWD UHTE RRAL
IYDB AELP UINL ICGL UECA EYXU GWIY HLDR FWZW HFLZ TLQQ ZZDA IXAC NGHS MEDQ
FLDH YNEC NCTE LVZP SDAR YWLC NSVE SIZA AHLD PHWS KYXS PLXA UVDW HWLZ EELP
WRFW ZWVQ IPGT EING FOCM YLFU ZQLG NCJG VBXH XNCJ GVBX HXPF WHYP XLPY IIDX
ZWTP AFFW LQAF GOKP RDSZ VDWH TNHQ APHX ETGG VXZI OHOF CHLX ESHZ LD`
