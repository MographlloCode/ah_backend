from fastapi import FastAPI
from core.utils import API_V1_ROUTE

from api.routes import (
    auth_router,
    athlete_router,
    competition_router,
    team_router
)

app = FastAPI(
    title="Athlete House",
    description="Athlete House API"
)

app.include_router(auth_router, prefix=f"{API_V1_ROUTE}/auth")
app.include_router(team_router, prefix=f"{API_V1_ROUTE}/teams")
app.include_router(athlete_router, prefix=f"{API_V1_ROUTE}/athletes")
app.include_router(competition_router, prefix=f"{API_V1_ROUTE}/competitions")

if __name__=="__main__":
    import uvicorn
    
    uvicorn.run("app:app", port=5000, log_level="info", reload=True)