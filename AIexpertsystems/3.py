def water_jug_problem():
    jug4 = 4
    jug3 = 3

    # Initial states for both jugs
    jug_state = [0, 0]

    # Function to print the current state of jugs
    def print_state():
        print(f"4-gallon jug: {jug_state[0]} gallons, 3-gallon jug: {jug_state[1]} gallons")

    # Function to pour water from one jug to another
    def pour_water(from_jug, to_jug):
        if jug_state[from_jug] == 0:
            return jug_state
        while jug_state[to_jug] < jug3 and jug_state[from_jug] > 0:
            jug_state[to_jug] += 1
            jug_state[from_jug] -= 1
        return jug_state

    # Function to empty a jug
    def empty_jug(jug):
        jug_state[jug] = 0
        return jug_state

    # Function to fill a jug to its capacity
    def fill_jug(jug):
        jug_state[jug] = jug4 if jug == 0 else jug3
        return jug_state

    # Implementing the solution steps
    print("Steps to get exactly 2 gallons in the 4-gallon jug:")
    print_state()

    jug_state = fill_jug(0)  # Fill the 4-gallon jug
    print_state()

    jug_state = pour_water(0, 1)  # Pour water from 4-gallon to 3-gallon
    print_state()

    jug_state = empty_jug(1)  # Empty the 3-gallon jug
    print_state()

    jug_state = pour_water(0, 1)  # Pour water from 4-gallon to 3-gallon
    print_state()

    jug_state = fill_jug(0)  # Fill the 4-gallon jug again
    print_state()

    jug_state = pour_water(0, 1)  # Pour water from 4-gallon to 3-gallon until it fills it
    print_state()

# Solve the Water Jug problem
water_jug_problem()
