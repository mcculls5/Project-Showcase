# Chat Room

## Overview
A server and client for the Boggle game. These were implemented in the C programming language using the Socket API to create TCP connections. The server pairs incoming clients for each two-player game session. Threading is used to allow many separate game instances to be played simultaneously.

## Contents
As this project is related to classwork, raw code must be omitted.
- **instructions/** : Contains the assignment instructions that outline the learning goals and tasks completed. 
- **observer** : Compiled Observer-client. This client associates with a participant upon connecting to the server to display messages meant for that user.
- **participant** : The compiled Participant-client. This client chooses a username upon connecting to the server. Participants can send public and private messages.
- **server** : The compiled chat-room server program.
