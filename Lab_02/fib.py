#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: fib.py
#	This is a pymtl fibonacci gloden algorithm implementation in pymtl3. 
#   	
#   Outputs:
#           out -> output of the block. contain fibonacci result fo 'n'
#

from pymtl3 import *

class add(Component):
  def construct(s,  Type):
    s.inl = InPort (Type)
    s.inr = InPort (Type)
    s.out = OutPort(Type)

    @s.update
    def add():
      s.out = s.inl + s.inr 



class Fib( Component ):

    def construct(s, dType, n):
        #s.in_ = InPort(dType)
        s.out = OutPort(dType)

        if n < 2 :
            s.out //= dType(n)
            return
        else:
            s.t1 = n - 1
            s.t2 = n - 2
            s.l = Fib(dType, s.t1)
            s.r = Fib(dType, s.t2)
            s.f = add(dType)
            s.f.inl //= s.l.out
            s.f.inr //= s.r.out
            s.f.out //= s.out
            return



