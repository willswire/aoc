class Round:
    def __init__(self, text: str):
        # Initialize the Round defaults
        self.red: int = 0
        self.green: int = 0
        self.blue: int = 0

        split_text = text.split(",")
        for color in split_text:
            if "red" in color:
                self.red = int(color.replace("red", "").strip())
            elif "green" in color:
                self.green = int(color.replace("green", "").strip())
            elif "blue" in color:
                self.blue = int(color.replace("blue", "").strip())
    
    def __repr__(self) -> str:
        return f"{self.red} red, {self.green} green, {self.blue} blue;"

class Game:
    def __init__(self, text: str):
        # Initialize the Game defaults
        self.id: int = 0
        self.rounds: list[Round] = []

        # Parse the incoming text
        split_text = text.split(":")

        # Parse the ID
        prefix = split_text[0]
        self.id = int(prefix.replace("Game ", "").strip())

        # Parse the Rounds
        suffix = split_text[1]
        text_rounds = suffix.split(";")
        for text_round in text_rounds:
            round = Round(text_round)
            self.rounds.append(round)

# Read the file
input = open('input.txt', 'r')
lines = input.readlines()

# Parse each line of the file
all_games: list[Game] = []
for line in lines:
    game = Game(line)
    all_games.append(game)

## PART ONE
def good_game_filter(game: Game) -> bool:
    for round in game.rounds:
        if (round.red > 12) or (round.green > 13) or (round.blue > 14):
            return False
    return True

good_games = list(filter(good_game_filter, all_games))
score = 0

# Print all the good_games
for game in good_games:
    print(f"Game {game.id}:")
    for round in game.rounds:
        print(f"  {round}")
    score += game.id

print(f"Score: {score}")

## PART TWO
import functools 

def power_generator(game: Game) -> int:
    max_red = functools.reduce(lambda a, b: max(a, b), map(lambda round: round.red, game.rounds))
    max_green = functools.reduce(lambda a, b: max(a, b), map(lambda round: round.green, game.rounds))
    max_blue = functools.reduce(lambda a, b: max(a, b), map(lambda round: round.blue, game.rounds))
    return max_red * max_green * max_blue

power_score = 0
for game in all_games:
    power_score += power_generator(game)

print(f"Power Score: {power_score}")