class Player:
    def __init__(self, id, me, strategy_crashed, score, remaining_action_cooldown_ticks):
        self.id = id
        self.me = me
        self.strategy_crashed = strategy_crashed
        self.score = score
        self.remaining_action_cooldown_ticks = remaining_action_cooldown_ticks
