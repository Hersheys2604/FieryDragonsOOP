
import pygame
from abc import ABC , abstractmethod
from Tiles.VolcanoTile import VolcanoTile
from Save.SaveInterface import SaveInterface

class Volcano(ABC):     
    '''
    Abstract class for Volcano
    '''

    def __init__(self, volcanoTiles: list[VolcanoTile], image: pygame.image) -> None:
        '''
        Constructor for Volcano
        
        Inputs:
        - volcanoTiles: List of VolcanoTiles on the Volcano (list[VolcanoTile])
        - image: Image of the Volcano (pygame.image)
        '''
        self.volcanoTiles = volcanoTiles
        self.image = image
    
    def get_volcano_tiles(self) -> list[VolcanoTile]:
        '''
        Returns the list of VolcanoTiles on the Volcano
        
        Outputs:
        - volcanoTiles: List of VolcanoTiles on the Volcano (list[VolcanoTile])
        '''
        return self.volcanoTiles
    
    @abstractmethod
    def get_cave_cut_tile(self) -> VolcanoTile:
        '''
        Returns the CaveCut VolcanoTile
        
        Outputs:
        - VolcanoTile: The CaveCut VolcanoTile (VolcanoTile)
        '''
        pass

    