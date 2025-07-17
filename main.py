import numpy as np
import matplotlib.pyplot as plt
import random

pirate_x, pirate_y = 0, 0

num_ships = 20

angles = np.linspace(0, 2 * np.pi, num_ships, endpoint=False)
radii = 2
ships = np.array([[pirate_x + radii * np.cos(angle), pirate_y + radii * np.sin(angle)] for angle in angles])

velocities = np.zeros((num_ships, 2))

c1, c2 = 2, 2
d = 0.7
iterations = 200


def plot_positions(ships, pirate_x, pirate_y, iteration):
    plt.clf()
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)

    plt.scatter(pirate_x, pirate_y, color='red', label='Treasure', marker='x', s=100)

    plt.scatter(ships[:, 0], ships[:, 1], color='blue', label='Pirates')

    for ship in ships:
        closest_ship_idx = np.argmin(np.linalg.norm(ships - ship, axis=1))
        if closest_ship_idx != np.where(ships == ship)[0][0]:
            plt.plot([ship[0], ships[closest_ship_idx][0]], [ship[1], ships[closest_ship_idx][1]], 'g--', alpha=0.5)

    plt.legend()
    plt.title(f"Iteration {iteration}")
    plt.pause(0.1)


for iteration in range(iterations):
    distances = np.sqrt((ships[:, 0] - pirate_x) ** 2 + (ships[:, 1] - pirate_y) ** 2)

    best_ship_idx = np.argmin(distances)
    global_best_position = ships[best_ship_idx]

    for i in range(ships.shape[0]):
        r1, r2 = random.random(), random.random()

        velocities[i, 0] = (d * velocities[i, 0] +
                            c1 * r1 * (global_best_position[0] - ships[i, 0]) +
                            c2 * r2 * (pirate_x - ships[i, 0]))

        velocities[i, 1] = (d * velocities[i, 1] +
                            c1 * r1 * (global_best_position[1] - ships[i, 1]) +
                            c2 * r2 * (pirate_y - ships[i, 1]))

        ships[i, 0] += velocities[i, 0]
        ships[i, 1] += velocities[i, 1]

        ships[i, 0] = np.clip(ships[i, 0], -5, 5)
        ships[i, 1] = np.clip(ships[i, 1], -5, 5)

    plot_positions(ships, pirate_x, pirate_y, iteration)

plt.show()
