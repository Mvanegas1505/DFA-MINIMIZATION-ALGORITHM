def find_equivalent_states(automaton):
    # Extract the alphabet from the automaton input
    alphabet = automaton[0]  # e.g., ['a', 'b']

    # Extract the final states and convert them to a set for faster lookup
    final_states = set(automaton[1])  # e.g., {1, 2, 5}

    # Extract the transition table from the automaton input
    transitions = automaton[2:]  # e.g., [[0, 1, 2], [1, 3, 4], [2, 4, 3], [3, 5, 5], [4, 5, 5], [5, 5, 5]]

    # Determine the number of states in the automaton
    num_states = len(transitions)

    # Step 1: Initialize groups
    # Create two groups: one with final states and another with non-final states
    groups = [final_states, set(range(num_states)) - final_states]

    while True:
        new_groups = []
        # Step 2: Refine groups
        for group in groups:
            # Try to split the group based on the transition function
            partition = {}
            for state in group:
                # Compute the transition signature for the state
                signature = tuple(
                    tuple(find_group(transitions[state][symbol_idx + 1], groups)) 
                    for symbol_idx in range(len(alphabet))
                )
                # Group states by their transition signatures
                if signature in partition:
                    partition[signature].append(state)
                else:
                    partition[signature] = [state]

            # Add all resulting partitions to new groups
            new_groups.extend(partition.values())

        # If no refinement was possible, stop the loop
        if new_groups == groups:
            break
        groups = new_groups

    # Step 3: Filter out non-equivalent states
    # Only keep groups with more than one state
    equivalent_states = [group for group in groups if len(group) > 1]

    # Step 4: Print pairs of equivalent states in lexicographical order
    pairs = []
    for group in equivalent_states:
        sorted_group = sorted(group)  # Sort the group to ensure lexicographical order
        for i in range(len(sorted_group)):
            for j in range(i + 1, len(sorted_group)):
                pairs.append((sorted_group[i], sorted_group[j]))

    # Sort pairs lexicographically
    pairs.sort()
    # Print the pairs in the required format
    print(" ".join(f"({a},{b})" for a, b in pairs))

def find_group(state, groups):
    # Helper function to find which group a state belongs to
    for group in groups:
        if state in group:
            return group
    return None

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

# Read automata from 'input.txt'
automata = read_automaton_from_file('input.txt')

# Process each automaton and print equivalent states
for automaton in automata:
    find_equivalent_states(automaton)

