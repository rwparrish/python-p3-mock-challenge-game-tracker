class Game:
    def __init__(self, title):
        if len(title) > 0:
            self._title = title
        else:
            raise Exception('Title must exist!!')
        
        self._results = []
        self._players = []
        
    @property
    def title(self):
        return self._title
    
        
    def results(self, new_result=None):
        from classes.result import Result
        pass
    
    def players(self, new_player=None):
        from classes.player import Player
        pass
    
    def average_score(self, player):
        pass