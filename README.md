# DFA Minimization Algorithm

## Project Overview
This project implements a Deterministic Finite Automaton (DFA) minimization algorithm based on Kozen's approach (1997, Lecture 14). The program identifies **equivalent states** in a DFA and outputs pairs of states that can be collapsed, effectively reducing the DFA to its minimal form.

The algorithm applies **state equivalence** theory, focusing on pairs of states that produce identical outputs for all possible strings. Such states can be grouped and merged to simplify the DFA without altering its language acceptance.

---

## Theoretical Background
### Deterministic Finite Automaton (DFA)
A DFA is defined as a 5-tuple:
*   **Q:** Finite set of states.
*   **Σ (Sigma):** Finite set of input symbols (alphabet).
*   **δ (Delta):** Transition function (δ: Q × Σ → Q). This means δ takes a state from Q and an input symbol from Σ and returns a new state in Q.
*   **s:** Initial state (s in Q).
*   **F:** Set of final (accepting) states (F is a subset of Q).
### Preliminaries

For this assignment, some definitions and notions are required. Let M = (Q, Σ, δ, s, F) be a deterministic finite automaton (DFA).

1.  **Inaccessible States:** A state *q* in *Q* is said to be inaccessible if there is no string *x* in Σ* (Sigma star, meaning zero or more symbols from Σ) such that δ-hat(*s*, *x*) = *q*.

    *   δ-hat represents the extended transition function, which describes the effect of a sequence of inputs.

2.  **Equivalent States:** A pair of states *p*, *q* in *Q* is said to be equivalent if and only if for all strings *x* in Σ*, δ-hat(*p*, *x*) is in *F*
    if and only if δ-hat(*q*, *x*) is in *F* as well.

    *   In simpler terms: If starting from state *p* and processing any string *x* leads to a final state (a state in *F*), then starting from state *q* and processing the *same* string *x* *must also* lead to a final state, and vice-versa.

4.  **Collapsible States:** Two states can be collapsed (merged) if they are equivalent.

### Algorithm Reference
The minimization algorithm implemented in this project is based on Dexter Kozen's **Automata and Computability** (1997). The algorithm iteratively partitions states into groups based on their transition behavior, refining these groups until no further splits are possible.

Reference:
Kozen, Dexter C. Automata and Computability. Springer, 1997. [DOI: 10.1007/978-1-4612-1844-9](https://doi.org/10.1007/978-1-4612-1844-9).

---

## Input/Output Specification
### Input Format
The program accepts multiple DFA cases as input. Each case includes:
1. Number of states \( n \).
2. Alphabet symbols separated by spaces.
3. List of final states.
4. Transition table with \( n \) rows, each specifying state transitions for each symbol in the alphabet.

NOTE: The Transition Table has *n* lines, one for each state. Each line contains a row of the table that represents *M*. Assume that the symbols of the alphabet appear in the table in the same order as they were given in step 2. If the automaton is represented by the following table:

| State | a | b |
|---|---|---|
| →0 | 1 | 2 |
| 1F | 3 | 4 |
| 2 | 4 | 5 |
| 3 | 5 | 5 |
| 4F | 5 | 5 |
| 5F | 5 | 5 |

 The n lines are
 0 1 2
 1 3 4
 2 4 3
 3 5 5
 4 5 5
 5 5 5

**Explanation of the table format:**

*   **State:** The current state. The arrow (→) indicates the initial state (0 in this case). The "F" indicates a final/accepting state (1, 4, and 5 in this case).
*   **a/b:** The input symbols of the alphabet.
*   The entries in the table indicate the next state reached upon reading the corresponding input symbol from the current state. For example, if the automaton is in state 0 and reads an "a", it transitions to state 1.

**Example Input:**
```
4
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
```

### Output Format
The output lists pairs of **equivalent states** in lexicographical order, separated by spaces.

**Example Output:**
```
(1,2) (3,4)
```

---

## Implementation Details
### Code Highlights
The program has two main components:
1. **find_equivalent_states** - Implements the minimization algorithm by partitioning states into groups and refining them based on transitions.
2. **read_automaton_from_file** - Parses DFA specifications from a file.

### Example Usage
```python
def read_automaton_from_file(file_path):
    # Open the file and read its lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Read the number of automata from the first line
    num_automata = int(lines[0].strip())
    automata = []

    index = 1
    for _ in range(num_automata):
        # Read the number of states for the current automaton
        num_states = int(lines[index].strip())

        # Read the alphabet for the current automaton
        alphabet = lines[index + 1].strip().split()

        # Read the final states for the current automaton
        final_states = list(map(int, lines[index + 2].strip().split()))

        # Read the transition table for the current automaton
        transitions = []
        for i in range(num_states):
            transitions.append(list(map(int, lines[index + 3 + i].strip().split())))

        # Append the current automaton to the list of automata
        automata.append([alphabet, final_states] + transitions)

        # Move the index to the next automaton
        index += (3 + num_states)

    return automata
```

---

## Installation and Usage
### 1. Clone the Repository
```
git clone https://github.com/username/repository-name
cd repository-name
```

### 2. Run the Program
```
python3 minimizer.py input.txt
```

---

## Sample Output
**Input:**
```
4
6
a b
1 2 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
```

**Output:**
```
(1,2) (3,4)
```

---

## Developers
- [Valentina Castro Pineda]
- [Martin Vanegas Ospina]
Thank you for contributing to this project!
