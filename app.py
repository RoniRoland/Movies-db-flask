from flask import Flask, request, jsonify
from Movie import Movies

app = Flask(__name__)

# Lista de objetos Movies (simulación)
movies = []


# Endpoint para agregar una película
@app.route("/api/new-movie", methods=["POST"])
def add_movie():
    data = request.get_json()
    movie_id = data.get("movieId")
    name = data.get("name")
    genre = data.get("genre")

    if movie_id is None or name is None or genre is None:
        return jsonify({"message": "Faltan datos requeridos"}), 400

    movie = Movies(movie_id, name, genre)
    movies.append(movie)

    print(f"Película {name} agregada con éxito")
    return jsonify({"message": "Película agregada con éxito"}), 201


# Endpoint para obtener todas las películas por género
@app.route("/api/all-movies-by-genre/<string:genre>", methods=["GET"])
def get_movies_by_genre(genre):
    genre_movies = [movie.__dict__ for movie in movies if movie.genre == genre]
    if not genre_movies:
        print(f"No se encontraron películas del género: {genre}")
        return (
            jsonify({"message": f"No se encontraron películas del género: {genre}"}),
            404,
        )

    print(f"Películas del género {genre}: {genre_movies}")
    return jsonify(genre_movies)


# Endpoint para actualizar una película
@app.route("/api/update-movie", methods=["PUT"])
def update_movie():
    data = request.get_json()
    movie_id = data.get("movieId")
    name = data.get("name")
    genre = data.get("genre")

    if movie_id is None:
        print("Falta el ID de la película")
        return jsonify({"message": "Falta el ID de la película"}), 400

    for movie in movies:
        if movie.MovID == movie_id:
            movie.name = name
            movie.genre = genre
            print("Película actualizada con éxito")
            return jsonify({"message": "Película actualizada con éxito"})

    print("Pelicula no encontrada")
    return jsonify({"message": "Película no encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)
