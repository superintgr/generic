from itertools import product, permutations

def permute(sequence):
    for order in permutations(sequence):
        yield order

def combine(associations):
    for pair in associations:
        yield product(pair)

class Construct:
    def __init__(self, label):
        self.center = label
        self.stereo = []

    def __call__(self, sequence):
        for i in range(len(sequence)):
            if sequence[i] == self.center:
                left = sequence[i - 1]
                right = sequence[i + 1]
                self.stereo.append((left, right))
            if sequence[i] in self.stereo:
                register = self.stereo.index(sequence[i])
                left, right = self.stereo[register]
                mid = sequence[i]
                sides = sequence[i - 1], sequence[i + 1]
                if left is mid:
                    if right in sides:
                        index = sides.index(right)
                        left = sides[index + 1]
                        if left in self.stereo:
                            # do that again since this left is the other element in sides tuple
                            ..
                        else:
                            # add mid (previously left) and right to the stereo registry
                            # indicate that the relative distance is further than 1 unit from the instance label
                            ## although i haven't implemented any weighting attribute to this code yet.


# construct is nuclei
# all possible neighbors are distance more than 1 unit away
# for all possible distances, the set of neighbors with constant maximum distance forms shell
# the constant unitary sequence of possible changes inside the environment, takes place at integer distance apart
# each orbital pathway at constant distance define the relative position of the orbiting class
