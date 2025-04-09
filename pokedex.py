# Define the Pokemon class
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    # Instance method for the Pokemon's sound
    def speak(self):
        print(f"{self.name}! {self.name}!")

    # Instance method to display details of the Pokemon
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")  # Join multiple types with commas
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet!")

# Create Pokemon objects
pikachu = Pokemon(
    entry=25,
    name="Pikachu",
    types=["Electric"],
    description="It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",
    is_caught=True
)

bulbasaur = Pokemon(
    entry=1,
    name="Bulbasaur",
    types=["Grass", "Poison"],
    description="A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.",
    is_caught=False
)

charmander = Pokemon(
    entry=4,
    name="Charmander",
    types=["Fire"],
    description="It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.",
    is_caught=True
)

# Use the instance methods
pikachu.speak()
pikachu.display_details()

print("\n")  # Line break for readability

bulbasaur.speak()
bulbasaur.display_details()

print("\n")  # Line break for readability

charmander.speak()
charmander.display_details()
