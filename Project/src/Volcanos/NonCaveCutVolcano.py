import os
import pygame

from Volcanos.Volcano import Volcano
from Tiles.VolcanoTile import VolcanoTile
from Save.SaveInterface import SaveInterface

class NonCaveCutVolcano(Volcano, SaveInterface):
    '''
    Class for NonCaveCutVolcano
    
    @see Volcano
    '''
    def __init__(self, volcanoTiles: list[VolcanoTile]) -> None:
        '''
        Constructor for NonCaveCutVolcano
        
        Inputs:
        - volcanoTiles: List of VolcanoTiles on the Volcano (list[VolcanoTile])
        '''
        super().__init__(volcanoTiles, pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'nonCaveCutVolcano.png')))
    
    def get_cave_cut_tile(self) -> VolcanoTile:
        '''
        Returns the CaveCut VolcanoTile
        
        Outputs:
        - VolcanoTile: The CaveCut VolcanoTile (VolcanoTile)
        '''
        return None

    def save(self) -> list:
        '''
        Saves the Volcano
        
        Outputs:
        - save: List of attributes to save (list)
        '''
        save = {"saveList": [], "type": "nonCaveCut"}
        for tile in self.get_volcano_tiles():
            save["saveList"].append(tile.save())
        return save
    