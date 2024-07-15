import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.Salamander import Salamander

class SalamanderFactory(AnimalFactory):
    '''
    Factory class for creating Salamanders.
    
    @see AnimalFactory
    @see Salamander
    '''

    def new(self, animalType: AnimalType) -> Salamander:
        '''
        Creates a new Salamander with the given animalType
        
        @param animalType: The type of the Salamander to create
        @return: A new Salamander
        '''
        if animalType == AnimalType.TILE:
            return Salamander("Salamander", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'dragonCardSalamander.png')), animalType)
        elif animalType == AnimalType.CAVE:
            return Salamander("Salamander", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveSalamander.png')), animalType)
        elif animalType == AnimalType.CHITCARD_1:
            return Salamander("Salamander", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard1Salamander.png')), animalType)
        elif animalType == AnimalType.CHITCARD_2:
            return Salamander("Salamander", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard2Salamander.png')), animalType)
        elif animalType == AnimalType.CHITCARD_3:
            return Salamander("Salamander", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCard3Salamander.png')), animalType)