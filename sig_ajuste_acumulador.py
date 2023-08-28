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

last_allocated_partition = 0  # Mantener el seguimiento de la última partición asignada
accumulated_memory = 0  # Mantener el seguimiento del sobrante acumulado

def show_accumulated_partition():
    global accumulated_memory, NUM_PARTITIONS, TOTAL_MEMORY
    if accumulated_memory > 0:
        new_partition_size = accumulated_memory
        PARTITION_SIZES.append(new_partition_size)
        memory.append(-1)
        process_names.append('')
        accumulated_memory = 0
        NUM_PARTITIONS += 1
        print(f"Nueva partición con acumulados: {new_partition_size} MB")
        TOTAL_MEMORY += new_partition_size


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
    print("3. Mostrar nueva partición con acumulados")
    print("4. Salir")
    

    choice = int(input())

    if choice == 1:
        processSize = int(input("Ingrese el tamaño del proceso: "))
        processName = input("Ingrese el nombre del proceso: ")

        if processSize <= TOTAL_MEMORY:
            allocated = False

            # Buscar la siguiente partición disponible a partir de last_allocated_partition
            for _ in range(NUM_PARTITIONS):
                i = last_allocated_partition % NUM_PARTITIONS  # Regresar a la primera partición si estamos en la última
                if memory[i] == -1 and PARTITION_SIZES[i] >= processSize:
                    memory[i] = processSize
                    process_names[i] = processName
                    allocated = True
                    last_allocated_partition = (i + 1) % NUM_PARTITIONS  # Actualizar la última partición asignada
                    print(f"Proceso '{processName}' asignado a la partición {i}: {memory[i]} MB")

                    TOTAL_MEMORY -= processSize
                    accumulated_memory += PARTITION_SIZES[i] - processSize

                    break

                last_allocated_partition = (i + 1) % NUM_PARTITIONS  # Pasar a la siguiente partición
            if not allocated:
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
        show_accumulated_partition()
    elif choice == 4:
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
