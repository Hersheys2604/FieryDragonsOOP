import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.Bat import Bat

class BatFactory(AnimalFactory):
    '''
    Factory class for creating Bats.

    @see AnimalFactory
    @see Bat
    '''

    def new(self, animalType: AnimalType) -> Bat:
        '''
        Creates a new Bat with the given animalType
        
        @param animalType: The type of the Bat to create
        @return: A new Bat
        '''
        if animalType == AnimalType.TILE:
            return Bat("Bat", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'dragonCardBat.png')), animalType)
        elif animalType == AnimalType.CAVE:
            return Bat("Bat", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveBat.png')), animalType)
        elif animalType == AnimalType.CHITCARD_1:
            return Bat("Bat", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard1Bat.png')), animalType)
        elif animalType == AnimalType.CHITCARD_2:
            return Bat("Bat", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard2Bat.png')), animalType)
        elif animalType == AnimalType.CHITCARD_3:
            return Bat("Bat", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard3Bat.png')), animalType)