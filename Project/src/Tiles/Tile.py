
from abc import ABC, abstractmethod
from Animals.Animal import Animal

class Tile(ABC):    ## There should be a save interface => but due to the limitations of Python, we cannot implement an interface here
    '''
    Abstract class for Tile
    '''

    def __init__(self, animal: Animal) -> None:
        '''
        Constructor for Tile
        
        Inputs:
        - animal: Animal on Tile (Animal)
        '''
        self.animal = animal
        self.next = None
        self.prev = None
        self.angle = None
    
    def get_animal(self) -> Animal:
        '''
        Returns the animal on the Tile
        
        Outputs:
        - animal: Animal on Tile (Animal)
        '''
        return self.animal
    
    def get_next(self) -> 'Tile':
        '''
        Returns the next Tile
        
        Outputs:
        - next: Next Tile (Tile)
        '''
        return self.next
    
    def get_prev(self) -> 'Tile':
        '''
        Returns the previous Tile
        
        Outputs:
        - prev: Previous Tile (Tile)
        '''
        return self.prev
    
    def set_angle(self, angle: int) -> None:
        '''
        Set the angle of the Tile
        
        Inputs:
        - angle: Angle of the Tile (int)
        '''
        self.angle = angle
    
    def get_angle(self) -> int:
        '''
        Returns the angle of the Tile
        
        Outputs:
        - angle: Angle of the Tile (int)
        '''
        return self.angle
    
    @abstractmethod
    def check_cave(self) -> bool:
        '''
        Check if the Tile is a cave
        
        Outputs:
        - True if Tile is a cave (bool), False otherwise
        '''
        pass