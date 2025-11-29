# File Integrity Monitor (FIM) — v1.0  

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Project-Stable-brightgreen)
![Security](https://img.shields.io/badge/Security-FIM%20Tool-orange)
![Version](https://img.shields.io/badge/Version-1.0-lightgrey)

A lightweight Python-based File Integrity Monitoring tool that creates a secure baseline of file hashes and later detects any unauthorized changes — modified, deleted, or newly added files.

This beginner-friendly cybersecurity automation project demonstrates the basic working of real enterprise FIM tools like Tripwire and OSSEC.

---

## Features
- Creates a baseline hash snapshot of all files in a selected directory  
- Detects:  
  • Modified files  
  • Newly added files  
  • Deleted files  
- Uses SHA-256 hashing  
- Saves reports to baseline_hashes.txt and integrity_results.txt  
- Clean command-line interface

---

## Usage

### *1. Create a baseline*
python FILE_INTEGRITY_CHECKER.py –baseline
### *2. Run integrity scan*
python FILE_INTEGRITY_CHECKER.py –scan
You will be asked for a directory path each time.

---

## Requirements
- Python 3.x  
- No external libraries required  

---

## Author
Paradox (shariq818)
