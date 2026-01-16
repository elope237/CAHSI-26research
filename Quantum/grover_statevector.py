import qiskit
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
import matplotlib
matplotlib.use("TkAgg")


target = "110"
n = len(target)
target = target[::-1]  # little-endian

def Oracle(circuit):
    for i in range(n):
        if target[i] == '0':
            circuit.x(i)

    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)

    for i in range(n):
        if target[i] == '0':
            circuit.x(i)

def Diffusion(circuit):
    circuit.h(range(n))
    circuit.x(range(n))

    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)

    circuit.x(range(n))
    circuit.h(range(n))

def plot_amplitudes(statevector, iteration):
    amplitudes = np.abs(statevector.data)

    labels = [format(i, f'0{n}b') for i in range(2**n)]

    plt.figure(figsize=(10, 4))
    plt.bar(labels, amplitudes)
    plt.xticks(rotation=90)
    plt.ylabel("|Amplitude|")
    plt.title(f"Grover amplitudes after iteration {iteration}")
    plt.tight_layout()
    plt.show()

def main():
    cir = qiskit.QuantumCircuit(n)
    cir.h(range(n))

    # Initial state
    state = Statevector.from_instruction(cir)
    plot_amplitudes(state, iteration=0)

    k = int(np.floor(np.pi / 4 * np.sqrt(2 ** n)))

    for i in range(1, k + 1):
        Oracle(cir)
        Diffusion(cir)

        state = Statevector.from_instruction(cir)
        plot_amplitudes(state, iteration=i)

if __name__ == "__main__":
    main()
