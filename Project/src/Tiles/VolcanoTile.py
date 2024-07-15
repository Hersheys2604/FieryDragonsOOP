
from Tiles.Tile import Tile
from Animals.Animal import Animal
from PrototypeInterface import PrototypeInterface
from Save.SaveInterface import SaveInterface

class VolcanoTile(Tile, PrototypeInterface, SaveInterface): 
    '''
    Class for VolcanoTile
    
    @see Tile
    @see PrototypeInterface
    '''
    def __init__(self, animal: Animal) -> None:
        '''
        Constructor for VolcanoTile
        
        Inputs:
        - animal: Animal on VolcanoTile (Animal)
        '''
        super().__init__(animal)
    
    def check_cave(self) -> bool:
        '''
        Check if the Tile is a cave
        
        Outputs:
        - False as VolcanoTile is not a cave (bool)
        '''
        return False

    def clone(self) -> 'VolcanoTile':
        '''
        Clone the VolcanoTile and return the cloned VolcanoTile (Prototype Pattern)
        
        Outputs:
        - VolcanoTile: Cloned VolcanoTile (VolcanoTile)
        '''
        return VolcanoTile(self.animal.clone())

    def save(self) -> str:
        '''
        Save the VolcanoTile as string
        
        Outputs:
        - VolcanoTile saved as string (str)
        '''
        return self.get_animal().get_name()
    
