
def merge_the_tools(string, k):
    k = 3
    string = 'AAABCADDE'
    # k : factor of n
    # no_substrings = int(n/k)
    n = len(string)
    for i in range(int(n/k)):
        substring = string[i * k:(i+1) * k]
        new_substring = ""
        unique_unused_characters = set(substring)
        print(unique_unused_characters)
        for character in substring:
            print(character)
            print(character in unique_unused_characters)
            if not unique_unused_characters:
                break
            if character in unique_unused_characters:
                new_substring += character
                unique_unused_characters.remove(character)
        print(new_substring)

        # uniqueify substring
        """
        new_substring = ""
        used_characters = set()
        unique_unused_characters = set(substring)
        for character in string[i * k:(i+1) * k]:
            if character not in used_characters:
                new_substring += character
                used_characters.add(character)
        print(new_substring)
        """
