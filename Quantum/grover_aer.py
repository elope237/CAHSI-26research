import qiskit
from qiskit_aer.primitives import SamplerV2
import numpy as np

target = "1010"
n = len(target)
target = target[::-1]

def Oracle(circuit):
    for i in range (n):
        if target[i] == '0':
            circuit.x(i)
    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)
    for i in range (n):
        if target[i] == '0':
            circuit.x(i)

def Diffusion(circuit):
    for i in range (n):
        circuit.h(i)
    for i in range (n):
        circuit.x(i)
    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)
    for i in range (n):
        circuit.x(i)
    for i in range (n):
        circuit.h(i)
    

def main():
    cir = qiskit.QuantumCircuit(n)
    cir.h(range(n))
    k = int(np.floor(np.pi / 4 * np.sqrt(2 ** n)))
    for _ in range(k):
        Oracle(cir)
        Diffusion(cir)
    cir.measure_all()

    # Construct an ideal simulator with SamplerV2
    sampler = SamplerV2()
    job = sampler.run([cir], shots=128)

    # Perform an ideal simulation
    result_ideal = job.result()
    counts_ideal = result_ideal[0].data.meas.get_counts()
    print('Counts(ideal):', counts_ideal)

if __name__ == "__main__":
    main()
