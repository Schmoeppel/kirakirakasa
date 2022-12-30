import numpy as np


class MatrixHandler:

    def __init__(self, real_matrix, user_matrix):
        self.real_matrix = real_matrix
        self.user_matrix = user_matrix
        self.look_up_dictionary = self.create_lookup_dictionary()

    def check_matrix_sizes(self):
        if self.real_matrix.shape == self.user_matrix.shape:
            print("Matrix shape is confirmed")
            return 0
        else:
            raise UserWarning("Matrices are not the same shape")

    def create_lookup_dictionary(self):
        return {a: b for row_a, row_b in zip(self.user_matrix, self.real_matrix) for a, b in zip(row_a, row_b)}

    def user_idx2real_idx(self, user_idx):
        return self.look_up_dictionary.get(user_idx)