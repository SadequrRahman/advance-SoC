from pymtl3 import *
from List import *
from pymtl3.passes.backends.yosys import TranslationImportPass


dut = List(b8, 10)
dut.elaborate()
dut.apply(SimulationPass())
dut.sim_reset()
dut.en = b1(0)
dut.tick()

for i in range(5):
    dut.data_i = b8(i)
    dut.cmd = b2(0)
    dut.en = b1(1)
    while dut.ack == b1(0):
        dut.tick()
    dut.en = b1(0)
    dut.tick()
dut.data_i = b8(0)
dut.cmd = b2(dut.REMOVE)
dut.en = b1(1)
while dut.ack == b1(0):
        dut.tick()
dut.en = b1(0)
dut.tick()



dut.data_i = b8(10)
dut.cmd = b2(dut.FIND)
dut.en = b1(1)
while dut.ack == b1(0):
        dut.tick()

dut.en = b1(0)
print("Found {}".format(dut.found))
dut.tick()

dut.data_i = b8(5)
dut.cmd = b2(dut.READ)
dut.en = b1(1)
while dut.ack == b1(0):
        dut.tick()

dut.en = b1(0)
print("Read Error Bit->{},\tData_O->{}".format(dut.rdErr,dut.data_o))

# ModeltoTranslate = List(b8, 32)
# ModeltoTranslate.yosys_translate_import = True
# ModeltoTranslate.elaborate()
# ModeltoTranslate = TranslationImportPass()( ModeltoTranslate )
# len = 5
# list = [Wire(b8) for _ in range(len)]
# list[0] = Bits(8,5)
# list[1] = Bits(8,7)
# list[2] = Bits(8,11)
# list[3] = Bits(8,15)
# list[4] = Bits(8,17)


# print(list[0:])
# newList = list[:1] + list[2:] + [Bits(8, 0)]
# print(newList)
# list = newList
# print(list)