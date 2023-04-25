import random
import sys


import pygame as pg


delta = {
        pg.K_UP: (0, -1),  # 上矢印キーの設定
        pg.K_DOWN: (0, +1),  # 下矢印キーの設定
        pg.K_LEFT: (-1, 0),  # 左矢印キーの設定
        pg.K_RIGHT: (+1, 0),  # 右矢印キーの設定
        }


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

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rect.move_ip(vx, vy)  # 爆弾の移動
        screen.blit(bb_img, bb_rect)  # 爆弾を表示

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()