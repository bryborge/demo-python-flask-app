from datetime import datetime
from flask import abort


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


POKEMON = {
    "Bulbasaur": {
        "name": "bulbasaur",
        "description": "A small, quadrupedal amphibian Pokemon that has blue-green skin with darker patches.",
        "types": ["grass", "poison"],
        "timestamp": get_timestamp(),
    },
    "Charmander": {
        "name": "charmander",
        "description": "A bipedal, reptilian Pokemon with a primarily orange body and blue eyes.",
        "types": ["fire"],
        "timestamp": get_timestamp(),
    },
    "Squirtle": {
        "name": "squirtle",
        "description": "A small reptilian Pokemon that resembles a light-blue turtle.",
        "types": ["water"],
        "timestamp": get_timestamp(),
    },
    "Pikachu": {
        "name": "pikachu",
        "description": "A short, chubby rodent Pokemon. It is covered in yellow fur with two horizontal brown stripes "
                       "on its back.",
        "types": ["electric"],
        "timestamp": get_timestamp(),
    }
}


def read_all():
    return list(POKEMON.values())


def read_one(name):
    if name in POKEMON:
        return POKEMON[name]
    else:
        abort(
            404, f"Pokemon with name {name} not found"
        )


def create(pokemon):
    name = pokemon.get("name")
    description = pokemon.get("description")
    types = pokemon.get("types")

    if name not in POKEMON:
        POKEMON[name] = {
            "name": name,
            "description": description,
            "types": types,
            "timestamp": get_timestamp()
        }
        return POKEMON[name], 201
    else:
        abort(
            406,
            f"Pokemon with name {name} already exists"
        )
