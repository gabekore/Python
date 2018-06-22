#! /usr/bin/env python3

import Token
import traceback
import LexerReader

#************************************************************
# Lexer = 字句解析
#
# 機能
# ・次のトークンが存在するかどうかを返すメソッド
# ・次のトークンの種類（文字or数値等）を返すメソッド
# ・（あるならば）トークンの値を返すメソッド
#************************************************************

class Lexer:
  tok = 0         # advance()の処理中にセットされる
  val = None      # advance()の処理中にセットされる
  reader = None   # LexerReader

  #---------------------------
  # コンストラクタ
  #
  # sio : io.StringIO
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
      self.skipWhiteSpace()
      # c = self.reader.read()
      c = self.reader.read()
      
      if c == "":
        return False
      
      if c == ";" or c == "+" or \
         c == "-" or c == "*" or \
         c == "/" or c == "(" or c == ")":
         # 演算記号等は文字そのものがトークンの種類を表す
         self.tok = c
      else:
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
  # 連続した数字を読み続ける
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

  #---------------------------
  # 空白文字を読み飛ばす
  #---------------------------
  def skipWhiteSpace(self):
    c = self.reader.read()
    while c != -1 and str(c).isspace():
      c = self.reader.read()
    
    self.reader.unread(c)
