from pymtl3 import *

class PRNG(Component):
    def construct(s, dtype):
        s.seed = InPort(dtype)
        s.out = OutPort(dtype)
        s.en = InPort(b1)
        s.ack = OutPort(b1)
        
        s.tap_ = [Wire(dtype) for _ in range(4)]
        s.cState = Wire(b4)
        s.nState = Wire(b4)
        s.bits = Wire(dtype)
        s.feedback = Wire(dtype)
        s.temp_bit = Wire(dtype)
        s.temp_out = Wire(dtype)

        s.it_rev = Wire(b6)
        s.it_fb = Wire(b3)
        s.it_bits = Wire(b6)
        s.it_out = Wire(b6)


        s.tap_[0] = dtype(1)
        s.tap_[1] = dtype(2)
        s.tap_[2] = dtype(22)
        s.tap_[3] = dtype(32)

        s.it_rev = b6(0)
        s.it_fb = b2(1)
        s.it_bits = b6(0)
        s.it_out = b6(31)

        s.temp_out = dtype(0)
        s.temp_bit = dtype(0)
        
        s.S0 = b4(0)
        s.S1 = b4(1)
        s.S2 = b4(2)
        s.S3 = b4(3)
        s.S4 = b4(4)
        s.S5 = b4(5)
        s.S6 = b4(6)
        s.S7 = b4(7)
        s.S8 = b4(8)
        s.S9 = b4(9)
        s.S10 = b4(10)
        s.S11 = b4(11)


        @s.update_ff
        def state_memory():
            if s.reset:
                s.cState <<= s.S0
            else:
                s.cState <<= s.nState

        @s.update
        def next_logic_state():
            if s.cState == s.S0:
                if s.en == b1(1):
                    s.nState = s.S1
                else:
                    s.nState = s.S0

            elif s.cState == s.S1:
                if s.it_rev <= b6(31):
                    s.nState = s.S2
                else:
                    s.nState = s.S3

            elif s.cState == s.S2:
                s.nState = s.S1

            elif s.cState == s.S3:
                s.nState = s.S4

            elif s.cState == s.S4:
                if s.it_fb <= b2(3):
                    s.nState = s.S5
                else:
                    s.nState = s.S6

            elif s.cState == s.S5:
                s.nState = s.S4

            elif s.cState == s.S6:
                if s.it_bits < b6(31):
                    s.nState = s.S7
                else:
                    s.nState = s.S8

            elif s.cState == s.S7:
                s.nState = s.S6

            elif s.cState == s.S8:
                s.nState = s.S9

            elif s.cState == s.S9:
                if s.it_out >= b6(0):
                    s.nState = s.S10
                else:
                    s.nState = s.S11

            elif s.cState == s.S10:
                s.nState = s.S9

            elif s.cState == s.S11:
                if s.en == b1(1):
                    s.nState = s.S11
                else:
                    s.nState = s.S0

        @s.update
        def output_logic():
            if s.cState == s.S0:
                s.ack = b1(0)

            elif s.cState == s.S2:
                s.bits[b6(31) - s.it_rev] = s.seed[s.it_rev]
                s.it_rev += b6(1)

            elif s.cState == s.S3:
                s.feedback = s.bits[s.tap_[0] - dtype(1)]

            elif s.cState == s.S5:
                s.feedback = s.feedback ^ s.bits[s.tap_[s.it_fb] - b2(1)]
                s.it_fb += b2(1)

            elif s.cState == s.S7:
                s.temp_bit[s.it_bits] = s.bits[s.it_bits]
                s.it_bits += b6(1)

            elif s.cState == s.S8:
                s.bits = concat(s.feedback, s.temp_bit)

            elif s.cState == s.S10:
                s.temp_out = (s.temp_out << dtype(1)) | s.bits[s.it_out]
                s.it_out -= b6(1)

            elif s.cState == s.S11:
                s.out = s.temp_out
                s.ack = b1(1)















