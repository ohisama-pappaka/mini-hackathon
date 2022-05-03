import React, { ChangeEventHandler, useState } from "react";
import { Button, Input, Text, VStack } from "@chakra-ui/react";
import axios from "axios";

import DisplayImage from "./DisplayImage";

const Body = () => {
  const [pokemonNameMe, setPokemonNameMe] = useState<string>("");
  const [pokemonNameOpp, setPokemonNameOpp] = useState<string>("");
  const [speedJudge, setSpeedJudge] = useState<string>("");

  const handleInputTextMe: ChangeEventHandler<HTMLInputElement> = (event) => {
    const inputText = event.target.value;
    setPokemonNameMe(inputText);
  };

  const handleInputTextOpp: ChangeEventHandler<HTMLInputElement> = (event) => {
    const inputText = event.target.value;
    setPokemonNameOpp(inputText);
  };

  const handleClickDecide = () => {
    axios
      .post("http://localhost:8000/", {
        paramPokemonNameMe: pokemonNameMe,
        paramPokemonNameOpp: pokemonNameOpp,
      })
      .then((res) => {
        setSpeedJudge(res.data);
      });
  };

  return (
    <>
      <VStack>
        <Input placeholder="Pokemon Name Me" onChange={handleInputTextMe} />
        <Input placeholder="Pokemon Name Opp" onChange={handleInputTextOpp} />
        <Button
          colorScheme="black"
          variant="outline"
          onClick={() => {
            handleClickDecide();
          }}
        >
          Decide
        </Button>
        <DisplayImage />
        <Text>判定結果</Text>
        <Text>{speedJudge}</Text>
      </VStack>
    </>
  );
};

export default Body;
