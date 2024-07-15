import pygame
from Animals.Animal import Animal
from AnimalType import AnimalType
from Animals.RegressiveAnimalInterface import RegressiveAnimalInterface

class Car(Animal, RegressiveAnimalInterface):
    '''
    Class for Car
    
    @see Animal
    '''
    
    def __init__(self, name: str, image: pygame.image, animalType: AnimalType):
        '''
        Constructor for Car
        
        Inputs:
        - name: Name of Car (str)
        - image: Image of Car (pygame)
        - animalType: Type of Car (AnimalType)
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

