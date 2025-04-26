from fastapi import APIRouter
from uuid import UUID

from api.athlete.controllers import AthleteController
from api.athlete.schemas import FootballAthleteSchema

router = APIRouter()

@router.get('/')
def get_all_athletes():
    return AthleteController.get_athletes()
    
@router.get('/{athlete_id}')
def get_specific_athlete(athlete_id: UUID):
    return AthleteController.get_athlete(athlete_id)

@router.post('/')
def create_athlete(athlete_data: FootballAthleteSchema.Base):
    if(athlete_data):
        AthleteController.create_athlete(athlete_data)
        return {
            "msg": f"Athlete Created",
            "athlete": athlete_data
        }
    
@router.patch('/{athlete_id}')
def update_athlete(athlete_id: UUID):
    return {"msg": f"Athlete: {athlete_id}"}
    
@router.delete('/')
def delete_athlete():
    return {"msg": "Athlete delete"}