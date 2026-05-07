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
    """Fitur 4: Menghapus task (Dariel)"""
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("\nMasukkan nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"✅ Tugas '{deleted_task['title']}' berhasil dihapus!")
        else:
            print("❌ Nomor tugas tidak ditemukan.")
    except ValueError:
        print("❌ Masukkan angka yang valid.")
    print("-" * 25)

def search_task():
    """Fitur 5: Mencari task berdasarkan assignee (Tugas Teman)"""
    pass

def main():
    while True:
        print("\n--- 📝 TO-DO LIST CLI ---")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Update Status")
        print("4. Delete Task")  # <--- Ini teks menu barunya
        print("6. Exit")
        
        choice = input("Pilih menu (1-6): ").strip()
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_status()
        elif choice == "4":      # <--- Pastikan ini juga ada
            delete_task()
        elif choice == "6":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("⚠️ Pilihan tidak valid.")

if __name__ == "__main__":
    main()