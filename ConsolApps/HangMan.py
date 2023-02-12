import random

stages = [
    """
   --------
   |      |
   |      O
   |     \|/
   |      |
   |     / \
   - 
   """
    ,

    """
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / 
       -
    """,

    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,

    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    """,

    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,

    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,

    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """]

end_of_game = False
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6

print(f"Psst, the solution is {chosen_word}")

display = []
for _ in range(word_lenght):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])