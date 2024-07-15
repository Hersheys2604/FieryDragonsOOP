
import pygame

from Animals.Animal import Animal
from Animals.AnimalTileInterface import AnimalTileInterface
from AnimalType import AnimalType
from PrototypeInterface import PrototypeInterface

class BabyDragon(Animal, AnimalTileInterface, PrototypeInterface):
    '''
    Class for BabyDragon
    
    @see Animal
    @see AnimalTileInterface
    @see PrototypeInterface
    '''

    def __init__(self, name: str, image: pygame.image, animalType: AnimalType):
        '''
        Constructor for BabyDragon
        
        Inputs:
        - name: Name of BabyDragon (str)
        - image: Image of BabyDragon (pygame)
        - animalType: Type of BabyDragon (AnimalType)
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
        return animal.checkBabyDragon()
    
    def checkSpider(self) -> bool:
        '''
        Checks if the move on Spider is valid
        
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
    
    def checkBabyDragon(self) -> bool:
        '''
        Checks if the move on BabyDragon is valid
        
        Returns:
        - True as move is valid
        '''
        return True
    
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
        - False as move is not valid
        '''
        return False
    
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
    
    def clone(self) -> 'BabyDragon':
        '''
        Clones the BabyDragon to create a new copy (prototype pattern).
        
        Returns:
        - Cloned BabyDragon
        '''
        return BabyDragon(self.get_name(), self.get_image(), self.get_animalType())