
import codecs
from array import *

# Read data from plaintext file
file = open('data/plaintext.txt')
dataPlaintext = file.read()

print("Plaintext message:")
print(dataPlaintext)
print()

# Read data from subkey files
file = open('data/subkey0.txt')
dataSubkey0 = file.read()

file = open('data/subkey1.txt')
dataSubkey1 = file.read()

# Set dimensions for matrices 
rows, cols = (4, 4) 

# Convert plaintex from ASCII to hex and print result
print("Hexadecimal message:")
ascii = [ord(character) for character in str(dataPlaintext)]
hexValues = ascii
hexValuesString = ""
for x in range(16):
    hexValues[x] = hex(ascii[x])
    hexValuesString = hexValuesString + hexValues[x]
print(hexValuesString)
print()

# Initialize initial state matrix and print result
initialState = [[0 for i in range(cols)] for j in range(rows)] 
initialState[0][0] = hexValues[0][2:4]
initialState[1][0] = hexValues[1][2:4]
initialState[2][0] = hexValues[2][2:4]
initialState[3][0] = hexValues[3][2:4]
initialState[0][1] = hexValues[4][2:4]
initialState[1][1] = hexValues[5][2:4]
initialState[2][1] = hexValues[6][2:4]
initialState[3][1] = hexValues[7][2:4]
initialState[0][2] = hexValues[8][2:4]
initialState[1][2] = hexValues[9][2:4]
initialState[2][2] = hexValues[10][2:4]
initialState[3][2] = hexValues[11][2:4]
initialState[0][3] = hexValues[12][2:4]
initialState[1][3] = hexValues[13][2:4]
initialState[2][3] = hexValues[14][2:4]
initialState[3][3] = hexValues[15][2:4]

print("Initial state:")
for row in initialState: 
    print(row) 
print()

# Initialize subkey0 matrix
subKey0 = [[0 for i in range(cols)] for j in range(rows)] 
subKey0[0][0] = dataSubkey0[0:2]
subKey0[1][0] = dataSubkey0[2:4]
subKey0[2][0] = dataSubkey0[4:6]
subKey0[3][0] = dataSubkey0[6:8]
subKey0[0][1] = dataSubkey0[8:10]
subKey0[1][1] = dataSubkey0[10:12]
subKey0[2][1] = dataSubkey0[12:14]
subKey0[3][1] = dataSubkey0[14:16]
subKey0[0][2] = dataSubkey0[16:18]
subKey0[1][2] = dataSubkey0[18:20]
subKey0[2][2] = dataSubkey0[20:22]
subKey0[3][2] = dataSubkey0[22:24]
subKey0[0][3] = dataSubkey0[24:26]
subKey0[1][3] = dataSubkey0[26:28]
subKey0[2][3] = dataSubkey0[28:30]
subKey0[3][3] = dataSubkey0[30:32]

# Initialize subkey1 matrix
subKey1 = [[0 for i in range(cols)] for j in range(rows)] 
subKey1[0][0] = dataSubkey1[0:2]
subKey1[1][0] = dataSubkey1[2:4]
subKey1[2][0] = dataSubkey1[4:6]
subKey1[3][0] = dataSubkey1[6:8]
subKey1[0][1] = dataSubkey1[8:10]
subKey1[1][1] = dataSubkey1[10:12]
subKey1[2][1] = dataSubkey1[12:14]
subKey1[3][1] = dataSubkey1[14:16]
subKey1[0][2] = dataSubkey1[16:18]
subKey1[1][2] = dataSubkey1[18:20]
subKey1[2][2] = dataSubkey1[20:22]
subKey1[3][2] = dataSubkey1[22:24]
subKey1[0][3] = dataSubkey1[24:26]
subKey1[1][3] = dataSubkey1[26:28]
subKey1[2][3] = dataSubkey1[28:30]
subKey1[3][3] = dataSubkey1[30:32]

# Function for AddKey
def addKey(state, key):
    result = [[0 for i in range(cols)] for j in range(rows)] 
    for c in range(4):
        for r in range(4):
            result[r][c] = str(hex(int(state[r][c],16) ^ int(key[r][c],16)))[2:4].zfill(2)

    return result

