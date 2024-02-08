import pygame 
pygame.font.init

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class Button:
    def __init__(self, x, y, width, height, text, bg_color, text_color,actif):
        self.pos = (x, y)
        self.size = (width, height)
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), height)
        self.text_surf = self.font.render(f"{text}", True, text_color)
        self.button_surf = pygame.Surface((width, height)).convert()
        self.button_surf.fill(bg_color)
        self.actif = actif


    def verif_render(self, window):
        if self.actif == True:

            window.blit(self.button_surf, (self.pos[0], self.pos[1]))
            window.blit(self.text_surf, (self.pos[0] + 1, self.pos[1] + 5))

    def clicked(self, events):
        if self.actif == True:

            mouse_pos = pygame.mouse.get_pos()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_surf.get_rect(topleft=self.pos).collidepoint(mouse_pos[0], mouse_pos[1]):
                        return True
            return False
    
class InputBox:

    def __init__(self, x, y, w, h,FONT, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event,FONT):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



class label:
    def __init__(self,x,y,largeur,hauteur,text):
        self.pos = (x,y)
        self.size = (largeur, hauteur)
        self.text = text
    
