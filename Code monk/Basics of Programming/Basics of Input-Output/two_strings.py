"""
Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is
equal to the string S2. See Sample explanation for more details.

Input :

    First line, contains an intger 'T' denoting no. of test cases.
    Each test consists of a single line, containing two space separated
    strings S1 and S2 of equal length.

Output:

    For each test case, if any of the permutation of string S1 is equal
    to the string S2 print YES else print NO.

Constraints:

    1<= T <=100
    1<= |S1| = |S2| <= 10^5
    String is made up of lower case letters only.

Note : Use Hashing Concept Only . Try to do it in O(string length).
"""

# Cada casillero coresponde a una letra en ascii
# indiceAscii = 97
# indice = indiceAscci - 97
# indice = 0
# abecedario[indice] = abecedario[indice] + 1

PALABRA_UNO = 'python'
PALABRA_DOS = 'pamram'

ABECEDARIO_UNO = [0] * 25
ABECEDARIO_DOS = [0] * 25

for letra in PALABRA_UNO:
    indiceAscci = ord(letra)
    indice = indiceAscci - 97
    ABECEDARIO_UNO[indice] = ABECEDARIO_UNO[indice] + 1

for letra in PALABRA_DOS:
    indiceAscci = ord(letra)
    indice = indiceAscci - 97
    ABECEDARIO_DOS[indice] = ABECEDARIO_DOS[indice] + 1

if ABECEDARIO_UNO == ABECEDARIO_DOS:
    print 'YES'
else:
    print 'NO'

# Solucion con hash
if hash(PALABRA_UNO) == hash(PALABRA_DOS):
    print 'YES'
else:
    print 'NO'
