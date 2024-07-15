from Save.SaveInterface import SaveInterface

class PlayerManager(SaveInterface):
    """
    Player Manager class to manage players and their turn
    """
    def __init__(self):
        """
        We only need to point to one player as all players are linked similar to a linked list
        """
        self.current_player = None
        self.original_player = None

    def add_player(self, player):
        """
        When adding a player we link a player to the next one similar to a circular linked list
        
        - input: 
        player: The Player class
        """
        if not self.current_player:
            self.current_player = player
            self.current_player.next = self.current_player
        else:
            new_node = player
            cur = self.current_player
            while cur.next != self.current_player:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.current_player

    def next_player(self):
        """
        Returns the next player which the current player is pointing to
        """
        self.current_player = self.current_player.next
        return self.current_player
    
    def get_current_player(self):
        """
        Returns the current player
        """
        return self.current_player
    
    def getOtherPlayers(self):
        """
        Retrieve Players other than itself
        """
        otherPlayers = []
        cur = self.current_player
        while cur.next != self.current_player:
            otherPlayers.append(cur.next)
            cur = cur.next
        return otherPlayers
    
    def remove_current_player(self):
        """
        Remove the current player
        """
        if self.current_player:
            cur = self.current_player
            while cur.next != self.current_player:
                cur = cur.next
            cur.next = self.current_player.next
            self.current_player = self.current_player.next

    def set_current_player(self, player):
        """
        Set the current player
        """
        cur = self.current_player
        while cur != player:
            cur = cur.next
        self.current_player = cur

    def get_length(self):
        """
        Returns the number of players
        """
        if not self.current_player:
            return 0

        count = 1
        cur = self.current_player
        while cur.next != self.current_player:
            count += 1
            cur = cur.next
        return count

    def save(self) -> dict:
        """
        Save the current player
        """
        players = {}
        cur = self.current_player
        while cur != self.original_player:
            cur = cur.next
            
        for _ in range(self.get_length()):
            if cur == self.current_player:
                players[cur.get_name()] = {"data": cur.save(), "current": True}
            else:
                players[cur.get_name()] = {"data": cur.save(), "current": False}
            cur = cur.next


        return players
        # # Save the players to a list
        # player_data = []
        # for player in players:
        #     player_data.append(player.save())

        # return {
        #     cur.get_name(): player_data
        # }


    