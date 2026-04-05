import math
import random

# Objective function
def objective(x):
    return x**2

def simulated_annealing(objective, initial_x, T=1000, cooling_rate=0.99, max_iter=1000):
    current_x = initial_x
    current_cost = objective(current_x)
    best_x, best_cost = current_x, current_cost

    for i in range(max_iter):
        # Generate neighbor (small random step)
        new_x = current_x + random.uniform(-1, 1)
        new_cost = objective(new_x)

        # Difference in cost
        delta = new_cost - current_cost

        # Acceptance condition
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_x, current_cost = new_x, new_cost

            # Update best solution
            if new_cost < best_cost:
                best_x, best_cost = new_x, new_cost

        # Cool down
        T *= cooling_rate

        # Optional: print progress
        # print(f"Iter {i}, x={current_x:.4f}, cost={current_cost:.4f}, T={T:.4f}")

    return best_x, best_cost

# Run simulated annealing
best_x, best_cost = simulated_annealing(objective, initial_x=random.uniform(-10, 10))
print("Best solution found:")
print("x =", best_x)
print("f(x) =", best_cost)
