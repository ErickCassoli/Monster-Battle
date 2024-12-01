import json

class SaveManager:
    @staticmethod
    def save_score(player_name, score, filename="scores.json"):
        try:
            with open(filename, "r") as file:
                scores = json.load(file)
        except FileNotFoundError:
            scores = {}

        scores[player_name] = max(scores.get(player_name, 0), score)

        with open(filename, "w") as file:
            json.dump(scores, file)

        print("Pontuação salva com sucesso!")

    @staticmethod
    def load_scores(filename="scores.json"):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
