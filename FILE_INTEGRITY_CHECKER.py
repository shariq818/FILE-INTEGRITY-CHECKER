# File Integrity Checker v1.0
# Author: Paradox (shariq818)

import hashlib
import os
import json

def hash_file(path):
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                sha.update(chunk)
        return sha.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline(directory):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            baseline[full_path] = hash_file(full_path)

    with open("baseline.json", "w") as out:
        json.dump(baseline, out, indent=4)
    print("Baseline created: baseline.json")

def check_integrity():
    try:
        with open("baseline.json", "r") as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print("Error: baseline.json not found!")
        return

    changes = []
    for path, old_hash in baseline.items():
        new_hash = hash_file(path)
        if new_hash != old_hash:
            changes.append(path)

    with open("integrity_report.txt", "w") as out:
        if changes:
            for c in changes:
                out.write(f"Changed: {c}\n")
        else:
            out.write("No changes detected.\n")

    print("Scan completed. Results: integrity_report.txt")

if __name__ == "__main__":
    print("1. Create baseline")
    print("2. Check integrity")
    choice = input("Select option: ")

    if choice == "1":
        directory = input("Enter directory to monitor: ")
        create_baseline(directory)
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid choice.")