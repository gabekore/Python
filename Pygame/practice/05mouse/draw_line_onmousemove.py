#! /usr/local/bin/python

# Python 3.5.1

#-------------------------------------
# import
#-------------------------------------
import sys

# pygame系
import pygame
# pygameの定数はpygame.localsに入っている
from pygame.locals import QUIT, \
            MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP


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
# マウスドラッグ中に線を描画する
# マウスボタンを離すとクリア
#-------------------------------------
def main():
    
    # マウスが動作中（ボタン押しっぱなし状態）の時のx,y座標を記録し続ける
    mousepos  = []
    # マウスが動作中か否かは判定するフラグ
    mousedown = False
    
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
            
            # マウスボタン押下
            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
            
            # マウスボタン動作中＆座標記録
            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            
            # マウスボタン押下解除
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                mousepos.clear()
        
        #-------------------------------------
        # 画面塗り潰し（真っ白）
        #-------------------------------------
        w.fill((255,255,255))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        # 記録されている座標を描画
        if len(mousepos) > 1:
            # pygame.draw.lines(Surface, color, closed, pointlist, width=1): return Rect
            # closed    : 始点と終点を結ぶか否か
            # pointlist : 座標のリスト
            # http://westplain.sakuraweb.com/translate/pygame/Draw.cgi#pygame.draw.lines
            pygame.draw.lines(w, (255,0,0), False, mousepos)
            # ※滑らかな線を描くならaalines()がある
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
