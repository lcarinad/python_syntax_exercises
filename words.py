def print_upper_words(words, must_start_with):
    """convert lowercase words to uppercase words"""
    for word in words:
        # question 2- upper=word.upper()
        # print (upper)
        # question 3- if word[0]=='e':
        #     print(word)
        # below is question 4
        for char in must_start_with:
            if char == word[0]:
                print(word.upper()) 
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})   
# print_upper_words(['hello', 'eyelash', 'hey', 'elephant', ])