import os
import random
import pygame
from Board import Board
from AnimalFactory.BabyDragonFactory import BabyDragonFactory
from AnimalFactory.BatFactory import BatFactory
from AnimalFactory.CarFactory import CarFactory
from AnimalFactory.PirateDragonFactory import PirateDragonFactory
from AnimalFactory.SalamanderFactory import SalamanderFactory
from AnimalFactory.SpiderFactory import SpiderFactory
from AnimalType import AnimalType
from GameProgression import GameProgression
from Tiles.VolcanoTile import VolcanoTile
from Volcanos.CaveCutVolcano import CaveCutVolcano
from Volcanos.NonCaveCutVolcano import NonCaveCutVolcano
from Tiles.CaveTile import CaveTile
from ChitCard import ChitCard
from Players.Player import Player
from ClickedState import clickedState
from Players.PlayerManager import PlayerManager
from Save.SaveManager import SaveManager

random.seed(9999) #Remove this later
class GameRunning:
    '''
    Class for the GameRunning
    '''

    def __init__(self, volcanos: list[CaveCutVolcano, NonCaveCutVolcano], caves: list[CaveTile], chitCards: list[ChitCard], players: list[Player]) -> None:
        '''
        Constructor for the GameRunning
        
        Inputs:
        - caveCutVolcanos: List of CaveCutVolcanos on the Board (list[CaveCutVolcano])
        - nonCaveCutVolcanos: List of NonCaveCutVolcanos on the Board (list[NonCaveCutVolcano])
        - caves: List of Caves on the Board (list[CaveTile])
        - chitCards: List of ChitCards on the Board (list[ChitCard])
        - players: List of Players on the Board (list[Player])
        '''
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((800, 630))
        
        # random.seed(9999) #Remove this later

        self.chitCards = chitCards

        self.players = players

        self.playerManager = PlayerManager()
        self.playerManager.original_player = self.players[0]

        self.volcano = volcanos
        self.caves = caves

        for player in self.players:
            self.playerManager.add_player(player)
        
        tileAnimals = []
        i = -1
        j = 0
        
        # Define the starting angle
        start_angle = 345

        amount  = 0

        for volcano in volcanos:
            amount += len(volcano.get_volcano_tiles())

        # amount = len(volcanos) * 3

        # Define the angles for the 24 circles
        volcano_angles = [(start_angle + i * (360 / amount)) % 360 for i in range(amount)]
        
        font = pygame.font.Font(None, 50)
        cave_angles = []
        
        cave_cut_encountered = False
        for volcano in self.volcano:
            for tile in volcano.get_volcano_tiles():
                tileAnimals.append(tile.get_animal())
                for player in self.players:
                    if tile == volcano.get_cave_cut_tile():
                        if not cave_cut_encountered:
                            i += 1
                            cave_cut_encountered = True    # Set the flag to True so that we only increment i once per cave cut volcano

                        # Create a new tile object
                        new_tile = tile.clone()
                        new_tileAfter = tile.clone()
                        player.get_gameProgress().insert(new_tile)
                        new_tile.set_angle(volcano_angles[j])   # because we have a circular board, we need to set different angles for different tiles
                        player.get_gameProgress().insert(caves[i])
                        caves[i].set_angle(volcano_angles[j])
                        if volcano_angles[j] not in cave_angles:
                            cave_angles.append(volcano_angles[j])
                        player.get_gameProgress().insert(new_tileAfter)
                        new_tileAfter.set_angle(volcano_angles[j])
                    else:
                        new_tile = tile.clone()
                        player.get_gameProgress().insert(new_tile)
                        new_tile.set_angle(volcano_angles[j])
                
                j+=1
            cave_cut_encountered = False  # Reset the flag for the next iteration of the outer loop

        i=0     # resetting i so we can iterate through players
        while i < len(self.players):
            self.players[i].get_gameProgress().set_current(caves[i])
            self.players[i].set_homeTileAngle(cave_angles[i])
            i+=1

        self.board = Board(self.volcano, caves, chitCards, self.players, tileAnimals, self.screen, cave_angles)

        self.clickedState = clickedState(self.playerManager, self.board)

         #Chit Cards
        card_width, card_height = 40, 40
        start_x = 800 / 2 - 55 - 2.6 * card_width
        start_y = 630 / 2 + 25 - 2.6 * card_height
        spacing = 15
        # Blit the chit cards in 3 rows of 4
        for i, chit_card in enumerate(self.chitCards):
            row = i // 6
            col = i % 6
            x = start_x + col * (card_width + spacing)
            y = start_y + row * (card_height + spacing)
            self.clickedState.addPosition((x, y, card_width, card_height), chit_card) 

    def run(self) -> None:
        '''
        Run the Game
        
        '''
        # Set up color
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Game loop
        running = True


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.clickedState.handle_event(event)
            
            
                
            # Fill the background with white
            try:
                self.screen.fill(WHITE)
            except:
                running = False
                break

            # Draw the quit button in the top right
            quit_button = pygame.draw.rect(self.screen, RED, (687, 8, 80, 30))
            quit_text = pygame.font.Font(None, 36).render('Quit', True, BLACK)
            self.screen.blit(quit_text, (697, 10))
            save_button = pygame.draw.rect(self.screen, GREEN, (687, 42, 80, 30))
            save_text = pygame.font.Font(None, 36).render('Save', True, BLACK)
            self.screen.blit(save_text, (697, 44))

            # Draw the player names in the top left 
            for i in range(len(self.players)):
                BLACK = (0,0,0)
                quit_text = pygame.font.Font(None, 36).render(f"{self.players[i].get_name()}: {self.players[i].get_ratioNum()}/{self.players[i].get_ratioDen()}", True, BLACK)
                self.screen.blit(quit_text, (50, 30*i))
                scaled_image = pygame.transform.scale(self.players[i].get_image(), (25, 25))
                self.screen.blit(scaled_image, (20, 30 * i))


