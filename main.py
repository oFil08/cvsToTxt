import csv

csv_file_path = input("Jaka jest nazwa pliku cvs?");

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    with open("plik.txt", "w", encoding="utf-8") as filetxt:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            filetxt.write(f"{row[1]} - {row[2]}\n")
        