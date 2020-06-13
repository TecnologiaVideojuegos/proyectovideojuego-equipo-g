import arcade
import random
import math
import os


class Enemy():  # solo existe para ahorrar código
    def __init__(self):
        self.cor_x = random.randint(220, 1280)  # Las coordenadas iniciales de la mayoría de enemigos serán aleatorias
        self.cor_y = 645


class Mosquito(Enemy):  # Clase Mosquito
    def __init__(self):
        super().__init__()
        self.sprite_animacion = [arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Fly.png", center_x=self.cor_x, center_y=self.cor_y),
                                 # Lista que contiene los 3 sprites necesarios para la animación
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "FlyBack.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep +  "images" + os.path.sep + "practicas" + os.path.sep + "FlyBack.png", center_x=self.cor_x, center_y=self.cor_y)]

        self.direc = random.randint(0, 1)  # Variable aleatoria que marcará el sentido inicial del enemigo al aparecer
        self.contador = 0  # Importante para la animación
        self.lista_balas = arcade.SpriteList()  # Lista que contendrá las balas
        self.vidas = 4
        self.bala = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "RedBullet.png", center_x=self.cor_x, center_y=self.cor_y)
        self.sprite = self.sprite_animacion[0]

    def movimiento(self):
        if self.direc == 1:  # cambia las coordenadas del enemigo
            self.cor_x += 3

        elif self.direc == 0:
            self.cor_x -= 3

        if self.cor_x < 220:  # cambia la dirección del enemigo al llegar a los bordes
            self.direc = 1

        elif self.cor_x > 1280:
            self.direc = 0

        self.sprite = self.sprite_animacion[
            self.contador]  # Seleccionamos el sprite a través del contador, de esta forma en cada interacción del bucle este sprite cambiará
        # de esta forma se consigue un mejor rendimiento
        self.sprite.center_x = self.cor_x  # reseteamos coordenadas ya que las hemos cambiado
        self.sprite.center_y = self.cor_y

        self.contador += 1  # sumamos uno al contador, en cada interacción del bucle se sumará uno
        if self.contador == 2:  # para que no salte error "outOfIndex" reseteamos el contador a 0
            self.contador = 0

        if len(self.lista_balas) < 1:  # si la lista está vacía crea una nueva bala
            self.bala = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "RedBullet.png", center_x=self.cor_x, center_y=self.cor_y)
            self.lista_balas.append(self.bala)

        for r in self.lista_balas:  # actualizamos posicion de la bala
            r.center_y -= 5
            if r.center_y <= 0:
                self.lista_balas.remove(r)  # si la bala se sale de la pantalla, se borra de la lista

