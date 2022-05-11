import * as React from "react";
import { StyleSheet } from 'react-native';
import Background from "../components/Background";
import HomeButton from "../components/HomeButton";
import { theme } from '../core/theme';
import { Avatar, Button, Card, Title, Paragraph } from "react-native-paper";

export default function LoginScreen({ navigation }) {
  return (
    <Background>
      <Title>Login Template</Title>

      <Paragraph>
        La mejor forma de tener en control las bateas
      </Paragraph>
      <HomeButton
        mode="contained"
        onPress={() => navigation.navigate("Login")}
      >
        Login
      </HomeButton>
      <HomeButton
        mode="outlined"
        onPress={() => navigation.navigate("Registro")}
      >
        Sign Up
      </HomeButton>
    </Background>
  );
}

const styles = StyleSheet.create({
    text: {
        fontSize: 16,
        lineHeight: 26,
        color: theme.colors.secondary,
        textAlign: 'center',
        marginBottom: 14,
    },
});