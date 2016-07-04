import itertools


class Environment:
    """
    This class is responsible for modelling the sample space of the problem.
    """

    def __init__(self, a):
        self.address_list = a
        self.sample_space = list()

    def create(self):
        for item in itertools.permutations(self.address_list):
            self.sample_space.append(item)

    def get_sample_space(self):
        return self.sample_space
