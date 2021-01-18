# Cybersecurity Final Project: Alberti Cipher
## Kaylee Yin and Zoe Piccirillo 

### Background: 
The Alberti Cipher is the first instance of a polyalphabetic cipher. Created in 1467 by Leon Battista Alberti, the cipher is best simplified through Alberti's disks, which are traditionally two metal disks with 24 cells each holding numbers/letters of the Latin alphabet. In this version of the Alberti Cipher, we have made a slight variation, creating 26 cells with the English alphabet in each, while also giving users the ability to create their own version of the cipher.  

### To use the regular cipher encoder/decoder:
**make run ARGS="encode/decode text outer_disk_key period_length"**

### To create your own Alberti cipher: 
*You will be prompted to type in any character/letter/number in any order 26 times to create your own version fo the Alberti cipher. This only affects the inner disk, as the outer disk will remain the same (English alphabetical order).*
**make diy**