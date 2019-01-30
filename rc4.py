S = [None] * 256 #Global array for easier implementation of prga and ksa

def ksa(key): #The Key Scheduling Algorithm
    global S
    S = [n for n in range(256)] #Fills S with values from 0 to 255

    j = 0

    for i in range(256): #Swaps values in S based on the key entered by the user
       j = (j + S[i] + key[i % len(key)]) % 256

       c = S[i]
       S[i] = S[j]
       S[j] = c


def prga(): #The Pseudo-Random Generation Algorithm
    global S, p, q

    p = 0
    q = 0

    p = (p + 1) % 256 #Set values from p and q
    q = (q + S[p]) % 256

    c = S[p] #Swap
    S[p] = S[q]
    S[q] = c

    byte = S[(S[p] + S[q]) % 256] #Takes a value from S based on p and q and then returns it
    return byte

def encryption(key, data): #Encrypts the data it is provided with
    new_key = [ord(c) for c in key] #Changes the key from characters to integers so that it can be used properly with the ksa
    ksa(new_key)
    return [ord(p) ^ prga() for p in data] #For every value in data, that value is converted to an int value and xor'd with the byte returned from the prga

def decryption(data, key): #Derypts the data that it is provided with
    decrypt = []
    str = "" #This is going to be the decrypted data
    new_key = [ord(c) for c in key] #The same as in the encryption function
    ksa(new_key)

    new_dat = [p ^ prga() for p in data] #Pretty much the same as encryption, but p doesn't need to be changed to an int

    for d in new_dat:  #For every value in new_dat, turn that value into a character and append it to decrypt
        decrypt.append(chr(d))

    for x in decrypt: #Takes each value from the decrypted data array and appends it to the string that will contain the data
        str = str + x

    return str

def hex_convert(ints): #Converts the ints into a hex string
    hexes = [] #This will be the converted string
    for i in ints: #For each value in ints, convert that value to hexadecimal and then append it to the hexes string
        hexes.append(hex(i))

    return hexes

def dec_convert(hexes): #Converts the hex string into the corresponding int and char values
    ints = [] #This will be the converted string
    for h in hexes: #For each value in hexes, convert that value to decimal and then append it to the ints string
        ints.append(int(h, 0))

    return ints


key = raw_input('Enter your desired key: ')
data = raw_input('Enter your data: ')
output = encryption(key, data)
output = hex_convert(output)
str1 = "0x"
for x in output: #For each value in output, take only the second index of that value to the end of that value and append it to str1
    str1 = str1 + x[2:]
print(str1)
output = dec_convert(output)
##print(output)
print(decryption(output, key))
