import pygame
import os
from AnimalFactory.AnimalFactory import AnimalFactory
from AnimalType import AnimalType
from Animals.Car import Car

class CarFactory(AnimalFactory):
    '''
    Factory class for creating Car objects.
    
    @see AnimalFactory
    @see Car
    '''

    def new(self, animalType: AnimalType) -> Car:
        '''
        Creates a new Car object with the given animalType
        
        @param animalType: The type of the Car object to create
        @return: A new Car object
        '''
        
        return Car("Car", pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'chitCardCar.png')), animalType)
