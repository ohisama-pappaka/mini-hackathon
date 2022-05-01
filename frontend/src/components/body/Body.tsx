import React, { ChangeEventHandler, useState } from "react";
import { Button, HStack, Input, Text, VStack } from "@chakra-ui/react";
import axios from "axios";

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

  const handleClickDecide = (param: string) => {
    if (param === "ME") {
      axios.post("http://localhost:8000/", { paramPokemonName: pokemonNameMe }).then((res) => {
        setSpeedJudge(res.data);
      });
    }
    if (param === "OPP") {
      axios.post("http://localhost:8000/", { paramPokemonName: pokemonNameOpp }).then((res) => {
        setSpeedJudge(res.data);
      });
    }
  };

  return (
    <>
      <VStack>
        <HStack>
          <Input placeholder="Pokemon Name Me" onChange={handleInputTextMe} />
          <Button
            onClick={() => {
              handleClickDecide("ME");
            }}
          >
            Decide
          </Button>
        </HStack>
        <HStack>
          <Input placeholder="Pokemon Name Opp" onChange={handleInputTextOpp} />
          <Button
            onClick={() => {
              handleClickDecide("OPP");
            }}
          >
            Decide
          </Button>
        </HStack>
        <Text>判定結果</Text>
        <Text>{speedJudge}</Text>
      </VStack>
    </>
  );
};

export default Body;
