import os
import pygame
from Volcanos.Volcano import Volcano
from Tiles.VolcanoTile import VolcanoTile
from Save.SaveInterface import SaveInterface


class CaveCutVolcano(Volcano, SaveInterface):
    '''
    Class for CaveCutVolcano
    
    @see Volcano
    '''
    def __init__(self, volcanoTiles: list[VolcanoTile]) -> None:
        '''
        Constructor for CaveCutVolcano
        
        Inputs:
        - volcanoTiles: List of VolcanoTiles on the Volcano (list[VolcanoTile])
        '''
        super().__init__(volcanoTiles, pygame.image.load(os.path.join(os.environ.get('RESOURCEPATH', 'Project/src'), 'graphics', 'caveCutVolcano.png')))
        self.cave_cut_tile = 1

    def set_cave_cut_tile(self, cave_cut_tile: int) -> None:
        '''
        Sets the CaveCut VolcanoTile
        
        Inputs:
        - cave_cut_tile: The CaveCut VolcanoTile (int)
        '''
        self.cave_cut_tile = cave_cut_tile

    def get_cave_cut_tile(self) -> VolcanoTile:
        '''
        Returns the CaveCut VolcanoTile
        
        Outputs:
        - VolcanoTile: The CaveCut VolcanoTile (VolcanoTile)
        '''
        return self.get_volcano_tiles()[self.cave_cut_tile]
    
    def save(self) -> list:
        '''
        Saves the Volcano
        
        Outputs:
        - save: List of attributes to save (list)
        '''
        save = {"saveList": [], "caveCutTileIndex": self.cave_cut_tile, "type": "caveCut"}
        for tile in self.get_volcano_tiles():
            save["saveList"].append(tile.save())
        return save
       