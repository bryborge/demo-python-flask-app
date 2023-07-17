from flask import render_template
import config
from models import Pokemon


app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    pokemon = Pokemon.query.all()
    return render_template("index.html", pokemon=pokemon)


if __name__ == "__main__":
    app.run(debug=True)
