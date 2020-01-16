from pymtl3 import *


class test_prng(Component):
    def construct(s, dtype, seed):
#        s.seed = InPort(dtype)
        s.tabs = [Wire(dtype) for _ in range(4)]
        s.out = OutPort(dtype)
        s.bits = Wire(dtype)
        s.feedback = Wire(dtype)

        s.feedback = dtype(0)
        s.bits = [int(x, 2) for x in reversed(format(seed, '032b'))]

        s.tabs[0] = dtype(1)
        s.tabs[1] = dtype(2)
        s.tabs[2] = dtype(22)
        s.tabs[3] = dtype(32)

        @s.update
        def generate_random():
            s.feedback = s.bits[s.tabs[3] - dtype(1)]
            for i in s.tabs[1:]:
                s.feedback = s.feedback ^ s.bits[i - 1]
            bits = [s.feedback] + s.bits[:-1]
            s.out = 0
            for bit in s.bits:
                s.out = (s.out << 1) | bit
            return s.out





            # feedback = bits[tabs[0] - 1]
            # for i in tabs[1:]:
            #     feedback = feedback ^ bits[i - 1]
            # bits = [feedback] + bits[:- 1]
            # # build integer from bits
            # out = 0
            # for bit in reversed(bits):
            #     out = (out << 1) | bit
            # return out
            # for i in s.in_[1:]:
            #     print(i)
                # s.feedback = s.feedback ^ s.bits[i - 1]
                # print(s.feedback)
