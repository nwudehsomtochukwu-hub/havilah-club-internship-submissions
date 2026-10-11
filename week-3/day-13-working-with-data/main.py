# Day 13 - Working With Data

import csv

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# Step 1: Load CSV

def load_data(filepath):
    rows = []
    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


# Step 2: Clean and Convert

def clean_data(rows):
    for row in rows:
        row["name"] = row["name"].strip()
        row["grade"] = row["grade"].strip().upper()
        row["score"] = int(row["score"])
    return rows


# Step 3: Print Summary

def print_summary(rows):
    scores = []
    for row in rows:
        scores.append(row["score"])

    print("--- Data Summary ---")
    print("Total records:", len(rows))
    print("Lowest score:", min(scores))
    print("Highest score:", max(scores))
    print("Average score:", round(sum(scores) / len(scores), 2))


# Step 4: Filter Data

def filter_data(rows):
    filtered = []
    for row in rows:
        if row["score"] > 70:
            filtered.append(row)
    return filtered


# Step 5: Sort and Export

def get_score(row):
    return row["score"]


def save_data(rows, filepath):
    sorted_rows = sorted(rows, key=get_score, reverse=True)

    with open(filepath, "w", newline="") as file:
        fieldnames = ["name", "score", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)


# Main 

def main():
    rows = load_data(INPUT_FILE)
    rows = clean_data(rows)
    print_summary(rows)

    filtered = filter_data(rows)
    print("\n--- Students who scored above 70 ---")
    for row in filtered:
        print(row["name"], "|", row["score"], "|", row["grade"])

    save_data(filtered, OUTPUT_FILE)
    print("\nDone.", len(filtered), "rows written to", OUTPUT_FILE)


main()
