import pygame
class player:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height
        image = pygame.transform.scale(image, (self.width, self.height))
        self.image = image

    def draw(self, x, y):
        screen.blit(self.image, (x, y))

class text:
    def __init__(self, font_size):
        base_font = pygame.font.Font(None, font_size)
        self.base_font = base_font

    def draw(self, text, color, x, y):
        text_surface = self.base_font.render(text, True, color)
        screen.blit(text_surface, (x, y))

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((700, 700))
    wpic = pygame.image.load("pug.png",100)

    white = (255, 255, 255)

    player_one = player(wpic, 700, 700)
    text_draw = text(40)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass

        screen.fill(white)
        player_one.draw(0, 0)

        text_draw.draw("This is my basic 'code art draw' thingy", white, 50, 60)
        text_draw.draw("Make a player object with: ", white, 50, 160)
        text_draw.draw("player = player(IMAGE, WIDTH, HEIGHT)", white, 50, 200)
        text_draw.draw("Make a text object with:", white, 50, 280)
        text_draw.draw("text = text(FONT_SIZE)", white, 50, 320)
        text_draw.draw("Draw a text with:", white, 50, 380)
        text_draw.draw("text.draw(TEXT_TO_DRAW, (R,G,B), X, Y", white, 50, 410)


        pygame.display.update()
