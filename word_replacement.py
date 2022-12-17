def replace_word():
    phrase = "Hello, my name is Sam"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(phrase.replace(word_to_replace, word_replacement))

replace_word()