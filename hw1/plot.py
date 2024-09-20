import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# SIR model differential equations
def sir_model(y, t, beta, gamma, v, N):
    S, I, R = y
    dSdt = -beta * S * I / N  - v * S
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I + v * S
    return [dSdt, dIdt, dRdt]

# Set parameters
N = 1000  # Total population
I0, R0 = 10, 0  # Initial number of infected and recovered individuals
S0 = N - I0 - R0  # Initial number of susceptible individuals
beta = 0.3  # Contact rate
gamma = 0.1  # Recovery rate
vs = [0.05, 0.00, 0.10, 0.30]    # Vaccination rate
t = np.linspace(0, 160, 160)  # Time grid


for v in vs:
    # Initial conditions vector
    y = [S0, I0, R0]

    # Solve the differential equations
    solution = odeint(sir_model, y, t, args=(beta, gamma, v, N))
    S, I, R = solution.T



    # Plot the data
    plt.figure(figsize=(10,6))
    plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
    plt.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
    plt.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')

    plt.xlabel('Time (days)')
    plt.ylabel('Number of individuals')
    plt.title(f'SIR Modified Model, nu = {v}')
    plt.legend()
    plt.grid(True)

    # Save the plot
    plt.savefig(f'./img/sir_model_{v}.png')
    plt.close()


