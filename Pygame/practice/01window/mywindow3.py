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

# クロックオブジェクト
fpsclock = pygame.time.Clock()

#-------------------------------------
# フレーム数（fps）の確認
#-------------------------------------
def main():
    
    # フォントオブジェクトの作成
    # Noneはデフォルトフォントになる
    # デフォルトフォントが嫌ならフォント名を指定する
    sysfont = pygame.font.SysFont(None, 36)

    # これがインクリされ続けて画面に表示される
    counter = 0
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        # イベントキューからイベントを取得
        # 閉じるボタンが押されたイベント発生
        for event in pygame.event.get(QUIT):
            # 画面閉じて終了
            pygame.quit()
            sys.exit()

        # インクリ
        counter += 1

        # 画面の色：真っ黒
        w.fill((0, 0, 0))
        
        # フォントオブジェクト（文字列）からを画像オブジェクトを作成する
        # => Font.render(text, antialias, color, background=None): return Surface
        # http://westplain.sakuraweb.com/translate/pygame/Font.cgi#Font.render
        count_image = sysfont.render("count -> " + str(counter), True, (225,225,225))

        # Surface上に
        # => Surface.blit(source, dest, area=None, special_flags = 0): return Rect
        #    destはx/y座標（ウィンドウの左上が(0,0)、右下が(999,999)）
        # http://westplain.sakuraweb.com/translate/pygame/Surface.cgi#Surface.blit
        w.blit(count_image, (50, 50))
        
        # 画面更新
        pygame.display.update()
        
        # 1フレーム毎に実行する
        # 1フレームの処理速度を抑えてCPU使用率も抑えるのが目的
        # なので、メインループの最後に実行する必要あり
        # 
        # フレームごとに一回Clock.tick(40)を実行すると、プログラムは一秒毎に40フレームを超える速度で実行されることはありません。
        # => Clock.tick(framerate=0): return milliseconds
        # http://westplain.sakuraweb.com/translate/pygame/Time.cgi#Clock.tick
        fpsclock.tick(10)


#-------------------------------------
# メイン時のみmain()関数コール
#-------------------------------------
if __name__ == '__main__':
    main()
