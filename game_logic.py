import random

# List of Pokémon with their shadow and real image filenames
POKEMONS = [
    {"name": "bulbasaur", "shadow": "bulbasaur_shadow.png", "real": "bulbasaur.png"},
    {"name": "charmander", "shadow": "charmander_shadow.png", "real": "charmander.png"},
    {"name": "charizard", "shadow": "charizard_shadow.png", "real": "charizard.png"},
    {"name": "pikachu", "shadow": "pikachu_shadow.png", "real": "pikachu.png"},
    {"name": "koffing", "shadow": "koffing_shadow.png", "real": "koffing.png"},
    {"name": "mewtwo", "shadow": "mewtwo_shadow.png", "real": "mewtwo.png"},
    {"name": "psyduck", "shadow": "psyduck_shadow.png", "real": "psyduck.jpeg"},
    {"name": "snorlax", "shadow": "snorlax_shadow.png", "real": "snorlax.png"}
]

def pick_random_pokemon(already_shown):
    """Return a random Pokémon that hasn't been shown yet."""
    remaining = [p for p in POKEMONS if p["name"] not in already_shown]
    if not remaining:
        return None  # all Pokémon have been shown
    return random.choice(remaining)
