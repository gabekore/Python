#! /usr/local/bin/python

# Python 3.5.1

#-------------------------------------
# import
#-------------------------------------
import sys
import os

# pygame系
import pygame
# pygameの定数はpygame.localsに入っている
from pygame.locals import QUIT


#-------------------------------------
# 定数
#-------------------------------------
# FPSクロック（1秒間に何回処理するか）
FPS_TIMES = 3000


#-------------------------------------
# 初期処理
#-------------------------------------
# pygame初期化
pygame.init()

# ウィンドウ
w = pygame.display.set_mode((400, 300))

# ウィンドウのタイトル（タイトルバーに表示）
pygame.display.set_caption("My First Window")

# クロックオブジェクト
fpsclock = pygame.time.Clock()


#-------------------------------------
# Windowの中で画像が回転する（左上基準）
# 回転する時に空いたスペースは勝手に近い色を付けてくれてる？
# ※全体的な平均色で埋めてる感じがする
#-------------------------------------
def main():
    
    logo = pygame.image.load(os.path.join("..", "_images", "pythonlog.jpg"))
    # logo = pygame.image.load(os.path.join("..", "_images", "strip.png"))
    # logo = pygame.image.load(os.path.join("..", "_images", "sqliteforexcel.jpg")) # サイズが1200x630なのでウィンドウサイズを大きくした方がいい
    
    
    # 回転度数
    # 数はどんどん増えていくが問題なし
    # プログラマは角度の倍数を意識すればいい
    theta = 0
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        for event in pygame.event.get(QUIT):
            # イベントキューからイベントを取得
            # 閉じるボタンが押されたイベント発生
            pygame.quit()
            sys.exit()
        
        theta += 1
        print(theta)
        
        #-------------------------------------
        # 画面塗り潰し（真っ白）
        #-------------------------------------
        w.fill((255,255,255))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        # ロゴを回転し、左上が(100,30)の位置にロゴを描画
        # http://westplain.sakuraweb.com/translate/pygame/Transform.cgi#pygame.transform.rotate
        # pygame.transform.rotate(Surface, angle): return Surface
        new_logo = pygame.transform.rotate(logo, theta)
        w.blit(new_logo, (100,30))
        #-------------------------------------
        # ～処理～↑
        #-------------------------------------
        
        
        #-------------------------------------
        # 画面更新
        #-------------------------------------
        pygame.display.update()
        
        #-------------------------------------
        # FPS CLOCK
        #-------------------------------------
        fpsclock.tick(FPS_TIMES)
        


#-------------------------------------
# メイン時のみmain()関数コール
#-------------------------------------
if __name__ == '__main__':
    main()
