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
"""
