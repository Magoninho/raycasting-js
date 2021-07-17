# This is just me trying to figure out an way of rendering sprites
# Perhaps I'm not going to make it because I'm just tired of this project

class Sprite:
    def __init__(self):
        self.x = x
        self.y = y
        self.angle = angle
        self.distance = distance


    def calculate_angle(self):
        vecX = self.x - player.x
        vecY = self.y - player.y

        angle = atan2(vecX, vecY)
        angle_diference = player.angle - angle
