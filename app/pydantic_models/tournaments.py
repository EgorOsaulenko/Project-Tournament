from pydantic import BaseModel, Field

from app.db.tournaments.db_actions import Vote
from app.db.tournaments.models import Tournament
from app.db.teams.models import Team


class TournamentModel(BaseModel):
    name: str = Field(...,)
    exp_days: int = Field(7)


class TournamentModelResponse(BaseModel):
    id: str


class VoteModel(BaseModel):
    team_id: str
    tournament_id: str
    vote: Vote 


class ResultModel(BaseModel):
    team_name: str
    tournament_name: str
    result: float
    vote_result: int