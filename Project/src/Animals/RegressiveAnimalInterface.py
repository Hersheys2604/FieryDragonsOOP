
from abc import ABC, abstractmethod

class RegressiveAnimalInterface(ABC):
    '''
    Abstract class (Interface) for AnimalTileInterface. Used for double dispatch and checking if player moves are valid
    '''
    
    @abstractmethod
    def checkSpider(self) -> bool:
        '''
        Abstract method to check if the move on Spider is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass
    
    @abstractmethod
    def checkBabyDragon(self) -> bool:
        '''
        Abstract method to check if the move on BabyDragon is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass
    
    @abstractmethod
    def checkSalamander(self) -> bool:
        '''
        Abstract method to check if the move on Salamander is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass
    
    @abstractmethod
    def checkBat(self):
        '''
        Abstract method to check if the move on Bat is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass

