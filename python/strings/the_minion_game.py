'''
The Minion Game
Link: https://www.hackerrank.com/challenges/the-minion-game/problem
'''

def minion_game(string):
    vowel_player = "Kevin"
    const_player = "Stuart"
    
    import re
    
    length = len(string)
    vowel_pattern = r'[aeiouAEIOU]'
    const_pattern = r'[^aeiouAEIOU]'
    
    vowel_indices = [m.start() for m in re.finditer(vowel_pattern, string)]
    const_indices = [m.start() for m in re.finditer(const_pattern, string)]
    
    vowel_score, const_score = 0, 0
    for ind in vowel_indices: vowel_score += length - ind 
    for ind in const_indices: const_score += length - ind
    
    if   vowel_score > const_score: print(f"{vowel_player} {vowel_score}")
    elif vowel_score < const_score: print(f"{const_player} {const_score}")
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)