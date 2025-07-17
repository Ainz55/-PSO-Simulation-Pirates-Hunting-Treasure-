# Particle Swarm Optimization (PSO) Simulation: Pirates Hunting Treasure

This Python script simulates pirate ships searching for treasure using a Particle Swarm Optimization algorithm. The ships start in a circular formation and dynamically adjust their positions to converge toward the treasure.

## Key Features
- **PSO Implementation**: Simulates swarm intelligence where ships follow:
  - Global best position (closest ship to treasure)
  - Treasure position
  - Inertia from previous velocity
- **Visualization**:
  - Real-time position updates
  - Green lines show nearest-neighbor connections
  - Treasure marked with red `X`
- **Dynamic Parameters**:
  - Acceleration coefficients (`c1`, `c2`)
  - Inertia weight (`d`)
  - Position constraints ([-5, 5] boundary)

## Requirements
- Python 3.x
- Libraries:
  ```
  numpy, matplotlib
  ```
_____
## Visualization
<img width="641" height="556" alt="image" src="https://github.com/user-attachments/assets/270a0aa9-e074-477b-98d1-315e3dab84bd" />

<img width="648" height="554" alt="image" src="https://github.com/user-attachments/assets/12ed3adf-0e93-4c8a-bc78-5625d94fd9e6" />

