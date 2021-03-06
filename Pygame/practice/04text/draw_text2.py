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
# 回転しながら文字を出す
#-------------------------------------
def main():
    
    # フォントオブジェクト作成
    # 「フォントオブジェクト＝画像」と思っていい
    sysfont = pygame.font.SysFont(None,72)
    msg = sysfont.render("Hello Python", True, (0,0,255))
    # フォントオブジェクトの四角エリアとその中心設定
    # msg_rectは画像のオブジェクトと同一と思っていい
    msg_rect = msg.get_rect()
    theta = 0
    scale = 1
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        for event in pygame.event.get(QUIT):
            # イベントキューからイベントを取得
            # 閉じるボタンが押されたイベント発生
            pygame.quit()
            sys.exit()
        
        #-------------------------------------
        # 画面塗り潰し（真っ白）
        #-------------------------------------
        w.fill((255,255,255))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        theta += 5
        scale = (theta % 360) / 180
        # rotozoom
        # Surfaceの変換を伴う画像の拡大縮小、回転を行います。
        # pygame.transform.rotozoom(Surface, angle, scale): return Surface
        # angle：回転角度
        # scale：ズーム倍率
        # http://westplain.sakuraweb.com/translate/pygame/Transform.cgi#pygame.transform.rotozoom
        tmp_msg = pygame.transform.rotozoom(msg, theta, scale)
        tmp_rect = tmp_msg.get_rect()
        tmp_rect.center = (200,150)
        w.blit(tmp_msg, tmp_rect)
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
