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
# each orbital pathway at constant distance
# define the relative position of the orbiting class

language = object
constructor = object

# we could construct a new language with full interoperable constructors
# apart from syntactic features there are universal approximators defined for every measurable attributes
# key operators of any extrinsic property must imply some abstract variables
# any intrinsic attribute of the abstract substrates (if) can be combined with any logical variables must imply some extrinsic attribute
# if an intrinsic attribute implies another intrinsic attribute for both properties under union operation, there exists a substrate whose extrinsic properties imply a pair of possible intrinsic state
# if an extrinsic state is an implication of operation performed on some physical variable and logical operator, there exists a physical quantity which never change under the same contructive transformation
# if some physical quantity is kept invarient via combinations of logical and physical attributes some substrate, there exists a physical variable which must remain in existence for yielding other measurable quantities
# if some measurable quantity that stays invarient undet the transformation applied on physical state of a substrate whose measure is implicated from the corresponding logical states, then the transformation implies some abstract state
# when some abstract state of a system which is composed of subsystems whose intrinsic and extrinsic measures correspond to logical and physical interoperability criterion of each of their composite substructures, the super-structure uniting those substrates produce information variable
# an information variable implies information media with reversible dynamics, therefore such dynamical laws encorporate the static properties on which abstract varible is imposed.
