import multiprocessing

class SharedData:
    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.players = self.manager.dict()  # {player_id: score}
        self.lock = multiprocessing.Lock()
        self.next_id = multiprocessing.Value('i', 1)
        
    def add_player(self):
        with self.lock:
            player_id = self.next_id.value
            self.players[player_id] = 0
            self.next_id.value += 1
            return player_id
            
    def remove_player(self, player_id):
        with self.lock:
            if player_id in self.players:
                del self.players[player_id]
                
    def increment_score(self, player_id):
        with self.lock:
            if player_id in self.players:
                self.players[player_id] += 1
                
    def get_score(self, player_id):
        with self.lock:
            return self.players.get(player_id, 0)