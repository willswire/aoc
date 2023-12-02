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
        self.rounds: Round = []

        # Parse the incoming text
        split_text = text.split(":")

        # Parse the ID
        prefix = split_text[0]
        self.id = prefix.replace("Game ", "")

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
for line in lines:
    game = Game(line)
    rounds = game.rounds
    print(f"Game {game.id}:")
    for round in rounds:
        print(f"  {round}")