import random
import os

def get_data_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "input_data.txt")
def generate_input_data(size: int = 10000):
    random.seed(42)
    data = [random.randint(-100000, 100000) for _ in range(size)]   
    filepath = get_data_file_path()  
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, data)))   
    print(f"Файл успешно создан/обновлён:")
    print(f"{filepath}")
    print(f"Количество элементов: {size}")   
    return data

if __name__ == "__main__":
    generate_input_data()