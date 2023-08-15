print("\n----- Question 8 -----")

def display_with_dash(word):
    formatWord = '-'.join(word)
    return print(formatWord)

words = ['Elvis', 'has', 'left', 'the', 'building!']

for i in words:
    display_with_dash(i)