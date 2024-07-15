
from abc import ABC, abstractmethod
import copy

class PrototypeInterface(ABC):
    '''
    Abstract class for Prototype
    '''

    @abstractmethod
    def clone(self) -> 'PrototypeInterface':
        '''
        Abstract method to clone the Prototype
        
        Returns:
        - clone: Cloned Prototype (PrototypeInterface)
        '''
        pass