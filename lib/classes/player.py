import ipdb

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)
        
    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else:
            raise Exception('Invalid username')
            
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False
      
    def num_times_played(self, game):
        game_player_score = [x for x in self._games_played if x == game]
        # game_player_score = [result for result in game._results if result.player == self]
        return len(game_player_score)
    
    @classmethod
    def highest_scored(cls, game):
        from classes.game import Game
        if cls.all == 0:
            return None
        else:
            highest_average_score = max([Game.average_score(game, player) and player for player in cls.all])
        
    
        
        
