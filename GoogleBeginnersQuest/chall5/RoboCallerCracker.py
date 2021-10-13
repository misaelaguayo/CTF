allowedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}123456789_-!#@$%&*()"

with open("master_secret.enc", "rb") as f:
    bytes_read = f.read()

for b in bytes_read:
    for num in range(256):
        xor = b ^ num
        if chr(xor) in allowedCharacters:
            print(chr(xor), end = "")
        else:
            print("?", end = "")
print()