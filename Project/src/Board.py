import math
import pygame
import os
from Volcanos.CaveCutVolcano import CaveCutVolcano
from Volcanos.NonCaveCutVolcano import NonCaveCutVolcano
from Tiles.CaveTile import CaveTile
from ChitCard import ChitCard
from Players.Player import Player
from Animals.Animal import Animal

class Board:
    '''
    Class for the Board
    '''

    def __init__(self, volcanos, caves: list[CaveTile], chitCards: list[ChitCard], players: list[Player], tileAnimals: list[Animal], screen, cave_angles) -> None:
        '''
        Constructor for the Board
        
        Inputs:
        - caveCutVolcano: List of CaveCutVolcanos on the Board (list[CaveCutVolcano])
        - nonCaveCutVolcano: List of NonCaveCutVolcanos on the Board (list[NonCaveCutVolcano])
        - caves: List of Caves on the Board (list[CaveTile])
        - chitCards: List of ChitCards on the Board (list[ChitCard])
        - players: List of Players on the Board (list[Player])
        - tileAnimals: List of Animals on the Board (list[Animal])
        '''
        self.volcano = volcanos
        self.caves = caves
        self.chitCards = chitCards
        self.players = players
        self.tileAnimals = tileAnimals
        self.screen = screen
        self.cave_angles = cave_angles

        
    def draw(self) -> None:
        '''
        Draw the Board on the PyGame screen
        '''

        

        center_x, center_y = 800 / 2, 630 / 2

        # else:
        volcanoHole = pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'VolcanoCardsAll.png'))
        x = center_x - volcanoHole.get_width() / 2
        y = center_y - volcanoHole.get_height() / 2
        self.screen.blit(volcanoHole, (x, y))
        caveHole = pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveHole.png'))
        caveHole = pygame.transform.scale(caveHole, (70, 70))  # Scale the caveHole image to the same size as the animal_image

        #Volcano Animals
        volcano_radius = 210
        start_angle = 345

        amount  = 0
        for volcano in self.volcano:
            amount += len(volcano.get_volcano_tiles())

        # Define the angles for the 24 circles
        angles = [(start_angle + i * (360 / amount)) % 360 for i in range(amount)]

        # Blit the animals in the circle
        for angle, animal in zip(angles, self.tileAnimals):
            animal_image = animal.get_image()
            animal_image = pygame.transform.scale(animal_image, (30, 30))
            x = center_x + volcano_radius * math.cos(math.radians(angle)) - animal_image.get_width() / 2
            y = center_y + volcano_radius * math.sin(math.radians(angle)) - animal_image.get_height() / 2
            rotated_animal = pygame.transform.rotate(animal_image, -angle) # Rotate the animal image so that it faces the center of the circle (Does not work as intended)
            self.screen.blit(rotated_animal, (int(x), int(y)))

        #Caves Animals
        # cave_angles = self.cave_angles
        cave_radius = 275
        # Blit the animals in the caves
        for angle, cave in zip(self.cave_angles, self.caves):
            animal_image = cave.get_animal().get_image()
            animal_image = pygame.transform.scale(animal_image, (40, 40))
            x = center_x + cave_radius * math.cos(math.radians(angle)) - animal_image.get_width() / 2
            y = center_y + cave_radius * math.sin(math.radians(angle)) - animal_image.get_height() / 2
            # if not self.base:
            caveHole_x = x + animal_image.get_width() / 2 - caveHole.get_width() / 2
            caveHole_y = y + animal_image.get_height() / 2 - caveHole.get_height() / 2
            self.screen.blit(caveHole, (int(caveHole_x), int(caveHole_y)))
            self.screen.blit(animal_image, (int(x), int(y)))
            
            
        
        #ChitCard Hole
        chitCardHole = pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCardHole.png'))
        x = center_x - chitCardHole.get_width() / 2
        y = center_y - chitCardHole.get_height() / 2
        self.screen.blit(chitCardHole, (x, y))
        
        #Chit Cards
        card_width, card_height = 40, 40
        start_x = center_x - 55 - 2.6 * card_width
        start_y = center_y + 25 - 2.6 * card_height
        spacing = 15
        # Blit the chit cards in 6 rows of 3
        for i, chit_card in enumerate(self.chitCards):
            row = i // 6
            col = i % 6
            x = start_x + col * (card_width + spacing)
            y = start_y + row * (card_height + spacing)
            if chit_card.isFlipped():
                chit_card_image = chit_card.get_animal().get_image()
            else:
                chit_card_image = chit_card.getClosedImage()
            chit_card_image = pygame.transform.scale(chit_card_image, (card_width, card_height))
            self.screen.blit(chit_card_image, (int(x), int(y)))

        #Players
        player_radius = 225
        for player in self.players:
            player_image = player.get_image()
            player_image = pygame.transform.scale(player_image, (40, 40)).convert_alpha()
            if player.get_gameProgress().get_current_tile().check_cave():
            # if player.get_gameProgress().get_previous_tile().get_angle() in cave_angles and player.get_gameProgress().get_next_tile().get_angle() in cave_angles:
                x = center_x + cave_radius * math.cos(math.radians(player.get_gameProgress().get_current_tile().get_angle())) - player_image.get_width() / 2
                y = center_y + cave_radius * math.sin(math.radians(player.get_gameProgress().get_current_tile().get_angle())) - player_image.get_height() / 2
            else:
                x = center_x + player_radius * math.cos(math.radians(player.get_gameProgress().get_current_tile().get_angle())) - player_image.get_width() / 2
                y = center_y + player_radius * math.sin(math.radians(player.get_gameProgress().get_current_tile().get_angle())) - player_image.get_height() / 2
            self.screen.blit(player_image, (int(x), int(y)))

        # Update the display
        pygame.display.flip()

 
    def drawWinning(self, player: Player) -> None:
        '''
        Draw the Winning Screen
        
        Inputs:
        - player: Player that won (Player)
        '''
            # Create the font and text surface
        font = pygame.font.Font(None, 50)
        text = f"{player.get_name()} has won the game!"
        text_surface = font.render(text, True, (0, 0, 0))

        # Create the text box
        text_rect = text_surface.get_rect(center=(800 // 2, 630 // 2))
        box_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)

        # Draw the text box and text
        pygame.draw.rect(self.screen, (255, 255, 255), box_rect)
        self.screen.blit(text_surface, text_rect)

        # Update the screen
        pygame.display.flip()

        # Wait for 5 seconds
        pygame.time.wait(5000)

        # Redraw the game board to remove the box
        self.draw()

