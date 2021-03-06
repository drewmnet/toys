import pygame


class Theme:
    def __init__(self):
        # ui theme
        # colour palette; GameBoy style
        self.ui_palette = { "light": (0xfa, 0xfb, 0xf6),
                         "shade": (0xc6, 0xb7, 0xbe),
                         "grey": (0x56, 0x5a, 0x75),
                         "dark": (0x0f, 0x0f, 0x1b)
                       }
        # dialogue attributes
        self.ui_background = self.ui_palette["grey"] # None for total transparency
        self.ui_padding = 5
        # fonts
        self.ui_basic_font = pygame.font.Font("dpcomic.ttf", 28)

class Selector:
    def __init__(self, labels, geometry, theme):
        self.theme = theme # replace ui with game
        self.labels = labels # a list strings
        
        self.font_height = theme.ui_basic_font.get_height()
        self.padding = theme.ui_padding
        height = len(self.labels) * self.font_height + self.padding + 2
        self.rect = list(geometry + tuple([height])) # (x, y, w) + (h)
        
        self.value = 0
        
    def render_label(self, label, value):
        if value == self.value:
            colour = self.theme.ui_palette["light"]
        else:
            colour = self.theme.ui_palette["shade"]
        return self.theme.ui_basic_font.render(label, 0, colour)
        
    def render(self, surface):
        pygame.draw.rect(surface, self.theme.ui_palette["grey"], self.rect)
        for i, l in enumerate(self.labels):
            label = self.render_label(l, i)
            x = self.rect[0] + self.padding
            y = self.rect[1] + self.font_height * i + self.padding
            surface.blit(label, (x, y))
    
    def change_value(self, value):
        self.value = (self.value + value) % len(self.labels)

class PlayerParty:
    
    positions = [ (10, 10), (30, 30), (50, 50) ]


    def __init__(self, members: list, selector: Selector):
        self.members = members
        self.selector = selector
        self.member = 0

    def start(self):
        self.member = 0
        self.selector.rect[0] = self.positions[self.member][0]
        self.selector.rect[1] = self.positions[self.member][1]

    def command(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector.change_value(1)
                elif event.key == pygame.K_UP:
                    self.selector.change_value(-1)
                elif event.key == pygame.K_RCTRL: # 'A' button
                    print(f"{self.members[self.member]} selects {self.selector.labels[self.selector.value]}")
                    self.selector.value = 0
                    self.member += 1
                    if self.member < len(self.members):
                        self.selector.rect[0] = self.positions[self.member][0]
                        self.selector.rect[1] = self.positions[self.member][1]

                
                # remove
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    def update(self):
        self.command()
        if self.member == len(self.members):
            print("Enemy commands\nInitiative\nCombat\nStatus Effects\n")
            pygame.time.wait(4000)
            pygame.quit()
            exit()
            
    def render(self, display):
        self.selector.render(display)

pygame.init()
display = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

theme = Theme()
battle_selector = Selector(["Fight","Run"], (10,10,100), theme)
party = [ "Elaine", "Talin", "AVAT5" ]
player_party = PlayerParty(party, battle_selector)

running = True
while running:
    clock.tick(60)

    player_party.update()
    player_party.render(display)
    pygame.display.flip()
