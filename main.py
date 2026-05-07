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
    """Fitur 5: Mencari task berdasarkan assignee (Dariel)"""
    if not tasks:
        print("\n--- 🔍 PENCARIAN TUGAS ---")
        print("---  Daftar tugas masih kosong ---")
        return

    keyword = input("\nMasukkan nama assignee yang dicari: ").strip().lower()
    found = False

    print(f"\n--- 🔍 HASIL PENCARIAN UNTUK '{keyword.upper()}' ---")
    for i, task in enumerate(tasks, 1):
        assignee = task.get("assignee", "Belum ada")
        # Menggunakan .lower() agar pencarian tidak sensitif huruf besar/kecil
        if keyword in assignee.lower():
            status = task.get("status", "pending").upper()
            title = task.get("title", "Tanpa Judul")
            print(f"{i}. [{status}] {title} - (PIC: {assignee})")
            found = True
            
    if not found:
        print(f"❌ Tidak ada tugas yang ditemukan untuk assignee '{keyword}'.")
    print("-" * 25)

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
            break
        else:
            print("⚠️ Pilihan tidak valid.")

if __name__ == "__main__":
    main()