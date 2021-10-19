#!/usr/bin/python3

# Python class for us to generate prime numbers
import sympy


# Keypair container used for rsa
class KeyPair:
    def __init__(self, e, n, d):
        self.e = e
        self.n = n
        self.d = d

    def __repr__(self):
        return (f"<KeyPair e={hex(self.e)}, n={hex(self.n)}, d={hex(self.d)}>")


# A collection of methods to calculate the RSA key pair
class RSA:
    # Number of bits to for each prime
    # n will have BIT_COUNT * 2 bits
    BIT_COUNT = 256

    # Based on https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    @staticmethod
    def generate_keypair(num_bits):
        p = sympy.randprime(2, 1 << num_bits)
        q = p
        while p == q:
            q = sympy.randprime(2, 1 << num_bits)

        n = p * q

        totient = RSA.lcm(p - 1, q - 1)

        e = 65537  # 2**16 + 1, it's a prime

        d = RSA.modular_inverse(e, totient)

        keypair = KeyPair(e, n, d)
        return keypair

    # Based on https://en.wikipedia.org/wiki/Euclidean_algorithm
    # Return the greatest common divisor between a and b
    @staticmethod
    def gcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    @staticmethod
    def lcm(a, b):
        # lcm(a, b) = |ab| / gcd(a, b)
        return (a * b) // RSA.gcd(a, b)

    # Based on https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    @staticmethod
    def modular_inverse(a, n):
        (t, new_t) = (0, 1)
        (r, new_r) = (n, a)

        while new_r != 0:
            q = r // new_r
            (t, new_t) = (new_t, t - q * new_t)
            (r, new_r) = (new_r, r - q * new_r)

        if r > 1:
            raise "SOMETHING WENT REALLY WRONG!! TRY AGAIN!!"
        if t < 0:
            t += n
        return t


def main():
    keypair = RSA.generate_keypair(RSA.BIT_COUNT)
    print(keypair)


# Generates RSA Keypair
if __name__ == "__main__":
    main()
