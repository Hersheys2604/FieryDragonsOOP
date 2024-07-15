import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.Spider import Spider

class SpiderFactory(AnimalFactory):
    '''
    Factory class for creating Spider objects.
    
    @see AnimalFactory
    @see Spider
    '''

    def new(self, animalType: AnimalType) -> Spider:
        '''
        Creates a new Spider object with the given animalType
        
        @param animalType: The type of the Spider object to create
        @return: A new Spider object
        '''
        if animalType == AnimalType.TILE:
            return Spider("Spider", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'dragonCardSpider.png')), animalType)
        elif animalType == AnimalType.CAVE:
            return Spider("Spider", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveSpider.png')), animalType)
        elif animalType == AnimalType.CHITCARD_1:
            return Spider("Spider", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard1Spider.png')), animalType)
        elif animalType == AnimalType.CHITCARD_2:
            return Spider("Spider", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard2Spider.png')), animalType)
        elif animalType == AnimalType.CHITCARD_3:
            return Spider("Spider", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard3Spider.png')), animalType)