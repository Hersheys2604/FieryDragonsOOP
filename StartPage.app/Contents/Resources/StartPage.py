import pygame
from Colours import Colours
import os
import random
from AnimalFactory.BatFactory import BatFactory
from AnimalFactory.BabyDragonFactory import BabyDragonFactory
from AnimalFactory.SalamanderFactory import SalamanderFactory
from AnimalFactory.SpiderFactory import SpiderFactory
from AnimalFactory.PirateDragonFactory import PirateDragonFactory
from AnimalFactory.CarFactory import CarFactory
from Volcanos.CaveCutVolcano import CaveCutVolcano
from Volcanos.NonCaveCutVolcano import NonCaveCutVolcano
from Tiles.VolcanoTile import VolcanoTile
from Tiles.CaveTile import CaveTile
from AnimalType import AnimalType
from ChitCard import ChitCard
from GameProgression import GameProgression
from Players.Player import Player
from GameRunning import GameRunning
from LoadManager import LoadManager

class StartGame:
    """
    This class is to set up the prescreen of the game where we decide how many players will be playing
    """

    players = [Player("Player 1", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenBlue.png')),
            Player("Player 2", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenGreen.png')),
            Player("Player 3", GameProgression(), os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenOrange.png')),
            Player("Player 4", GameProgression(),  os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'playerTokenRed.png'))]

    def __init__(self) -> None:
        """
        Initialising StartGame class
        """
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((625, 625))
    
    def clear_screen(self):
        """
        Sets the screen to a white colour
        """
        self.screen.fill((128, 128, 128))  # Clear the screen with white color

    def get_player_name(self, player_number):
        """
        Asks the player for their name
        
        Inputs:
        - player_number: The number associated with that player (order of turn)
        
        Returns:
        - player_name: The name of the player as a str
        """
        font = pygame.font.Font(None, 50)
        player_name = ""
        
        # Storing inputs from the player
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return player_name
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Remove last character
                    else:
                        player_name += event.unicode

            # Displaying such input on the screen
            self.clear_screen()
            input_surface = font.render(player_name, True, (255, 255, 255))
            input_rect = input_surface.get_rect(center=(625 // 2, 625 // 2))
            question_text = f"Please Enter Player {player_number} Name:"
            text_surface = font.render(question_text, True, (0, 0, 0))
            questiontext_rect = text_surface.get_rect(center=(625//2, 200))
            self.screen.blit(text_surface, questiontext_rect)
            self.screen.blit(input_surface, input_rect)
            pygame.display.flip()

    def drawHome(self):
        """
        Displays the home screen and allows players to select how many will be playing
        """

        running = True
        new_game_started = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            FONT_SIZE = 50

            self.screen.fill(Colours.WHITE.value)

            # Calculate the center coordinates
            grid_center_x = 625 // 2
            grid_center_y = 625 // 2

            # Define the button dimensions
            button_width = 300
            button_height = 80

            # Calculate the button positions
            new_game_button_y = grid_center_y - button_height // 2 - 50
            quit_button_y = grid_center_y + button_height // 2 + 50

            # Draw the "New Game" button
            new_game_button = pygame.draw.rect(self.screen, Colours.GREY.value, (grid_center_x - button_width // 2, new_game_button_y, button_width, button_height))
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render("New Game", True, Colours.BLACK.value)
            text_rect = text.get_rect(center=new_game_button.center)
            self.screen.blit(text, text_rect)

            load_game_button = pygame.draw.rect(self.screen, Colours.GREY.value, (grid_center_x - button_width // 2, new_game_button_y - button_height - 30, button_width, button_height))
            textLoad = font.render("Load Old Game", True, Colours.BLACK.value)
            text_rect = textLoad.get_rect(center=load_game_button.center)
            self.screen.blit(textLoad, text_rect)
            # Check if the load button has been pressed
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            #-------------------------------------------------LOADING GAME-----------------------------------------------------
            # loading the game
            if load_game_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                fileName = ""
                self.screen.fill((255, 255, 255))
                font = pygame.font.Font(None, 50)
                question_text = "Enter File Name to be Loaded:"
                text_surface = font.render(question_text, True, (0, 0, 0))
                questiontext_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 200))
                self.screen.blit(text_surface, questiontext_rect)

                pygame.display.flip()
                input_active = True
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

                self.loadGame(fileName) #Need to change this to be a user input!

#-------------------NEW GAME------------------------------------
            if new_game_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                new_game_started = True

            if new_game_started:
                # Draw the "How many players?" question
                question_y = new_game_button_y + button_height + 50
                question_text = font.render("How many players?", True, Colours.BLACK.value)
                self.screen.blit(question_text, (grid_center_x - question_text.get_width() // 2, question_y))

                # Draw the player number buttons
                button_y = question_y + question_text.get_height() + 10
                player_buttons = []
                button_spacing = 15  # Define the amount of whitespace between each button
                total_width = 0  # Total width of all buttons including the spacing
                for i in range(1, 4):  # Change this to range(1, 4) to create only 3 buttons
                    text = font.render(str(i+1), True, Colours.BLACK.value)
                    button_width = text.get_width() + 50  # Add some padding
                    button_height = text.get_height() + 20  # Add some padding
                    total_width += button_width + button_spacing
                total_width -= button_spacing  # Subtract the last spacing
                start_x = grid_center_x - total_width // 2  # Adjust the starting x-coordinate to center the buttons
                for i in range(1, 4):  # Change this to range(1, 4) to create only 3 buttons
                    text = font.render(str(i+1), True, Colours.BLACK.value)
                    button_width = text.get_width() + 50  # Add some padding
                    button_height = text.get_height() + 20  # Add some padding
                    button_x = start_x + (i - 1) * (button_width + button_spacing)  # Adjust the x-coordinate calculation to center the buttons
                    button = pygame.draw.rect(self.screen, Colours.GREY.value, (button_x, button_y, button_width, button_height))
                    player_buttons.append(button)
                    text_rect = text.get_rect(center=button.center)
                    self.screen.blit(text, text_rect)

                    # Check if the button has been pressed
                    if button.collidepoint(mouse_pos) and mouse_pressed[0]:
                        if i == 1:
                            for i in range(1+1):
                                player_name = self.get_player_name(i+1)
                                self.players[i].set_name(player_name)
                                print(f"Player {i + 1} entered name: {player_name}")
                            self.initialiseGame(2)
                            return
                        elif i == 2:
                            for i in range(2+1):
                                player_name = self.get_player_name(i + 1)
                                self.players[i].set_name(player_name)
                                print(f"Player {i + 1} entered name: {player_name}")
                            self.initialiseGame(3)
                            return
                        elif i == 3:
                            for i in range(3+1):
                                player_name = self.get_player_name(i + 1)
                                self.players[i].set_name(player_name)
                                print(f"Player {i + 1} entered name: {player_name}")
                            self.initialiseGame(4)
                            return


            if not new_game_started:
                # Draw the "Quit" button
                try:
                    quit_button = pygame.draw.rect(self.screen, Colours.GREY.value, (grid_center_x - button_width // 2, quit_button_y, button_width, button_height))
                except:
                    running = False
                text = font.render("Quit", True, Colours.BLACK.value)
                text_rect = text.get_rect(center=quit_button.center)
                self.screen.blit(text, text_rect)
                # Check if the quit button has been pressed
                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()
                if quit_button.collidepoint(mouse_pos) and mouse_pressed[0]:
                    running = False

            pygame.display.flip()

        pygame.quit()

    def initialiseGame(self, playerQuantity):
        """
        Initialisation of the game where we decide how many Volcanos, ChitCards etc will be in the game
        
        Inputs:
        - playerQuantity: The amount of players that will be playing
        """
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

                            NonCaveCutVolcano([VolcanoTile(salamanderFactory.new(AnimalType.TILE)), 
                                               VolcanoTile(babyDragonFactory.new(AnimalType.TILE)), 
                                               VolcanoTile(spiderFactory.new(AnimalType.TILE))])]
        
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

        # putting all volcanos inside 1 list to set the board in that order
        volcanos = []
        for caveCut, nonCaveCut in zip(caveCutVolcanos, nonCaveCutVolcanos):
            volcanos.append(caveCut)
            volcanos.append(nonCaveCut)
        
        game_running_instance = GameRunning(volcanos, caves, chitCards, self.players[:playerQuantity])
        game_running_instance.run()

    def loadGame(self,file_name):
        """
        Load the game from the saved file
        """
        #Call the load manager which will convert the JSON strings into ojects 
        load_manager = LoadManager(file_name)
        volcanos, cavesList, chitCardsList, playerList, angles, isHomeList, currentPlayer, openChitCards = load_manager.initialiseClasses() #CHECK
        game_running_instance = GameRunning(volcanos, cavesList, chitCardsList, playerList)   # because we are always laoding diff set up and not the standard

        amount  = 0

        for volcano in volcanos:
            amount += len(volcano.get_volcano_tiles())

        volcano_angles = [round((0 + i * (360 / amount)) % 360, 3) for i in range(amount)]

        # i=0     # resetting i so we can iterate through players
        for i in range(len(game_running_instance.players)):
            if not isHomeList[i]:
                angle = round(angles[i] - game_running_instance.players[i].get_homeTileAngle(),3)
                if angle < 0:
                    angle += 360
                amount = volcano_angles.index(angle) + 1
                for _ in range(amount):
                    if game_running_instance.players[i].get_gameProgress().get_current_tile().check_cave() and not game_running_instance.players[i].isHome():
                        game_running_instance.players[i].get_gameProgress().forward()
                        game_running_instance.players[i].get_gameProgress().forward()

                        
                    game_running_instance.players[i].get_gameProgress().forward()

        game_running_instance.playerManager.set_current_player(currentPlayer)
        game_running_instance.clickedState.openChitCards = openChitCards
        game_running_instance.run()


 #Setup the board
#After loading or initialising without loading, we need to start the game and draw home
game = StartGame()
game.drawHome()