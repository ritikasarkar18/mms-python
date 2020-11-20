# mms-python

For use with [mackorone/mms](https://github.com/mackorone/mms), a Micromouse simulator.<br>
Credits to [Pratik Garai](https://github.com/PratikGarai) for collaborating by implementing Maze Exploration using Floodfill for the graph.

## Approach Used

- Floodfill algorithm for maze traversal
- Create a graph simultaneously while traversing the maze
- Use the generated graph to find shortest path using BFS

## Advantages of the used approach

- Size of maze doesn't matter
- Works for finishing point located anywhere in the maze (not only the center)

## Notes

- Communication with the simulator is done via stdin/stdout, use stderr for logging
- Descriptions of all available API methods can be found at [mackorone/mms#mouse-api](https://github.com/mackorone/mms#mouse-api)

## Setup

1. Clone this repository
1. [Download the Micromouse simulator](https://github.com/mackorone/mms#download)
1. Run the simulator and click the "+" button to configure a new algorithm
1. Enter the config for your algorithm (name, directory, and run command)
1. Click the "Run" button
