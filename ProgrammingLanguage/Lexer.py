#! /usr/bin/env python3

import Token
import traceback
import LexerReader

# Lexer = 字句解析

# 機能
# ・次のトークンが存在するかどうかを返すメソッド
# ・次のトークンの種類（文字or数値等）を返すメソッド
# ・（あるならば）トークンの値を返すメソッド

class Lexer:
  tok = 0         # advance()の処理中にセットされる
  val = None      # advance()の処理中にセットされる
  reader = None   # LexerReader

  #---------------------------
  # コンストラクタ
  #
  # tw : io.StringIO
  #---------------------------
  def __init__(self, sio):
    self.reader = LexerReader.LexerReader(sio)



  #---------------------------
  # 現在のトークンの種類を返す
  #---------------------------
  def token(self):
    return self.tok
  
  #---------------------------
  # 現在のトークンの値を返す
  #---------------------------
  def value(self):
    return self.val


  #---------------------------
  # 次のトークンに進む
  # True:次のトークンがある、False:ない
  #---------------------------
  def advance(self):
    try:
      # c = self.reader.read()
      c = self.reader.read()
      
      if c == "":
        return False
      
      if str(c).isdigit():
        self.reader.unread(c)
        self.lexDigit()
        self.tok = Token.TokenType.INT
      else:
        raise("数字じゃないです。")
      
    except:
      print(traceback.format_exc())
      
    return True
    

  #---------------------------
  #
  #---------------------------
  def lexDigit(self):
    num = 0
    
    while True:
      c = self.reader.read()
      if c == "":
        break
      
      if str(c).isdigit() == False:
        self.reader.unread(c)
        break
      
      num = (num * 10) + (int(c) - int('0'))
    
    self.val = num
