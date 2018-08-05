#! /usr/local/bin/python

# Python 3.5.1

#*************************************
# ◆！！重要！！◆
# このソースコードは、以下の書籍からのコードです。
# 
# 『ゲームを作りながら楽しく学べるPythonプログラミング』
#  https://amzn.to/2Ofeytk
# 
# このソースコードを参照するのであれば、
# 上記書籍を必ず購入してください。
# 
# このソースコードは、上記書籍のソースコードに、
# 独自の改造と独自のコメントを加えていますが、
# あくまでも個人の見解です。
# 
# なお、使用画像は上記書籍が準備してくれています。
# 
#*************************************


#-------------------------------------
# import
#-------------------------------------
import sys

# 乱数系
from random import randint

# pygame系
import pygame
# pygameの定数はpygame.localsに入っている
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE


#-------------------------------------
# 定数
#-------------------------------------
# FPSクロック（1秒間に何回処理するか）
FPS_TIMES = 15
# ブロック（自機が通る黒い部分）のサイズ
BLOCK_W = 10
BLOCK_H = 400
# ブロック（自機が通る黒い部分）を削る高さ
# ※ブロックが画面をはみ出す度に縦サイズを小さくしていく
#   そのときに小さくするサイズの値
#   このサイズが大きいと難易度が上がる
SHAVE_H = -20
# 自機の上下の動作量
# 数字が高いと難易度上がる（標準：3）
VELOCITY_AMOUNT = 3
# ウィンドウのサイズ
WINDOW_W = 800
WINDOW_H = 600
# 得点表示座標
SCORE_X = 600
SCORE_Y = 20
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
w = pygame.display.set_mode((WINDOW_W, WINDOW_H))

# ウィンドウのタイトル（タイトルバーに表示）
pygame.display.set_caption("Cave")

# クロックオブジェクト
fpsclock = pygame.time.Clock()


