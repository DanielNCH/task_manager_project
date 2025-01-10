# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Nombre de la tarea: ")
        description = input("Descripción: ")
        due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
        priority = input("Prioridad (alta, media, baja): ")
        
        task = {
            "name": name,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": "Pendiente"
        }
        self.tasks.append(task)
        print("Tarea añadida con éxito.")

    def view_tasks(self):
        if not self.tasks:
            print("No hay tareas registradas.")
            return
        
        print("\n--- Lista de Tareas ---")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"[{idx}] {task['name']} - {task['status']}\n    Descripción: {task['description']}\n    Fecha de Vencimiento: {task['due_date']}\n    Prioridad: {task['priority']}\n")

    def update_task(self):
        self.view_tasks()
        try:
            index = int(input("Selecciona el índice de la tarea a actualizar: ")) - 1
            if 0 <= index < len(self.tasks):
                new_status = input("Nuevo estado (Pendiente, En progreso, Completada): ")
                self.tasks[index]["status"] = new_status
                print("Estado actualizado con éxito.")
            else:
                print("Índice no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Selecciona el índice de la tarea a eliminar: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                print("Tarea eliminada con éxito.")
            else:
                print("Índice no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")