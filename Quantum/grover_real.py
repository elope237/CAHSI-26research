import qiskit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit_ibm_runtime import SamplerV2
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="gX06pQc4pj7AZk7DHIWM_Ye3pzXUvqr9z7SEST5W-FMm",
    overwrite=True 
)

service = QiskitRuntimeService()

backend = service.least_busy(
    operational=True,
    simulator=False,
    min_num_qubits=3
)
print("Running on:", backend.name)


target = "11001"
target = target[::-1]
n = len(target)

qc = QuantumCircuit(n)
qc.h(range(n))

def Oracle(circuit):
    for i in range(n):
        if target[i] == "0":
            circuit.x(i)
    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)
    for i in range(n):
        if target[i] == "0":
            circuit.x(i)

def Diffusion(circuit):
    for i in range(n):
        circuit.h(i)
    for i in range(n):
        circuit.x(i)
    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)
    for i in range(n):
        circuit.x(i)
    for i in range(n):
        circuit.h(i)

k = int(np.floor(np.pi / 4 * np.sqrt(2 ** n)))
for _ in range(k):
    Oracle(qc)
    Diffusion(qc)

qc.measure_all()


qc_transpiled = transpile(qc, backend=backend, optimization_level=3)

sampler = SamplerV2(mode=backend)

# Submit the job and get results
job = sampler.run([qc_transpiled], shots=1024)
print(f"Job ID: {job.job_id}")
result = job.result()
counts = result[0].data.meas.get_counts()
print(f"Measurement counts: ", counts)


plot_histogram(counts)
plt.show()