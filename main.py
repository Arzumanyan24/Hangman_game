# import random

# from hangman_words import word_list
# from hangman_art import logo
# from hangman_art import stages
# print(logo)

# chosen_word= random.choice(word_list)
# worlds_len= len(chosen_word)
# end_of_game = False
# lives= 6
# display=[]
# for _ in range(worlds_len):
#     display+="_"
    
# while not end_of_game:
#     x = input("gushakir tary ").lower()
    
#     if x in display:
#         print(f"chisht e {x}")
        
#     for position in range(worlds_len):
#         letter=chosen_word[position]
#         if letter == x:
#             display[position]=letter
#     if x not in chosen_word:
        
#         print(f"sxal e {x} ays tary chka ")
    
#         lives -=1
#         if lives == 0:
#             end_of_game= True
#             print("partvecir")
#     print(f"{' '.join(display)}")
    
#     if "_" not in display:
#         end_of_game = True
#         print("haxtecir")
#     print(stages[lives])
    
        
         
 