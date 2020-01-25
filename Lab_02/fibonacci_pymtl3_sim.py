#
# Copyright (C) 2020 Mohammad Arafath Uz Zaman <mohammad.zaman@tuhh.de>
#
# This file is part of Advance SoC Design Lab Soultion.
#
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#
#	File: fibonacci_pymtl3_sim.py
#	This is a pymtl simulation file for fibonacci series calculation

#

from pymtl3 import *
from fibonacci_pymtl3 import *


model = Fibonacci(b8)

model.elaborate()
model.dump_vcd = True
model.vcd_file_name = "gcd_fsm"
model.en = b1(0)
model.ip_ = Bits(8, 10)
model.apply(SimulationPass)
model.sim_reset()
model.en = b1(0)
model.ip_ = Bits(8, 10)
model.sim_reset()
model.en = b1(1)
while model.ack == b1(0):
    model.tick()
    print("cState: {} ack:{} en:{}" .format(model.cState, model.ack, model.en))

model.en = b1(0)
print("ip_: {} out: {} ".format(int(model.ip_), int(model.out)))
