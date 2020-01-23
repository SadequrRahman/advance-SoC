#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: gcd_fsm.py
#	This is a pymtl gcd gloden algo. implementation. 
#   	
#   Inputs:
#           a   -> first value to calculated gcd
#           b   -> second value to calculated gcd
#           en  -> to enable the block. After updating a and b value
#                   assert en signal
#   Outputs:
#           out -> output of the block. contain gcd result of a and b
#           ack -> asserted high to indicate current gcd calculation is done.
#

from pymtl3 import *

class Gcd_fsm( Component ):

    def construct(s, dType ):
        s.a = InPort(dType)
        s.b = InPort(dType)
        s.en = InPort(b1)
        s.out = OutPort(dType)
        s.ack = OutPort(b1)

        s.ra = Wire(dType)
        s.rb = Wire(dType)

        s.cState = Wire(b3)
        s.nState = Wire(b3)
        s.S0 = b3(0)
        s.S1 = b3(1)
        s.S2 = b3(2)
        s.S3 = b3(3)
        s.S4 = b3(4)
        s.S5 = b3(5)


        @s.update_ff
        def state_memory():
            if s.reset :
                s.cState <<= s.S0
            else:
                s.cState <<= s.nState 

        @s.update
        def next_state_logic():
            if s.cState == s.S0:
                if s.en == b1(1):
                    s.nState = s.S1
                else:
                    s.nState = s.S0
           
            elif s.cState == s.S1:
                s.nState = s.S2
            
            elif s.cState == s.S2:
                if s.ra < s.rb :
                    s.nState = s.S3
                elif s.rb != dType(0):
                    s.nState = s.S4
                else:
                    s.nState = s.S5
            
            elif s.cState == s.S3:
                s.nState = s.S2
            
            elif s.cState == s.S4:
                s.nState = s.S2

            elif s.cState == s.S5:
                if s.en == b1(0):
                    s.nState = s.S0
                else:
                   s.nState = s.S5

        @s.update
        def output_logic():
            if s.cState == s.S0:
               s.ack = b1(0)
           
            elif s.cState == s.S1:
                s.ra = s.a
                s.rb = s.b
            
            # elif s.cState == s.S2:
            #     pass
            
            elif s.cState == s.S3:
                s.ra = s.ra + s.rb
                s.rb = s.ra - s.rb
                s.ra = s.ra - s.rb
            
            elif s.cState == s.S4:
               s.ra = s.ra - s.rb

            elif s.cState == s.S5:
                s.out = s.ra
                s.ack = b1(1)
                
        
        
        





