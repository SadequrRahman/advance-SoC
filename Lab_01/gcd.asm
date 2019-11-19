#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: gcd.asm
#	This is an assembly function imlementation 
#	for gcd calculation for TinyRISC-V architecture
#	
#   gcd function expect two paramenters in register a0 and a1
#   and return calculated gcd value in a0 register according
#   to register uses convention.
#

.globl gcd					# export gcd to global scope

.text
gcd:						# gcd function expect two parameters in a0 and a2
	addi t0, a0, 0			# copy parameter to working register
    addi t1, a1, 0			#
condition_check:			# checking condition
	blt t0, t1, A_LT_B  	# branch to A_LT_B if param1 is less the  param2
	bne t1, t0, B_NE_0		# branch to B_NE_0 if param2 is not equal to zero
    addi a0, t0, 0			# load a0 for return result
	jalr zero, 0(ra)		# transfer control to caller
B_NE_0:
	sub t0, t0, t1			# param1 = param1 - param2
    j condition_check		# unconditional jump 
A_LT_B:						# this block swap param1 and param2
	add t0, t0, t1			#
    sub t1, t0, t1			# 
    sub t0, t0, t1			# 
 	j condition_check		# unconditional jump 