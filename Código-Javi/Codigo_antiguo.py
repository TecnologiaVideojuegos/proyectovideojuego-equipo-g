import arcade
import random
import os
import math
import Enemigos

SPRITE_SCALING_NAVE = 0.85
SPRITE_SCALING_ENEMY = 0.1
SPRITE_SCALING_BULLET = 0.5
MOVEMENT_SPEED = 7
ENEMY_COUNT = 10
VIEWPORT_MARGIN = 40
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HOLLOW RIDERS"
MUSIC_VOLUME = 0.5
"""Para que no se sobrecargue todo de balas he puesto que haya un limite de balas en pantalla"""
MAX_PLAYER_BULLETS = 5
MAX_ENEMY1_BULLETS = 1
BULLET_SPEED = 9

def bordes():
    """" Los bordes para poner imagenes en ellos la puntuacion etc """

    arcade.draw_lrwh_rectangle_textured(0, 0, 200, 867, arcade.load_texture(":resources:images/practicas/Layout.jpg"))
    arcade.draw_lrwh_rectangle_textured(1300, 0, 200, 800, arcade.load_texture(":resources:images/practicas/LayoutDerecha.jpg"))


class Explosion(arcade.Sprite):
    """Esta clase creara una explosion de forma animada"""

    def __init__(self, texture_list):
        super().__init__()
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()


class nave(arcade.Sprite):
    def update(self):
        """Las cordenadas x e y que vayan variando segun su posicion y los limites a los que puede llegar la nave"""
        self.center_x += self.change_x
        self.center_y += self.change_y

        """Sistema de margenes que hay que implementar"""
        if self.left < 201:
            self.left = 201
        elif self.right > 1300 - 1:
            self.right = 1300 - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 400 - 1:
            self.top = 400 - 1


