import React from "react";

import Header from "./components/header/Header";
import Body from "./components/body/Body";
import { Container } from "@chakra-ui/react";

const App = () => {
  return (
    <>
      <Header />
      <Container maxW="container.md" pt="20px">
        <Body />
      </Container>
    </>
  );
};

export default App;
