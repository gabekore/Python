#! /usr/bin/env python3

import JTCode

class JTInt(JTCode):
# class JTInt:
    
  value = 0
  
  #---------------------------
  # コンストラクタ
  #
  # sio : io.StringIO
  #---------------------------
  def __init__(self, integer):
    self.value = integer

  # ---------------------------
  # 値取得（数値型）
  # ---------------------------
  def getValue(self):
    return self.value
  
  # ---------------------------
  # 値取得
  # ---------------------------
  def toString(self):
    return str(self.value)


  # ---------------------------
  # 足し算
  # ---------------------------
  def add(self, code):
    if type(code) != JTInt:
      raise("数値以外のものを足そうとしました。")
    
    result = JTInt.JTInt(self.value + code.getValue())

    return result

  # ---------------------------
  # 引き算
  # ---------------------------
  def sub(self, code):
    if type(code) != JTInt:
      raise ("数値以外のものを足そうとしました。")
    
    result = JTInt.JTInt(self.value - code.getValue())
    
    return result
  
  # ---------------------------
  # 掛け算
  # ---------------------------
  def multiply(self, code):
    if type(code) != JTInt:
      raise ("数値以外のものを掛けようとしました。")
    
    result = JTInt.JTInt(self.value * code.getValue())
    
    return result

  # ---------------------------
  # 割り算
  # ---------------------------
  def devide(self, code):
    if type(code) != JTInt:
      raise ("数値以外のものを割ろうとしました。")
  
    result = JTInt.JTInt(self.value / code.getValue())
  
    return result




