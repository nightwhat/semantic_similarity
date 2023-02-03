import spacy

def find_similar_movie(description, movies_file):
    nlp = spacy.load("en_core_web_md")
    description = nlp(description)

    max_similarity = 0
    most_similar_movie = ''
    with open("movies.txt", "r") as file:
        for line in file:
            title, movie_description = line.strip().split(':', maxsplit=1)
            movie_description = nlp(movie_description)
            similarity = description.similarity(movie_description)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_movie = title

    return most_similar_movie

Planet_Hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

movies_file = "movies.txt"

similar_movie = find_similar_movie(Planet_Hulk_description, movies_file)

print(f"Because you enjoyed Planet Hulk you should watch {similar_movie}!")

