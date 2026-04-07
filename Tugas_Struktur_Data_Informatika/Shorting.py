def bubble_sort(arr, order='ascending'):
    """
    Fungsi Bubble Sort dengan pilihan ascending atau descending
    """
    n = len(arr)
    arr_copy = arr.copy()
    iterations = []
    
    print(f"Array awal: {arr_copy}")
    print(f"Mode sorting: {order}")
    print("=" * 50)
    
    for i in range(n):
        swapped = False
        print(f"\n--- Iterasi {i + 1} ---")
        
        for j in range(0, n - i - 1):
            if order == 'ascending':
                condition = arr_copy[j] > arr_copy[j + 1]
                comparison = f"{arr_copy[j]} > {arr_copy[j + 1]}"
            else:
                condition = arr_copy[j] < arr_copy[j + 1]
                comparison = f"{arr_copy[j]} < {arr_copy[j + 1]}"
            
            print(f"  Bandingkan: {comparison} ? {condition}")
            
            if condition:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                print(f"  -> TUKAR! Array menjadi: {arr_copy}")
            else:
                print(f"  -> Tidak tukar. Array tetap: {arr_copy}")
        
        iterations.append(arr_copy.copy())
        print(f"Hasil akhir iterasi {i + 1}: {arr_copy}")
        if not swapped:
            print(f"\nTidak ada pertukaran pada iterasi {i + 1}. Array sudah terurut!")
            break
    
    return arr_copy, iterations
data = [8, 10, 30, 0, -4, 3]

print("=" * 60)
print("PROGRAM SORTING ARRAY - BUBBLE SORT")
print("=" * 60)
print(f"Data: {data}")
print()
print("Pilihan:")
print("1. Ascending (kecil ke besar)")
print("2. Descending (besar ke kecil)")
print()
print("\n" + "=" * 60)
print("PERHITUNGAN MANUAL - ASCENDING ORDER")
print("=" * 60)
result_asc, iter_asc = bubble_sort(data, 'ascending')

print("\n" + "=" * 60)
print("HASIL AKHIR ASCENDING:")
print(f"Array terurut: {result_asc}")
print("=" * 60)
print("\n" + "=" * 60)
print("PERHITUNGAN MANUAL - DESCENDING ORDER")
print("=" * 60)
result_desc, iter_desc = bubble_sort(data, 'descending')

print("\n" + "=" * 60)
print("HASIL AKHIR DESCENDING:")
print(f"Array terurut: {result_desc}")
print("=" * 60)
