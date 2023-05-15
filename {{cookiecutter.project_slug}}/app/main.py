"""
Creating the FastAPI application
"""
from fastapi import FastAPI
from app.routers.dome import router as dome_router
from app import __version__


def create_app():
    """
    Create the FastAPI app and include a DOME 4.0 router.

    Returns:
        A FastAPI app with a DOME 4.0 router included.
    """
    app = FastAPI(
        title="FASTAPI-TEMPLATE",
        version=__version__,
        description="Start your project here",
    )

    app.include_router(dome_router)
    return app


APP = create_app()
