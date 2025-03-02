class PuntPlay:
    def __init__(self, game_id, teams, yards, qtr, date, time):
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.qtr = qtr  
        self.date = date  
        self.time = time  

    def __repr__(self):
        return f"PuntPlay({self.game_id}, {self.teams}, {self.yards}, {self.qtr}, {self.date}, {self.time})"