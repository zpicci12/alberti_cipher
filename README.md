# Cybersecurity Final Project: Alberti Cipher
## Kaylee Yin and Zoe Piccirillo 

Link to presentation: http://bit.ly/AlbertiCipherPresentation (presentation must be downloaded to view the video demo)

### Background: 
The Alberti Cipher is the first instance of a polyalphabetic cipher. Created in 1467 by Leon Battista Alberti, the cipher is best simplified through Alberti's disks, which are traditionally two metal disks with 24 cells each holding numbers/letters of the Latin alphabet. In this version of the Alberti Cipher, we made a slight variation, creating 26 cells with the English alphabet in each, while also giving users the ability to create their own version of the cipher.  

In both versions of the cipher, you must choose any letter from A-Z (denoted the outer_disk_key) that will be used to align with every random rotation of the inner disk. This random rotation occurs every period_length letters. 

### Cloning: 
`git clone https://github.com/zpicci12/alberti_cipher.git`

### To use the regular cipher encoder/decoder:
`make run ARGS="encode/decode text outer_disk_key period_length"`  
Example: make run ARGS="encode helloworld F 5"

### To create your own Alberti cipher:
`make diy`  
*You will be prompted to type in any character/letter/number in any order 26 times to create your own version of the Alberti cipher. This only affects the inner disk, as the outer disk will remain the same (English alphabetical order).*
