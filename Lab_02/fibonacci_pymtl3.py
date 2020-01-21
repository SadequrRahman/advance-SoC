#
# Copyright (C) 2019 Mohammad Arafath Uz Zaman <mohammad.zaman@tuhh.de>
#
# This file is part of Advance SoC Design Lab Soultion.
#
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Arafath Uz Zaman
#
#	File: fibonacci_pymtl3.py
#	This is a pymtl fibonachhi gloden algo. implementation.
#
#   Inputs:
#           series_length   -> nth element of the fibonacci series
#           en  -> to enable the block. After updating a and b value
#                   assert en signal
#   Outputs:
#           out -> output of the block. nth element of the fibonacci series
#           ack -> asserted high to indicate current gcd calculation is done.
#

from pymtl3 import *


class Fibonacci(Component):
    def construct(s, dtype ):
        s.ip_ = InPort(dtype)
        s.en = InPort(b1)
        s.out = OutPort(dtype)
        s.ack = OutPort(b1)

        s.cState = Wire(b3)
        s.nState = Wire(b3)

        s.fib = Wire(dtype)
        s.iterate = Wire(dtype)
        s.series_length = Wire(dtype)
        s.fib_prev = Wire(dtype)
        s.temp = Wire(dtype)

        s.S0 = b3(0)
        s.S1 = b3(1)
        s.S2 = b3(2)
        s.S3 = b3(3)
        s.S4 = b3(4)
        s.S5 = b3(5)
        s.S6 = b3(6)
        s.S7 = b3(7)

        @s.update_ff
        def state_memory():
            if s.reset:
                s.cState <<= s.S0
            else:
                s.cState <<= s.nState

        @s.update
        def transition_logic():
            if s.cState == s.S0:
                if s.en:
                    s.nState = s.S1
                else:
                    s.nState = s.S0

            elif s.cState == s.S1:
                if s.series_length <= dtype(1):
                    s.nState = s.S6
                else:
                    s.nState = s.S2

            elif s.cState == s.S2:
                s.nState = s.S3

            elif s.cState == s.S3:
                if s.iterate < s.series_length:
                    s.nState = s.S4
                else:
                    s.nState = s.S5

            elif s.cState == s.S4:
                s.nState = s.S3

            elif s.cState == s.S5:
                s.nState = s.S7

            elif s.cState == s.S6:
                s.nState = s.S7

            elif s.cState == s.S7:
                if s.en:
                    s.nState = s.S7
                else:
                    s.nState = s.S0

        @s.update
        def output_logic():
            if s.cState == s.S0:
                s.ack = b1(0)

            elif s.cState == s.S1:
                s.series_length = s.ip_

            elif s.cState == s.S2:
                s.fib = dtype(1)
                s.fib_prev = dtype(1)
                s.iterate = dtype(2)

            elif s.cState == s.S3:
                pass

            elif s.cState == s.S4:
                s.iterate += dtype(1)
                s.temp = s.fib
                s.fib = s.fib + s.fib_prev
                s.fib_prev = s.temp

            elif s.cState == s.S5:
                s.out = s.fib
                s.ack = dtype(1)

            elif s.cState == s.S6:
                s.out = s.series_length
                s.ack = dtype(1)

            elif s.cState == s.S7:
                pass


