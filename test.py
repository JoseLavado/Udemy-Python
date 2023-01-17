


def yoda(text):
    wordlist = text.split()
    rev_word = wordlist[::-1]
    return rev_word


rever=yoda("There is no try")


print(rever)

final_words=" ".join(rever)

print(final_words)



