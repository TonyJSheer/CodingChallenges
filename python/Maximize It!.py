
"""

Action space: which number to select from list
State space: previous numbers selected
Reward space: the function, S
Transition space: adding the selected number (chosen action) to the state


"""
import time
from math import pow
time1 = time.time()
K = 3
M = 1000
X = [[2, 5, 4],
[3, 7, 8, 9],
[5, 5, 7, 8, 9, 10]]
"""
X = [
    set((
            (int(x) * int(x))
            % M
        )for x in "6429964 4173738 9941618 2744666 5392018 5813128 9452095".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "6517823 4135421 6418713 9924958 9370532 7940650 2027017".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "1506500 3460933 1550284 3679489 4538773 5216621 5645660".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "7443563 5181142 8804416 8726696 5358847 7155276 4433125".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "2230555 3920370 7851992 1176871 610460 309961 3921536".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "8518829 8639441 3373630 5036651 5291213 2308694 7477960".split(' ')),
    set((
            (int(x) * int(x))
            % M
        )for x in "7178097 249343 9504976 8684596 6226627 1055259 4880436".split(' ')),
]
"""

time2 = time.time()


COUNT = [0, 0, 0, 0]
def Final_Reward(selected):
    return sum(selected) % M


def V(selected, k):
    # Caching key to prevent recalculations
    key = selected

    # Termination condition
    if k == K:
        if key not in V_:
            V_[key] = Final_Reward(selected)
        else:
            COUNT[1] += 1
        return V_[key]

    if key not in V_:
        V_[key] = max(
            (V(selected + (action,), k + 1),
             action)
            for action in X[k]
    )
    else:
        COUNT[2] += 1
    return V_[key]

# speedup by introducing dictionary of V with sorted tuple for inputs.
starting_selection = tuple()
# speedup by introducing dictionary of V with sorted tuple for inputs.
V_ = dict()

print(time.time() - time1)

best_selection = V(starting_selection, 0)
print(time.time() - time1)

while type(best_selection) == tuple:
    best_selection = best_selection[0]
print(best_selection)

print(time.time() - time1)
print(time.time() - time2)
print(COUNT)
print(len(V_))
