def read_and_sort_numbers(file_path, reverse=False):

    try:

        with open(file_path, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

        numbers.sort(reverse=reverse)
        return numbers

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return []
    except ValueError:
        print("Erro: O arquivo contém valores não numéricos.")
        return []

def save_sorted_numbers(numbers, output_path):

    try:
        with open(output_path, "w") as file:
            for number in numbers:
                file.write(f"{number}\n")
        print(f"Números ordenados salvos em '{output_path}'.")

    except IOError:
        print("Erro ao tentar salvar o arquivo.")

input_file = "extra.txt"
output_file = "sorted_numbers.txt"
reverse_order = False

sorted_numbers = read_and_sort_numbers(input_file, reverse_order)
if sorted_numbers:
    print("Números ordenados:")
    print(sorted_numbers)

with open("extra.txt", "r") as file:

    numbers = [int(line.strip()) for line in file]

numbers.sort()

print("Números ordenados:")
for number in numbers:
    print(number)