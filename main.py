# Proyek To-Do List
tasks = []

def show_tasks():
    """Fitur 1: Menampilkan seluruh data yang ada"""
    print("\n--- 📋 DAFTAR TUGAS ---")
    if not tasks:
        print("---  Daftar tugas masih kosong ---")
    else:
        for i, task in enumerate(tasks, 1):
            # Mengambil data dari dictionary
            status = task.get("status", "pending").upper()
            title = task.get("title", "Tanpa Judul")
            assignee = task.get("assignee", "Belum ada")
            print(f"{i}. [{status}] {title} - (PIC: {assignee})")
    print("-" * 25)

def add_task():
    """Fitur 2: Menambahkan task baru (Reezqee)"""
    print("\n--- ➕ TAMBAH TUGAS BARU ---")
    title = input("Masukkan judul tugas: ").strip()
    assignee = input("Masukkan nama assignee (PIC): ").strip()
    
    if title == "" or assignee == "":
        print("❌ Gagal: Judul dan Assignee tidak boleh kosong!")
    else:
        # Menambahkan data ke list tasks dalam bentuk dictionary
        new_task = {
            "title": title,
            "assignee": assignee,
            "status": "pending"  # Status default saat baru ditambah
        }
        tasks.append(new_task)
        print(f"✅ Tugas '{title}' berhasil ditambahkan untuk {assignee}.")
        print("-" * 25)

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
        if choice == "1":
            show_tasks()
        elif choice == "2":
            break

if __name__ == "__main__":
    main()