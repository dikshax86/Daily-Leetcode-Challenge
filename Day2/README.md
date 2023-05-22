# Division Evaluation

The "Evaluate Division" problem involves evaluating division equations and answering queries based on the provided equations and values.

## Problem Description

Given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`, the task is to answer queries of the form `Cj / Dj = ?`, where `queries[j] = [Cj, Dj]`. The goal is to determine the answers to all the queries and return them. If a single answer cannot be determined, `-1.0` is returned.

### Assumptions

- The input is always valid.
- Division by zero is not allowed.
- There are no contradictions in the provided equations.

## Solution Approach

1. Build the graph: Create a directed weighted graph using the given equations and values. Each variable represents a node in the graph, and the weights of the edges represent the division values.

2. Depth-First Search (DFS): Implement a DFS algorithm to traverse the graph and calculate the division results. Start from the dividend and recursively explore the neighboring nodes until reaching the divisor. Keep track of visited nodes to avoid infinite loops.

3. Evaluate queries: For each query, perform the DFS to find a valid path between the dividend and divisor. Multiply the weights along the path to calculate the division result. If a valid path is found, return the division result; otherwise, return `-1.0`.

## Usage

To use the solution for the "Evaluate Division" problem, follow these steps:

1. Provide the equations and their corresponding values as input.
2. Create an instance of the `Solution` class.
3. Call the `calcEquation` method, passing the equations, values, and queries as arguments.
4. The method will return the results of the queries.

## Example

```python
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

result = Solution().calcEquation(equations, values, queries)
print(result)
