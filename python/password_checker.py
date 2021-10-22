def strongPasswordChecker(s: str) -> int:
    insertions = max(6 - len(s), 0)
    deletions = max(len(s) - 20, 0)
    print(insertions, deletions)

    needs_lower = not any(char.islower() for char in s)
    needs_upper = not any(char.isupper() for char in s)
    needs_digit = not any(char.isnumeric() for char in s)
    needs_count = needs_lower + needs_upper + needs_digit

    # if deletions:
    #     return deletions + needs_lower + needs_upper + needs_digit
    # else:
    #     return max(insertions, needs_lower + needs_upper + needs_digit)

    # Temp strings of 3, 4 can be fixed with on insertion, 3 with one deletion
    # Len, Ins, Del, Rep
    #  3 ,(n-1)//2, (n-2), n//3


    # on the 3rd repeated object, can do an insertion, deletion or replacement
    # Create dynamic programming solution that makes a decision every time a 'repeat' is hit

    # State: (insertions, deletions, needs_lower, needs_upper, needs_digit, repetition_count)
    # Actions: (Insert, Delete, Replace)
    # Transitions: (move to next, +1 I/R, reset count, remove a needs lud), (move to next, maintain count, +1 D)
    # Rewards: Sum of I, D, R
    def Actions(state: tuple):
        char_index, insertions, deletions, current_run, I, D, R = state

        if char_index > len(s):
            return []
        if len(current_run) > 0 and current_run[-1] == s[char_index]:
            if len(current_run) < 2:
                return ('increment_current_run',)
            elif len(current_run) == 2:
                return ('insert', 'delete', 'replace')
        else:
            return ('reset_run',)

    def Transition(state: tuple, action: str):
        char_index, insertions, deletions, current_run, I, D, R = state
        char_index += 1
        if action == 'reset_run':
            current_run = ''
        elif action == 'increment_current_run':
            current_run += current_run[-1]
        elif action == 'insert':
            I += 1
            current_run = ''
        elif action == 'delete':
            D += 1
        elif action == 'replace':
            R += 1
            current_run = ''

        return (char_index, insertions, deletions, current_run, I, D, R)

    def Reward(state):
        char_index, insertions, deletions, current_run, I, D, R = state
        if char_index < len(s):  # TODO check final index
            return 0
        else:
            print(max(insertions, I) + max(deletions, D) + max(R) + max(0, needs_count - I - R))
            return max(insertions, I) + max(deletions, D) + max(R) + max(0, needs_count - I - R)

    def Changes(state):
        # TODO
        return min(
            (Changes(Transition(state, action),)
            for action in Actions(state)),
            default=0
        ),

    char_index = 0
    current_run = ''
    state = (char_index, insertions, deletions, current_run, 0, 0, 0)
    return Changes(state)


def testPWChecker():
    data_and_expected = [
        (
            '',
            6
        ),
        (
            'abc',
            3
        ),
        (
            'AbC123',
            0
        ),
        (
            'aaaa',
            2
        ),
        (
            'aaaaaaaaaaaa',
            4
        ),
    ]
    for data, expected in data_and_expected:
        assert strongPasswordChecker(data) == expected, strongPasswordChecker(data)
