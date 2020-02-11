#
# Copyright (C) 2019 Mohammad Sadequr Rahman <mohammad.rahman@tuhh.de>
# 
# This file is part of Advance SoC Design Lab Soultion.
# 
# SoC Design Lab Soultion can not be copied and/or distributed without the express
# permission of Mohammad Sadequr Rahman
#	
#	File: List.py
#

from pymtl3 import *
from math import ceil, log2
from Register import *


class List(Component):
  def construct(s,  dType, nItem):
    s.data_i = InPort(dType)
    s.data_o = OutPort(dType)
    s.cmd    = InPort(b3)
    s.en     = InPort(b1)
    s.ack    = OutPort(b1)
    s.found  = OutPort(b1)
    s.rdErr  = OutPort(b1)
    s.rdy    = OutPort(b1)

    iType = mk_bits(ceil(log2(nItem)))
    # register file
    s.pIndex_reg  = Register(iType)
    s.tIndex_reg = Register(iType)
    s.tData_reg = Register(dType)
    # max item number
    s.MAX_INDEX = Bits(nItem+1, nItem -1 )
    # list
    s.list = [Wire(dType) for _ in range(nItem)]
    # commands
    s.INSERT  = b3(0)
    s.FIND    = b3(1)
    s.REMOVE  = b3(2)
    s.READ    = b3(3)
    s.SORT    = b3(4)
    
    #logic enum
    HIGH = b1(1)
    LOW  = b1(0)

    # state registers
    s.cState = Wire(b8)
    s.nState = Wire(b8)
    #states enum
    s.IDEL_STATE          = b8(0)
    s.INSET_STATE         = b8(1)
    s.START_REMOVE_STATE  = b8(2)
    s.REMOVE_STATE        = b8(3)
    s.REMOVE_DONE_STATE   = b8(4)
    s.FIND_START_STATE    = b8(5)
    s.ACK_STATE           = b8(6)
    s.FIND_STATE          = b8(7)
    s.READ_STATE          = b8(8)

    @s.update_ff
    def seq_logic():
      if s.reset: 
          s.cState <<= s.IDEL_STATE 
          s.pIndex_reg.c <<= HIGH
          s.tIndex_reg.c <<= HIGH
          s.tData_reg.c <<= HIGH
      else: 
          s.cState <<= s.nState
          s.pIndex_reg.c <<= LOW
          s.tIndex_reg.c <<= LOW
          s.tData_reg.c <<= LOW

    @s.update
    def output_logic():
      if s.cState == s.IDEL_STATE:
        s.ack = LOW
        s.pIndex_reg.d = iType(0)
        s.pIndex_reg.l = LOW
        s.tIndex_reg.l = LOW
        s.tData_reg.l = LOW
        s.found       = LOW
        s.rdErr       = LOW
        s.rdy         = HIGH

      
      elif s.cState == s.INSET_STATE:
        s.rdy = LOW
        s.list[s.pIndex_reg.q] = s.data_i
        s.pIndex_reg.d = s.pIndex_reg.q + iType(1)
        s.pIndex_reg.l = HIGH

      elif s.cState == s.START_REMOVE_STATE:
        s.rdy = LOW
        s.tIndex_reg.d = iType(s.data_i)
        s.tIndex_reg.l = HIGH

      elif s.cState == s.REMOVE_STATE:
        # s.list = s.list[:s.data_i] + s.list[s.data_i+dType(1):] + [dType(0)]
        if s.tIndex_reg.q < s.pIndex_reg.q:
          s.list[s.tIndex_reg.q] = s.list[s.tIndex_reg.q+iType(1)]
          s.tIndex_reg.d = s.tIndex_reg.q + iType(1)
          s.tIndex_reg.l = HIGH
        else:
          s.tIndex_reg.l = LOW
      
      elif s.cState == s.REMOVE_DONE_STATE:
        s.rdy = LOW
        if s.pIndex_reg.q > iType(0):
          s.pIndex_reg.d = s.pIndex_reg.q - iType(1)
          s.pIndex_reg.l = HIGH

      elif s.cState == s.FIND_START_STATE:
        s.rdy = LOW
        s.tIndex_reg.d = iType(0)
        s.tData_reg.d = s.data_i
        s.tIndex_reg.l = HIGH
        s.tData_reg.l = HIGH

      elif s.cState == s.FIND_STATE:
        s.tData_reg.l = LOW
        if s.tData_reg.q == s.list[s.tIndex_reg.q]:
          s.found = HIGH
          s.tIndex_reg.l = LOW
        else:
          s.tIndex_reg.d = s.tIndex_reg.q + iType(1)
          s.tIndex_reg.l = HIGH
        
      elif s.cState == s.READ_STATE:
        s.rdy = LOW
        if iType(s.data_i) < s.pIndex_reg.q:
          s.data_o = s.list[iType(s.data_i)]
          s.rdErr = LOW
        else:
          s.rdErr = HIGH

      elif s.cState == s.ACK_STATE:
        s.ack = HIGH

    @s.update
    def transition_logic():
      if s.cState == s.IDEL_STATE:
        if(s.en == HIGH):
          if s.cmd == s.INSERT:
            s.nState = s.INSET_STATE
          elif s.cmd == s.REMOVE:
            s.nState = s.START_REMOVE_STATE
          elif s.cmd == s.FIND:
            s.nState = s.FIND_START_STATE
          elif s.cmd == s.READ:
            s.nState = s.READ_STATE
          else:
            s.nState = s.IDEL_STATE
        else:
          s.nState = s.IDEL_STATE

      elif s.cState == s.INSET_STATE:
          s.nState = s.ACK_STATE
      
      elif s.cState == s.START_REMOVE_STATE:
        s.nState = s.REMOVE_STATE

      elif s.cState == s.REMOVE_STATE:
        if s.tIndex_reg.q < s.pIndex_reg.q:
          s.nState = s.REMOVE_STATE
        else:
          s.nState = s.REMOVE_DONE_STATE

      elif s.cState == s.REMOVE_DONE_STATE:
        s.nState = s.ACK_STATE
      
      elif s.cState == s.FIND_START_STATE:
        s.nState = s.FIND_STATE
        
      elif s.cState == s.ACK_STATE:
        s.nState = s.IDEL_STATE

      elif s.cState == s.FIND_STATE:
        if s.found == HIGH:
          s.nState = s.ACK_STATE
        elif s.tIndex_reg.d < s.pIndex_reg.q:
          s.nState = s.FIND_STATE
        else:
          s.nState = s.ACK_STATE

      elif s.cState == s.READ_STATE:
        s.nState = s.ACK_STATE
          


  def state_trace(s):
    return "cState->{}\t nState->{}".format(s.cState,s.nState)
  
  def list_trace(s):
    return s.list