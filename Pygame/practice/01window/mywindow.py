#! /usr/local/bin/python

# Python 3.5.1

#-------------------------------------
# import
#-------------------------------------
import sys

# pygame系
import pygame
# pygameの定数はpygame.localsに入っている
from pygame.locals import QUIT


#-------------------------------------
# 初期処理
#-------------------------------------
# pygame初期化
pygame.init()

# ウィンドウ
w = pygame.display.set_mode((400,300))

# ウィンドウのタイトル（タイトルバーに表示）
pygame.display.set_caption("My First Window")


#-------------------------------------
# Windowを出すだけ
#-------------------------------------
def main():
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        # 画面の色：真っ白
        w.fill((255, 255, 255))
        
        # 画面更新
        pygame.display.update()
        
        # イベントキューからイベントを取得
        for event in pygame.event.get():
            # 閉じるボタンが押されたイベント発生
            if event.type == QUIT:
                # 画面閉じて終了
                pygame.quit()
                sys.exit()


#-------------------------------------
# メイン時のみmain()関数コール
#-------------------------------------
if __name__ == '__main__':
    main()
