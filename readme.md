# RSA Key Generator

## Requirements
- sympy
- python >= 3.8

## Usage
Run `./RSA.py` in terminal to generate a public key and a private key.

<br />

# RSA Details
## What is RSA
RSA (Rivest-Shamir-Adleman) is a public-key encryption (asymmetric encryption) algorithm that is commonly used in the real world. It contains a key pair with a public key (that can be shared with others) and a private key (that should be kept hidden from others). In order to send data from the owner to the recipient, the owner encrypts the message using the private key, which can then only be decrypted by the public key and this detail can be used to verify the authenticity of the message. Similarly, to send data to the owner, you would encrypt the message using the public key, and only the private key can decrypt it.

## How does this implementation work
There are five main steps to generate an RSA key pair:

1. Generate two unique prime numbers `p` and `q` randomly.
2. Compute the modulus `n` where `n = p * q`.
3. Compute `λ(n)`, where `λ` is the totient function.
4. Chose an integer `e` such that `λ(n)` is coprime.
5. Calculate `d`, which is the modular multiplicate inverse of `e` mod `λ(n)`.


### Step 1
There are several ways to generate random prime numbers, for example, generating a long list of primes using [Sieves of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) or looping through all the numbers and checking factors or using some heuristic tests. Given that the size of our prime would normally be 256 bits or more, the only feasible way is either by heuristics or probabilistic tests. The ideal method would be probabilistic tests since it is more rigorous.

In the code, I have used `sympy` to generate prime numbers for simplicity. 

### Step 2
`n` forms part of the public key and it's used in both the encryption and decryption steps.

### Step 3
This step can be simplified down to finding the LCM (Lowest Common Multiple) between `p-1` and `q-1`. The LCM can be calculated from GCD (Greatest Common Divisor) as `LCM(a, b) = |a * b| / GCD(a, b)`, then we can calculate GCD using the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).


### Step 4
There are multiple ways to find a coprime number. We can either generate random numbers and check the `gcd` between `e` and `λ(n)`, or a faster alternative, generate an `e` that is a prime, which we can use the methods described in [step 1](#step-1) to do so.  

However in practice, it is common to use `(2**16 + 1) -> 65537` as this makes the encryption faster.

### Step 5
The last step can be solved by using the [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) to find the coefficients of [Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity).


# How to use the generated key pair
To encrypt an plain text `P` you compute `(P ** e) % n`.

To decrypt an cipher text `C` you compute `(C ** d) % n`.

See more details on [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).
