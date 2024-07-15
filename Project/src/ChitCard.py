import pygame
import os
from Animals.Animal import Animal

class ChitCard:
    '''
    Class for ChitCard
    '''

    def __init__(self, animal: Animal) -> None:
        '''
        Constructor for ChitCard
        
        Inputs:
        - animal: Animal on ChitCard (Animal)
        '''
        self.animal = animal
        self.closedImage = pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCardClosed.png'))
        # self.closedImage = self.animal.get_image()
        self.flipped = False
    
    def get_animal(self) -> Animal:
        '''
        Returns the animal on the ChitCard
        
        Outputs:
        - animal: Animal on ChitCard (Animal)
        '''
        return self.animal
    
    def getClosedImage(self) -> pygame:
        '''
        Returns the closed image of the ChitCard

        Outputs:
        - pygame: The closed image of the ChitCard (pygame)
        '''
        return self.closedImage
    
    def flip(self) -> None:
        '''
        Flips the ChitCard
        '''
        self.flipped = not self.flipped
    
    def isFlipped(self) -> bool:
        '''
        Returns whether the ChitCard is flipped
        
        Outputs:
        - isFlipped: Whether the ChitCard is flipped (bool)
        '''
        return self.flipped

    def save(self) -> str:
        '''
        Saves the ChitCard
        
        Outputs:
        - saveString: String to save the ChitCard (str)
        '''
        type = self.get_animal().get_animalType()
        
        return [self.get_animal().get_name(), str(self.isFlipped()), type.name]
        