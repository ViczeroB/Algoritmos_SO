NUM_PARTITIONS = int(input("Ingrese la cantidad de particiones: "))
PARTITION_SIZES = []
for i in range(NUM_PARTITIONS):
    size = int(input(f"Ingrese el tamaño para la partición {i + 1}: "))
    PARTITION_SIZES.append(size)

# Tamaño de la partición del sistema operativo
SYSTEM_PARTITION_SIZE = int(input("Ingrese el tamaño para la partición del sistema operativo:"))

TOTAL_MEMORY = sum(PARTITION_SIZES) + SYSTEM_PARTITION_SIZE

memory = [-1] * (NUM_PARTITIONS + 1)
process_names = [''] * (NUM_PARTITIONS + 1)

def find_best_fit_partition(process_size):
    best_fit_index = -1
    smallest_free_space = float('inf')

    for i in range(NUM_PARTITIONS):
        if memory[i] == -1 and PARTITION_SIZES[i] >= process_size:
            free_space = PARTITION_SIZES[i] - process_size
            if free_space < smallest_free_space:
                best_fit_index = i
                smallest_free_space = free_space

    return best_fit_index

while True:
    print(f"Estado de la memoria: {TOTAL_MEMORY}")
    # Mostrar partición del sistema operativo
    print(f"Partición del sistema: Sistema Operativo ({SYSTEM_PARTITION_SIZE} MB)")

    for i in range(NUM_PARTITIONS):
        if memory[i] == -1:
            print(f"Partición {PARTITION_SIZES[i]}: Libre")
        else:
            print(f"Partición {PARTITION_SIZES[i]}: Proceso '{process_names[i]}' ({memory[i]} MB)")

    print("\n1. Asignar proceso a partición (Siguiente ajuste)")
    print("2. Liberar partición")
    print("3. Salir")
    

    choice = int(input())

    if choice == 1:
        processSize = int(input("Ingrese el tamaño del proceso: "))
        processName = input("Ingrese el nombre del proceso: ")

        if processSize <= TOTAL_MEMORY:
            best_fit_index = find_best_fit_partition(processSize)

            if best_fit_index != -1:
                memory[best_fit_index] = processSize
                process_names[best_fit_index] = processName
                print(f"Proceso '{processName}' asignado a la partición {best_fit_index}: {memory[best_fit_index]} MB")
                TOTAL_MEMORY -= processSize
            else:
                print("No se pudo asignar el proceso a ninguna partición.")
        else:
            print("El tamaño del proceso excede la memoria total.")

    elif choice == 2:
        partitionIndex = int(input("Ingrese el índice de la partición a liberar: "))

        if 0 <= partitionIndex < NUM_PARTITIONS and memory[partitionIndex] != -1:
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
    
    # Crear una nueva partición con el sobrante acumulado si todas las particiones están ocupadas
    if all(memory[i] != -1 for i in range(NUM_PARTITIONS)):
        new_partition_size = accumulated_memory
        if new_partition_size > 0:
            PARTITION_SIZES.append(new_partition_size)
            memory.append(-1)
            process_names.append('')
            accumulated_memory = 0
            NUM_PARTITIONS += 1
            print(f"Se creó una nueva partición de tamaño {new_partition_size} MB.")
            TOTAL_MEMORY += new_partition_size

print("Saliendo del programa.")
