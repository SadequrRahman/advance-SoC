from pymtl3 import *
from prng_pymtl import *


model = PRNG(b32)
model.elaborate()
sim = model.apply(SimulationPass)
model.en = b1(0)
model.seed = b32(3904692793)
model.sim_reset()
model.en = b1(1)
while model.ack == b1(0):
    model.tick()
    print("cState: {} ack:{} en:{}" .format(model.cState, model.ack, model.en))

model.en = b1(0)
print("out: {} ".format( model.out ))

