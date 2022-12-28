
class Animation:
    def __init__(self, leds, sequence):
        self.leds = leds
        self.total_time = 0
        self.start_time = 0
        self.end_time = 0
        self.speed = 1.0
        self.animation_sequence = sequence

    def create_binary(self):
        pass

    def read_binary(self, path):
        pass

    def run_preview(self):
        pass

    def create_layout(self):
        pass