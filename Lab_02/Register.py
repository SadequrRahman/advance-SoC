from pymtl3 import *


class Register(Component):
    
    def construct(s, dType):
        s.d = InPort(dType)
        s.q = OutPort(dType)
        s.l = InPort(b1)
        s.c = InPort(b1)

        @s.update_ff
        def seq_logic():
            if s.c == b1(1):
                s.q <<= dType(0)
            elif s.l == b1(1):
                s.q <<= s.d

    def line_trace(s):
        return "d->{} q->{} l->{} c->{}".format(s.d,s.q,s.l,s.c)