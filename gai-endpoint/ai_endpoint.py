import uvicorn
from fastapi import FastAPI

from service.nsf import NSFAwardsAPI, NSFAwardsAPISearchParams


# endpoint for openapi http://127.0.0.1:8000/openapi.json


app = FastAPI()


@app.get("/")
async def health():
    return {"status": "ok"}


@app.post("/search_awards/")
def search_awards(params: NSFAwardsAPISearchParams):
    api = NSFAwardsAPI(format='json')
    api.set_search_params(**params.dict(exclude_none=True))
    return api.search_awards()


@app.get("/award/{award_id}")
def get_award(award_id: str):
    api = NSFAwardsAPI(format='json')
    return api.get_award_by_id(award_id)

@app.get("/project_outcomes/{award_id}")
def get_project_outcomes(award_id: str):
    api = NSFAwardsAPI(format='json')
    return api.get_project_outcomes(award_id)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




