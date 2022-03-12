def machineEpsilon(func=float):
    machine_epsilon = func(1)
    while func(1)+machine_epsilon != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last
print(machineEpsilon())

print(abs(3.0*(4.0/3.0-1)-1))
print(int(abs(3.0*(4.0/3.0-1)-1)))