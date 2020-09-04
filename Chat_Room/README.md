# Chat Room

## Overview
Server and clients for a simple chat room application. These were implemented in the C programming language using the Socket API to create TCP connections. Participant-clients send messages to the server. Observer-clients associate with participant-clients via username to receive and display appropriate public and private messages. The server uses select(2) to manage many connections on multiple ports.

## Skills & Experience Gained
- Improved proficiency in the C programming language.
- Experience using the socket(2) api.
- Knowledge of networking concepts.

## Contents
As this project is related to classwork, raw code must be omitted.
- **instructions/** : Contains the assignment instructions that outline the learning goals and tasks completed. 
- **observer** : Compiled Observer-client. This client associates with a participant upon connecting to the server to display messages meant for that user.
- **participant** : The compiled Participant-client. This client chooses a username upon connecting to the server. Participants can send public and private messages.
- **server** : The compiled chat-room server program.
