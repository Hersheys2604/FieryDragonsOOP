import pygame
from GameProgression import GameProgression
from Save.SaveInterface import SaveInterface

class Player(SaveInterface):
    '''
    Class for Player
    '''

    def __init__(self, name: str, gameProgress: GameProgression, image: pygame.image) -> None:
        '''
        Constructor for Player
        
        Inputs:
        - name: Name of Player (str)
        - gameProgress: GameProgression of Player (GameProgression)
        - image: Image of Player (pygame.image)
        '''
        self.name = name
        self.gameProgress = gameProgress
        self.image = image      
        self.homeTileAngle = None
        self.next = None
        self.ratioNum = 0
        self.ratioDen = 0
    
    def get_ratioNum(self) -> int:
        '''
        Returns the numerator of the Player
        
        Outputs:
        - ratioNum: Numerator of Player (int)
        '''
        return self.ratioNum
    
    def set_ratioNum(self, ratioNum: int) -> None:
        '''
        Set the numerator of the Player
        
        Inputs:
        - ratioNum: Numerator of Player (int)
        '''
        self.ratioNum = ratioNum
    
    def get_ratioDen(self) -> int:
        '''
        Returns the denominator of the Player
        
        Outputs:
        - ratioDen: Denominator of Player (int)
        '''
        return self.ratioDen
    
    def set_ratioDen(self, ratioDen: int) -> None:
        '''
        Set the denominator of the Player
        
        Inputs:
        - ratioDen: Denominator of Player (int)
        '''
        self.ratioDen = ratioDen
        
    def get_name(self) -> str:
        '''
        Returns the name of the Player
        
        Outputs:
        - name: Name of Player (str)
        '''
        return self.name
    
    def set_name(self, name: str) -> None:
        '''
        Set the name of the Player
        
        Inputs:
        - name: Name of Player (str)
        '''
        self.name = name
    
    def get_gameProgress(self) -> GameProgression:
        '''
        Returns the GameProgression of the Player
        
        Outputs:
        - gameProgress: GameProgression of Player (GameProgression)
        '''
        return self.gameProgress

    def get_image(self) -> pygame.image:
        '''
        Returns the image of the Player
        
        Outputs:
        - image: Image of Player (pygame.image)
        '''
        return pygame.image.load(self.image)
    
    def get_image_path(self) -> str:
        '''
        Returns the image path of the Player
        
        Outputs:
        - image: Image path of Player (str)
        '''
        return self.image

    def get_homeTileAngle(self) -> int:
        '''
        Returns the angle of the Home Tile
        
        Outputs:
        - homeTileAngle: Angle of the Home Tile (int)
        '''
        return self.homeTileAngle
    
    def set_homeTileAngle(self, homeTileAngle: int) -> None:
        '''
        Set the angle of the Home Tile (Cave)
        
        Inputs:
        - homeTileAngle: Angle of the Home Cave (int)
        '''
        self.homeTileAngle = homeTileAngle
    
    def isHome(self) -> bool:
        '''
        Check if the Player is home
        
        Outputs:
        - isHome: True if Player is home, False otherwise (bool)
        '''
        if self.get_gameProgress().get_current_tile().check_cave():
            return self.gameProgress.get_current_tile().get_angle() == self.homeTileAngle
        return False
        # return self.gameProgress.get_current_tile().get_angle() == self.homeTileAngle
    
    def isOccupied(self, player: 'Player') -> bool:
        '''
        Check if the Player is on the same Tile as another Player
        
        Inputs:
        - player: Player to compare with (Player)
        
        Outputs:
        - isOccupied: True if Player is on the same Tile as another Player, False otherwise (bool)
        '''
        if not player.get_gameProgress().get_current_tile().check_cave():
            return player.get_gameProgress().get_current_tile().get_angle() == self.gameProgress.get_current_tile().get_angle()
        return False
    

    def save(self) -> int:
        '''
        Save the Player
        
        Outputs:
        - angle: get the angle of the current tile (int)
        '''
        return {"angle": self.get_gameProgress().get_current_tile().get_angle(), "img_path": self.get_image_path(), "player_num": self.get_ratioNum(), "player_den": self.get_ratioDen(), "isHome": self.isHome()}