class Bala_Rebot():
    def __init__(self):
        self.cor_x = random.randint(300, 1000)
        self.cor_Y = 700
        self.direc = 0
        self.sprite_animacion = [arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BalaRebota.png", center_x=self.cor_x, center_y=self.cor_Y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "BalaRebotaCharged.png", center_x=self.cor_x, center_y=self.cor_Y)]
        self.contador = 0
        self.sprite = self.sprite_animacion[0]
        self.vidas = 2

    def movimiento(self):
        if self.direc == 1:  # cambia las coordenadas del enemigo
            self.cor_x += 5

        elif self.direc == 0:
            self.cor_x -= 5

        if self.direc_y == 0:
            self.cor_y -= 5

        elif self.direc_y == 1:
            self.cor_y += 5

        if self.cor_x < 220:  # cambia la dirección del enemigo al llegar a los bordes
            self.direc = 1

        elif self.cor_x > 1280:
            self.direc = 0

        if self.cor_y < 20:
            self.direc_y = 1

        if self.cor_y > 750:
            self.direc_y = 0

        self.contador += 1
        if self.contador % 60 == 0:
            if self.contador_animacion % 2 != 0:
                self.sprite = self.sprite_animacion[1]
                self.contador_animacion += 1

            elif self.contador_animacion % 2 == 0:
                self.sprite = self.sprite_animacion[0]
                self.contador_animacion += 1

        self.sprite.center_x = self.cor_x
        self.sprite.center_y = self.cor_y

class Huevo():
    def __init__(self, coordenada_x, coordenada_y):
        self.cor_x = coordenada_x
        self.cor_y = coordenada_y
        self.contador = 0
        self.nacer = False
        self.vidas = 3
        self.animacion = 0
        self.sprite_animacion = [arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "hueva.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "hueva_1.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "hueva_2.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "hueva_3.png", center_x=self.cor_x, center_y=self.cor_y)]
        self.sprite = self.sprite_animacion[self.animacion]

    def movimiento(self):
        self.contador += 1
        if self.contador % 13 == 0:  # se cambia de animacion cada pocas interacciones
            self.animacion += 1
            if self.animacion == 4:
                 self.animacion = 3
            self.sprite = self.sprite_animacion[self.animacion]

            if self.contador > 60:  # cuando llega el momento, el huevo "nace"
                self.nacer = True

class Mosquito_Elite(Enemy):  # Clase Mosquito De Elite
    def __init__(self):
        self.cor_x = random.randint(220, 1280)  # Las coordenadas iniciales de la mayoría de enemigos serán aleatorias
        self.cor_y = 645
        self.sprite_animacion = [arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "EliteFly.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "EliteFlyBack.png", center_x=self.cor_x, center_y=self.cor_y)]
        self.direc = random.randint(0, 1)  # Variable aleatoria que marcará el sentido inicial del enemigo al aparecer
        self.contador = 0  # Importante para la animación
        self.lista_balas = arcade.SpriteList()  # Lista que contendrá las balas
        self.vidas = 25
        self.tiempo = 0
        self.balas_contador = 0
        self.disparando = False  # booleano que indica si se esta disparando o no
        self.listo_disparo = False  # booleano que indica si se puede disparar o no
        self.hueva = True  # booleano que indica si se puede hacer un huevo o no
        self.lista_crias = []  # lista de huevos que se transformaran en mosquitos
        self.lista_mosquitos = []  # lista de mosquitos
        self.sprite = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "EliteFlySaco.png", center_x=self.cor_x, center_y=self.cor_y - 111)
        # 2 sprites separados, de esta forma se consigue determinar una mejor hit-box
        self.sprite_arriba = self.sprite_animacion[0]
        self.vidas = 25

    def movimiento(self):
        if self.direc == 1:  # cambia las coordenadas del enemigo
            self.cor_x += 4

        elif self.direc == 0:
            self.cor_x -= 4

        if self.cor_x < 300:  # cambia la dirección del enemigo al llegar a los bordes
            self.direc = 1

        elif self.cor_x > 1200:
            self.direc = 0

        self.sprite_arriba = self.sprite_animacion[self.contador]
        # Seleccionamos el sprite a través del contador, de esta forma este sprite cambiará
        # se consigue un mejor rendimiento

        self.sprite_arriba.center_x = self.cor_x  # reseteamos coordenadas ya que las hemos cambiado
        self.sprite.center_x = self.cor_x

        self.tiempo += 1  # sumamos uno al contador, en cada interacción del bucle se sumará uno

        if len(self.lista_crias) > 0:  # si se tienen crias se inicia el procedimiento de nacer
            for s in self.lista_crias:
                s.movimiento()
                if s.nacer:  # si el huevo nace, se elimina de la lista de huevos, se anotan las coordenadas y se
                    # crea un nuevo mosquito
                    nuevo_mosquito = Mosquito()
                    nuevo_mosquito.cor_x = s.cor_x
                    nuevo_mosquito.cor_y = s.cor_y
                    nuevo_mosquito.sprite.center_x = s.cor_x
                    nuevo_mosquito.sprite.center_y = s.cor_y
                    self.lista_mosquitos.append(nuevo_mosquito)
                    self.lista_crias.remove(s)

        if self.tiempo % 3 == 0:  # para que no salte error "outOfIndex" reseteamos el contador
            if self.contador == 1:
                self.contador -= 1
                self.sprite.center_y -= 1
            elif self.contador == 0:
                self.contador += 1
                self.sprite.center_y += 1

        if self.tiempo % 20 == 0:
            if self.listo_disparo:  # 2 booleanos, se consigue que haya un espacio entre oleada y oleada
                if self.disparando:
                    for k in range(3):
                        self.bala = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "EliteFlyBullet.png", center_x=self.cor_x, center_y=self.sprite.bottom)
                        self.bala.change_y = -5
                        if k == 0:
                            self.bala.center_x = self.cor_x + 10
                            self.bala.change_x = 5
                        elif k == 1:
                            self.bala.center_x = self.cor_x - 10
                            self.bala.center_x = -5
                        elif k == 2:
                            self.bala.center_x = self.cor_x
                        self.lista_balas.append(self.bala)
                        if len(self.lista_balas) == 16:
                            self.disparando = False  # cambiamos ambos booleanos
                            self.listo_disparo = False

            elif self.hueva:
                self.hueva = False
                cria = Huevo(self.cor_x, (self.sprite.bottom - 60 + random.randint(0, 120)))
                self.lista_crias.append(cria)


            else:
                aleatorio = random.randint(0, 5)  # se elije de forma aleatoria que va a hacer el enemigo
                if aleatorio == 2:
                    print(aleatorio)
                    self.listo_disparo = True
                elif aleatorio == 3:
                    if len(self.lista_mosquitos) < 8:  # control de plagas
                        self.hueva = True

            if len(self.lista_balas) == 0:
                self.disparando = True  # cuando no haya balas en pantalla, se puede disparar otra vez


            else:  # chekeamos las coordenadas de cada bala
                for k in self.lista_balas:
                    if k.center_y < 0 or k.center_x > 1300 or k.center_x < 200:
                        self.lista_balas.remove(k)

class Trimandibula(Enemy):
    def __init__(self):
        super().__init__()
        self.sprite_animacion = [
            arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Trimandibulaclose.png", center_x=self.cor_x, center_y=self.cor_y),
            arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "TrimandibulaOpen.png", center_x=self.cor_x, center_y=self.cor_y)]
        self.direc = random.randint(0, 1)  # Variable aleatoria que marcará el sentido inicial del enemigo al aparecer
        self.direc_y = 0
        self.contador = 0  # Importante para la animación
        self.lista_balas = arcade.SpriteList()  # Lista que contendrá las balas
        self.sprite = self.sprite_animacion[self.contador]
        self.contador_espera = 0
        self.espera = False
        self.bala = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Trimandibulabullet.png", center_x=self.cor_x, center_y=self.cor_y)
        self.vidas = 5

    def movimiento(self):
        if self.direc == 1:  # cambia las coordenadas del enemigo
            self.cor_x += 5

        elif self.direc == 0:
            self.cor_x -= 5

        if self.direc_y == 0:
            self.cor_y -= 1

        elif self.direc_y == 1:
            self.cor_y += 1

        if self.cor_x <= 220:  # cambia la dirección del enemigo al llegar a los bordes
            self.direc = 1

        elif self.cor_x >= 1280:
            self.direc = 0

        if self.cor_y <= 420:
            self.direc_y = 1

        if self.cor_y >= 750:
            self.direc_y = 0

        self.sprite = self.sprite_animacion[self.contador]  # Seleccionamos el sprite a través del contador, de esta forma el sprite cambia sin alterar
        # el rendimiento
        # de esta forma se consigue un mejor rendimiento
        self.sprite.center_x = self.cor_x  # reseteamos coordenadas ya que las hemos cambiado
        self.sprite.center_y = self.cor_y

        if self.espera:
            self.contador_espera += 1
            if self.contador_espera == 20:
                self.contador_espera = 0
                self.espera = False

        if len(self.lista_balas) < 1 and not self.espera:  # si la lista está vacía crea una nueva bala
            self.bala = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "TriMandibulaBullet.png", center_x=self.cor_x, center_y=self.cor_y)
            self.bala.change_y = -9
            self.lista_balas.append(self.bala)
            self.contador = 1 #cambia el sprite cuando el mountro dispara
        if len(self.lista_balas) == 1:
            self.lista_balas[0].center_x = self.cor_x
            if self.lista_balas[0].center_y <= 0:
                self.lista_balas.pop()  # elimina la bala
                self.espera = True  # esto otorga un tiempo entre disparo y disparo
                self.contador = 0  # cuando termina de disparar, cambia el sprite