class StartView(arcade.View):
    """Pantalla para dar comiendo al juego"""

    def __init__(self):
        super().__init__()
        self.FondoMenuPrincipal = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep +"FondoMenuPrincipal.jpg")
        self.Logo = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "LogoEquipoVideojuegos.png")
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.musica.play()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoMenuPrincipal)
        arcade.draw_text("HOLLOW RIDERS", SCREEN_WIDTH / 2, 575, arcade.color.CYBER_YELLOW, font_size=100, anchor_x="center")
        arcade.draw_text("<Pulsa Click para avanzar>", SCREEN_WIDTH / 2, 370, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(1200, -30, 400, 400, self.Logo)

    def on_mouse_press(self, _x, _y, _buttom, _modifiers):
        menu_view = MenuView()
        self.window.show_view(menu_view)


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.FondoMenuPrincipal = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep +"FondoMenuPrincipal.jpg")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoMenuPrincipal)
        arcade.draw_text("HOLLOW RIDERS", SCREEN_WIDTH / 2, 575, arcade.color.CYBER_YELLOW, font_size=100, anchor_x="center")
        arcade.draw_text("1. JUGAR", SCREEN_WIDTH / 2, 450, arcade.color.CYBER_YELLOW, font_size=50, anchor_x="center")
        arcade.draw_text("2. CONTROLES", SCREEN_WIDTH / 2, 325, arcade.color.CYBER_YELLOW, font_size=50, anchor_x="center")
        arcade.draw_text("3. SALIR", SCREEN_WIDTH / 2, 200, arcade.color.CYBER_YELLOW, font_size=50, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.KEY_1:
            historia_view = HistoriaView()
            self.window.show_view(historia_view)
        if key == arcade.key.KEY_2:
            controles_view = ControlesView()
            self.window.show_view(controles_view)
        if key == arcade.key.KEY_3:
            exit()


class HistoriaView(arcade.View):
    """Pantalla para dar comiendo al juego"""

    def on_show(self):
        self.FondoHistoria = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoEspacioPlaneta.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoHistoria)
        arcade.draw_text("HOLLOW RIDERS", 750, 700, arcade.color.CYBER_YELLOW, font_size=70, anchor_x="center")
        arcade.draw_text(
            "En el año 1357 la colonia del imperio Caladino, Spe, está siendo invadida por la especie de los Isithsaba, una raza invasora, que sobrevive\ninvadiendo mundos y extrayendo todo sus recursos hasta destruir el planeta, el pueblo caladino no puede permitirse perder su colonia, tras haber\nabusado en exceso de su planeta están llevando a cabo una migración a Spe un planeta lleno de vida sin ninguna especie que halla desarrollado\nningún tipo de civilización, pero con la llegada de los Isithsaba los caladinos estan viendo la posible extinción de su especie y eso no es algo que\npiensan permitir, como pueblo guerrero que son lucharan hasta el final por su planeta."
            , 750, 550, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text("<Click para continuar>", SCREEN_WIDTH / 2, 250, arcade.color.CYBER_YELLOW, font_size=25,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _buttom, _modifiers):
        game_view = MyGame()
        self.window.show_view(game_view)


class ControlesView(arcade.View):
    """Pantalla para dar comiendo al juego"""

    def on_show(self):
        self.FondoMenuPrincipal = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep +"FondoMenuPrincipal.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoMenuPrincipal)
        arcade.draw_text("CONTROLES:", SCREEN_WIDTH / 2, 700, arcade.color.CYBER_YELLOW, font_size=75, anchor_x="center")
        arcade.draw_text("MOVIMIENTO:", 80, 600, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text(
            "El sistema de movimiento de este videojuego se basa en un movimiento con una perspectiva isométrica.\nEl movimiento de la nave es muy comodo ya que puedes moverla con las letras W, A, S y D, tanto con las flechas del teclado.\nAsi que puedes jugar como mas comodo te halles.",
            625, 525, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text("DISPAROS:", 60, 475, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text(
            "El sistema de disparo se basa en un disparo recto de 90º que se activa con la barra espaciadora o el click izquierdo, \n solo puede haber 3 balas a la vez en pantalla",
            585, 425, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text("<Pulsa Click para volver al menu>", SCREEN_WIDTH / 2, 300, arcade.color.CYBER_YELLOW, font_size=20,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _buttom, _modifiers):
        menu_view = MenuView()
        self.window.show_view(menu_view)


class MyGame(arcade.View):
    """Es arcade.View para facilitar numerosas ventanas"""

    def __init__(self):
        super().__init__()
        """La biblioteca "os" permite localizar archivos lo que permmite importar imagenes mas facilmente"""
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0

        self.nave_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.nave_sprite = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.enemybullet_list = arcade.SpriteList()
        self.background1 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoMarino.jpg")
        self.background2 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoMarino2.jpg")
        self.background3 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoMarino3.jpg")
        self.background4 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "NaveCayendose.jpg")
        self.background5 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "NaveCayendose2.jpg")
        self.background6 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "NaveCayendose3.jpg")
        self.background7 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoGalaxia.jpg")
        self.background8 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoGalaxia2.jpg")
        self.background9 = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoGalaxia3.jpg")
        self.score = 0
        self.Vidas = 3
        self.nivel = 1
        self.time_taken = 0
        self.lista1 = []
        self.lista2 = []
        self.lista3 = []
        self.nivel_1()
        self.nave_sprite = nave(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "NewNave.png", SPRITE_SCALING_NAVE)
        self.nave_sprite.center_x = 750
        self.nave_sprite.center_y = 125
        self.nave_list.append(self.nave_sprite)

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        """Tamaño de la explosion cuando derribas una nave"""
        self.explosion_texture_list = []
        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        explosion = ":resources:images/spritesheets/explosion.png"
        self.explosion_texture_list = arcade.load_spritesheet(explosion, sprite_width, sprite_height, columns, count)

        self.gun_sound = arcade.load_sound(":resources:" + os.path.sep + "sounds" + os.path.sep +"hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:" + os.path.sep + "sounds" + os.path.sep +"hit5.wav")

        arcade.set_background_color(arcade.color.BLACK)

    """Bases del sistema de niveles"""
    def nivel_1(self):
        for i in range(3):
            """Aparicion de enemigos en posiciones randomizadas dentro de unas cordenadas"""
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_2(self):
        for i in range(7):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_3(self):
        for i in range(12):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)
        for j in range(1):
            enemy2 = Enemigos.Mosquito()
            self.lista1.append(enemy2)
        for k in range(1):
            enemy4 = Enemigos.NaveSOS()
            self.lista3.append(enemy4)

    def nivel_4(self):
        for i in range(17):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)
        for j in range(4):
            enemy2 = Enemigos.Mosquito()
            self.lista1.append(enemy2)

    def nivel_5(self):
        for i in range(0):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)
        for j in range(0):
            enemy2 = Enemigos.Mosquito()
            self.lista1.append(enemy2)
        for k in range(5):
            enemy3 = Enemigos.Bala_Rebot()
            self.lista2.append(enemy3)

    def nivel_6(self):
        for i in range(20):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.nave_sprite.center_x = 750
            self.nave_sprite.center_y = 125
            self.enemy_list.append(enemy1)

    def nivel_7(self):
        for i in range(23):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_8(self):
        for i in range(25):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)
        for k in range(1):
            enemy4 = Enemigos.NaveSOS()
            self.lista3.append(enemy4)

    def nivel_9(self):
        for i in range(27):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1140)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_10(self):
        for i in range(1):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_11(self):
        for i in range(30):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.nave_sprite.center_x = 750
            self.nave_sprite.center_y = 125
            self.enemy_list.append(enemy1)

    def nivel_12(self):
        for i in range(33):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_13(self):
        for i in range(35):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)
        for k in range(1):
            enemy4 = Enemigos.NaveSOS()
            self.lista3.append(enemy4)
    def nivel_14(self):
        for i in range(37):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def nivel_15(self):
        for i in range(1):
            enemy1 = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BichoMalo.png", SPRITE_SCALING_ENEMY)
            enemy1.center_x = random.randrange(340, 1200)
            enemy1.center_y = random.randrange(400, 790)
            self.enemy_list.append(enemy1)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        bordes()
        """El sistema de puntuaciones y de vida"""
        arcade.draw_text(f"Score: {self.score}", 10, 725, arcade.color.WHITE, 14)
        arcade.draw_text(f"Vidas: {self.Vidas}", 10, 750, arcade.color.WHITE, 14)
        time_taken_formatted = f"{round(self.time_taken, 2)} segundos"
        arcade.draw_text(f"Tiempo: {time_taken_formatted}", 95, 700, arcade.color.WHITE, font_size=15,
                         anchor_x="center")
        if self.nivel == 1:
            arcade.draw_text("Nivel: 1", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background1)
        if self.nivel == 2:
            arcade.draw_text("Nivel: 2", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background1)
        if self.nivel == 3:
            arcade.draw_text("Nivel: 3", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_text("NaveSOS cura 1 vida si\nimpactas con ella pero si la\ndisparas restara puntos" ,95, 610, arcade.color.CYBER_YELLOW, font_size = 13, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background2)
        if self.nivel == 4:
            arcade.draw_text("Nivel: 4", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background2)
        if self.nivel == 5:
            arcade.draw_text("PRIMER JEFE", 50, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background3)
        if self.nivel == 6:
            arcade.draw_text("Nivel: 6", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background4)
        if self.nivel == 7:
            arcade.draw_text("Nivel: 7", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background4)
        if self.nivel == 8:
            arcade.draw_text("Nivel: 8", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background5)
        if self.nivel == 9:
            arcade.draw_text("Nivel: 9", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background5)
        if self.nivel == 10:
            arcade.draw_text("SEGUNDO JEFE", 60, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background6)
        if self.nivel == 11:
            arcade.draw_text("Nivel: 11", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background7)
        if self.nivel == 12:
            arcade.draw_text("Nivel: 12", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background7)
        if self.nivel == 13:
            arcade.draw_text("Nivel: 13", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background8)
        if self.nivel == 14:
            arcade.draw_text("Nivel: 14", 40, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background8)
        if self.nivel == 15:
            arcade.draw_text("JEFE FINAL", 50, 675, arcade.color.WHITE, font_size=15, anchor_x="center")
            arcade.draw_lrwh_rectangle_textured(200, 0, 1100, 800, self.background9)

        self.enemy_list.draw()
        self.bullet_list.draw()
        self.nave_list.draw()
        self.enemybullet_list.draw()
        self.explosions_list.draw()
        for k in self.lista1:
            k.sprite.draw()
            k.bala.draw()
        for m in self.lista2:
            m.sprite.draw()
        for n in self.lista3:
            n.sprite.draw()

    def on_key_press(self, key, modifiers):
        """La programacion de movimiento tanto si quieres moverlo con WASD como si quieres moverlo con las letras"""
        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        if key == arcade.key.SPACE:
            if len(self.bullet_list) < MAX_PLAYER_BULLETS:
                arcade.play_sound(self.gun_sound)
                bullet = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "space_shooter" + os.path.sep + "laserBlue01.png", SPRITE_SCALING_BULLET)
                bullet.angle = 90
                bullet.change_y = BULLET_SPEED
                bullet.center_x = self.nave_sprite.center_x
                bullet.bottom = self.nave_sprite.top
                self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False
        """Activar el menu de pausa"""
        if key == arcade.key.ESCAPE:
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_mouse_press(self, x, y, button, modifiers):
        """Sistema de disparo totalmente vertical que se ejecuta si pulsas el boton izq del raton"""
        if len(self.bullet_list) < MAX_PLAYER_BULLETS:
            arcade.play_sound(self.gun_sound)
            bullet = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "LaserNave.png", SPRITE_SCALING_BULLET)
            bullet.angle = 90
            bullet.change_y = BULLET_SPEED
            bullet.center_x = self.nave_sprite.center_x
            bullet.bottom = self.nave_sprite.top
            self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        self.frame_count += 1
        self.time_taken += delta_time
        self.bullet_list.update()
        self.nave_list.update()
        self.explosions_list.update()
        self.nave_sprite.change_x = 0
        self.nave_sprite.change_y = 0
        for l in self.lista2:
            l.movimiento()
        for k in self.lista1:
            k.movimiento()
            k.bala.update()
        for j in self.lista3:
            j.movimiento()

        """Para calculaar la velocidad segun las teclas que pulses"""
        if self.up_pressed and not self.down_pressed:
            self.nave_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.nave_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.nave_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.nave_sprite.change_x = MOVEMENT_SPEED
        self.nave_list.update()

        """Para que la bala no atraviese objetivos y si das a un objetivo que te sume un punto"""
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if len(hit_list) > MAX_ENEMY1_BULLETS:
                bullet.remove_from_sprite_lists()
            """Para que cuando mates a un enemigo desaparezca la bala y no siga"""
            for enemy1 in hit_list:
                enemy1.remove_from_sprite_lists()
                self.score += 1
                self.window.total_score += 1
                arcade.play_sound(self.hit_sound)
                bullet.remove_from_sprite_lists()
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            """Cuando estas a cero vidas no puedes disparar"""
            if self.Vidas <= 0:
                bullet.remove_from_sprite_lists()
        self.bullet_list.update()

        """Toda la programacion para que los enemigos te miren y te disparen, esta hecho gracias a la bibliteca math para aprovechar los angulos"""
        for enemy1 in self.enemy_list:
            start_x = enemy1.center_x
            start_y = enemy1.center_y
            dest_x = self.nave_sprite.center_x
            dest_y = self.nave_sprite.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            enemy1.angle = math.degrees(angle) - 90

            """Los enemigos te apuntan y no disparan todos a la vez si no en una franja de tiempo"""
            if random.randrange(120) == 0:
                enemy1bullet = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "laserRed01.png", SPRITE_SCALING_BULLET)
                enemy1bullet.center_x = start_x
                enemy1bullet.center_y = start_y
                enemy1bullet.angle = math.degrees(angle)
                enemy1bullet.change_x = math.cos(angle) * BULLET_SPEED
                enemy1bullet.change_y = math.sin(angle) * BULLET_SPEED
                self.enemybullet_list.append(enemy1bullet)

        """Que los enemigos puedan golpearte y te quiten vidas"""
        for enemy1bullet in self.enemybullet_list:
            hit_list2 = arcade.check_for_collision_with_list(enemy1bullet, self.nave_list)
            for self.nave_sprite in hit_list2:
                self.Vidas -= 1
                arcade.play_sound(self.hit_sound)
                enemy1bullet.remove_from_sprite_lists()
                if self.Vidas <= 0:
                    game_over_view = GameOverView()
                    game_over_view.time_taken = self.time_taken
                    self.window.show_view(game_over_view)

        """Que las balas te persigan y desaparezcan si chocan con bordes"""
        for enemy1bullet in self.enemybullet_list:
            if enemy1bullet.top < 0:
                enemy1bullet.remove_from_sprite_lists()
            elif enemy1bullet.center_x < 201:
                enemy1bullet.remove_from_sprite_lists()
            elif enemy1bullet.top > 1001:
                enemy1bullet.remove_from_sprite_lists()
            elif self.Vidas <= 0:
                enemy1bullet.remove_from_sprite_lists()
        self.enemybullet_list.update()

        """Para comprobar las colisiones entre las balas que rebotan y la nave"""
        for rueda in self.lista2:
            if arcade.check_for_collision(self.nave_sprite, rueda.sprite):
                self.Vidas -= 1
                self.lista2.remove(rueda)
                if self.Vidas <= 0:
                    game_over_view = GameOverView()
                    game_over_view.time_taken = self.time_taken
                    self.window.show_view(game_over_view)
        """Para comprobar las colisiones entre mosquitos y la nave"""
        for venga in self.lista2:
            for bala in self.bullet_list:
                if arcade.check_for_collision(venga.sprite, bala):
                    self.bullet_list.remove(bala)
                    venga.vidas -= 1
                    if venga.vidas == 0:
                        self.lista2 .remove(venga)
                        self.score += 2
                        self.window.total_score += 2
        """Revision colisiones entre las balas del jugador y las balas que reboten"""
        for venga in self.lista1:
            for bala in self.bullet_list:
                if arcade.check_for_collision(venga.sprite, bala):
                    self.bullet_list.remove(bala)
                    venga.vidas -= 1
                    if venga.vidas == 0:
                        self.lista1.remove(venga)
                        self.score += 4
                        self.window.total_score += 4
        """Para comprobar las colisiones entre la nave el SOS"""
        for naveSos in self.lista3:
            if arcade.check_for_collision(self.nave_sprite, naveSos.sprite):
                self.Vidas += 1
                self.lista3.remove(naveSos)
        """Para comprobar las colisiones entre NaveSOS y la nave"""
        for venga in self.lista3:
            for bala in self.bullet_list:
                if arcade.check_for_collision(venga.sprite, bala):
                    self.bullet_list.remove(bala)
                    venga.vidas -= 1
                    if venga.vidas == 0:
                        self.lista3.remove(venga)
                        self.score -= 3
                        self.window.total_score -= 3
            if naveSos.cor_Y < 0:
                self.lista3.remove(venga)
        """Revision colisiones entre las balas del jugador y las balas que reboten"""
        for s in self.lista1:
            colision = arcade.check_for_collision_with_list(s.bala, self.nave_list)
            for self.nave_sprite in colision:
                s.lista_balas.remove(s.lista_balas[0])
                self.Vidas -= 1
                if self.Vidas <= 0:
                    game_over_view = GameOverView()
                    game_over_view.time_taken = self.time_taken
                    self.window.show_view(game_over_view)

        """Sistema de cambio de niveles"""
        if len(self.enemy_list) == 0 and self.nivel == 1:
            self.nivel += 1
            self.nivel_2()
        elif len(self.enemy_list) == 0 and self.nivel == 2:
            self.nivel += 1
            self.nivel_3()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and len(self.lista3) == 0 and self.nivel == 3:
            self.nivel += 1
            self.nivel_4()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 4:
            self.nivel += 1
            self.nivel_5()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 5:
            intermedio1_view = Intermedio1View(self)
            self.window.show_view(intermedio1_view)
            self.nivel += 1
            self.nivel_6()
            self.Vidas += 1
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 6:
            self.nivel += 1
            self.nivel_7()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 7:
            self.nivel += 1
            self.nivel_8()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and len(self.lista3) == 0 and self.nivel == 8:
            self.nivel += 1
            self.nivel_9()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 9:
            self.nivel += 1
            self.nivel_10()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 10:
            intermedio2_view = Intermedio2View(self)
            self.window.show_view(intermedio2_view)
            self.nivel += 1
            self.Vidas += 1
            self.nivel_11()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 11:
            self.nivel += 1
            self.nivel_12()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 12:
            self.nivel += 1
            self.nivel_13()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and len(self.lista3) == 0 and self.nivel == 13:
            self.nivel += 1
            self.nivel_14()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 14:
            self.nivel += 1
            self.nivel_15()
        elif len(self.enemy_list) == 0 and len(self.lista1) == 0 and len(self.lista2) == 0 and self.nivel == 15:
            victoria_view = VictoriaView()
            victoria_view.time_taken = self.time_taken
            self.window.show_view(victoria_view)

