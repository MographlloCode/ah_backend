from uuid import UUID

from core.db import athletes
from api.athlete.schemas import FootballAthleteSchema

class AthleteController():
    def get_athletes():
        return athletes

    def get_athlete(athlete_id: UUID):
        for athlete in athletes:
            if athlete.id == athlete_id:
                return athlete
        return {"msg": "No athlete found"}

    def create_athlete(athlete_data: FootballAthleteSchema.Base):
        athletes.append(athlete_data)
        
    def update_athlete(athlete_id: UUID, athlete: FootballAthleteSchema.Update):
        ...
        
    def delete_athlete(athlete_id: UUID):
        for athlete in athletes:
            if athlete.id == athlete_id:
                athletes.remove(athlete)