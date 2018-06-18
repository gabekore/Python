#! /usr/bin/env python3

import sys
import Lexer
import Parser
import traceback

interactive = False

# ---------------------------
# Usage
#---------------------------
def usage():
  print("usage: python3 JoyToy [source_filename]")


#---------------------------
# エントリポイント
#---------------------------
# 引数チェック
if len(sys.argv) > 2:
  # 引数の数が変なときには使い方を表示して終了
  usage()
  exit()

# 処理開始
try:
  buffin = None
  
  if len(sys.argv) <= 1:
    # 引数が無いときは、標準入力から読み込む
    buffin = input()
    interactive = True
  else:
    # 引数で指定されたファイルから読み込む
    # buffin = open(sys.argv[1]).read()
    buffin = open(sys.argv[1])

  # スキャナを作成
  lex = Lexer.Lexer(buffin)
  # パーサを作成
  parser = Parser.Parser()
  
  while True:
    if interactive:
      # 標準入力から読み込んでいるときにはプロンプトを表示
      print("JoyToy: ")
  
    # codeはJTCode
    code = parser.parse(lex)  # 実際に構文解析する
    if code == None:
      break
    
    print("result = " + code.toString())
  
  buffin.close()

except FileNotFoundError as e:
    print("FileNotFoundError : ", e.args)
    print(traceback.format_exc())

    if sys.argv.count() == 0:
      # 引数が無いとき
      print("can't open file '{0}'",sys.argv[0])
    else:
      # 引数があるとき
      print("can't open file")

except FileExistsError as e:
    print("FileExistsError : ", e.args)
    print(traceback.format_exc())
    
except Exception as e:
    print("Exception : ", e.args)
    print(traceback.format_exc())
  
