import sys

# read the input from stdin
with open("input.txt") as f:
    strategy_guide = f.read().strip()
score = 0

def calculate_total_score(strategy_guide):
  score = 0
  for line in strategy_guide.split('\n'):
    opponent_choice = line[0]
    if opponent_choice is 'A':
      player_choice_score = 2
    elif opponent_choice is 'B':
      player_choice_score = 1
    else:
      player_choice_score = 3
    
    result = line[2]
    if result is 'X':
      result_score = 0
    elif result is 'Y':
      result_score = 6
    else:
      result_score = 3
    
    score += player_choice_score + result_score
  
  return score

total_score = calculate_total_score(strategy_guide)

print(f'Your total score will be {total_score}.') # Your total score will be 16.
