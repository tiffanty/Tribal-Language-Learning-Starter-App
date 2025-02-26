# Project Description: This app is a starter tool to teach users basic Yoruba or Igbo—two Nigerian languages. It introduces the user to a mentor (a Nigerian artist like WizKid or Flavour) and assesses the user’s proficiency level based on their input (1-10). Depending on their level, the app provides tailored feedback.

# List of Nigerian artists
nigerian_artists = ["WizKid", "Flavour"]

# Vocabulary dictionary
dictionary = {
    "Yoruba": {
        "beginner": "Hello: Bawo",
        "intermediate": "How are you? : Bawo ni",
        "expert": "What are you doing today? : kini o n ṣe loni?"
    },
    "Igbo": {
        "beginner": "Hello: Ndewo",
        "intermediate": "How are you? : Kedu ka ịna?",
        "expert": "What are you doing today? : Kedu ihe ị na-eme taa?"
    }
}

def display_vocab(language, level):
    if level in dictionary[language]:
        print(f"\nVocabulary Lesson: {dictionary[language][level]}")
    else:
        print("\nNo vocabulary available for this level.")

# Yoruba class
class Yoruba:
    def __init__(self):
        self.mentor = nigerian_artists[0]  # WizKid is the mentor for Yoruba

    def start_learning(self):
        print(f"\nAwesome! You get to have celebrity {self.mentor} help you learn Yoruba!")
        self.check_proficiency()

    def check_proficiency(self):
        try:
            level = int(input("\nOn a scale of 1 to 10, how much do you know Yoruba? Enter (1-10): "))

            if 1 <= level <= 4:
                print("\nYou're a Beginner! Let's start with the basics!")
                display_vocab("Yoruba", "beginner")
            elif 5 <= level <= 7:
                print("\nOk you can listen here and speak there....Let's build on what you know!")
                display_vocab("Yoruba", "intermediate")
            elif 8 <= level <= 10:
                print("\nOh you're a natural expert... let's make you fluent!")
                display_vocab("Yoruba", "expert")
            else:
                print("\nInvalid input. Please enter a number between 1 and 10.")
                self.check_proficiency()
        except ValueError:
            print("Please enter a valid number!")
            self.check_proficiency()

# Igbo class
class Igbo:
    def __init__(self):
        self.mentor = nigerian_artists[1]  # Flavour is the mentor for Igbo

    def start_learning(self):
        print(f"\nAwesome! You get to have celebrity {self.mentor} help you learn Igbo!")
        self.check_proficiency()

    def check_proficiency(self):
        try:
            level = int(input("\nOn a scale of 1 to 10, how much do you know Igbo? Enter (1-10): "))

            if 1 <= level <= 4:
                print("\nYou're a Beginner! Let's start with the basics!")
                display_vocab("Igbo", "beginner")
            elif 5 <= level <= 7:
                print("\nOk you can listen here and speak there....Let's build on what you know!")
                display_vocab("Igbo", "intermediate")
            elif 8 <= level <= 10:
                print("\nOh you're a natural expert... let's make you fluent!")
                display_vocab("Igbo", "expert")
            else:
                print("\nInvalid input. Please enter a number between 1 and 10.")
                self.check_proficiency()
        except ValueError:
            print("Please enter a valid number!")
            self.check_proficiency()

# Main function
def main():
    print("Hi! What Nigerian language do you want to learn today?")
    print("1. Yoruba")
    print("2. Igbo")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        yoruba = Yoruba()
        yoruba.start_learning()
    elif choice == "2":
        igbo = Igbo()
        igbo.start_learning()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()