#--------------------------------------------------SAVING GAME----------------------------------------------------------
            # Check if the save button has been pressed --> Load the old data to a JSON file
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if quit_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                running = False

            if save_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                fileName = ""
                input_active = True  # Flag to indicate if text input is active

                # Display input prompt on the screen
                self.screen.fill((255, 255, 255))
                font = pygame.font.Font(None, 50)
                question_text = "Please Enter File Character to be Loaded:"
                text_surface = font.render(question_text, True, (0, 0, 0))
                questiontext_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 200))
                self.screen.blit(text_surface, questiontext_rect)

                pygame.display.flip()

                while input_active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                input_active = False
                            elif event.key == pygame.K_BACKSPACE:
                                fileName = fileName[:-1]  # Remove last character
                            elif event.unicode.isalnum() and len(fileName) < 20:  # Limiting file name to 20 alphanumeric characters
                                fileName += event.unicode
                            if not input_active:
                                break

                    # Render file name input
                    self.screen.fill((255, 255, 255))
                    self.screen.blit(text_surface, questiontext_rect)
                    input_surface = font.render(fileName, True, (0, 0, 0))
                    input_rect = input_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                    self.screen.blit(input_surface, input_rect)

                    pygame.display.flip()

                # Saving game data with file name provided
                save_manager = SaveManager()
                save_manager.saveAll(self.chitCards, self.volcano, self.playerManager, self.caves, fileName)
                running = False

            self.board.draw()
            pygame.display.set_caption(f"{self.playerManager.get_current_player().name}")

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()




