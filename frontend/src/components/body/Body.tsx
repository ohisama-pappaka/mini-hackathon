import React from "react";
import { Button, HStack, Input, Text, VStack } from "@chakra-ui/react";

const Body = () => {
  return (
    <>
      <VStack>
        <HStack>
          <Input placeholder="Pokemon Name Me" />
          <Button>Decide</Button>
        </HStack>
        <HStack>
          <Input placeholder="Pokemon Name Opp" />
          <Button>Decide</Button>
        </HStack>
        <Text>判定結果</Text>
        <Text>temp</Text>
      </VStack>
    </>
  );
};

export default Body;
