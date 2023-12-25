class State:
    def __init__(self, missionaries, devils, boat_side):
        self.missionaries = missionaries
        self.devils = devils
        self.boat_side = boat_side

    def __eq__(self, other):
        return (
            self.missionaries == other.missionaries and
            self.devils == other.devils and
            self.boat_side == other.boat_side
        )

    def __hash__(self):
        return hash((self.missionaries, self.devils, self.boat_side))

    def __str__(self):
        return f'M: {self.missionaries}, D: {self.devils}, B: {self.boat_side}'

def is_valid(state):
    # Check if the state is valid (no missionaries outnumbered by devils on either side)
    if (state.missionaries < state.devils and state.missionaries > 0) or \
       (3 - state.missionaries < 3 - state.devils and 3 - state.missionaries > 0):
        return False
    return True

def generate_successors(state):
    # Generate valid successor states based on the current state
    successors = []
    for m in range(3):
        for d in range(3):
            if 1 <= m + d <= 2:
                # Generate successor state based on the number of missionaries and devils in the boat
                new_state = State(
                    state.missionaries + (-1) ** state.boat_side * m,
                    state.devils + (-1) ** state.boat_side * d,
                    1 - state.boat_side
                )
                if is_valid(new_state):
                    successors.append(new_state)
    return successors

def depth_first_search(current_state, goal_state, visited):
    if current_state == goal_state:
        return [current_state]

    visited.add(current_state)
    for successor in generate_successors(current_state):
        if successor not in visited:
            path = depth_first_search(successor, goal_state, visited)
            if path:
                return [current_state] + path

    return None

def print_solution(path):
    for state in path:
        print(state)

if __name__ == "__main__":
    initial_state = State(3, 3, 0)
    goal_state = State(0, 0, 1)

    visited_states = set()
    solution_path = depth_first_search(initial_state, goal_state, visited_states)

    if solution_path:
        print_solution(solution_path)
    else:
        print("No solution found.")
