from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import requests

# python -m uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

class parmPokemon(BaseModel):
  paramPokemonNameMe: str
  paramPokemonNameOpp: str

@app.post("/")
def post_root(param: parmPokemon):
  url_me = "https://pokeapi.co/api/v2/pokemon/" + param.paramPokemonNameMe
  url_opp = "https://pokeapi.co/api/v2/pokemon/" + param.paramPokemonNameOpp

  # # GETリクエストでデータを取得し、JSON形式に変える
  response_me = requests.get(url_me)
  pokemon_data_me = response_me.json()
  response_opp = requests.get(url_opp)
  pokemon_data_opp = response_opp.json()

  # データを見る
  photoUrl_me = (pokemon_data_me['sprites']['front_default'])
  photoUrl_opp = (pokemon_data_opp['sprites']['front_default'])

  #画像の取得

  
  if pokemon_data_me["stats"][5]["base_stat"] >pokemon_data_opp["stats"][5]["base_stat"]:
    output_name = param.paramPokemonNameMe
  elif pokemon_data_me["stats"][5]["base_stat"] <pokemon_data_opp["stats"][5]["base_stat"]:
    output_name = param.paramPokemonNameOpp
  else :
    output_name = "DRAW"

  return output_name, photoUrl_me, photoUrl_opp
