# main.py
from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Registrar tarea")
        print("2. Ver tareas")
        print("3. Actualizar estado")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        choice = input("Selecciona una opción: ")
        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.update_task()
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
