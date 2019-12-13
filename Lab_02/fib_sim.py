#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: fib_sim.py
#	This is a pymtl simulation file fib model. 
#   	
#


from pymtl3 import *
from fib import *



model = Fib(b8,13)
model.elaborate()
model.apply(SimulationPass)
model.sim_reset()
print("out: {} ".format( model.out))