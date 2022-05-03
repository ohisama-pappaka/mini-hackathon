from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

# python -m uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
print("HOGE")
class parmPokemon(BaseModel):
  paramPokemonName: str

@app.post("/")
def post_root(param: parmPokemon):
  return "Before Judge"
