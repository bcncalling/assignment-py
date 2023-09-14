from .config import config
from .routes import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=int(config.PORT), host="127.0.0.1")
