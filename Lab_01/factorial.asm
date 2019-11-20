#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: factorial.asm
#	This is an assembly function to calculated 
#	factorial for TinyRISC-V architecture
#	
#   factorial function expect two paramenters in register a0 and a1
#   and return calculated gcd value in a0 register according
#   to register uses convention.
#
.globl factorial

.text
li a0, 10
jal ra, factorial
addi a1, a0, 0
li a0, 1
ecall
li a0, 10
ecall



factorial:					# expect paramenter  n in register a0
	addi sp, sp, -16 		# adjust stack for 2 items
    sw ra, 8(sp)			# push return address to stack
    sw a0, 0(sp)			# push return a0 to stack
    addi t0, a0, -1			# t0 <- n-1
    bge t0, zero, L1		# check base condition for recursive function
    addi a0, zero, 1		# upload return
    addi sp, sp, 16			# adjust stack pointer
    jalr zero, 0(ra)    	# return to caller
L1:
	addi a0, a0, -1			# prepare parameter for recursive function call
    jal ra, factorial		# call factorial recursively
    addi t1, a0, 0			# store result to working register
    lw a0, 0(sp)			# load n from stack
    mul a0, a0, t1			# n * factorial(n-1)
    lw ra, 8(sp)			# load return addres from stack
    addi sp, sp, 16			# adjust stack pointer
    jalr zero, 0(ra)		# return to caller
    