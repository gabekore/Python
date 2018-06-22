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
import JTBinExpr


class Parser:
  lex = None    # Lexer
  token = 0     # 先読みしたトークン

  #---------------------------
  # parse
  #---------------------------
  def parse(self, lexer):
    code = None   # JTCode
    self.lex = lexer
    
    # トークンの先読み
    self.getToken()
    
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
    code = self.expr()
    
    if code != None:
      if self.token == ";":
        # 「;」が文の終わり
        pass
      else:
        raise("文法エラーです。")
    
    return code

  # ---------------------------
  # expr
  # ---------------------------
  def expr(self):
    # expr（式）はnumber（数値）から構成される
  
    code = self.term()
  
    if self.token == "+" or self.token == "-":
      code = expr2(code)
  
    return code

  #---------------------------
  # expr2
  #---------------------------
  def expr2(self, code):
    result = None
    
    while self.token == "+" or self.token == "-":
      op = self.token
      
      self.getToken()
      
      code2 = self.term()
      
      if result == None:
        result = JTBinExpr.JTBinExpr(op, code, code2)
      else:
        result = JTBinExpr.JTBinExpr(op, result, code2)
      
    return result


  #---------------------------
  # term
  #---------------------------
  def term(self):
    code = self.factor()
    
    if self.token == "*" or self.token == "/":
      code = self.term2(code)
    
    return code


  #---------------------------
  # term2
  #---------------------------
  def term2(self, code):
    result = None
    
    while self.token == "*" or self.token == "/":
      op = self.token
      self.getToken()
      code2 = self.term()

      if result == None:
        result = JTBinExpr.JTBinExpr(op, code, code2)
      else:
        result = JTBinExpr.JTBinExpr(op, result, code2)

    return result

  # ---------------------------
  # factor
  # ---------------------------
  def factor(self):
    code = None
    
    if self.token == Token.TokenType.EOS:
      pass
    elif self.token == Token.TokenType.INT:


  # ---------------------------
  # トークンを先読みする
  # ---------------------------
  def getToken(self):
    if self.lex.advance():
      # 次のトークンが存在する
      self.lex.token()
    else:
      # 次のトークンが存在しない
      self.token = Token.TokenType.EOS
    
