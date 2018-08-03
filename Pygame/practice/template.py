#! /usr/local/bin/python

# Python 3.5.1

#-------------------------------------
# import
#-------------------------------------
import sys

# pygame系
import pygame
# pygameの定数はpygame.localsに入っている
from pygame.locals import QUIT, Rect


#-------------------------------------
# 定数
#-------------------------------------
# FPSクロック（1秒間に何回処理するか）
FPS_TIMES = 30


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
# Windowを出すだけ
#-------------------------------------
def main():
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        for event in pygame.event.get():
            # イベントキューからイベントを取得
            # 閉じるボタンが押されたイベント発生
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        #-------------------------------------
        # 画面塗り潰し（真っ白）
        #-------------------------------------
        w.fill((255,255,255))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        
        
        
        
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