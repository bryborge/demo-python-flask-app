from flask import abort
from flask import make_response
# Custom
from config import db
from models import Pokemon
from models import pokemon_schema


def read_all():
    pokemon = Pokemon.query.all()
    return pokemon_schema.dump(pokemon)


def read_one(name):
    pokemon = Pokemon.query.filter(Pokemon.name == name).one_or_none()

    if pokemon is not None:
        pokemon_schema.dump(pokemon)
    else:
        abort(404, f"Pokemon with name {name} not found")


def create(pokemon):
    name = pokemon.get("name")
    # description = pokemon.get("description")
    # types = pokemon.get("types")
    existing_pokemon = Pokemon.query.filter(Pokemon.name == name).one_or_none()

    if existing_pokemon is not None:
        new_pokemon = pokemon_schema.load(pokemon, session=db.session)
        db.session.add(new_pokemon)
        db.session.commit()
        return pokemon_schema.dump(new_pokemon), 201
    else:
        abort(406, f"Pokemon with name {name} already exists")


def update(name, pokemon):
    existing_pokemon = pokemon.query.filter(pokemon.name == name).one_or_none()

    if existing_pokemon:
        update_pokemon = pokemon_schema.load(pokemon, session=db.session)
        existing_pokemon.fname = update_pokemon.fname
        db.session.merge(existing_pokemon)
        db.session.commit()
        return pokemon_schema.dump(existing_pokemon), 201
    else:
        abort(404, f"Pokemon with name {name} not found")


def delete(name):
    existing_pokemon = Pokemon.query.filter(Pokemon.name == name).one_or_none()

    if existing_pokemon:
        db.session.delete(existing_pokemon)
        db.session.commit()
        return make_response(f"{name} successfully deleted", 200)
    else:
        abort(404, f"Pokemon with name {name} not found")
