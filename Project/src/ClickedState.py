import pygame
import time
from AnimalType import AnimalType
from GameProgression import GameProgression
from Players.Player import Player
from Players.PlayerManager import PlayerManager
from Board import Board
#from GameRunning import GameRunning
import random

# Concrete State: State when the game is clicked
class clickedState():

    def __init__(self, players: PlayerManager, board: Board) -> None:
        '''
        Constructor for the clickedState
        
        Inputs:
        - players: PlayerManager object (PlayerManager)
        - board: Board object (Board)
        '''
        self.positions = {}
        self.players = players
        self.board = board
        self.openChitCards = []
        self.priorOpenedCards = []
    
    def addPosition(self, position, animal) -> None:
        x, y, width, height = position
        self.positions[(x, y, width, height)] = animal
    
    def getPositions(self):
        return self.positions

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            keys = self.positions.keys()
            for key in keys:
                button = pygame.Rect(*key)
                if button.collidepoint(mouse_pos):
                    player = self.players.get_current_player()
                    gameProgress = player.get_gameProgress()
                    currentAnimal = gameProgress.get_current_tile().get_animal()
                    chitCard = self.positions[key]
                    if chitCard.isFlipped():
                        return
                    chitCard.flip()
                    self.openChitCards.append(chitCard)
                    self.priorOpenedCards.append(chitCard)
                    self.board.draw()

                    # time.sleep(1)
                    if currentAnimal.checkMove(chitCard.get_animal()):
                        animal = chitCard.get_animal()
                        animalType = animal.get_animalType()
                        if animalType == AnimalType.CHITCARD_1:
                            self.forward(gameProgress, player, 1)
                        elif animalType == AnimalType.CHITCARD_2:
                            self.forward(gameProgress, player, 2)
                        elif animalType == AnimalType.CHITCARD_3:
                            self.forward(gameProgress, player, 3)
                        elif animalType == AnimalType.REGRESSIVE_1:
                            self.backward(gameProgress, player, 1)
                        elif animalType == AnimalType.REGRESSIVE_2:
                            self.backward(gameProgress, player, 2)
                        elif animalType == AnimalType.REGRESSIVE_TRANSPORT:
                            self.transportBack(gameProgress,player)
                    else:
                        self.nextPlayer()

    def forward(self, gameProgress: GameProgression, player: Player, amount: int) -> None:
            '''
            Move the player forward by the amount specified
            
            Inputs:
            - gameProgress: GameProgression object for the player (GameProgression)
            - player: Player object (Player)
            - amount: Amount to move the player forward by (int)
            '''
            for i in range(amount):
                gameProgress.forward()
                player.set_ratioNum(player.get_ratioNum() + 1)
                if gameProgress.get_current_tile().check_cave() and not player.isHome():
                    gameProgress.forward()
                    gameProgress.forward()


                if gameProgress.get_current_tile().check_cave() and player.isHome() and i != amount - 1 :
                    for _ in range(i+1):
                        gameProgress.backward()
                        player.set_ratioNum(player.get_ratioNum() - 1)

                    #Extension: If a player incorrectly guesses their chit card and they move past their cave, they move back between 6-10 steps.
                    #This is a random amount (6-10)
                    # Then they see all the previously opened volcano cards (throughout the whole game) for 3 seconds, they all turn back over
                    random_number = random.randint(6,10)
                    print(self.priorOpenedCards)
                    self.backward(gameProgress, player, random_number)
                    for chitCard in self.priorOpenedCards:
                        if not chitCard.isFlipped():
                            chitCard.flip()

                    self.board.draw()
                    time.sleep(2)

                    self.nextPlayer()

                    for chitCard in self.priorOpenedCards:
                        if chitCard.isFlipped():
                            chitCard.flip()
                            
                    return
            
            if player.isHome() and gameProgress.get_current_tile().check_cave():
                self.board.drawWinning(player)
                self.players.remove_current_player()
                self.nextPlayer()
                if self.players.get_length() == 1:
                    pygame.quit()
                return
            
            otherPlayers = self.players.getOtherPlayers()
            for otherPlayer in otherPlayers:
                if otherPlayer != player:
                    if player.isOccupied(otherPlayer):
                        for _ in range(amount):
                            gameProgress.backward()
                        player.set_ratioNum(player.get_ratioNum() - amount)


    def backward(self, gameProgress: GameProgression, player: Player, amount: int) -> None:
        '''
        Move the player backward by the amount specified
        
        Inputs:
        - gameProgress: GameProgression object for the player (GameProgression)
        - player: Player object (Player)
        - amount: Amount to move the player backward by (int)
        '''
        if player.isHome():
            self.nextPlayer()
            return
        for _ in range(amount):
            gameProgress.backward()
            player.set_ratioDen(player.get_ratioDen() + 1)
            if gameProgress.get_current_tile().check_cave():
                gameProgress.backward()
                gameProgress.backward()
        
        otherPlayers = self.players.getOtherPlayers()
        for otherPlayer in otherPlayers:
            if otherPlayer != player:
                if player.isOccupied(otherPlayer):
                    self.forward(gameProgress, player, amount)
                    player.set_ratioDen(player.get_ratioDen() - amount)
                    player.set_ratioNum(player.get_ratioNum() - amount)

    def transportBack(self, gameProgress: GameProgression, player: Player) -> None:
        '''
        Transport the player back to the closest open cave
        Inputs: Game Progress: Game Progression object for the player
        player: Player object '''
        if gameProgress.get_current_tile().check_cave():
            self.nextPlayer()
            return 
        
        otherPlayers = self.players.getOtherPlayers()

        while True:
            gameProgress.backward()
            player.set_ratioDen(player.get_ratioDen() + 1)
            if gameProgress.get_current_tile().check_cave():
                for otherPlayer in otherPlayers:
                    if gameProgress.get_current_tile().get_angle() == otherPlayer.get_homeTileAngle() and not otherPlayer.isHome():
                        player.set_ratioDen(player.get_ratioDen() - 1)
                        return
                    elif gameProgress.get_current_tile().get_angle() == otherPlayer.get_homeTileAngle():
                        player.set_ratioDen(player.get_ratioDen() - 2)
                    elif gameProgress.get_current_tile().check_cave() and not player.isOccupied(otherPlayer):
                        player.set_ratioDen(player.get_ratioDen() - 1)
                        return


                if player.isHome():
                    return

                        

    def nextPlayer(self):
        time.sleep(1) #Added a manual 1 second delay to show the chit card before moving to the next player
        self.players.next_player()
        for chitCard in self.openChitCards:
            chitCard.flip()
        self.openChitCards.clear()