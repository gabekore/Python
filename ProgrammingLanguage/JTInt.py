#! /usr/bin/env python3

# import JTCode
#
# class JTInt(JTCode):
class JTInt:
    
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