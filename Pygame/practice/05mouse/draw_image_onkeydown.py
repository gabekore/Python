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
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN


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

# キーを押しっぱなしにした場合の繰り返し入力について
# pygame.key.get_repeat(): return (delay, interval)
# http://westplain.sakuraweb.com/translate/pygame/Key.cgi#pygame.key.set_repeat
pygame.key.set_repeat(5,5)



#-------------------------------------
# 上下左右キーで画像が動く
#-------------------------------------
def main():
    
    # ウィンドウに表示する画像
    logo = pygame.image.load(os.path.join("..", "_images", "pythonlog.jpg"))
    
    # 画像の中心座標
    # 上下左右キーで値は変化する
    pos = [200, 150]
    
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
            # 上下左右キー押下で中心座標を変更する
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos[0] -= 5
                elif event.key == K_RIGHT:
                    pos[0] += 5
                elif event.key == K_UP:
                    pos[1] -= 5
                elif event.key == K_DOWN:
                    pos[1] += 5
        
        # 中心座標を計算し直す（画面外に出た場合）
        pos[0] %= 400
        pos[1] %= 300
        print(pos[0], pos[1])
        
        #-------------------------------------
        # 画面塗り潰し（真っ白）
        #-------------------------------------
        w.fill((255,255,255))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        rect = logo.get_rect()
        rect.center = pos
        w.blit(logo, rect)
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
