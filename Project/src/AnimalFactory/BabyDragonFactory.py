import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.BabyDragon import BabyDragon

class BabyDragonFactory(AnimalFactory):
    '''
    Factory class for creating Baby Dragon objects

    @see AnimalFactory
    @see BabyDragon
    '''

    def new(self, animalType: AnimalType) -> BabyDragon:
        '''
        Creates a new Baby Dragon object with the given animalType
        
        @param animalType: The type of the Baby Dragon to create
        @return: A new Baby Dragon object
        '''
        if animalType == AnimalType.TILE:
            return BabyDragon("BabyDragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'dragonCardBabyDragon.png')), animalType)
        elif animalType == AnimalType.CAVE:
            return BabyDragon("BabyDragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveBabyDragon.png')), animalType)
        elif animalType == AnimalType.CHITCARD_1:
            return BabyDragon("BabyDragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard1BabyDragon.png')), animalType)
        elif animalType == AnimalType.CHITCARD_2:
            return BabyDragon("BabyDragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard2BabyDragon.png')), animalType)
        elif animalType == AnimalType.CHITCARD_3:
            return BabyDragon("BabyDragon", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard3BabyDragon.png')), animalType)