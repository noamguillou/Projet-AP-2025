"""
simplest possible starting code with one motionless boid
display a single object, inert, at (100, 100)
"""

import arcade
import math
import random

BACKGROUND = arcade.color.ALMOND

class Boid(arcade.SpriteCircle):
    def __init__(self, position_x: float, position_y: float, angle: float, speed: float = 1.0, etat:  bool):
        super().__init__(5, arcade.color.BLUE, False)
        self.center_x = position_x
        self.center_y = position_y
        self.angle = angle
        self.speed = speed
        etat = False


   # def move_left(self):
    #    self.angle -= 5
    
    #def move_right(self):
    #    self.angle += 5
    
    #def move(self):
        """
        Ceci va permettre de faire bouger mes boids
        """
    #   self.center_x += math.cos(self.angle_radian()) * self.speed
    #   self.center_y -= math.sin(self.angle_radian()) * self.speed

    def angle_radian(self):
        return self.angle / 180 * math.pi
    
    def accelerate(self):
        self.speed += 0.1

class Window(arcade.Window):

    def __init__(self):
        super().__init__(800, 800, "My first boid")
        arcade.set_background_color(BACKGROUND)
        self.set_location(800, 100)

        N = 50  # Nombre de boids
        for k in range(N):
        self.boids = [Boid(100, 600, 10), Boid(90, 500, -20, 2)]

        self.sprites = arcade.SpriteList()
        for boid in self.boids:
            self.sprites.append(boid)

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        for boid in self.boids:
            boid.move()
        self.sprites.update()

window = Window()
arcade.run()


def distance (p1,p2) : 
    return math.sqrt( (p1.center_x - p2.center_x)**2 + (p1.center_y - p2.center_y)**2 )



def test_contacte (liste_personnes, rayon_personne) : 
    personnes_en_contacte = []
    for i in range (len (liste_personnes)) : 
        for j in range (i+1, len (liste_personnes)) : 
            if distance (liste_personnes[i], liste_personnes[j]) < 2*rayon_personne : 
                personnes_en_contacte.append ( (liste_personnes[i], liste_personnes[j]) )
    return personnes_en_contacte 

def contamination (personne_en_contacte, p_contamination) : 
    for (p1, p2) in personne_en_contacte : 
        if p1.etat == True and p2.etat == False : 
            if random.radom() < p_contamination : 
                p2.etat = True
        elif p2.etat == True and p1.etat == False : 
            if random.radom() < p_contamination : 
                p1.etat = True