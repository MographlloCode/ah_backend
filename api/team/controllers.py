from uuid import UUID
from api.team.schemas import TeamSchema

class TeamController:
    def get_teams():
        ...
    
    def get_team(team_id: UUID):
        ...
    
    def create_team(team: TeamSchema.Base):
        ...
        
    def update_team(team_id: UUID, team: TeamSchema.Update):
        ...
        
    def delete_team(team_id: UUID):
        ...