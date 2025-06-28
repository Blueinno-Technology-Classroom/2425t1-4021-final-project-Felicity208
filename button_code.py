import pgzrun
from pygame import Rect

#button
class Button:
    def __init__(self, pos, text="button text", padding=20):
        self.text = text
        self.pos = pos
        self.padding = padding
        self.fontsize = 40

        text_width = round(len(text)*self.fontsize)
        text_height = self.fontsize
        self.size = (text_width + padding*2, text_height + padding*2)

        self.rect = Rect((pos[0] - self.size[0], pos[1] - self.size[1]), self.size)

    

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self):
        screen.draw.filled_rect(self.rect, (0, 128, 255))
        screen.draw.text(self.text, center=self.pos, fontsize=40, color=(255, 255, 255))