from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # replace with a random secret key

# List of 8 Pokémon
POKEMONS = [
    {"name": "bulbasaur", "shadow": "bulbasaur_shadow.png", "real": "bulbasaur.png"},
    {"name": "charmander", "shadow": "charmander_shadow.png", "real": "charmander.png"},
    {"name": "charizard", "shadow": "charizard_shadow.png", "real": "charizard.png"},
    {"name": "pikachu", "shadow": "pikachu_shadow.png", "real": "pikachu.png"},
    {"name": "koffing", "shadow": "koffing_shadow.png", "real": "koffing.png"},
    {"name": "mewtwo", "shadow": "mewtwo_shadow.png", "real": "mewtwo.png"},
    {"name": "psyduck", "shadow": "psyduck_shadow.png", "real": "psyduck.png"},
    {"name": "snorlax", "shadow": "snorlax_shadow.png", "real": "snorlax.png"}
]

def pick_random_pokemon(shown):
    remaining = [p for p in POKEMONS if p["name"] not in shown]
    if not remaining:
        return None
    return random.choice(remaining)

@app.route("/")
def home():
    session["shown"] = []
    session["score"] = 0
    return render_template("home.html") #redirect(url_for("game"))

@app.route("/game", methods=["GET", "POST"])
def game():
    if "shown" not in session:
        session["shown"] = []
    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":
        # Get the current Pokémon from session
        current_name = session.get("current_pokemon")
        current = next((p for p in POKEMONS if p["name"] == current_name), None)

        guess = request.form.get("pokemon_guess", "").strip().lower()
        session["shown"].append(current["name"])
        correct = guess == current["name"]
        if correct:
            session["score"] += 1

        # Remove current_pokemon from session so next GET picks a new one
        session.pop("current_pokemon", None)

        return render_template("result.html",
                               final=False,
                               correct=correct,
                               answer=current["name"],
                               image=current["real"])

    # GET → pick a new Pokémon
    current = pick_random_pokemon(session["shown"])
    if current is None:
        # All Pokémon done
        total = len(session.get("shown", []))
        score = session.get("score", 0)
        percent = int((score / total) * 100) if total > 0 else 0
        return render_template("result.html", final=True, score=score, total=total, percent=percent)

    # Save current Pokémon in session
    session["current_pokemon"] = current["name"]

    return render_template("game.html", shadow_image=current["shadow"])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
