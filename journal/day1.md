# Day 1 – Project Setup & Password Generator

## Goal
Start building a secure password manager in Python.

## Concepts Learned

### Cryptographically Secure Randomness

Normal Python random module is predictable and should not be used for generating passwords.

Instead we use the `secrets` module which is designed for security-sensitive applications.

Example:

secrets.choice()

This ensures passwords cannot be predicted.

## Progress

- Created project structure
- Created virtual environment
- Implemented password generator using Python secrets module
- Tested password generation via main.py

## Next Steps

- Implement encryption system for storing passwords securely
- Use the cryptography library