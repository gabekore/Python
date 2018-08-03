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
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT


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

# キーを押しっぱなしにした場合の繰り返し入力について
# pygame.key.get_repeat(): return (delay, interval)
# http://westplain.sakuraweb.com/translate/pygame/Key.cgi#pygame.key.set_repeat
pygame.key.set_repeat(5,5)

# ウィンドウ
w = pygame.display.set_mode((400, 300))

# ウィンドウのタイトル（タイトルバーに表示）
pygame.display.set_caption("My First Window")

# クロックオブジェクト
fpsclock = pygame.time.Clock()


#-------------------------------------
# 画像を読み出すが、サブリージョンを使い一枚の画像から複数の画像を読み出すような感じにしている
# 二枚の画像を交互に差し替えて動きがあるように見せている
# 砲台の画像は左右キーで動く
#-------------------------------------
def main():
    
    strip = pygame.image.load(os.path.join("..", "_images", "strip.png"))
    images = []
    
    # 0,1：緑の縦波線
    # 2,3：赤の縦波線
    # 4,5：赤のインベーダー
    # 6,7：黄のインベーダー
    # 8  ：緑の砲台
    for index in range(9):
        image = pygame.Surface((24,24))
        # Rect(Left, Top, Width, Height)
        image.blit(strip, (0,0), Rect(index * 24, 0, 24, 24))
        images.append(image)
    
    counter = 0
    pos_x = 100
    
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
            
            # 左右キーで砲台が動く
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x -= 5
                elif event.key == K_RIGHT:
                    pos_x += 5
        
        #-------------------------------------
        # 画面塗り潰し（真っ黒）
        #-------------------------------------
        w.fill((0,0,0))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        # 0,1→0,1
        w.blit(images[counter % 2 + 0], ( 50,50))
        # 0,1→2,3
        w.blit(images[counter % 2 + 2], (100,50))
        # 0,1→4,5
        w.blit(images[counter % 2 + 4], (150,50))
        # 0,1→6,7
        w.blit(images[counter % 2 + 6], (200,50))
        
        counter += 1
        
        # 8：砲台が左右に動く
        w.blit(images[8], (pos_x,150))
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
