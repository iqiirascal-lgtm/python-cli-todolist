# Proyek To-Do List
tasks = []

def show_tasks():
    """Fitur 1: Menampilkan seluruh data yang ada"""
    pass

def add_task():
    """Fitur 2: Menambahkan task baru (Reezqee)"""
    pass

def update_status():
    """Fitur 3: Mengubah status task (Reezqee)"""
    pass

def delete_task():
    """Fitur 4: Menghapus task (Tugas Teman)"""
    pass

def search_task():
    """Fitur 5: Mencari task berdasarkan assignee (Tugas Teman)"""
    pass

def main():
    while True:
        print("\n--- 📝 TO-DO LIST CLI ---")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Update Status")
        print("6. Exit")
        
        choice = input("Pilih menu (1-6): ").strip()
        if choice == "6": 
            print("Sampai jumpa!")
            break

if __name__ == "__main__":
    main()