# Write your solution here

def find_words(search):

    found = []

    with open("words.txt") as f1:

        for word in f1:
            word = word.strip()
            if search == word:
                found.append(word)
            elif "*" in search:
                if "*" == search[0]:
                    if word.endswith(search[1:]):
                        found.append(word)
                elif "*" == search[-1]:
                    if word.startswith(search[:-1]):
                        found.append(word)
            else:
                if len(word) == len(search):
                    match = True
                    for i in range(len(search)):
                        if search[i] != "." and search[i] != word[i]:
                            match = False
                            break
                    if match:
                        found.append(word)
                         
                  


    return found


