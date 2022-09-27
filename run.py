from app.config import config
from app.models import Genre, Director, Movie
from app.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        'db': db,
        'Genre': Genre,
        'Director': Director,
        'Movie': Movie,
    }
