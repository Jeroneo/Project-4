# React Go Game (Project 4)

This is a web-based implementation of the classic board game **Go**, built using React, TypeScript, and Vite.

## Features

* **Interactive Go Board**: Developed with React components (`GoBoard.tsx`).
* **Game Rules & Logic**: Core game mechanics handled purely in TypeScript (`GoEngine.ts`).
* **Modern Stack**: Blazing fast development server and build process using Vite + React + TypeScript.

## Getting Started

### Prerequisites

Make sure you have [Node.js](https://nodejs.org/) installed on your machine.

### Installation

1. Navigate to the project directory.
2. Install the dependencies:

```bash
npm install
```

### Running the App

Start the development server:

```bash
npm run dev
```

Open your browser and visit the local URL provided by Vite (usually `http://localhost:5173`) to play the game!

## Project Structure

* `src/components/GoBoard.tsx`: The UI component for the game board.
* `src/logic/GoEngine.ts`: The underlying logic handling captures, legal moves, scoring, and game state.

