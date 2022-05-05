def LanguageConversion(pokemonNameMe, pokemonNameOpp):
  import json

  returnPokemonNameMe = pokemonNameMe
  returnPokemonNameOpp = pokemonNameOpp

  pokemonData_open = open("./data/pokemon.json", "r", encoding="utf-8")
  pokemonData = json.load(pokemonData_open)

  for i in range(len(pokemonData)):
    if pokemonData[i]["ja"] == pokemonNameMe:
      returnPokemonNameMe = pokemonData[i]["en"].lower()
    if pokemonData[i]["ja"] == pokemonNameOpp:
      returnPokemonNameOpp = pokemonData[i]["en"].lower()

  return returnPokemonNameMe, returnPokemonNameOpp
