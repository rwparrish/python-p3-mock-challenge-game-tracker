class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
        
        player.results(self)
        player.games_played(game)
        
        game.results(self)
        game.players(player)
        
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception('Score must be')
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player
        if player and isinstance(player, Player):
            self._player = player
        else:
            raise Exception
            
    @property
    def game(self):
        return self._game
        
    @game.setter
    def game(self, game):
        from classes.game import Game
        if game and isinstance(game, Game):
            self._game = game
        else:
            raise Exception
        
    
    
        
    
