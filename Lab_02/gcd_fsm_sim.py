#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: gcd_fsm_sim.py
#	This is a pymtl simulation file for gcd calculation 
#	


from pymtl3 import *
from pymtl3.passes.backends.yosys import TranslationImportPass
from pymtl3.passes                import TracingConfigs
from gcd_fsm import *


model = Gcd_fsm(b8)
model.elaborate()
vcd_file_name = model.__class__.__name__
model.config_tracing = TracingConfigs( tracing='vcd', vcd_file_name=vcd_file_name )
model.apply(SimulationPass())
model.en = b1(0)
model.a = Bits(8, 49)
model.b = Bits(8, 7)
model.sim_reset()
model.en = b1(1)
while model.ack == b1(0):
    model.tick()
    print("cState: {} ack:{} en:{}" .format(model.cState, model.ack, model.en))

model.en = b1(0)
print("in[0]: {} in[1]: {} out: {} ".format(model.a, model.b, model.out ))

print("\r\nTranslate design into systemVerilog...\r\n")
ModeltoTranslate = Gcd_fsm(b8)
ModeltoTranslate.elaborate()
ModeltoTranslate.yosys_translate_import = True
ModeltoTranslate = TranslationImportPass()( ModeltoTranslate )
ModeltoTranslate.elaborate()