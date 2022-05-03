import { Box, HStack, Image } from "@chakra-ui/react";
import React from "react";

type Props = {
  photoUrlMe: string;
  photoUrlOpp: string;
} 

const DisplayImage = ({photoUrlMe, photoUrlOpp}: Props) => {
  return (
    <>
      <HStack>
        <Image src={photoUrlMe} fallbackSrc="https://via.placeholder.com/150" /*boxSize="150px" *//>
        <Box>VS</Box>
        <Image src={photoUrlOpp} fallbackSrc="https://via.placeholder.com/150" /*boxSize="150px" *//>
      </HStack>
    </>
  );
};

export default DisplayImage;