class Intermedio1View(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        self.FondoHistoria = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoEspacioPlaneta.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoHistoria)
        arcade.draw_text("HOLLOW RIDERS", 750, 700, arcade.color.CYBER_YELLOW, font_size=70, anchor_x="center")
        arcade.draw_text(
            "Tras derrotar la primera oleada de enemigos que atacaba el nucleo de la ciudad, el ejercito caladino se dirije hacia la naves de asalto\nde los Isithsaba que estaban preparando una segunda oleada, el contraataque impedira a los Isithsaba seguir detruyendo la ciudad y\nllevara el combate a su terreno, si el contraataque falla podria ser el fin de los caladinos.",
            750, 550, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text("<Click para continuar>", SCREEN_WIDTH / 2, 300, arcade.color.CYBER_YELLOW, font_size=25,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _buttom, _modifiers):
        self.window.show_view(self.game_view)


class Intermedio2View(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        self.FondoHistoria = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoEspacioPlaneta.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.FondoHistoria)
        arcade.draw_text("HOLLOW RIDERS", 750, 700, arcade.color.CYBER_YELLOW, font_size=70, anchor_x="center")
        arcade.draw_text(
            "El contrataque ha sido exitoso, tras derrotar al comandante Isithsaba, Ukoyisa las tropas invasoras se baten en retirada hacia el nucleo de su flota\nlos caladinos mantienen su ofensiva para no perder la iniciativa, no quieren dejar reagruparse a las tropas enemigas y persiguen a los enemigos\nen retirada hasta su fuerza principal"
            , 750, 550, arcade.color.CYBER_YELLOW, font_size=20, anchor_x="center")
        arcade.draw_text("LA VERDADERA BATALLA ESTA POR COMENZAR", SCREEN_WIDTH/2, 400, arcade.color.CYBER_YELLOW, font_size= 40, anchor_x="center")
        arcade.draw_text("<Click para continuar>", SCREEN_WIDTH / 2, 300, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")

    def on_mouse_press(self, _x, _y, _buttom, _modifiers):
        self.window.show_view(self.game_view)


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.backgroundVictoria = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoVictoria.jpg")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        nave_sprite = self.game_view.nave_sprite
        nave_sprite.draw()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.backgroundVictoria)
        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100, arcade.color.CYBER_YELLOW, font_size=50, anchor_x="center")
        arcade.draw_text("Pulsa ENTER para volver al juego", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 , arcade.color.CYBER_YELLOW,font_size=25, anchor_x="center")
        arcade.draw_text("Pulsa R para resetar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.CYBER_YELLOW,font_size=25, anchor_x="center")
        arcade.draw_text("Pulsa M para volver al menu", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.CYBER_YELLOW,font_size=25, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)
        elif key == arcade.key.R:
            game = MyGame()
            self.window.show_view(game)
        elif key == arcade.key.M:
            menu_view = MenuView()
            self.window.show_view(menu_view)


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.backgroundGameOver = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoGameOver.jpg")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.backgroundGameOver)
        arcade.draw_text("GAME OVER", 400, 600, arcade.color.CYBER_YELLOW, 100)
        time_taken_formatted = f"{round(self.time_taken, 2)} segundos"
        arcade.draw_text(f"Tiempo: {time_taken_formatted}", 700, 500, arcade.color.CYBER_YELLOW, font_size=25,
                         anchor_x="center")
        output_total = f"Puntuacion Total: {self.window.total_score} puntos"
        arcade.draw_text(output_total, 563, 430, arcade.color.CYBER_YELLOW, 25)
        arcade.draw_text("Para volver a jugar pulsa: R", 710, 360, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")
        arcade.draw_text("Para volver al menu: M", 710, 290, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")
        arcade.draw_text("Para salir del juego: ESC", 710, 220, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            game = MyGame()
            self.window.show_view(game)
        if key == arcade.key.M:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        if key == arcade.key.ESCAPE:
            exit()

class VictoriaView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.backgroundVictoria = arcade.load_texture(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FondoVictoria.jpg")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1500, 800, self.backgroundVictoria)
        arcade.draw_text("VICTORIA", 500, 600, arcade.color.CYBER_YELLOW, 100)
        time_taken_formatted = f"{round(self.time_taken, 2)} segundos"
        arcade.draw_text(f"Tiempo: {time_taken_formatted}", 700, 500, arcade.color.CYBER_YELLOW, font_size=25,anchor_x="center")
        output_total = f"Puntuacion Total: {self.window.total_score} puntos"
        arcade.draw_text(output_total, 563, 430, arcade.color.CYBER_YELLOW, 25)
        arcade.draw_text("Para volver a jugar pulsa: R", 710, 360, arcade.color.CYBER_YELLOW, font_size=25,anchor_x="center")
        arcade.draw_text("Para volver al menu: M", 710, 290, arcade.color.CYBER_YELLOW, font_size=25, anchor_x="center")
        arcade.draw_text("Para salir del juego: ESC", 710, 220, arcade.color.CYBER_YELLOW, font_size=25,anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            game = MyGame()
            self.window.show_view(game)
        if key == arcade.key.M:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        if key == arcade.key.ESCAPE:
            exit()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    start = StartView()
    window.show_view(start)
    arcade.run()


if __name__ == "__main__":
    main()
