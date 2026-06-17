from datetime import datetime

from pydantic import BaseModel


class GameScoreCreate(BaseModel):
    game: str
    score: int


class GameScorePublic(BaseModel):
    id: int
    game: str
    score: int
    created_at: datetime
    model_config = {"from_attributes": True}


class GameScoreInDB(GameScoreCreate):
    user_id: int


class GameScoreUpdate(BaseModel):
    pass


class LeaderboardEntry(BaseModel):
    rank: int
    username: str
    score: int
    achieved_at: datetime
