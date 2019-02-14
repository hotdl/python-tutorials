if __name__ == "__main__":
    print([1, 3, 5])
    print([1, 'str', 4])

    letters = ['a', 'b', 'c', 'd']
    print(letters)
    print(len(letters))
    letters[1:2] = ['B']
    print(letters)
    letters.append('e')
    print(letters)
    letters[:] = []
    print(letters)
