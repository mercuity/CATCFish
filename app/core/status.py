import csv
from base64 import b64decode

def setStatus(id, stat, table):
    email = b64decode(id).decode('utf-8').strip().lower()
    print(email,stat)
    newRows = []
    with open(table, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldNames = reader.fieldnames
        for row in reader:
            rowEmail = row.get("Email", "").strip().lower()
            if rowEmail == email:
                current = row.get("Статус", "").strip()
                if stat == 1:
                    if current == "Обратился":
                        row["Статус"] = "Перешел & Обратился"
                    elif current == "Ввел данные":
                        pass
                    else:
                        row["Статус"] = "Перешел"
                elif stat == 2:
                    row["Статус"] = "Ввел данные"
                elif stat == 3:
                    if current == "Перешел":
                        row["Статус"] = "Перешел & Обратился"
                    elif current == "Ввел данные":
                        pass
                    else:
                        row["Статус"] = "Обратился"
            newRows.append(row)

    with open(table, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(newRows)