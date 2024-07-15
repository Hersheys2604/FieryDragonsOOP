from abc import ABC, abstractmethod
from AnimalType import AnimalType

class AnimalFactory(ABC):
    '''
    Abstract class for AnimalFactory
    '''
    
    @abstractmethod
    def new(self, animalType: AnimalType):
        '''
        Abstract method to create a new Animal

        Inputs:
        - animalType: AnimalType

        Returns:
        - Animal
        '''
        pass