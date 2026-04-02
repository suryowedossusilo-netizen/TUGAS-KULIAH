def main():
    # Input data angka (pisahkan dengan spasi)
    input_data_number = input("Masukan data angka (pisahkan dengan spasi): ")
    
    # Input tipe sorting
    input_type_sort = input("Masukan tipe sorting (ascending atau descending): ").lower().strip()
    
    # Konversi string ke list integer
    datas = input_data_number.split()
    numbers = [int(num) for num in datas]
    
    print(numbers, "\n")
    
    # Bubble Sort Ascending
    if input_type_sort == "ascending":
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                prev_number = numbers[j]
                if prev_number >= numbers[j + 1]:
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = prev_number
        
        result = numbers
        print(f"Hasil sorting ascending: {result}")
    
    # Bubble Sort Descending
    elif input_type_sort == "descending":
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                next_number = numbers[j + 1]
                if next_number >= numbers[j]:
                    numbers[j + 1] = numbers[j]
                    numbers[j] = next_number
        
        result = numbers
        print(f"Hasil sorting descending: {result}")
    
    else:
        print("Tipe sorting tidak valid! Gunakan 'ascending' atau 'descending'")