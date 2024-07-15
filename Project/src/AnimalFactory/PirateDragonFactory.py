import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.PirateDragon import PirateDragon

class PirateDragonFactory(AnimalFactory):
    '''
    Factory class for creating PirateDragon objects.
    
    @see AnimalFactory
    @see PirateDragon
    '''

    def new(self, animalType: AnimalType) -> PirateDragon:
        '''
        Creates a new PirateDragon object with the given animalType
        
        @param animalType: The type of the PirateDragon object to create
        @return: A new PirateDragon object
        '''
        if animalType == AnimalType.REGRESSIVE_1:
            return PirateDragon("Pirate Dragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard1Pirate.png')), animalType)
        elif animalType == AnimalType.REGRESSIVE_2:
            return PirateDragon("Pirate Dragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard2Pirate.png')), animalType)