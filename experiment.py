import random
import time
import json
import os
import numpy as np
import matplotlib.pyplot as plt
from red_black_tree import RedBlackTree

def get_project_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_filepath(filename: str):
    return os.path.join(get_project_dir(), filename)

def load_data():
    filepath = get_filepath("input_data.txt")
    if not os.path.exists(filepath):
        print("Файл input_data.txt не найден. Генерируем новый...")
        from generate_data import generate_input_data
        return generate_input_data()  
    with open(filepath, "r", encoding="utf-8") as f:
        data = list(map(int, f.read().strip().split()))
    print(f"Загружено {len(data)} элементов из input_data.txt")
    return data

def run_experiment():
    data = load_data()
    rbt = RedBlackTree()
    print("\nЗапуск эксперимента с Красно-Чёрным деревом...\n")
    insert_times = []
    insert_iters = []
    print("Выполняется вставка 10 000 элементов...")

    for val in data:
        t, it = rbt.insert(val)
        insert_times.append(t)
        insert_iters.append(it)

    search_sample = random.sample(data, 100)
    search_times = []
    search_iters = []
    print("Выполняется поиск 100 случайных элементов...")

    for val in search_sample:
        t, it = rbt.search(val)
        search_times.append(t)
        search_iters.append(it)

    delete_sample = random.sample(data, 1000)
    delete_times = []
    delete_iters = []
    print("Выполняется удаление 1000 случайных элементов...")

    for val in delete_sample:
        t, it = rbt.delete(val)
        delete_times.append(t)
        delete_iters.append(it)

    results = {
        "insert": {
            "avg_time": float(np.mean(insert_times)),
            "avg_iterations": float(np.mean(insert_iters))
        },
        "search": {
            "avg_time": float(np.mean(search_times)),
            "avg_iterations": float(np.mean(search_iters))
        },
        "delete": {
            "avg_time": float(np.mean(delete_times)),
            "avg_iterations": float(np.mean(delete_iters))
        },
        "total_elements": 10000,
        "search_count": 100,
        "delete_count": 1000
    }

    json_path = get_filepath("rbt_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"\nРезультаты сохранены в: rbt_results.json")

    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.plot(insert_times, 'b-', alpha=0.6)
    plt.title('Время вставки элементов')
    plt.xlabel('Номер операции')
    plt.ylabel('Время (секунды)')

    plt.subplot(2, 2, 2)
    plt.plot(insert_iters, 'r-', alpha=0.6)
    plt.title('Количество итераций при вставке')
    plt.xlabel('Номер операции')
    plt.ylabel('Итерации')

    plt.subplot(2, 2, 3)
    plt.hist(insert_times, bins=50, color='blue', alpha=0.7)
    plt.title('Распределение времени вставки')

    plt.subplot(2, 2, 4)
    plt.hist(search_iters, bins=30, color='green', alpha=0.7)
    plt.title('Распределение итераций поиска')

    plt.tight_layout()
    
    graph_path = get_filepath("rbt_graphs.png")
    plt.savefig(graph_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Графики сохранены в: rbt_graphs.png")

    print("\n" + "="*60)
    print("                  ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
    print("="*60)
    print(f"Вставка   →  Среднее время: {results['insert']['avg_time']:.7f} сек | Итераций: {results['insert']['avg_iterations']:.1f}")
    print(f"Поиск     →  Среднее время: {results['search']['avg_time']:.7f} сек | Итераций: {results['search']['avg_iterations']:.1f}")
    print(f"Удаление  →  Среднее время: {results['delete']['avg_time']:.7f} сек | Итераций: {results['delete']['avg_iterations']:.1f}")
    print("="*60)

    return results

if __name__ == "__main__":
    run_experiment()