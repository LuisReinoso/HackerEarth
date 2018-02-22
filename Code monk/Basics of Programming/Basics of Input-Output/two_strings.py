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

ABECEDARIO = [0] * 26

LONGITUD_LETRA = len(PALABRA_UNO)

for indice in range(0, LONGITUD_LETRA):
    indiceAscciUno = ord(PALABRA_UNO[indice])
    indiceAscciDos = ord(PALABRA_DOS[indice])
    indiceUno = indiceAscciUno - 97
    indiceDos = indiceAscciDos - 97
    ABECEDARIO[indiceUno] = ABECEDARIO[indiceUno] + 1
    ABECEDARIO[indiceDos] = ABECEDARIO[indiceDos] + 1

IS_ABECEDARIO_IGUAL = True

for indice in range(0, 26):
    if ABECEDARIO[indice] != 0:
        print 'NO'
        IS_ABECEDARIO_IGUAL = False
        break

if IS_ABECEDARIO_IGUAL:
    print 'YES'
