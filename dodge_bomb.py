import random
import sys


import pygame as pg


delta = {
        pg.K_UP: (0, -1),  # 上矢印キーの設定
        pg.K_DOWN: (0, +1),  # 下矢印キーの設定
        pg.K_LEFT: (-1, 0),  # 左矢印キーの設定
        pg.K_RIGHT: (+1, 0),  # 右矢印キーの設定
        }



def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    '''
    オブジェクトが画面内or画面外を判定し、真理値タプルを表す関数
    引数１：画面SurfaceのRect
    引数２：こうかとん、または、爆弾SurfaceのRect
    引数３：横方向、縦方向のはみ出し判定結果（画面内：True／画面外：False）
    '''

    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:  # オブジェクトが横方向に画面外へ出たとき
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:  # オブジェクトが縦方向に画面外へ出たとき
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()  # rectクラスの定義
    kk_rct.center = 900, 400  # こうかとんの座標を指定
    tmr = 0
    bb_img = pg.Surface((20, 20))  # 1辺が20の正方形
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 中心に半径10の赤い円
    bb_img.set_colorkey((0, 0, 0))  # 黒を透過
    x, y = random.randint(0, 1600), random.randint(0, 900)  # 爆弾のx座標とｙ座標をスクリーンの範囲でランダムに指定
    vx, vy = +1, +1  # 爆弾の速度を指定
    bb_rect = bb_img.get_rect()  # rectクラスを定義
    bb_rect.center = x, y  # 爆弾の座標を指定
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()  # キーの押下状態のリストの取得
        for k, mv in delta.items():  # 辞書を取り出す
            if key_lst[k]:  # 指定したキーが押されたとき
                kk_rct.move_ip(mv)  # こうかとんの移動方向

        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():  # 辞書を取り出す
                if key_lst[k]:  # 指定したキーが押されたとき
                    kk_rct.move_ip(-mv[0], -mv[1])  # こうかとんの移動方向

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rect.move_ip(vx, vy)  # 爆弾の移動
        yoko, tate = check_bound(screen.get_rect(), bb_rect)
        if not yoko:  # 爆弾が横方向に画面外へ出たとき 
            vx *= -1
        if not tate:  # 爆弾が縦方向に画面外へ出たとき
            vy *= -1
        screen.blit(bb_img, bb_rect)  # 爆弾を表示
        if kk_rct.colliderect(bb_rect) == True:  # こうかとんと爆弾が衝突したとき
            return main()  # main関数からreturnする

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()