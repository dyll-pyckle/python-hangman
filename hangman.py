import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

list_of_words = [
    "apple", "grape", "stone", "water", "cloud", "light", "dream", "smile", 
    "chair", "table", "bread", "plant", "green", "river", "ocean", "storm", 
    "dance", "music", "voice", "laugh", "heart", "spark", "flame", "bliss", 
    "peace", "magic", "story", "world", "flora", "fauna", "sunny", "rainy", 
    "windy", "clear", "snowy", "petal", "leafy", "roots", "spice", "sugar",
    "amber", "pearl", "coral", "ivory", "onyx", "velvet", "linen", "silk", 
    "wool", "cotton"
]
tries = 0
chosen_word = random.choice(list_of_words)
wrong_letters = []

length = len(chosen_word)

hidden_list = list("_"*length)
hangmanpics_index = 0

found_list = []
guessed_letters = set()

for i in range(8):
    while True:
        choice = input("Which letter do you guess?").lower()
        if choice in guessed_letters:
            print(f"You already guessed '{choice}'!")
        else:
            guessed_letters.add(choice)
            break
    
    if choice in chosen_word:
        print("you got a letter!")
        
        for i, letter in enumerate(chosen_word):
            if letter == choice:
                hidden_list[i] = choice
        found_list.append(choice)
        print(*hidden_list, sep=' ')
        print(HANGMANPICS[hangmanpics_index])
       
        if "".join(hidden_list) == chosen_word:
            print("you win!")
            break
            
    else:
        print("wrong")
        wrong_letters.append(choice)
        hangmanpics_index += 1
        print(f"you got {" ".join(wrong_letters)} wrong")
        print(HANGMANPICS[hangmanpics_index])
        
        
    if hangmanpics_index == 6:
        print("you lose!")
        break
print(f"the word was {chosen_word}.")
