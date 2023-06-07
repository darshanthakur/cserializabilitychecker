# Precedence Graph for Conflict Serializability

This Python program builds a precedence graph for a given schedule and determines whether it is "Conflict Serializable" or not. The program utilizes the `networkx` and `matplotlib.pyplot` libraries to visualize the graph.

## Input Format

The program expects the operations of the schedule to be entered, separated by commas or spaces. Each operation should follow the format:

```
<operation_type><transaction_id><variable>
```

- `<operation_type>`: Specifies the type of operation (r for read or w for write).
- `<transaction_id>`: Represents the ID of the transaction (1-9).
- `<variable>`: Specifies the variable on which the operation is performed.

## Sample Input

```
r1x w2x w3x r1x w1x r4x r4y
```

## Output

The program generates a precedence graph plot and determines whether the given schedule is conflict serializable or not. If a cycle exists in the precedence graph, it is highlighted in red.

- If no cycle is found: The output indicates that the given schedule is conflict serializable.
- If a cycle is found: The output indicates that the given schedule is not conflict serializable, and the cycle in the precedence graph is highlighted in red.

## Usage

1. Clone the repository: `git clone https://github.com/your-username/precedence-graph.git`
2. Navigate to the project directory: `cd precedence-graph`
3. Ensure that the `networkx` and `matplotlib` libraries are installed.
4. Run the program: `python main.py`
5. Enter the operations of the schedule as prompted.
6. The program will display the precedence graph plot and the conflict serializability result.

## Requirements

The program requires the following libraries:

- `networkx`
- `matplotlib.pyplot`

You can install the required libraries using `pip`:

```
pip install networkx matplotlib
```
