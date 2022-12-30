from led_creator_class import LedCreator
import pygame

class Animation:
    def __init__(self, user_matrix, sequence):
        self.user_matrix = user_matrix
        self.leds = []
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

    def create_circular_layout(self):
        leds

    def create_square_layout(self):
        pass