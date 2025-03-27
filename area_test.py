# Store known A/A* values
area_to_astar = {
    # Example: "A1": 2.0
}

# Store connections: dict of section -> list of (neighbor, ratio)
connections = {}

# Add a ratio like: A_to / A_from = ratio
def add_ratio(section_to, section_from, ratio):
    if section_from not in connections:
        connections[section_from] = []
    if section_to not in connections:
        connections[section_to] = []

    # Add forward and backward ratios
    connections[section_from].append((section_to, ratio))         # A_to = ratio * A_from
    connections[section_to].append((section_from, 1.0 / ratio))   # A_from = (1/ratio) * A_to

# Propagate A/A* values from known values
def propagate_area_ratios(area_to_astar, connections):
    queue = list(area_to_astar.keys())  # Start with known sections
    i = 0
    while i < len(queue):
        current = queue[i]
        current_val = area_to_astar[current]
        neighbors = connections.get(current, [])

        for neighbor, ratio in neighbors:
            if neighbor not in area_to_astar:
                area_to_astar[neighbor] = current_val * ratio
                queue.append(neighbor)
        i += 1

# Print results
def print_results(area_to_astar):
    print("\n--- Computed A/A* Values ---")
    for section in sorted(area_to_astar):
        print(f"{section} / A* = {area_to_astar[section]:.4f}")

# ---------------------
# 🧪 Example Usage
# ---------------------

# Known: A1 / A* = 2.0
area_to_astar["A1"] = 2.0

# Known: A3 / A1 = 1.5
add_ratio("A3", "A1", 1.5)

# Known: A5 / A3 = 2.1
add_ratio("A5", "A3", 2.1)

# Known: A6 / A5 = 1.2
add_ratio("A6", "A5", 1.2)

# Known: A9 / A6 = 0.5
add_ratio("A9", "A6", 0.5)

# Run propagation
propagate_area_ratios(area_to_astar, connections)

# Show result
print_results(area_to_astar)

"""
--- Computed A/A* Values ---
A1 / A* = 2.0000
A3 / A* = 3.0000
A5 / A* = 6.3000
A6 / A* = 7.5600
A9 / A* = 3.7800




# Dictionary to store known A/A* values
Initialize area_to_astar as an empty dictionary

# Dictionary to store connections between sections
Initialize connections as an empty dictionary

# Function to add a known area ratio between two sections
Function add_ratio(section_to, section_from, ratio):
    If section_from is not in connections:
        Add section_from to connections with an empty list
    If section_to is not in connections:
        Add section_to to connections with an empty list

    # Add the forward ratio: A_to = ratio * A_from
    Append (section_to, ratio) to connections[section_from]

    # Add the backward ratio: A_from = (1/ratio) * A_to
    Append (section_from, 1/ratio) to connections[section_to]

# Function to compute all unknown A/A* values using known ones
Function propagate_area_ratios(area_to_astar, connections):
    Initialize queue as list of keys in area_to_astar
    Set index i = 0

    While i < length of queue:
        Set current = queue[i]
        Set current_val = area_to_astar[current]
        Set neighbors = connections[current] (if any)

        For each (neighbor, ratio) in neighbors:
            If neighbor is not in area_to_astar:
                Set area_to_astar[neighbor] = current_val * ratio
                Append neighbor to queue

        Increment i

# Function to print out all A/A* values
Function print_results(area_to_astar):
    Print "--- Computed A/A* Values ---"
    For each section in sorted keys of area_to_astar:
        Print section + " / A* = " + area_to_astar[section] formatted to 4 decimal places

# ---------------------
# Example usage
# ---------------------

# Add known A/A* value
Set area_to_astar["A1"] = 2.0

# Add known ratios between sections
Call add_ratio("A3", "A1", 1.5)
Call add_ratio("A5", "A3", 2.1)
Call add_ratio("A6", "A5", 1.2)
Call add_ratio("A9", "A6", 0.5)

# Compute all area ratios using propagation
Call propagate_area_ratios(area_to_astar, connections)

# Display the results
Call print_results(area_to_astar)








"""
