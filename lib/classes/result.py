class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
    @property
    def score(self):
        self.score
    
    @score.setter
    def score(self, value):
        if 1 <= value <= 5000:
            self.score = value
        else:
            raise Exception('Score must be')
    
        
    
