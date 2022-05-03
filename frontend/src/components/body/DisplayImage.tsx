import { Box, HStack, Image } from "@chakra-ui/react";
import React from "react";

const DisplayImage = () => {
  return (
    <>
      <HStack>
        <Image src="###" fallbackSrc="https://via.placeholder.com/150" boxSize="150px" />
        <Box>VS</Box>
        <Image src="###" fallbackSrc="https://via.placeholder.com/150" boxSize="150px" />
      </HStack>
    </>
  );
};

export default DisplayImage;
