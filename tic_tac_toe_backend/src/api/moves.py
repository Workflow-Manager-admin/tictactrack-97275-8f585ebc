"""Move endpoints: Make a move and get move history for a game."""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List


router = APIRouter(
    prefix="/moves",
    tags=["moves"],
)


class MoveRequest(BaseModel):
    game_id: str = Field(..., description="ID of the game")
    row: int = Field(..., ge=0, le=2, description="Row index (0-2)")
    col: int = Field(..., ge=0, le=2, description="Column index (0-2)")


class MoveResponse(BaseModel):
    success: bool
    message: str


class MoveHistoryResponse(BaseModel):
    moves: List[dict]


# PUBLIC_INTERFACE
@router.post(
    "/make",
    response_model=MoveResponse,
    summary="Make a move",
    description="Submit a player's move.",
)
def make_move(request: MoveRequest):
    """Endpoint to process a player's move (stub)."""
    # Stub implementation
    return MoveResponse(success=True, message="Move accepted (stub)")


# PUBLIC_INTERFACE
@router.get(
    "/{game_id}/history",
    response_model=MoveHistoryResponse,
    summary="Get move history",
    description="Get all moves for a specific game.",
)
def get_move_history(game_id: str):
    """Endpoint to get move history for a specific game (stub)."""
    # Stub implementation
    return MoveHistoryResponse(moves=[])
