NUM_PARTITIONS = int(input("Ingrese la cantidad de particiones: "))
PARTITION_SIZES = []
for i in range(NUM_PARTITIONS):
    size = int(input(f"Ingrese el tamaño para la partición {i + 1}: "))
    PARTITION_SIZES.append(size)

PARTITION_SIZES.insert(0, 100)

TOTAL_MEMORY = sum(PARTITION_SIZES)

memory = [-1] * (NUM_PARTITIONS + 1)
process_names = [''] * (NUM_PARTITIONS + 1)

while True:
    print(f"Estado de la memoria: {TOTAL_MEMORY}")
    for i in range(NUM_PARTITIONS + 1):
        if memory[i] == -1:
            if i == 0:
                print(f"Partición del sistema: Reservada")
            else:
                print(f"Partición {PARTITION_SIZES[i - 1]}: Libre")
        else:
            if i == 0:
                print(f"Partición del sistema: Sistema Operativo ({memory[i]} MB)")
            else:
                print(f"Partición {PARTITION_SIZES[i - 1]}: Proceso '{process_names[i]}' ({memory[i]} MB)")

    print("\n1. Asignar proceso a partición")
    print("2. Liberar partición")
    print("3. Salir")
    choice = int(input())

    if choice == 1:
        processSize = int(input("Ingrese el tamaño del proceso: "))
        processName = input("Ingrese el nombre del proceso: ")

        if processSize <= TOTAL_MEMORY:
            allocated = False
            for i in range(NUM_PARTITIONS + 1):
                if memory[i] == -1 and PARTITION_SIZES[i - 1] >= processSize:
                    memory[i] = processSize
                    process_names[i] = processName
                    allocated = True
                    print(f"Proceso '{processName}' asignado a la partición {i}: {memory[i]} MB")
                    TOTAL_MEMORY -= processSize
                    break

            if not allocated:
                print("No se pudo asignar el proceso a ninguna partición.")
        else:
            print("El tamaño del proceso excede la memoria total.")
    elif choice == 2:
        partitionIndex = int(input("Ingrese el índice de la partición a liberar: "))

        if 0 <= partitionIndex <= NUM_PARTITIONS and memory[partitionIndex] != -1:
            process_names[partitionIndex] = ''
            TOTAL_MEMORY += memory[partitionIndex]
            memory[partitionIndex] = -1
            print("Partición liberada.")
        else:
            print("Índice de partición inválido o la partición ya está libre.")
    elif choice == 3:
        break
    else:
        print("Opción inválida.")

print("Saliendo del programa.")
