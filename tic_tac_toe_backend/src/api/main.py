from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from .auth import router as auth_router
from .game import router as game_router
from .moves import router as moves_router
from .scores import router as scores_router


app = FastAPI(
    title="Tic Tac Toe Backend",
    description=(
        "Backend API for Tic Tac Toe Game: handles authentication, game logic, "
        "moves, and score tracking."
    ),
    version="0.1.0",
    openapi_tags=[
        {"name": "auth", "description": "Authentication operations"},
        {"name": "games", "description": "Manage Tic Tac Toe games"},
        {"name": "moves", "description": "Submit and view game moves"},
        {"name": "scores", "description": "Score and history endpoints"},
    ],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routers
app.include_router(auth_router)
app.include_router(game_router)
app.include_router(moves_router)
app.include_router(scores_router)


@app.get("/", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}
