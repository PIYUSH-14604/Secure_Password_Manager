# Day 2 – Encryption System

## Goal
Implement encryption for secure password storage.

## Concepts Learned

### Key Derivation (PBKDF2)

Instead of directly using the password, we derive a secure key using PBKDF2.

Why:
- Prevents brute force attacks
- Adds computational cost

### Salt

A random value added to password before hashing.

Purpose:
- Prevent rainbow table attacks

### Fernet Encryption

Provides:
- AES encryption
- Authentication (ensures data integrity)

## Progress

- Implemented key derivation using PBKDF2
- Implemented encryption and decryption functions
- Tested encryption workflow successfully

## Challenges

- Understanding how key derivation works
- Managing salt securely

## Next Step

- Store encrypted passwords in file
- Persist salt and load it later