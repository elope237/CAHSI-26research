import qiskit
from qiskit_aer.primitives import SamplerV2
import numpy as np

target = "110"   
n = len(target)
target = target[::-1]

def QFT(circuit, n):
    for i in range(n):
        circuit.h(i)
        for k in range(i + 1, n):
            N = np.pi / (2 ** (k - i))
            circuit.cp(N, k, i)
    for i in range(n // 2): #swap at end
        circuit.swap(i, n - i - 1)

def IQFT(circuit, n):
    for i in range(n // 2):
        circuit.swap(i, n - i - 1)
    for i in reversed(range(n)):
        for k in reversed(range(i + 1, n)):
            N = np.pi / (2 ** (k - i))
            circuit.cp(-N, k, i)
        circuit.h(i)

def main():
    qcQFT = qiskit.QuantumCircuit(n)

    for i in range(n):
        if target[i] == "1":
            qcQFT.x(i)

    QFT(qcQFT, n)
    qcQFT.measure_all()
    sampler = SamplerV2()
    result = sampler.run([qcQFT], shots=256).result()
    counts = result[0].data.meas.get_counts()
    print(qcQFT.draw())
    print("Counts QFT:", counts)
    print("\n ---BREAK LINE--- \n")


    qcIQFT = qiskit.QuantumCircuit(n)

    for i in range(n):
        if target[i] == "1":
            qcIQFT.x(i)

    QFT(qcIQFT, n)
    IQFT(qcIQFT, n)
    qcIQFT.measure_all()
    sampler = SamplerV2()
    result = sampler.run([qcIQFT], shots=256).result()
    counts = result[0].data.meas.get_counts()
    print(qcIQFT.draw())
    print("Counts IQFT:", counts)


if __name__ == "__main__":
    main()
