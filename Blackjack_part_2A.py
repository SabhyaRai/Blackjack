from random import randint

# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
x = 0
hand_value = 0
while x < 2:
  card_rank = randint(1,13)
  if card_rank == 1:
      card_name = "Ace"
  elif card_rank == 11:
# An 11 stands for a Jack.
      card_name = "Jack"
  elif card_rank == 12:
# A 12 stands for a Queen.
      card_name = "Queen"
  elif card_rank == 13:
# A 13 stands for a King.
      card_name = "King"
  else:
# All other cards are named by their number or rank.
      card_name = str(card_rank)
  if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
  else:
      drew_prefix = 'Drew a '
  print(drew_prefix + card_name)
  x = x + 1
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
# Kings, Queens, and Jacks are worth 10.
       card_value = 10
  elif card_rank == 1:
# All Aces are worth 11
       card_value = 11
  else:
# All other cards are named by their number or rank.
       card_value = card_rank
  hand_value = hand_value + card_value
while hand_value < 17:
  print("Dealer has " + str(hand_value) + ".")
  card_rank = randint(1,13)
  if card_rank == 1:
     card_name = "Ace" 
  elif card_rank == 11:
#An 11 stands for a Jack.
      card_name = "Jack"
  elif card_rank == 12:
# A 12 stands for a Queen.
       card_name = "Queen"
  elif card_rank == 13:
# A 13 stands for a King.
        card_name = "King"
  else:
# All other cards are named by their number or rank.
         card_name = str(card_rank) 
  if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
  else:
      drew_prefix = 'Drew a '
  print(drew_prefix + card_name)
    
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
# Kings, Queens, and Jacks are worth 10.
          card_value = 10
  elif card_rank == 1:
# All Aces are worth 11
          card_value = 11
  else:
# All other cards are named by their number or rank.
          card_value = card_rank
  hand_value = hand_value + card_value
print("Final hand: " + str(hand_value) + ".")
if hand_value == 21:
  print('BLACKJACK!')
elif hand_value > 21 and hand_value <= 31:
  print('BUST.')
