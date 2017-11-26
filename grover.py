"""
Implementation of Grover algorithm in python for simulation purposes.

Copyright: Evgeni Makarov
evgeni.makarov@gmail.com
github.com/emakarov
"""
import numpy as np
import matplotlib.pyplot as plt


def grover_sim(nqubits=3, desired_mode=0):
    """Simple simulation of Grover algorithm."""
    #: number of elements in database
    n = 2**nqubits

    # Defining quantum gates
    #: Diffusion transform
    diffuse = -np.eye(n) + 2/n

    #: Oracle
    oracle = np.eye(n)
    oracle[desired_mode][desired_mode] = -1

    # Calculate the optimal number of iterations
    finish = np.round(np.pi/4*np.sqrt(n))

    # Initialization of Psi function.
    psistart = np.ones([n, 1])/np.sqrt(n)

    # Lets move psi function to some random angle.
    psi = psistart*np.exp(1j*np.random.rand())

    probability = []

    for step in range(int(finish)):
        # Applying operators oracle and diffuse
        psi = oracle.dot(psi)
        psi = diffuse.dot(psi)

        # Logging every iteration step to console
        prob = psi[desired_mode]*np.conj(psi[desired_mode])
        probability.append(prob)
        psiconj = psi*np.conj(psi)
        mods = [x[0] for x in np.abs(psiconj)]
        print('Distribution at step {}'.format(step))
        for k, v in enumerate(mods):
            print('mode {}:'.format(k), v)

    return probability, psi


def stem_psi(psi):
    """Plotting the final distribution."""
    markerline, stemlines, baseline = plt.stem(psi*np.conj(psi))
    plt.setp(baseline, 'color', 'r', 'linewidth', 2)
    plt.show()


if __name__ == "__main__":
    probability, psi = grover_sim(nqubits=6, desired_mode=5)
    stem_psi(psi)
