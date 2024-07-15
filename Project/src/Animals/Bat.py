
import pygame

from Animals.Animal import Animal
from Animals.AnimalTileInterface import AnimalTileInterface
from AnimalType import AnimalType
from PrototypeInterface import PrototypeInterface

class Bat(Animal, AnimalTileInterface, PrototypeInterface):
    '''
    Class for Bat
    
    @see Animal
    @see AnimalTileInterface
    @see PrototypeInterface
    '''

    def __init__(self, name: str, image: pygame.image, animalType: AnimalType):
        '''
        Constructor for Bat
        
        Inputs:
        - name: Name of Bat (str)
        - image: Image of Bat (pygame)
        - animalType: Type of Bat (AnimalType)
        '''
        super().__init__(name, image, animalType)

    def checkMove(self, animal: Animal) -> bool:
        '''
        Checks if the move is valid
        
        Inputs:
        - animal: Animal to check against
        
        Returns:
        - True if the move is valid, False otherwise
        '''
        return animal.checkBat()
    
    def checkSpider(self) -> bool:
        '''
        Checks if the move on Spider is valid
        
        Returns:
        - False as move is not valid
        '''
        return False
    
    def checkBabyDragon(self) -> bool:
        '''
        Checks if the move on BabyDragon is valid
        
        Returns:
        - False as move is not valid
        '''
        return False
    
    def checkSalamander(self) -> bool:
        '''
        Checks if the move on Salamander is valid
        
        Returns:
        - False as move is not valid
        '''
        return False
    
    def checkBat(self) -> bool:
        '''
        Checks if the move on Bat is valid

        Returns:
        - True as move is valid
        '''
        return True
    
    def checkPirateDragon(self) -> bool:
        '''
        Checks if the move on Pirate Dragon is valid
        
        Returns:
        - True as move is valid
        '''
        return True
    
    def checkCar(self) -> bool:
        '''
        Checks if the move on Car is valid
        
        Returns:
        - True as move is valid
        '''
        return True

    def clone(self) -> 'Bat':
        '''
        Clones Bat to create a new copy (prototype pattern)
        
        Returns:
        - New instance of Bat
        '''
        return Bat(self.get_name(), self.get_image(), self.get_animalType())
        
        