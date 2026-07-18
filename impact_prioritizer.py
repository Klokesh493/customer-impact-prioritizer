import csv
import sys


def score(row):
    points = int(row["affected_users"]) // 1000
    if row["payment_impact"].lower() == "yes":
        points += 8
    if int(row["regions"]) >= 3:
        points += 5
    if row["tier"].lower() == "tier1":
        points += 4
    return points


def prioritize(rows):
    enriched = [{**row, "score": score(row)} for row in rows]
    return sorted(enriched, key=lambda row: row["score"], reverse=True)


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in prioritize(list(csv.DictReader(handle))):
            print(f"{row['score']:02d} {row['service']} {row['summary']}")


if __name__ == "__main__":
    main(sys.argv[1])
