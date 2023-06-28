class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
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
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