class Seguimiento():
    def __init__(self):
        self.cor_y = 800
        self.cor_x = random.randint(220, 1280)
        self.sprite = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "TrimandibulaBullet.png", center_x=self.cor_x, center_y=self.cor_y)
        self.coord_x = 750
        self.coord_y = 0
        self.variacion = 0

    def trakeo(self, sprite):
        self.coord_x = sprite.center_x + random.randint(self.variacion * (-1), self.variacion)
        self.coord_y = sprite.center_y + random.randint(self.variacion * (-1), self.variacion)

        if self.coord_x <= self.cor_x:  # Condiciones para el algoritmo de seguimiento
            self.cor_x -= 5

        elif self.coord_x > self.cor_x:
            self.cor_x += 5

        if self.coord_y <= self.cor_y:
            self.cor_y -= 5

        elif self.cor_y < self.coord_y:
            self.cor_y += 5

        self.sprite.angle = self.calcula_angulo()  # cambiamos las coordenadas y ángulos del sprite
        self.sprite.center_x = self.cor_x
        self.sprite.center_y = self.cor_y

    def calcula_angulo(self):
        cateto_x = self.cor_y - self.coord_y
        cateto_y = self.coord_x - self.cor_x
        hipotenusa = math.hypot(cateto_x, cateto_y)
        if hipotenusa == 0:  # Evitamos dividir entre 0
            hipotenusa = 1
        angulo_x = math.degrees(math.acos(cateto_x / hipotenusa))
        if cateto_y < 0:  # Cambiamos el angulo por sus opuestos negativos si hace falta
            if angulo_x > 90:
                angulo_x += ((180 - angulo_x) * 2)
            elif angulo_x <= 90:
                angulo_x = 360 - angulo_x

        return angulo_x

class Cria(Seguimiento):
    def __init__(self):
        super().__init__()
        self.sprite_animacion = [arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Cria.png", center_x=self.cor_x, center_y=self.cor_y),
                                 arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Cria_2.png", center_x=self.cor_x, center_y=self.cor_y)]
        self.contador = 0
        self.variacion = 10
        self.vidas = 1

    def movimiento(self, sprite):
        self.contador += 1  # lleva a cabo la animacion
        self.sprite = self.sprite_animacion[self.contador]
        if self.contador == 1:
            self.contador = -1

        super().trakeo(sprite)  # llamamos a la funcion de la clase superior

class NaveSOS(Enemy):
    def __init__(self):
        super().__init__()
        self.cor_x = random.randint(300, 1000)
        self.cor_y = 800
        self.vidas = 1
        self.sprite = arcade.Sprite(":resources:" + os.path.sep + "images" + os.path.sep + "practicas" + os.path.sep + "Nave_ayuda.png", 1.25)

    def movimiento(self):
        self.cor_y -= 3
        self.sprite.center_x = self.cor_x
        self.sprite.center_y = self.cor_y

