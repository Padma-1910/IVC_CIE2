def words_in_sentence(sentence):
    words = sentence.split()
    
    print(f"Total number of words: {len(words)}")
    
    for i, w in enumerate(words, 1):
        print(f"Word {i}: {w}")

# Take input from user
sentence = input("Enter a sentence: ")
words_in_sentence(sentence)

