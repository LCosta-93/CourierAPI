try:
    from app import create_app
except ImportError:
    raise RuntimeError("Failed to import create_app from app package")

app = create_app()
