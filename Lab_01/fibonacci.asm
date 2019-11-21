#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: fibonacci.asm
#	This is an assembly function to calculated 
#	fibonacci for TinyRISC-V architecture
#	
#   fibonacci function expect one paramenters in register a0
#   and return calculated fibonacci value in a0 register according
#   to register uses convention.
#
.globl fibonacci

.text
fibonacci:
    addi t0, zero, 2
    bge a0, t0, L1
    jalr zero, 0(ra)    
L1:
	addi sp, sp, -24 	# adjust stack for 3 items
    sw ra, 0(sp)		# stroe ra
    sw a0, 8(sp)		# store n
	addi a0, a0, -1		# n-1
    jal ra, fibonacci			# call fib(n-1)
    lw t0, 8(sp)		# restore n
    sw a0, 16(sp)		# save result for fib(n-1)
    addi a0, t0, -2		# n-2
    jal ra, fibonacci			# call fib(n-2)
    lw t1, 16(sp)		# restore result fib(n-1)
    add a0, a0, t1		# fib(n-1) + fib(n-2)
    lw ra, 0(sp)
    addi sp, sp, 24
    jalr zero, 0(ra)
    