#--------------------------------------------------MAIN----------------------------------------------------------
if __name__ == "__main__":
    players = [Player("Player 1", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenBlue.png')),
                Player("Player 2", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenGreen.png')),
                Player("Player 3", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenOrange.png')),
                Player("Player 4", GameProgression(),  os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenRed.png'))]


    salamanderFactory = SalamanderFactory()
    batFactory = BatFactory()
    spiderFactory = SpiderFactory()
    babyDragonFactory = BabyDragonFactory()
    pirateDragonFactory = PirateDragonFactory()
    carFactory = CarFactory()


    caveCutVolcanos = [CaveCutVolcano([VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                                        VolcanoTile(batFactory.new(AnimalType.TILE)), 
                                        VolcanoTile(spiderFactory.new(AnimalType.TILE))]),

            CaveCutVolcano([VolcanoTile(salamanderFactory.new(AnimalType.TILE)), 
                            VolcanoTile(spiderFactory.new(AnimalType.TILE)), 
                            VolcanoTile(batFactory.new(AnimalType.TILE))]),

            CaveCutVolcano([VolcanoTile(spiderFactory.new(AnimalType.TILE)), 
                            VolcanoTile(salamanderFactory.new(AnimalType.TILE)), 
                            VolcanoTile(babyDragonFactory.new(AnimalType.TILE))]),

            CaveCutVolcano([VolcanoTile(batFactory.new(AnimalType.TILE)), 
                            VolcanoTile(spiderFactory.new(AnimalType.TILE)), 
                            VolcanoTile(babyDragonFactory.new(AnimalType.TILE))])]


    nonCaveCutVolcanos = [NonCaveCutVolcano([VolcanoTile(spiderFactory.new(AnimalType.TILE)), 
                                                VolcanoTile(batFactory.new(AnimalType.TILE)), 
                                                VolcanoTile(salamanderFactory.new(AnimalType.TILE))]), 

                        NonCaveCutVolcano([VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                                            VolcanoTile(salamanderFactory.new(AnimalType.TILE)), 
                                            VolcanoTile(batFactory.new(AnimalType.TILE))]),

                        NonCaveCutVolcano([VolcanoTile(batFactory.new(AnimalType.TILE)), 
                                            VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                                            VolcanoTile(salamanderFactory.new(AnimalType.TILE))]),

                        # NonCaveCutVolcano([VolcanoTile(batFactory.new(AnimalType.TILE)), 
                        #                     VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                        #                     VolcanoTile(salamanderFactory.new(AnimalType.TILE))]),

                        NonCaveCutVolcano([VolcanoTile(salamanderFactory.new(AnimalType.TILE)), 
                                        VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                                        VolcanoTile(spiderFactory.new(AnimalType.TILE)),
                                        VolcanoTile(spiderFactory.new(AnimalType.TILE)),
                                        VolcanoTile(spiderFactory.new(AnimalType.TILE)),
                                        VolcanoTile(spiderFactory.new(AnimalType.TILE))])]

    caveCutVolcanos[0].set_cave_cut_tile(0)
    caveCutVolcanos[1].set_cave_cut_tile(0)
    caveCutVolcanos[2].set_cave_cut_tile(0)
    caveCutVolcanos[3].set_cave_cut_tile(0)

    caves = [CaveTile(salamanderFactory.new(AnimalType.CAVE)), 
                CaveTile(batFactory.new(AnimalType.CAVE)), 
                CaveTile(spiderFactory.new(AnimalType.CAVE)), 
                CaveTile(babyDragonFactory.new(AnimalType.CAVE))]

    chitCards = [ChitCard(salamanderFactory.new(AnimalType.CHITCARD_1)), 
                    ChitCard(batFactory.new(AnimalType.CHITCARD_1)), 
                    ChitCard(spiderFactory.new(AnimalType.CHITCARD_1)), 
                    ChitCard(babyDragonFactory.new(AnimalType.CHITCARD_1)),
                ChitCard(salamanderFactory.new(AnimalType.CHITCARD_2)), 
                ChitCard(batFactory.new(AnimalType.CHITCARD_2)), 
                ChitCard(spiderFactory.new(AnimalType.CHITCARD_2)), 
                ChitCard(babyDragonFactory.new(AnimalType.CHITCARD_2)),
                ChitCard(salamanderFactory.new(AnimalType.CHITCARD_3)), 
                ChitCard(batFactory.new(AnimalType.CHITCARD_3)), 
                ChitCard(spiderFactory.new(AnimalType.CHITCARD_3)), 
                ChitCard(babyDragonFactory.new(AnimalType.CHITCARD_3)),
                ChitCard(pirateDragonFactory.new(AnimalType.REGRESSIVE_1)),
                ChitCard(pirateDragonFactory.new(AnimalType.REGRESSIVE_1)),
                ChitCard(pirateDragonFactory.new(AnimalType.REGRESSIVE_2)),
                ChitCard(pirateDragonFactory.new(AnimalType.REGRESSIVE_2)),
                ChitCard(carFactory.new(AnimalType.REGRESSIVE_TRANSPORT)), 
                ChitCard(carFactory.new(AnimalType.REGRESSIVE_TRANSPORT))]

    random.shuffle(caveCutVolcanos) #Randomise the order of the caveCutVolcanos
    random.shuffle(nonCaveCutVolcanos) #Randomise the order of the nonCaveCutVolcanos
    random.shuffle(caves)
    random.shuffle(chitCards)


    # # putting all volcanos inside 1 list to set the board in that order
    # volcanos = []
    # for caveCut, nonCaveCut in zip(caveCutVolcanos, nonCaveCutVolcanos):
    #     volcanos.append(caveCut)
    #     volcanos.append(nonCaveCut)

    volcanos = caveCutVolcanos + nonCaveCutVolcanos

    game_running_instance = GameRunning(volcanos, caves, chitCards, players, False)
    game_running_instance.run()