#-------------------------------------
# スペースキーでロケットが上下するので、
# 障害物を避けながら先に進むゲーム
#-------------------------------------
def main():
    
    walls    = 80               # 洞窟を構成する矩形の数
    ship_y   = 250              # 自機のy座標
    velocity = 0                # 自機が上下移動する際の速度
    score    = 0                # 点数
    slope    = randint(1,6)     # 洞窟の傾き（隣の矩形とy軸方向にどれだけずらすか）
    holes    = []               # 洞窟を構成する矩形を格納する配列
    sysfont  = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    
    # ブロック（黒い部分でロケットが通る道）の作成
    # ウィンドウ幅800 == walls(80個)*幅(10)
    # ウィンドウ高600 ,  各wallsの高さ400
    for xpos in range(walls):
        holes.append(Rect(xpos * BLOCK_W, (WINDOW_H - BLOCK_H) / 2, BLOCK_W, BLOCK_H))
    
    game_over = False
    
    #-------------------------------------
    # メインループ
    #-------------------------------------
    while True:
        
        # スペースキー押下中を表すフラグ
        is_space_down = False
        
        #-------------------------------------
        # イベントキューからイベントを取得
        #-------------------------------------
        for event in pygame.event.get():
            #-------------------------------------
            # 閉じるボタンが押されたイベント発生
            #-------------------------------------
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #-------------------------------------
            # キーイベント取得
            #-------------------------------------
            elif event.type == KEYDOWN:
                # スペースキー
                if event.key == K_SPACE:
                    is_space_down = True
        
        
        # 自機を移動
        # 一度ゲームオーバーしたら二度と入らない
        if not game_over:
            # 1フレーム毎に加点
            score += 10
            
            # 通常はvelocityを増やし続ける
            # スペースキー押下中はvelocityを減らし続ける
            # ※増減されるのは自機のy座標
            # ？velocityは要らないんじゃないの？
            # ？ship_yのみでもいいような気がする
            # ↑と思ったけど、velocityに値は累積されるので、velocityは必要
            #   velocityが無かったら自機の上下動は一定になる
            #   velocityがあると自機の上下動は時間とともに動作量は変わる
            velocity += (-VELOCITY_AMOUNT)    if is_space_down else VELOCITY_AMOUNT
            ship_y += velocity
            
            # 洞窟をスクロール
            # 最後のブロック（画面右端のブロック）をslope分ズラす（ズレるのはy座標）
            edge = holes[-1].copy()
            # ※moveは破壊的メソッドではない
            test = edge.move(0, slope)
            
            # ズラしたブロックが画面上下限からはみ出した場合、
            if test.top <= 0 or test.bottom >= WINDOW_H:
                # ◆真の場合（slopeがプラス）→ -1 を使用
                #   slopeがプラスで画面からはみ出したということは、
                #   画面下限の外に出たということ
                #   なので、上に持っていき、画面下限の上にしたいので、-1（←要はy座標マイナス方向）を使用
                # ◆偽の場合（slopeが0orマイナス）→ 1 を使用
                #   slopeがマイナスで画面からはみ出したということは、
                #   画面上限の外に出たということ
                #   なので、下に持っていき、画面上限の下にしたいので、1（←要はy座標プラス方向）を使用
                slope = randint(1,6) * (-1  if slope > 0 else 1)
                
                #-------------------------------------
                # 黒部分は画面をはみ出す度に縦サイズを小さくしていく
                # ※難易度を上げるためと思われる
                #-------------------------------------
                # 縦サイズを小さくする
                # inflate_ip
                # Rect.inflate_ip(x, y): return None
                # Rectオブジェクトの大きさを拡大・縮小します。
                # ※move_ipは破壊的メソッド
                # http://westplain.sakuraweb.com/translate/pygame/Rect.cgi#Rect.inflate_ip
                edge.inflate_ip(0, SHAVE_H)
            
            
            #-------------------------------------
            # 1. 描画位置を一つ右にズラす
            #    この時点でのイメージでは画面右端の外
            # 2. holesリストに追加（後でholesを描画するので）
            #    この時点ではholesの持つブロックの数が1つ多い（wallsの数を1つ超えてることになる）
            # 3. なので先頭（画面左端のブロックにあたる）を削除
            #    これでholesの持つブロックの数がwallsピッタシになる
            # 4. 全てのブロックのx座標を左へズラす
            #-------------------------------------
            # move_ip
            # Rect.move_ip(x, y): return None
            # Rectオブジェクトの描写位置を移動
            # http://westplain.sakuraweb.com/translate/pygame/Rect.cgi#Rect.move_ip
            edge.move_ip(BLOCK_W, slope)                    # 1.
            holes.append(edge)                              # 2.
            del holes[0]                                    # 3.
            holes = [ x.move(-BLOCK_W,0) for x in holes ]   # 4.
            
            
            #-------------------------------------
            # 衝突判定
            #-------------------------------------
            # ◆top
            #   本来はholesのどこに当たっても衝突と判定すべきだが、
            #   自機は常に左端にいるので、簡易的にするため0番目の要素のみで判定している
            #   『0番目に接触しておらず＆1番目以降に接触している』
            #   ↑ということはあり得るが、それは接触していないという判定になる
            #----
            # ◆bottom
            #   自機がbottomが下回るとアウトだが、判定に使うship_y（自機のy座標）は、
            #   自機の左上を示している
            #   なので、+80が無い場合は自機が緑部分にめり込んだ時点でアウトとなってしまう
            #   それを避けるために、80を足して調整している
            #   ※80に特別の意味はない、難易度調整のために80以外の値でもOK
            #   ※ちなみに自機画像高さは60
            if holes[0].top > ship_y or \
               holes[0].bottom < ship_y + 80:
                # 衝突したのであればゲームオーバー
                game_over = True
        
        
        #-------------------------------------
        # 画面塗り潰し（緑）
        #-------------------------------------
        w.fill((0,255,0))
        
        
        #-------------------------------------
        # ～処理～↓
        #-------------------------------------
        # 黒い通り道ブロック（holes）を描画
        for hole in holes:
            pygame.draw.rect(w, (0,0,0), hole)

        # 自機を描画
        w.blit(ship_image, (0,ship_y))

        # 得点（フォントオブジェクト）を描画、青色
        # フォントオブジェクト（文字列）からを画像オブジェクトを作成する
        # => Font.render(text, antialias, color, background=None): return Surface
        # http://westplain.sakuraweb.com/translate/pygame/Font.cgi#Font.render
        score_image = sysfont.render("score is {}".format(score), True, (0,0,255))
        w.blit(score_image, (SCORE_X,SCORE_Y))
        
        # ゲームオーバー時は、爆発画像を自機の上に描画
        if game_over:
            w.blit(bang_image, (0, ship_y - 40))
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
