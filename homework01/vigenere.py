def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = "ATTACKATDAWN"
    shift = 0
    keyword_i = 0
    for Tsymb in plaintext:
        symb_ord = ord(Tsymb)
        symb_ord_keyword = ord(keyword[keyword_i])
        if ord("A") <= symb_ord_keyword <= ord("Z"):
            shift = symb_ord_keyword % ord("A")
        if ord("a") <= symb_ord_keyword <= ord("z"):
            shift = symb_ord_keyword % ord("a")
        if ord("A") <= symb_ord <= ord("Z"):
            symb_ord += shift
            if symb_ord > ord("Z"):
                symb_ord = ord("A") + symb_ord % ord("Z") - 1
        if ord("a") <= symb_ord <= ord("z"):
            symb_ord += shift
            if symb_ord > ord("z"):
                symb_ord = ord("a") + symb_ord % ord("z") - 1
        ciphertext += chr(symb_ord)
        keyword_i += 1
        if keyword_i == len(keyword):
            keyword_i = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    shift = 0
    keyword_i = 0
    for Tsymb in ciphertext:
        symb_ord = ord(Tsymb)
        symb_ord_keyword = ord(keyword[keyword_i])
        if ord("A") <= symb_ord_keyword <= ord("Z"):
            shift = symb_ord_keyword % ord("A")
        if ord("a") <= symb_ord_keyword <= ord("z"):
            shift = symb_ord_keyword % ord("a")
        if ord("A") <= symb_ord <= ord("Z"):
            symb_ord -= shift
            if symb_ord < ord("A"):
                symb_ord = ord("Z") - ord("A") % symb_ord + 1
        if ord("a") <= symb_ord <= ord("z"):
            symb_ord -= shift
            if symb_ord < ord("a"):
                symb_ord = ord("z") - ord("a") % symb_ord + 1
        plaintext += chr(symb_ord)
        keyword_i += 1
        if keyword_i == len(keyword):
            keyword_i = 0
    return plaintext
