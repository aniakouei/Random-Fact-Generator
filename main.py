from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import random

app = FastAPI()

class Fact(BaseModel):
    id: int
    fact: str

# Sample data of facts
facts = [
    Fact(id=1, fact="Canadian Northwest Territories License plates are shaped like polar bears."),
    Fact(id=2, fact="The Governor of Moscow trained a large bear to serve pepper Vodka to his guests."),
    Fact(id=3, fact="Grass is Green."),
    Fact(id=4, fact="Birds Chirping release endorphins")
]

@app.get("/")
async def root():
    return {"message": "Welcome to the Random Fact API!"}

@app.get("/fact")
async def get_random_fact(id: int = None):
    if id is not None:
        for fact in facts:
            if fact.id == id:
                return fact
        raise HTTPException(status_code=404, detail="Fact not found")
    else:
        return random.choice(facts)

@app.get("/fact/{id}")
async def get_fact_by_id(id: int):
    for fact in facts:
        if fact.id == id:
            return fact
    raise HTTPException(status_code=404, detail="Fact not found")

@app.get("/fact/query")
async def get_fact_by_query_id(id: int = Query(..., title="The ID of the fact to retrieve")):
    for fact in facts:
        if fact.id == id:
            return fact


@app.post("/fact")
async def add_fact(fact: Fact):
    new_id = max(fact.id for fact in facts) + 1
    fact.id = new_id
    facts.append(fact)
    return fact



