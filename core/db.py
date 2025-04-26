# Users
users = [
    {
        "id": "uuid4",
        "first_name": "Gustavo",
        "last_name": "Mello",
        "birth_date": "31072000",
        "nacionality_id": 2,
        "username": "ogusmello",
        "password": "encryptedpassword",
        "email": "ogusmello@gmail.com",
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4"
    }
]

# Athletes
athletes = [
    {
        "id": "uuid4",
        "first_name": "Gustavo",
        "last_name": "Mello",
        "birth_date": "31072000",
        "nacionality_id": 2,
        "sport_id": 2,
        "weight": 137.5,
        "height": 193,
        "pref_leg": "right",
        "jersey_number": 31,
        "position": "CB",
        "goals": 3,
        "assists": 1,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

# Teams
teams = [
    {
        "id": "uuid4",
        "name": "Sport Club Corinthians Paulista",
        "short_name": "SCCP",
        "public_known_as": "Corinthians",
        "stadium_id": "uuid4", 
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4", 
    }
]

team_althletes = [
    {
        "id": 1,
        "team_id": "uuid4",
        "athlete_id": "uuid4",
        "joined_at": "23042025",
        "left_at": None,
        "salary": 10000.00,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

team_stadiums = [
    {
        "id": "uuid4",
        "team_id": "uuid4",
        "stadium_name": "Neo Química Arena",
        "seats": 45000,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

# Competition
competitions = [
    {
        "id": "uuid4",
        "name": "Copa do Brasil",
        "rounds": 24,
        "competition_type": "mata_mata",
        "total_prize": 1000000.00,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

competition_seasons = [
    {
        "id": "uuid4",
        "season": "24/25",
        "competition_id": "uuid4",
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

competition_prizes = [
    {
        "id": 1,
        "competition_id": "uuid4",
        "position": 4,
        "prize": 1000000.00,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

competition_season_teams = [
    {
        "id": 1,
        "competition_id": "uuid4",
        "season_id": "uuid4",
        "team_id": "uuid4",
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

competition_matches = [
    {
        "id": "uuid4",
        "competition_id": "uuid4",
        "season_id": "uuid4",
        "home_team_id": "uuid4",
        "away_team_id": "uuid4",
        "home_team_score": 0,
        "away_team_score": 0,
        "stadium_id": "uuid4",
        "match_day": "31072000T160000",
        "fans": 32234,
        "ticket_income": 2000000.00,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]

competition_rounds = [
    {
        "id": "uuid4",
        "round": 1,
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]
competition_round_matches = [
    {
        "id": "uuid4",
        "round_id": "uuid4",
        "match_id": "uuid4",
        "created_at": "31012025T160823",
        "updated_at": "31012025T160823",
        "created_by": "uuid4",
        "updated_by": "uuid4",
    }
]