addKeyResult0 = addKey(initialState, subKey0)

# Print AddKey0 result
print("AddKey0 Result:")
for row in addKeyResult0: 
    print(row) 
print()

# Initialize S-Box matrix
sBox = [[0 for i in range(16)] for j in range(16)] 
sBox = [["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
           ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
           ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
           ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
           ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
           ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "cf"],
           ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
           ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
           ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
           ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
           ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
           ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
           ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
           ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
           ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
           ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

# Function for SubBytes
def subBytes(state):
    subBytesResult = [[0 for i in range(cols)] for j in range(rows)] 

    for c in range(4):
        for r in range(4):
            indexRow = str(state[r][c])[0]
            indexCol = str(state[r][c])[1]

            if (indexRow.isalpha()):
                indexRow = int(indexRow, 16)
            if (indexCol.isalpha()):
                indexCol = int(indexCol, 16)
            
            subBytesResult[r][c] = sBox[int(indexRow)][int(indexCol)]
    return subBytesResult

subBytesResult = subBytes(addKeyResult0)

# Print SubBytes result
print("SubBytes Result:")
for row in subBytesResult: 
    print(row) 
print()

# Function for ShiftRows
def shiftRows(state):
    shiftRowsResult = [[0 for i in range(cols)] for j in range(rows)] 
    for r in range(4):
        for c in range(4):
            if (r == 0):
                shiftRowsResult[r][c] = state[r][c]
            elif (r == 1):
                shiftRowsResult[r][0] = state[r][1]
                shiftRowsResult[r][1] = state[r][2]
                shiftRowsResult[r][2] = state[r][3]
                shiftRowsResult[r][3] = state[r][0]
            elif (r == 2):
                shiftRowsResult[r][0] = state[r][2]
                shiftRowsResult[r][1] = state[r][3]
                shiftRowsResult[r][2] = state[r][0]
                shiftRowsResult[r][3] = state[r][1]
            else:
                shiftRowsResult[r][0] = state[r][3]
                shiftRowsResult[r][1] = state[r][0]
                shiftRowsResult[r][2] = state[r][1]
                shiftRowsResult[r][3] = state[r][2]

    return shiftRowsResult

shiftRowsResult = shiftRows(subBytesResult)

# Print ShiftRows result
print("ShiftRows Result:")
for row in shiftRowsResult: 
    print(row) 
print()

# Function for Galois Multiplication
# I got this function from an library I found online
# https://github.com/hlilje/aes-python/blob/master/aes.py
def galois_mult(a, b):
    """
    Multiplication in the Galois field GF(2^8).
    """
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80: a ^= 0x1b
        b >>= 1
    return p % 256

# Initialize FixedState array
fixedState = [[0 for i in range(cols)] for j in range(rows)] 
fixedState = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

# Function for MixColumns
def mixColumns(state):
    mixColumnsResult = [[0 for i in range(cols)] for j in range(rows)] 
    values = []
    xorResults = []

    for i in range(4):
        for c in range(4):
            for r in range(4):
                values.append(galois_mult(int((state[r][i]), 16), fixedState[c][r]))
            xorResults.append(hex(values[0] ^ values[1] ^ values[2] ^ values[3])[2:4])   
            mixColumnsResult[c][i] = xorResults[0].zfill(2)
            values.clear()
            xorResults.clear()

    return mixColumnsResult

mixColumnsResult = mixColumns(shiftRowsResult)

# Print MixColumns result
print("MixColumns Result:")
for row in mixColumnsResult: 
    print(row) 
print()

addKeyResult1 = addKey(mixColumnsResult, subKey1)

# Print Addkey1 result
finalString = ""
print("AddKey1 Result")
for row in addKeyResult1: 
    print(row) 
    for x in row:
        finalString = finalString + x
print()

# Print final string
print("Result After One Round of Encryption:")
print(finalString)
print()

# Write final string to results file
file = open('data/result.txt', 'w')
file.write(finalString)