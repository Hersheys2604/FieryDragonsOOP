
from abc import ABC, abstractmethod
from Animals.Animal import Animal

class AnimalTileInterface(ABC):
    '''
    Abstract class (Interface) for AnimalTileInterface. Used for doubel dispatch and checking if player moves are valid
    '''

    @abstractmethod
    def checkMove(self, animal: Animal) -> bool:
        '''
        Abstract method to check if the move is valid
        
        Inputs:
        - animal: Animal to check against
        
        Returns:
        - True of False depending on if the move is valid'''
        pass
    
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
    
    @abstractmethod
    def checkPirateDragon(self) -> bool:
        '''
        Abstract method to check if the move on Pirate Dragon is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass

    @abstractmethod
    def checkCar(self) -> bool:
        '''
        Abstract method to check if the move on Car  is valid
        
        Returns True if the move is valid, False otherwise
        '''
        pass