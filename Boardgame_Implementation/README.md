# Deadwood Boardgame Implementation
<img src="https://raw.githubusercontent.com/mcculls5/Project-Showcase/master/Boardgame_Implementation/Game.png" alt="Image of Game.exe gameplay" width="800"/>

![Image of Game.exe gameplay](https://raw.githubusercontent.com/mcculls5/Project-Showcase/master/Boardgame_Implementation/Game.png)

## Overview
Object-Oriented design patterns were used to implement the Deadwood boardgame in Java. This includes the use of interfaces, abstract classes, state machines, observers and observables. OOP Concepts of inheritance, polymorphism, abstraction, and encapsulation were emphasized in the program's design.

- Inheritance: Used throughout the program to organize classes and their functionality, e.g., the TrailerRoom class inherits from the more generic Room abstract class.
- Polymorphism: dynamic polymorphism is used in tandem with the use of abstract classes and state machines to allow for overriding of default behavior when necessary, e.g., the player's changeRoom() default behavior is potentially overridden  based on the player's state.
- Abstraction: Abstraction manifests heavily in the separation of functional groups, and the limiting of data they communicate with each other, e.g., the separation of the program into abstracted Model, View, and Controller components was ingrained into the design from an early stage.
- Encapsulation: Almost all data fields are private and only accessible to their respective classes. When appropriate, modifier methods are implemented with logical checks in place.

## Skills & Experience gained
- Improved proficiency of Java.
- Experience using OOP concepts and design-patterns.
- Experience with software Use-cases and UML diagrams.

## Contents
As this project is related to classwork, the raw Java code must be omitted.
- **instructions/** : Contains the assignment instructions that outline the learning goals and tasks completed. 
- **resources/** : XML and images required for Game.exe.
- **Game.exe** : An executable version of the finished game.
- **Game-Rules.pdf** : The gameplay rules of the original boardgame.