"""Score and history endpoints: View user scores and game history."""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter(
    prefix="/scores",
    tags=["scores"],
)


class ScoreEntry(BaseModel):
    username: str
    wins: int
    losses: int
    draws: int


class GameHistoryEntry(BaseModel):
    game_id: str
    result: str
    date: str


# PUBLIC_INTERFACE
@router.get(
    "/",
    response_model=List[ScoreEntry],
    summary="Get user scores",
    description="List scores for all users.",
)
def get_scores():
    """List scores for all users (stub)."""
    # Stub implementation
    return [
        ScoreEntry(username="user1", wins=2, losses=3, draws=1),
        ScoreEntry(username="user2", wins=4, losses=2, draws=0),
    ]


# PUBLIC_INTERFACE
@router.get(
    "/{username}/history",
    response_model=List[GameHistoryEntry],
    summary="Get user game history",
    description="Get all games played by a user.",
)
def get_user_history(username: str):
    """Get all games played by a user (stub)."""
    # Stub implementation
    return [
        GameHistoryEntry(game_id="game-123", result="win", date="2024-05-01"),
        GameHistoryEntry(game_id="game-456", result="loss", date="2024-05-03"),
    ]
