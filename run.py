from app import create_app, db, cli
from app.models import Post
from app.blueprints.authentication.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    # ALWAYS HAVE TO RETURN A PYTHON DICTIONARY FROM CONTEXT
    return {
        'db': db,
        'Post': Post,
        'User': User
    }