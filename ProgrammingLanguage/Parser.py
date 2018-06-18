#! /usr/bin/env python3

#************************************************************
# Parser = 文の解剖
#
# 機能
# ・
# ・
# ・
#************************************************************
import traceback
import Token
import JTInt


class Parser:
  lex = None    # Lexer

  #---------------------------
  # parse
  #---------------------------
  def parse(self, lexer):
    code = None   # JTCode
    self.lex = lexer
    
    try:
      # program()がすべての始まり
      code = self.program()
    except:
      # 例外は受け止めておく
      print(traceback.format_exc())
  
    return code

  #---------------------------
  # program
  #---------------------------
  def program(self):
    # program（プログラム）はexpr（式）から構成される
    return self.expr()

  #---------------------------
  # expr
  #---------------------------
  def expr(self):
    # expr（式）はnumber（数値）から構成される
    
    code = None   # JTCode
    
    if self.lex.advance():
      token = self.lex.token()
      
      if token == Token.TokenType.INT:
        code = JTInt.JTInt(int(self.lex.value()))
      else:
        raise("文法エラーです。")
    
    return code


    
    
