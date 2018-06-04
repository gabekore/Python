#! /usr/bin/env python3


#************************************************************
# 字句の取得及びungetc的な機能
#
# 機能
# ・読み込んだトークンを戻す（C言語のungetcみたいなもの）
#************************************************************

class LexerReader:

  reader = None
  unget_p = False
  ch = 0
  

  #---------------------------
  # コンストラクタ
  #
  # sio : io.StringIO
  #---------------------------
  def __init__(self, sio):
    self.reader = sio

  #---------------------------
  # 次の文字を取得
  # unget_pがTrueなら前回読んだ文字を返す
  #---------------------------
  def read(self):
    if self.unget_p:
      self.unget_p = False
    else:
      self.ch = self.reader.read(1)
    
    return self.ch
  
  #---------------------------
  # unget_pフラグをTrueにし、
  # 次のread()で現在の文字を返すようにする
  #---------------------------
  def unread(self,c):
    self.unget_p = True