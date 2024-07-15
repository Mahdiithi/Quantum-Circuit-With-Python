import cirq

# We define the number of qubits
# we start from 2 qubits
Number_of_Qubits = 2

# Create a Quantum Circuit
quantum_circuit = cirq.Circuit()

# Create qubits
qubits = [cirq.GridQubit(i, 0) for i in range(Number_of_Qubits)]

# Add Hadamard gate to qubit 0 to create a superposition.
quantum_circuit.append(cirq.H(qubits[0]))

# Add CNOT gate with qubit 0 as control and qubit 1 as target to create an entanglement
quantum_circuit.append(cirq.CNOT(qubits[0], qubits[1]))

# Print the circuit
print("Quantum Circuit:")
print(quantum_circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.simulate(quantum_circuit)

# Print the final state vector
print("\nFinal State Vector:")
print(result.final_state_vector)
