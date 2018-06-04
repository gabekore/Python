from unittest import TestCase

import Lexer
import Token
import io

class TestLexer(TestCase):
  def test_token(self):
    tw = io.StringIO("1234")
    lex = Lexer.Lexer(tw)
    if lex.advance():
      self.assertEqual(lex.token(), Token.TokenType.INT)
    else:
      self.fail()
  
  def test_value(self):
    tw = io.StringIO("1234")
    lex = Lexer.Lexer(tw)
    if lex.advance():
      self.assertEqual(lex.value(), 1234)
    else:
      self.fail()
  
  # def test_advance(self):
    # self.fail()
  
  # def test_lexDigit(self):
    # self.fail()
