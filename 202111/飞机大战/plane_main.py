import pygame
from plane_sprites import *


class PlaneGame(object):
     """飞机大战主游戏"""

     def __init__(self):
        print("游戏初始化..")
        self.screen =  pygame.display.set_mode((480,700))
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器－－创建敌机出现 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

     def __create_sprites(self):
         """创建精灵和精灵组"""
         # 1.创建背景精灵和精灵组
         bg1 = Background()
         bg2 = Background(True)
         bg2.rect.y = -bg2.rect.height
         self.back_group = pygame.sprite.Group(bg1, bg2)
         # 2.创建敌机精灵组
         self.enemy_group = pygame.sprite.Group()
         # 3.创建英雄精灵组
         self.hero = Hero()
         self.hero_group = pygame.sprite.Group(self.hero)

     def start_game(self):
         print("游戏开始...")
         while True:
             # 1.设置刷新帧率
             self.clock.tick(FRAME_PER_SEC)
             # 2.事件监听
             self.__event_handle()
             # 3.碰撞检测
             self.__check_collide()
             # 4.更新精灵组
             self.__update_sprites()
             # 5.更新屏幕显示
             pygame.display.update()
     def __event_handle(self):
         """事件监听"""

         for event in pygame.event.get():
             # 监听游戏是否退出
             if event.type == pygame.QUIT:
                 PlaneGame.__game_over()
             # 监听敌机的出现
             elif event.type == CREATE_ENEMY_EVENT:
                 print("敌机出场...")
                 # 创建敌机精灵
                 enemy = Enemy()
                 self.enemy_group.add(Enemy())
             # 让英雄发射子弹
             elif event.type == Hero_FIRE_EVENT:
                 self.hero.fire()
         # 获取用户按键
         keys_pressed = pygame.key.get_pressed()
         if keys_pressed[pygame.K_RIGHT]:
             self.hero.speed = 2
         elif keys_pressed[pygame.K_LEFT]:
             self.hero.speed = -2
         elif keys_pressed[pygame.K_DOWN]:
             self.hero.speedy = 2
         elif keys_pressed[pygame.K_UP]:
             self.hero.speedy = -2
         else:
             self.hero.speed = 0
             self.hero.speedy = 0

     def __check_collide(self):
         """碰撞检测"""
         # 1.设置子弹摧毁敌机
         pygame.sprite.groupcollide(self.hero.bullets,
                                    self.enemy_group, True, True)
         # 2.敌机摧毁英雄
         enemies = pygame.sprite.spritecollide(self.hero,
                                               self.enemy_group, True)
         # 2.1判断列表是否有内容
         if len(enemies) > 0:
             # 让英雄牺牲
             self.hero.kill()
             # 结束游戏
             PlaneGame.__game_over()

     def __update_sprites(self):
         """更新精灵组"""
         # 1.背景更新渲染显示
         self.back_group.update()
         self.back_group.draw(self.screen)
         # 2.敌机渲染更新显示
         self.enemy_group.update()
         self.enemy_group.draw(self.screen)
          # 3.英雄渲染更新显示
         self.hero_group.update()
         self.hero_group.draw(self.screen)
         # 4.子弹渲染更新显示
         self.hero.bullets.update()
         self.hero.bullets.draw(self.screen)

     @staticmethod
     def __game_over():
         """游戏结束"""
         print("游戏结束")
         pygame.quit()
         exit()

if __name__ == '__main__':
         # 创建游戏对象
         game = PlaneGame()
         # 开始游戏
         game.start_game()