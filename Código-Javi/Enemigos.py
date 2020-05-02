import arcade
import random


class Enemy():  # solo existe para ahorrar código
    def __init__(self):
        self.cor_x = random.randint(220, 1280)  # Las coordenadas iniciales de la mayoría de enemigos serán aleatorias
        self.cor_y = random.randint(420, 780)


class Mosquito(Enemy):  # Clase Mosquito
    def __init__(self):
        super().__init__()
        self.sprite = [arcade.Sprite("sprites/Fly.png", center_x=self.cor_x, center_y=self.cor_y),
                       # Lista que contiene los 3 sprites necesarios para la animación
                       arcade.Sprite("sprites/FlyBack.png", center_x=self.cor_x, center_y=self.cor_y),
                       arcade.Sprite("sprites/FlyBack.png", center_x=self.cor_x, center_y=self.cor_y)]

        self.direc = random.randint(0, 1)  # Variable aleatoria que marcará el sentido inicial del enemigo al aparecer
        self.contador = 0  # Importante para la animación
        self.lista_balas = arcade.SpriteList()  # Lista que contendrá las balas

    def movimiento(self):
        if self.direc == 1:  # cambia las coordenadas del enemigo
            self.cor_x += 3

        elif self.direc == 0:
            self.cor_x -= 3

        if self.cor_x < 220:  # cambia la dirección del enemigo al llegar a los bordes
            self.direc = 1

        elif self.cor_x > 1280:
            self.direc = 0

        self.prueba = self.sprite[self.contador]  # Seleccionamos el sprite a través del contador, de esta forma en cada interacción del bucle este sprite cambiará
        # de esta forma se consigue un mejor rendimiento
        self.prueba.center_x = self.cor_x  # reseteamos coordenadas ya que las hemos cambiado
        self.prueba.center_y = self.cor_y

        self.contador += 1  # sumamos uno al contador, en cada interacción del bucle se sumará uno
        if self.contador == 2:  # para que no salte error "outOfIndex" reseteamos el contador a 0
            self.contador = 0

        if len(self.lista_balas) < 1:  # si la lista está vacía crea una nueva bala
            self.bala = arcade.Sprite("sprites/RedBullet.png", center_x=self.cor_x, center_y=self.cor_y)
            self.lista_balas.append(self.bala)

        for r in self.lista_balas:  # actualizamos posicion de la bala
            r.center_y -= 5
            if r.center_y <= 0:
                self.lista_balas.remove(r)   #si la bala se sale de la pantalla, se borra de la lista
