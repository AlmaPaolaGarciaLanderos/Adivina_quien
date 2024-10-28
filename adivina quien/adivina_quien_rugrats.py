#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial 

import json
import os

class AdivinaQuienRugrats:
    def __init__(self):
        self.questions = [
            "¿Es un bebé?",
            "¿Es un niño o niña?",
            "¿Es el líder del grupo?",
            "¿Tiene un animal de compañía?",
            "¿Es un chico?",
            "¿Es muy travieso?",
            "¿Tiene hermanos?",
            "¿Le gusta hacer travesuras?",
            "¿Es amigo de Tommy?",
            "¿Es un personaje femenino?",
        ]
        self.characters = {}
        self.load_data()

    def load_data(self):
        if os.path.exists('characters.json'):
            with open('characters.json', 'r') as f:
                self.characters = json.load(f)
        else:
            # Inicializa los personajes predeterminados
            self.characters = {
                "Tommy Pickles": ["Sí", "Sí", "Sí", "No", "Sí", "Sí", "No", "Sí", "Sí", "No"],
                "Chuckie Finster": ["Sí", "Sí", "No", "No", "Sí", "Sí", "No", "Sí", "Sí", "No"],
                "Angelica Pickles": ["Sí", "Sí", "No", "No", "No", "Sí", "Sí", "Sí", "No", "Sí"],
                "Phil y Lil DeVille": ["Sí", "Sí", "No", "No", "No", "Sí", "Sí", "Sí", "Sí", "Sí"],
                "Susie Carmichael": ["Sí", "Sí", "No", "No", "No", "Sí", "No", "Sí", "Sí", "Sí"],
                "Dil Pickles": ["Sí", "Sí", "No", "No", "Sí", "No", "No", "No", "Sí", "No"],
                "Kimi Watanabe-Finster": ["Sí", "Sí", "No", "No", "Sí", "Sí", "No", "Sí", "Sí", "Sí"],
                "Grandpa Lou": ["No", "No", "No", "No", "No", "No", "Sí", "No", "No", "No"],
                "Spike": ["No", "No", "No", "Sí", "No", "No", "No", "No", "No", "No"],
                "Carlitos": ["Sí", "Sí", "No", "No", "Sí", "Sí", "No", "Sí", "No", "No"],
                "Liliana": ["Sí", "Sí", "No", "No", "No", "Sí", "Sí", "Sí", "Sí", "Sí"],
                "Didi Pickles": ["No", "No", "No", "No", "No", "No", "Sí", "No", "No", "Sí"],
            }

    def save_data(self):
        with open('characters.json', 'w') as f:
            json.dump(self.characters, f)

    def ask_questions(self):
        answers = []
        for question in self.questions:
            while True:
                answer = input(question + " (Sí/No/Tal vez): ").strip().lower()
                if answer in ["sí", "si", "no", "tal vez"]:
                    answers.append(answer)
                    break
                else:
                    print("Por favor, responde solo con 'Sí', 'No' o 'Tal vez'.")
        return answers

    def guess_character(self, answers):
        normalized_answers = ["Sí" if ans in ["sí", "si"] else "No" if ans == "no" else "Tal vez" for ans in answers]
        for character, character_answers in self.characters.items():
            if character_answers == normalized_answers:
                return character
        return None

    def ask_additional_questions(self):
        print("No puedo adivinar. ¿Puedes ayudarme a aprender?")
        new_character = input("¿Cuál es el personaje en el que pensabas? ")
        new_answers = []
        for question in self.questions:
            while True:
                answer = input(question + " (Sí/No/Tal vez): ").strip().lower()
                if answer in ["sí", "si", "no", "tal vez"]:
                    new_answers.append(answer)
                    break
                else:
                    print("Por favor, responde solo con 'Sí', 'No' o 'Tal vez'.")
        self.characters[new_character] = new_answers
        self.save_data()  # Guarda los datos después de aprender
        print(f"He aprendido sobre {new_character}.")

    def play(self):
        print("¡Piensa en un personaje de Rugrats y yo intentaré adivinarlo!")
        answers = self.ask_questions()
        result = self.guess_character(answers)
        if result:
            print("Creo que el personaje en el que estás pensando es:", result)
        else:
            self.ask_additional_questions()

if __name__ == "__main__":
    game = AdivinaQuienRugrats()
    game.play()
