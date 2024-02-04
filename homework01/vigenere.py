def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    shift = 0
    keyword_i = 0
    for cur_char in plaintext:
        char_ord = ord(cur_char)
        char_ord_keyword = ord(keyword[keyword_i])
        if ord("A") <= char_ord_keyword <= ord("Z"):
            shift = char_ord_keyword % ord("A")
        if ord("a") <= char_ord_keyword <= ord("z"):
            shift = char_ord_keyword % ord("a")
        if ord("A") <= char_ord <= ord("Z"):
            char_ord += shift
            if char_ord > ord("Z"):
                char_ord = ord("A") + char_ord % ord("Z") - 1
        if ord("a") <= char_ord <= ord("z"):
            char_ord += shift
            if char_ord > ord("z"):
                char_ord = ord("a") + char_ord % ord("z") - 1
        ciphertext += chr(char_ord)
        keyword_i += 1
        if keyword_i == len(keyword):
            keyword_i = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    shift = 0
    keyword_i = 0
    for cur_char in ciphertext:
        char_ord = ord(cur_char)
        char_ord_keyword = ord(keyword[keyword_i])
        if ord("A") <= char_ord_keyword <= ord("Z"):
            shift = char_ord_keyword % ord("A")
        if ord("a") <= char_ord_keyword <= ord("z"):
            shift = char_ord_keyword % ord("a")
        if ord("A") <= char_ord <= ord("Z"):
            char_ord -= shift
            if char_ord < ord("A"):
                char_ord = ord("Z") - ord("A") % char_ord + 1
        if ord("a") <= char_ord <= ord("z"):
            char_ord -= shift
            if char_ord < ord("a"):
                char_ord = ord("z") - ord("a") % char_ord + 1
        plaintext += chr(char_ord)
        keyword_i += 1
        if keyword_i == len(keyword):
            keyword_i = 0
    return plaintext
