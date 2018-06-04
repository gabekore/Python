from unittest import TestCase

import Lexer
import Token
import io

class TestLexer(TestCase):
  def test_token(self):
    # テスト1
    tw = io.StringIO("1234")
    lex = Lexer.Lexer(tw)
    if lex.advance():
      self.assertEqual(lex.token(), Token.TokenType.INT)
    else:
      self.fail()

    # テスト2
    tw = io.StringIO("1234 5678")
    lex = Lexer.Lexer(tw)
    while lex.advance():
      self.assertEqual(lex.token(), Token.TokenType.INT)
    
  def test_value(self):
    # テスト1
    tw = io.StringIO("1234")
    lex = Lexer.Lexer(tw)
    if lex.advance():
      self.assertEqual(lex.value(), 1234)
    else:
      self.fail()

    # テスト2
    tw = io.StringIO("1234 5678")
    lex = Lexer.Lexer(tw)
    if lex.advance():
      self.assertEqual(lex.value(), 1234)
    else:
      self.fail()
      
    if lex.advance():
      self.assertEqual(lex.value(), 5678)
    else:
      self.fail()
  
  # def test_advance(self):
    # self.fail()
  
  # def test_lexDigit(self):
    # self.fail()
