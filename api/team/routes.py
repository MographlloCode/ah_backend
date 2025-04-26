from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_all_teams():
    ...

@router.get('/{team_id}')
def get_team():
    ...
    
@router.post('/')
def create_team():
    ...

@router.patch('/{team_id}')
def update_team():
    ...

@router.delete('/{team_id}')
def delete_team():
    ...