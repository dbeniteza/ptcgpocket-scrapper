# constants.py

# Base URL for the Pokémon TCG API
BASE_URL = "https://pocket.limitlesstcg.com/cards/"

# Starting ID for card iteration
START_ID = 1

# Filename to save the card data
FILENAME = "ptcgp_cards.json"

# Mapping of type symbols to type names
TYPE_MAPPING = {
  "G": "Grass",
  "R": "Fire",
  "W": "Water",
  "L": "Lightning",
  "P": "Psychic",
  "F": "Fighting",
  "D": "Darkness",
  "M": "Metal",
  "Y": "Fairy",
  "C": "Colorless",
}

# List of sets to iterate over (update with every new event or set release)
SETS = ["A1", "P-A", "A1a", "A2", "A2a", "A2b", "A3"]

# Number of cards in each set (update with every new event or set release)
SETS_CARDS_NO = {
  "A1": 286,
  "P-A": 73,
  "A1a": 86,
  "A2": 207,
  "A2a": 96,
  "A2b": 111,
  "A3": 239
}

# List of packs
PACKS = [
  "Pikachu pack",
  "Charizard pack",
  "Mewtwo pack",
  "Mew pack",
  "Dialga pack",
  "Palkia pack",
  "Arceus pack",
  # Shining Revelry (A2b) - No pack name
  "Solgaleo pack",
  "Lunala pack"
]

# List of full art rarities
FULLART_RARITIES = ["☆", "☆☆", "☆☆☆", "Crown Rare", "☆ Shiny", "☆☆ Shiny"]

# Crafting cost by rarity
CRAFTING_COST = {
  "◊": 35,
  "◊◊": 70,
  "◊◊◊": 150,
  "◊◊◊◊": 500,
  "☆": 400,
  "☆☆": 1250,
  "☆☆☆": 1500,
  "♛": 2500,
  "☆ Shiny": 1000,
  "☆☆ Shiny": 1350
}

# Probability rates by rarity and row
PROBABILITYS_PER_ROW = RATE_BY_RARITY = {
  # Probability rates for different rows and rarities
  "1-3 card": {
    "◊": "100.000%",
    "◊◊": "0.000%",
    "◊◊◊": "0.000%",
    "◊◊◊◊": "0.000%",
    "☆": "0.000%",
    "☆☆": "0.000%",
    "☆☆☆": "0.000%",
    "♛": "0.000%",
    "☆ Shiny": "0.000%",
    "☆☆ Shiny": "0.000%"
  },
  "4 card": {
    "◊": "0.000%",
    "◊◊": "90.000%",
    "◊◊◊": "5.000%",
    "◊◊◊◊": "1.666%",
    "☆": "2.572%",
    "☆☆": "0.500%",
    "☆☆☆": "0.222%",
    "♛": "0.040%",
    "☆ Shiny": "0.714%",
    "☆☆ Shiny": "0.333%"
  },
  "5 card": {
    "◊": "0.000%",
    "◊◊": "60.000%",
    "◊◊◊": "20.000%",
    "◊◊◊◊": "6.664%",
    "☆": "10.288%",
    "☆☆": "2.000%",
    "☆☆☆": "0.888%",
    "♛": "0.160%",
    "☆ Shiny": "2.857%",
    "☆☆ Shiny": "1.333%"
  },
}

