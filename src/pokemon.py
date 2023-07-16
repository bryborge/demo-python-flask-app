from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


POKEMON = {
    "0001": {
        "name": "bulbasaur",
        "description": "A small, quadrupedal amphibian Pokemon that has blue-green skin with darker patches.",
        "types": ["grass", "poison"],
        "timestamp": get_timestamp(),
    },
    "0004": {
        "name": "charmander",
        "description": "A bipedal, reptilian Pokemon with a primarily orange body and blue eyes.",
        "types": ["fire"],
        "timestamp": get_timestamp(),
    },
    "0007": {
        "name": "squirtle",
        "description": "A small reptilian Pokemon that resembles a light-blue turtle.",
        "types": ["water"],
        "timestamp": get_timestamp(),
    },
    "0025": {
        "name": "pikachu",
        "description": "A short, chubby rodent Pokemon. It is covered in yellow fur with two horizontal brown stripes "
                       "on its back.",
        "types": ["electric"],
        "timestamp": get_timestamp(),
    }
}


def read_all():
    return list(POKEMON.values())
