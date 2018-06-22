#! /usr/bin/env python3

import JTCode
import JTInt

class JTMinus(JTCode):
  code = None
  
  def __init__(self, c):
    self.code = c
  
  def run(self):
    c = self.code.run()
    
    if type(c) != JTInt:
      raise("数値以外のものに単項演算子ーを適用しようとしました。")
    
    return JTInt.JTInt(c.getValue())