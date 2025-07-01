"""Game endpoints: Create, join, and manage Tic Tac Toe games."""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List


router = APIRouter(
    prefix="/games",
    tags=["games"],
)


class CreateGameRequest(BaseModel):
    opponent_username: Optional[str] = Field(
        None, description="Username of the opponent to invite to the game."
    )


class JoinGameRequest(BaseModel):
    game_id: str = Field(..., description="ID of the game to join.")


class GameStateResponse(BaseModel):
    game_id: str
    board: List[List[str]]
    current_player: str
    players: List[str]
    status: str


# PUBLIC_INTERFACE
@router.post(
    "/create",
    summary="Create a new game",
    description="Start a new Tic Tac Toe game.",
)
def create_game(request: CreateGameRequest):
    """Create a new Tic Tac Toe game (stub)."""
    # Stub implementation
    return {
        "game_id": "fake-game-id",
        "status": "waiting_for_player",
    }


# PUBLIC_INTERFACE
@router.post(
    "/join",
    summary="Join an existing game",
    description="Join a Tic Tac Toe game by ID.",
)
def join_game(request: JoinGameRequest):
    """Join an existing game (stub)."""
    # Stub implementation
    return {
        "message": "Joined game (stub)",
        "game_id": request.game_id,
    }


# PUBLIC_INTERFACE
@router.get(
    "/{game_id}/state",
    response_model=GameStateResponse,
    summary="Get game state",
    description="Get the current state of a game.",
)
def get_game_state(game_id: str):
    """Get current state of a specified game (stub)."""
    # Stub implementation for a blank board
    return GameStateResponse(
        game_id=game_id,
        board=[["", "", ""] for _ in range(3)],
        current_player="user1",
        players=["user1", "user2"],
        status="in_progress",
    )
