from Tiles.Tile import Tile
from Animals.Animal import Animal
from Save.SaveInterface import SaveInterface

class CaveTile(Tile, SaveInterface):
    '''
    Class for CaveTile
    
    @see Tile
    '''
    def __init__(self, animal: Animal) -> None:
        '''
        Constructor for CaveTile
        
        Inputs:
        - animal: Animal on CaveTile (Animal)
        '''
        super().__init__(animal)
    
    def check_cave(self) -> bool:
        '''
        Check if the Tile is a cave
        
        Outputs:
        - True as CaveTile is a cave (bool)
        '''
        return True
    
    def save(self) -> str:
        '''
        Save the CaveTile
        
        Outputs:
        - CaveTile saved as string (str)
        '''
        return self.get_animal().get_name()

    