def yoda(text):
    wordlist = text.split()
    rev_word = wordlist[::-1]
    return rev_word

def paper_doll(text):
    new_word=""
    for i in range(len(text)):
        new_word = new_word + text[i]*3
    return new_word


rever=yoda("There is no try")
print(rever)
final_words=" ".join(rever)
print(final_words)

print("\n")

print(paper_doll("MILTON"))





        











