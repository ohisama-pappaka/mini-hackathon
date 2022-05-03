from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import requests

# python -m uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[""],
  allow_credentials=True,
  allow_methods=[""],
  allow_headers=["*"]
)

class parmPokemon(BaseModel):
  paramPokemonNameMe: str
  paramPokemonNameOpp: str

@app.post("/")
def post_root(param: parmPokemon):
  url_me = f"https://pokeapi.co/api/v2/pokemon/%7Bparam.paramPokemonNameMe%7D/"
  url_opp = f"https://pokeapi.co/api/v2/pokemon/%7Bparam.paramPokemonNameOpp%7D/"

  # GETリクエストでデータを取得し、JSON形式に変える
  response_me = requests.get(url_me)
  pokemon_data_me = response_me.json()
  response_opp = requests.get(url_opp)
  pokemon_data_opp = response_opp.json()

  # データを見る
 
  photoUrl_me = (pokemon_data_me['sprites']['front_default'])
  photoUrl_opp = (pokemon_data_opp['sprites']['front_default'])

  photoUrl = [photoUrl_me, photoUrl_opp]

  return photoUrl
