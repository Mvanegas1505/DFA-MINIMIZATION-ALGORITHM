# DFA Minimization Algorithm

## Project Overview
This project implements a Deterministic Finite Automaton (DFA) minimization algorithm based on Kozen's approach (1997, Lecture 14). The program identifies **equivalent states** in a DFA and outputs pairs of states that can be collapsed, effectively reducing the DFA to its minimal form.

The algorithm applies **state equivalence** theory, focusing on pairs of states that produce identical outputs for all possible strings. Such states can be grouped and merged to simplify the DFA without altering its language acceptance.

---

## Theoretical Background
### Deterministic Finite Automaton (DFA)
A DFA is defined as a 5-tuple:
- **Q**: Finite set of states
- **Σ**: Finite set of input symbols (alphabet)
- **δ**: Transition function \( \delta : Q \times \Sigma \rightarrow Q \)
- **s**: Initial state \( s \in Q \)
- **F**: Set of final (accepting) states \( F \subseteq Q \)

### Preliminaries
1. **Inaccessible States**: A state \( q \in Q \) is said to be inaccessible if there is no string \( x \in \Sigma^* \) such that \( \hat{\delta}(s, x) = q \).
2. **Equivalent States**: A pair of states \( p, q \in Q \) is said to be equivalent if and only if:
\[
(\forall x \in \Sigma^*)(\hat{\delta}(p, x) \in F \iff \hat{\delta}(q, x) \in F)
\]
That is, any string \( x \) that allows access to a final state from \( p \) must also allow access to a final state from \( q \), and vice versa.
3. **Collapsible States**: Two states can be collapsed if they are equivalent.

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
def find_equivalent_states(automaton):
    alphabet = automaton[0] 
    final_states = set(automaton[1]) 
    transitions = automaton[2:] 
    num_states = len(transitions)
    groups = [final_states, set(range(num_states)) - final_states]

    while True:
        new_groups = []
        for group in groups:
            partition = {}
            for state in group:
                signature = tuple(
                    tuple(find_group(transitions[state][symbol_idx + 1], groups)) 
                    for symbol_idx in range(len(alphabet))
                )
                if signature in partition:
                    partition[signature].append(state)
                else:
                    partition[signature] = [state]
            new_groups.extend(partition.values())
        if new_groups == groups:
            break
        groups = new_groups

    equivalent_states = [group for group in groups if len(group) > 1]
    pairs = []
    for group in equivalent_states:
        sorted_group = sorted(group)
        for i in range(len(sorted_group)):
            for j in range(i + 1, len(sorted_group)):
                pairs.append((sorted_group[i], sorted_group[j]))
    pairs.sort()
    print(" ".join(f"({a},{b})" for a, b in pairs))

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

## Contributors
- [Contributor 1]
- [Contributor 2]
- [Contributor 3]
- [Contributor 4]
- [Contributor 5]

---
Thank you for contributing to this project!
