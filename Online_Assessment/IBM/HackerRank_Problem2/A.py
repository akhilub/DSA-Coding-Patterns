#TC:O(n)
#SC:O(n)
def simpleCipher(encrypted, k):
    decrypted = ""
    k = k%26
    for char in encrypted:
        # Convert char to ASCII value, shift it, and wrap around if necessary
        ascii_val = ord(char) - k
        if ascii_val < ord('A'):
            ascii_val += 26
        decrypted += chr(ascii_val)
    return decrypted

#TC:O(n)
#SC:O(1)
def simpleCipher(encrypted, k):
    k = k % 26  # Reduce k to its effective value
    return ''.join(chr((ord(c) - ord('A') - k) % 26 + ord('A')) for c in encrypted)


