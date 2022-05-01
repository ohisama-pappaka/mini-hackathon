import React from "react";
import { Container } from "@chakra-ui/react";

import Header from "./components/header/Header";
import Body from "./components/body/Body";

const App = () => {
  return (
    <>
      <Header />
      <Container maxW="container.md">
        <Body />
      </Container>
    </>
  );
};

export default App;
