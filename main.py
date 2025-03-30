import csv
import os

csv_file_path = None
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".csv"):
        csv_file_path = os.path.join(os.path.dirname(__file__), file)
        break

if not csv_file_path:
    raise FileNotFoundError("No CSV file found in the script's directory.")

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as filecvs:
    with open("plik.txt", "w", encoding="utf-8") as filetxt:
        csv_reader = csv.reader(filecvs)
        
        for row in csv_reader:
            filetxt.write(f"\"{row[1]}\" - {row[2]}\n")
        