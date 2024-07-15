from abc import ABC, abstractmethod

class SaveInterface(ABC):

    @abstractmethod
    def save(self):
        pass