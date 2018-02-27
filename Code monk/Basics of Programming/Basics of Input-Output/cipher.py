"""
Indian army is going to do a surprise attack on one of its enemies country.
The President of India, the Supreme Commander of the Indian Army will be
sending an alert message to all its commanding centers. As enemy would be
monitoring the message, Indian army is going to encrypt(cipher) the message
using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message.
Your cipher must rotate every character in the message by a fixed number
making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols,
followed by a number '0<=N<=1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9).
All Symbols, such as - , ; %, remain unencrypted.
"""

FRASEACONVERTIR = "abcdZXYzxy-999.@"
CLAVECIFRADO = 200
FRASEDESCIFRADA = []

for letra in FRASEACONVERTIR:
    indiceAscci = ord(letra)

    if indiceAscci >= 48 and indiceAscci <= 57: # 10 numeros
        numeroRotacion = CLAVECIFRADO % 10
        indiceSuperior = indiceAscci + numeroRotacion
        if indiceSuperior > 57:
            auxIndice = indiceSuperior - 57
            indiceRespuesta = 47 + auxIndice
        else:
            indiceRespuesta = indiceSuperior
        FRASEDESCIFRADA.append(chr(indiceRespuesta))

    elif indiceAscci >= 65 and indiceAscci <= 90: # 26 A-Z
        numeroRotacion = CLAVECIFRADO % 26
        indiceSuperior = indiceAscci + numeroRotacion
        if indiceSuperior > 90:
            auxIndice = indiceSuperior - 90
            indiceRespuesta = 64 + auxIndice
        else:
            indiceRespuesta = indiceSuperior
        FRASEDESCIFRADA.append(chr(indiceRespuesta))

    elif indiceAscci >= 97 and indiceAscci <= 122: # 26 a-z
        numeroRotacion = CLAVECIFRADO % 26
        indiceSuperior = indiceAscci + numeroRotacion
        if indiceSuperior > 122:
            auxIndice = indiceSuperior - 122
            indiceRespuesta = 96 + auxIndice
        else:
            indiceRespuesta = indiceSuperior
        FRASEDESCIFRADA.append(chr(indiceRespuesta))
    else:
        FRASEDESCIFRADA.append(letra)

print ''.join(FRASEDESCIFRADA)
