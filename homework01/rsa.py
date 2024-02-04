import math
import random
import typing as tp


def is_prime(int_n: int) -> bool:
    if int_n < 2:
        return False
    int_m = int(math.sqrt(int_n)) + 1
    for i in range(2, int_m):
        if int_n % i == 0:
            return False
    return True


def gcd(int_a: int, int_b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while int_a != 0 and int_b != 0:
        int_a, int_b = int_b, int_a % int_b
    return int_a + int_b


def multiplicative_inverse(int_e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    for i in range(phi):
        if (int_e * i) % phi == 1:
            return i
    return 0


def generate_keypair(int_p: int, int_q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(int_p) and is_prime(int_q)):
        raise ValueError("Both numbers must be prime.")
    elif int_p == int_q:
        raise ValueError("p and q cannot be equal")

    int_n = int_p * int_q

    phi = (int_p - 1) * (int_q - 1)

    # Choose an integer e such that e and phi(int_n) are coprime
    int_e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(int_n) are coprime
    int_g = gcd(int_e, phi)
    while int_g != 1:
        int_e = random.randrange(1, phi)
        int_g = gcd(int_e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    int_d = multiplicative_inverse(int_e, phi)

    # Return public and private keypair
    # Public key is (int_e, int_n) and private key is (int_d, int_n)
    return ((int_e, int_n), (int_d, int_n))


def encrypt(tuple_pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, int_n = tuple_pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod int_m
    cipher = [(ord(char) ** key) % int_n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(tuple_pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, int_n = tuple_pk
    # Generate the plaintext based on the ciphertext and key using a^b mod int_m
    plain = [chr((char**key) % int_n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    int_p = int(input("Enter a prime number (17, 19, 23, etc): "))
    int_q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(int_p, int_q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
