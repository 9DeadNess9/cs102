def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        i = ord(i)
        if ord("A") <= i <= ord("Z"):
            i += shift
        if i == ord("Z"):
             i = ord("A") + i % ord("Z") - 1
        if ord("a") <= i <= ord("z"):
            i += shift
            if i > ord("z"):
                i = ord("a") + i % ord("z") - 1
        ciphertext += chr(i)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    if shift >= 26:
        shift = shift % 26
    for j in ciphertext:
        j = ord(j)
        if ord("A") <= j <= ord("Z"):
            j -= shift
            if j < ord("A"):
                j = ord("Z") - ord("A") % j + 1
        if ord("a") <= j <= ord("z"):
            j -= shift
            if j < ord("a"):
                j = ord("z") - ord("a") % j + 1
        plaintext += chr(j)
    return plaintext
