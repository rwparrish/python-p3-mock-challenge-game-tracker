class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
    @property
    def username(self):
        self.username
        
    @username.setter
    def Username(self, value):
        if 2 <= len(value) <= 16:
            self.username = value
        else:
            raise Exception('Invalid username')
            
    def results(self, new_result=None):
        from classes.result import Result
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        pass
    
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
