import pygame
from Animals.Animal import Animal
from AnimalType import AnimalType
from Animals.RegressiveAnimalInterface import RegressiveAnimalInterface

class PirateDragon(Animal, RegressiveAnimalInterface):
    '''
    Class for PirateDragon
    
    @see Animal
    '''
    
    def __init__(self, name: str, image: pygame.image, animalType: AnimalType):
        '''
        Constructor for PirateDragon
        
        Inputs:
        - name: Name of PirateDragon (str)
        - image: Image of PirateDragon (pygame)
        - animalType: Type of PirateDragon (AnimalType)
        '''
        super().__init__(name, image, animalType)
    
    def checkSpider(self) -> bool:
        '''
        Checks if the move on Spider is valid
        
        Returns:
        - True as move is valid
        '''
        return True
    
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
        - True as move is valid
        '''
        return True
    
    def checkBat(self) -> bool:
        '''
        Checks if the move on Bat is valid

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