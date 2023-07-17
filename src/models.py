from datetime import datetime
from config import db, ma


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(1000))
    type = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        load_instance = True
        sqla_session = db.session


pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)
