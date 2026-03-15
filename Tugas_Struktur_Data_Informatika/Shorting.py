def bubble_sort(arr, ascending=True):
    """
    Bubble Sort - Algoritma sederhana dengan kompleksitas O(n²)
    """
    n = len(arr)
    data = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    
    return data


def selection_sort(arr, ascending=True):
    """
    Selection Sort
    """
    n = len(arr)
    data = arr.copy()
    
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if ascending:
                if data[j] < data[target_idx]:
                    target_idx = j
            else:
                if data[j] > data[target_idx]:
                    target_idx = j
        data[i], data[target_idx] = data[target_idx], data[i]
    
    return data


def insertion_sort(arr, ascending=True):
    """
    Insertion Sort
    """
    data = arr.copy()
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        if ascending:
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
        else:
            while j >= 0 and data[j] < key:
                data[j + 1] = data[j]
                j -= 1
        
        data[j + 1] = key
    
    return data


def quick_sort(arr, ascending=True):
    """
    Quick Sort
    """
    if len(arr) <= 1:
        return arr
    
    data = arr.copy()
    pivot = data[len(data) // 2]
    
    if ascending:
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
    else:
        left = [x for x in data if x > pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x < pivot]
    
    return quick_sort(left, ascending) + middle + quick_sort(right, ascending)


def merge_sort(arr, ascending=True):
    """
    Merge Sort
    """
    if len(arr) <= 1:
        return arr
    
    data = arr.copy()
    mid = len(data) // 2
    left = merge_sort(data[:mid], ascending)
    right = merge_sort(data[mid:], ascending)
    
    return merge(left, right, ascending)


def merge(left, right, ascending):
    """Helper untuk merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if ascending:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_array(arr, ascending=True, method='built-in'):
    """
    Fungsi sorting utama
    """
    if not arr:
        return []
    
    if not isinstance(arr, list):
        raise TypeError("Input harus berupa list/array")
    
    if method == 'built-in':
        return sorted(arr, reverse=not ascending)
    elif method == 'bubble':
        return bubble_sort(arr, ascending)
    elif method == 'selection':
        return selection_sort(arr, ascending)
    elif method == 'insertion':
        return insertion_sort(arr, ascending)
    elif method == 'quick':
        return quick_sort(arr, ascending)
    elif method == 'merge':
        return merge_sort(arr, ascending)
    else:
        raise ValueError(f"Metode '{method}' tidak tersedia")


def input_angka():
    """
    Fungsi untuk input angka dari user
    """
    print("\n" + "="*50)
    print("INPUT DATA ARRAY")
    print("="*50)
    
    # Input jumlah elemen
    while True:
        try:
            n = int(input("Masukkan jumlah angka yang ingin diurutkan: "))
            if n <= 0:
                print("Jumlah elemen harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka bulat.")
    
    # Input setiap angka
    data = []
    print(f"\nMasukkan {n} angka:")
    for i in range(n):
        while True:
            try:
                angka = float(input(f"  Angka ke-{i+1}: "))
                data.append(angka)
                break
            except ValueError:
                print("  Input tidak valid! Masukkan angka.")
    
    return data


def pilih_metode():
    """
    Fungsi untuk memilih metode sorting
    """
    print("\n" + "="*50)
    print("PILIH METODE SORTING")
    print("="*50)
    print("1. Built-in (Timsort) - Paling cepat")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("5. Quick Sort")
    print("6. Merge Sort")
    
    while True:
        pilihan = input("\nPilih metode (1-6): ")
        metode_dict = {
            '1': 'built-in',
            '2': 'bubble',
            '3': 'selection',
            '4': 'insertion',
            '5': 'quick',
            '6': 'merge'
        }
        if pilihan in metode_dict:
            return metode_dict[pilihan]
        else:
            print("Pilihan tidak valid! Masukkan 1-6.")


def pilih_urutan():
    """
    Fungsi untuk memilih ascending atau descending
    """
    print("\n" + "="*50)
    print("PILIH JENIS PENGURUTAN")
    print("="*50)
    print("1. Ascending (Kecil ke Besar)")
    print("2. Descending (Besar ke Kecil)")
    
    while True:
        pilihan = input("\nPilih (1-2): ")
        if pilihan == '1':
            return True
        elif pilihan == '2':
            return False
        else:
            print("Pilihan tidak valid! Masukkan 1 atau 2.")


def main():
    """
    Program utama
    """
    print("="*50)
    print("PROGRAM SORTING ARRAY")
    print("="*50)
    
    while True:
        # 1. Input data
        data = input_angka()
        
        # 2. Pilih metode
        metode = pilih_metode()
        
        # 3. Pilih urutan
        ascending = pilih_urutan()
        
        # 4. Proses sorting
        try:
            hasil = sort_array(data, ascending=ascending, method=metode)
            
            # 5. Tampilkan hasil
            print("\n" + "="*50)
            print("HASIL SORTING")
            print("="*50)
            print(f"Data asli:      {data}")
            print(f"Metode:         {metode.upper()}")
            print(f"Urutan:         {'Ascending' if ascending else 'Descending'}")
            print(f"Data terurut:   {hasil}")
            print("="*50)
            
        except Exception as e:
            print(f"\nError: {e}")
        
        # Tanya apakah ingin mengulang
        ulang = input("\nApakah ingin mengulang? (y/n): ").lower()
        if ulang != 'y':
            print("\nTerima kasih telah menggunakan program ini!")
            break


# Jalankan program
if __name__ == "__main__":
    main()