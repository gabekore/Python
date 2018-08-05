#! /usr/local/bin/python

# Python 3.5.1

#-------------------------------------
# import
#-------------------------------------
import sys

# 数学系
from math import sin, cos, radians

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
# 二つの☆を描画する
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
        # 画面塗り潰し（真っ黒）
        #-------------------------------------
        w.fill((0,0,0))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        pointlist0, pointlist1 = [], []
        
        # 360度の円の図形を思い浮かべる
        # ※右0度、360度、上90度、左180度、下270度
        #   1.   0度：右
        #   2. 144度：左上
        #   3. 288度：右下
        #   4. 432度：右上
        #   5. 576度：ほぼ左
        # この五点を順番につなげると☆形になる
        for theta in range(0, 720, 144):
            # 度をラジアンに変換
            rad = radians(theta)
            
            # sin/cosで座標を算出
            # x軸方向はcos、y軸方向はsin
            pointlist0.append( (cos(rad) * 100 + 100, sin(rad) * 100 + 150) )
            pointlist1.append( (cos(rad) * 100 + 300, sin(rad) * 100 + 150) )
            
            print("--------------", theta)
            print(pointlist0)
            print(pointlist1)
        
        
        # pygame.draw.lines(Surface, color, closed, pointlist, width=1): return Rect
        # closed    : 始点と終点を結ぶか否か
        # pointlist : 座標のリスト
        pygame.draw.lines  (w, (255,255,255), True, pointlist0, 5)
        pygame.draw.aalines(w, (255,255,255), True, pointlist1)
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
