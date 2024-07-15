
import pygame
from abc import ABC, abstractmethod
from AnimalType import AnimalType


class Animal(ABC):
    '''
    Abstract class for Animal
    '''

    def __init__(self, name: str, image: pygame.image, animalType: AnimalType) -> None:
        '''
        Constructor for Animal
        
        Inputs:
        - name: Name of Animal (str)
        - image: Image of Animal (pygame)
        - animalType: Type of Animal (AnimalType)
        '''
        self.name = name
        self.image = image
        self.animalType = animalType

    def get_name(self) -> str:
        '''
        Returns the name of the Animal

        Returns:
        - name: Name of Animal (str)
        '''
        return self.name
    
    def get_image(self) -> pygame:
        '''
        Returns the image of the Animal
        
        Returns:
        - image: Image of Animal (pygame)
        '''
        return self.image 
    
    def get_animalType(self) -> AnimalType:
        '''
        Returns the type of the Animal
        
        Returns:
        - animalType: Type of Animal (AnimalType)
        '''
        return self.animalType