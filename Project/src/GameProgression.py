
from Tiles.Tile import Tile
from Tiles.VolcanoTile import VolcanoTile
from Tiles.CaveTile import CaveTile
from Animals.Animal import Animal

class GameProgression:
    '''
    Class for GameProgression
    '''

    def __init__(self):
        '''
        Constructor for GameProgression (Circular Doubly Linked List)
        '''
        self.head = None
        self.current = None

    def insert(self, tile: Tile) -> None:
        '''
        Insert a Tile into the Circular Doubly Linked List
        
        Inputs:
        - tile: Tile to be inserted (Tile)
        '''
        new_node = tile
        if not self.head:
            self.head = new_node
            self.current = self.head
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
    
    def insert_cave(self, after_node: VolcanoTile, new_node: CaveTile) -> None:
        '''
        Insert a CaveTile after a VolcanoTile
        
        Inputs:
        - after_node: VolcanoTile after which the CaveTile is to be inserted (VolcanoTile)
        - new_node: CaveTile to be inserted (CaveTile)
        '''
        new_node.prev = after_node
        new_node.next = after_node.next
        after_node.next.prev = new_node
        after_node.next = new_node

    def get_current_animal(self) -> Animal:
        '''
        Returns the animal on the current Tile
        
        Outputs:
        - animal: Animal on the current Tile (Animal)
        '''
        if self.current:
            return self.current.get_animal()
        else:
            return None
    
    def get_current_tile(self) -> Tile:
        '''
        Returns the current Tile Player is on
        
        Outputs:
        - current: Current Tile (Tile)
        '''
        if self.current:
            return self.current
        else:
            return None

    def get_previous_tile(self) -> Tile:
        '''
        Returns the previous Tile
        
        Outputs:
        - prev: Previous Tile (Tile)
        '''
        if self.current:
            return self.current.get_prev()
        else:
            return None
    
    def get_next_tile(self) -> Tile:
        '''
        Returns the next Tile
        
        Outputs:
        - next: Next Tile (Tile)
        '''
        if self.current:
            return self.current.get_next()
        else:
            return None

    def forward(self) -> None:
        '''
        Move the Player forward
        '''

        if self.current:
            self.current = self.current.get_next()
        else:
            return None

    def backward(self) -> None:
        '''
        Move the Player backward
        '''
        if self.current:
            self.current = self.current.get_prev()
        else:
            return None
    
    def set_current(self, tile: Tile) -> None:
        '''
        Set the current Tile
        
        Inputs:
        - tile: Tile to be set as current (Tile)
        '''
        self.current = tile