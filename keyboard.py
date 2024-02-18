import pygame

class Keyboard:

    def __init__(self, keys : dict):
        self.k = keys

    def get(self):
        """
        Updates pressed Keys in self.k dict
        """
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.k['quit'] = True

        if pressed_keys[self.k['horizontal'][1][0]]:
            self.k['horizontal'][0] = -1
        if pressed_keys[self.k['horizontal'][1][1]]:
            self.k['horizontal'][0] = 1
        if pressed_keys[self.k['vertical'][1][0]]:
            self.k['vertical'][0] = -1
        if pressed_keys[self.k['vertical'][1][1]]:
            self.k['vertical'][0] =  1

        

        if pressed_keys[pygame.K_ESCAPE]:
            self.k['quit'] = True

        if not pressed_keys[self.k['horizontal'][1][0]] and not pressed_keys[self.k['horizontal'][1][1]]:
            self.k['horizontal'][0] = 0
        if not pressed_keys[self.k['vertical'][1][0]] and not pressed_keys[self.k['vertical'][1][1]]:
            self.k['vertical'][0] = 0

        if pressed_keys[pygame.K_c]:
            self.k['horizontal'][0] = 1
        

        return self.k