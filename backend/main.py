from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import requests

from language_conversion import LanguageConversion

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
  # 日本語入力を英語入力に変換した
  inputPokemonNameMe, inputPokemonNameOppEn = LanguageConversion(param.paramPokemonNameMe, param.paramPokemonNameOpp)

  url_me = "https://pokeapi.co/api/v2/pokemon/" + inputPokemonNameMe
  url_opp = "https://pokeapi.co/api/v2/pokemon/" + inputPokemonNameOppEn

  # # GETリクエストでデータを取得し、JSON形式に変える
  response_me = requests.get(url_me)
  pokemon_data_me = response_me.json()
  response_opp = requests.get(url_opp)
  pokemon_data_opp = response_opp.json()

  # 画像の取得
  photoUrl_me = (pokemon_data_me['sprites']['front_default'])
  photoUrl_opp = (pokemon_data_opp['sprites']['front_default'])

  # 素早さの判定
  if pokemon_data_opp["stats"][5]["base_stat"] < pokemon_data_me["stats"][5]["base_stat"]:
    output_name = param.paramPokemonNameMe
  elif pokemon_data_me["stats"][5]["base_stat"] < pokemon_data_opp["stats"][5]["base_stat"]:
    output_name = param.paramPokemonNameOpp
  else :
    output_name = "DRAW"

  return output_name, photoUrl_me, photoUrl_opp
