from pwn import *
from urllib.parse import unquote
import base64
import codecs

p = remote('pwn-2021.duc.tf', 31905)

print(p.recvuntil('quiz...'))
p.sendline()
print(p.recvuntil("1+1=?"))
p.sendline("2")
print(p.recvuntil("then.\n\n"))

first_hex = p.recvline()
print(first_hex)
decode_hex = int(str(first_hex).split(":")[1][1:-3], 16)
print("Hex decoded: " + str(decode_hex))

p.sendline(str(decode_hex))
print(p.recvuntil("least.\n\n"))
first_ascii = p.recvline()
print(first_ascii)
decode_ascii = chr(int(str(first_ascii).split(":")[1][1:-3], 16))
print("Ascii decoded: " + decode_ascii)
p.sendline(decode_ascii)

print(p.recvuntil("yakka\n\n"))

first_url = p.recvline()
print(first_url)
decode_url = unquote(str(first_url).split(":")[1][1:-3])
print("decoded url: " + decode_url)
print(p.sendline(decode_url))

p.recvuntil("Keep going!\n\n")
first_base64 = p.recvline()
print(first_base64)
decode_base64 = str(base64.b64decode(str(first_base64).split(":")[1][1:-3]))[2:-1]
print("Decoded base64: " + decode_base64)
p.sendline(decode_base64)

print(p.recvuntil("whip.\n\n"))

second_base64 = p.recvline()
print(second_base64)
encode_base64 = str(base64.b64encode(str(second_base64).split(":")[1][1:-3].encode("ascii")))[2:-1]
print("The encoded base 64: " + encode_base64)
p.sendline(encode_base64)

p.recvuntil("That's not bad.\n\n")
first_rot13 = p.recvline()
print(first_rot13)
decode_rot13 = codecs.decode(str(first_rot13).split(":")[1][1:-3], "rot13")
print("Decoded rot13: " + decode_rot13)
p.sendline(decode_rot13)

p.recvuntil("dummy yet!\n\n")
second_rot13 = p.recvline()
encode_rot13 = codecs.encode(str(second_rot13).split(":")[1][1:-3], "rot13")
print("Encoded rot13: " + encode_rot13)
p.sendline(encode_rot13)

p.recvuntil("quickly.\n\n")
first_binary = p.recvline()
decode_binary = str(int(str(first_binary).split(":")[1][1:-3], 2))
print("Decoded binary: " + decode_binary)
p.sendline(decode_binary)

p.recvuntil("computer?\n\n")
second_binary = p.recvline()
encode_binary = bin(int(str(second_binary).split(":")[1][1:-3]))
print("Encoded binary: " + encode_binary)
p.sendline(encode_binary)

p.recvuntil("universe?\n")
p.sendline("DUCTF")

print(p.recv())
