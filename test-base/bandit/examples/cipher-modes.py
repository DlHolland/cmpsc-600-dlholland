from cryptography.hazmat.primitives.ciphers.modes import CBC, ECB

# Insecure mode
mode = ECB(iv)

# Secure cipher and mode
cipher = AES.new(key, blockalgo.MODE_CTR, iv)

# Secure mode
mode = CBC(iv)
