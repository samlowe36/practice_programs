from PyDictionary import PyDictionary

dictionary = PyDictionary()


#def main():
    #word_dictionary = {
        #"hi": "A way of greeting someone",
        #"eyes": "An organ for seeing",
        #"earth": "A planet in space",
    #}

    #while True:
        #word = input("Enter a word: ")
        #if word == "":
            #break
        #if word in word_dictionary:
            #print(word, ":", word_dictionary[word])


#main()
#Above is an extremely basic implementation of how to do a dictionary

while True:
    word = input("Enter your word: ")
    if word == "":
        break
    print(dictionary.meaning(word))

#implementation using PyDictionary