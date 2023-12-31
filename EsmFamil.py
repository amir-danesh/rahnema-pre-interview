class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class Game:
    def __init__(self, players):
        self.players = players
        self.answers = {'naam': [], 'shahr': [], 'ghaza': [], 'rang': []}

    def start_round(self, letter):
        for player in self.players:
            print(f"\nNobate {player.name} ast:")
            for category in self.answers.keys():
                ans = input(f"yek '{category}' vared konid ke ba {letter} shoru mishavad: ")
                self.answers[category].append((player, ans.lower()))
        self.calculate_scores(self.answers, letter)


    def calculate_scores(self, answers, letter):
        for category, responses in answers.items():
            for player, response in responses:
                if response[0] != letter:
                    continue
                
                same_responses = False
                for _, tempResp in responses:
                    if tempResp == response:
                        same_responses = True
                        break

                if same_responses:
                    player.add_score(5)
                else:
                    player.add_score(10)

    def update_categories(self):
        while True:
            category = input("\nbaraye shorue bazi 'done' ra Vared konid, dar gheire in surat, categoryi ke mikhahid ezafe ya hazf konid ra benevisid(be surate khodkar anjam mishavad): ")
            if category == 'done':
                break
            elif category in self.answers:
                del self.answers[category]
                print(f"Category '{category}' hazf shod.")
            else:
                self.answers[category] = []
                print(f"Category '{category}' ezafe shod.")



    def display_scores(self):
        for player in self.players:
            print(f"bazikon {player.name}, {player.score} emtiaz darad")

def main():

    num_players = int(input("Tedad nafarat bazi: "))

    players = []
    for i in range(num_players):
        name = input(f"esm nafare {i + 1}: ")
        players.append(Player(name))

    game = Game(players)
    game.update_categories()
    while True:

        letter = input("\nbaraye kharej shodan az bazi benevisid 'exit', dar gheire in surat charachteri ke mikhahid ba an bazi konid ra vared konid: ")
        letter = letter.lower()
        if letter == 'exit':
            break
        game.start_round(letter)
        game.display_scores()

if __name__ == "__main__":
    main()
