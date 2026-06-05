# Module 1 Assignment: Building "Loglytics" (In-Memory Log Engine)

## Objective
Welcome to your first DSA assignment! In this practical module, you will step into the shoes of a backend engineer building **Loglytics**—a lightweight, in-memory analytics engine designed to process high-velocity application logs. 

This assignment will test your understanding of:
1. **Introduction to DSA:** Choosing the right structure based on constraints.
2. **Abstract Data Types (ADTs):** Designing interfaces for lists, sets, maps, and priority queues.
3. **Python Collections:** Leveraging Python's built-in `list`, `dict`, `set`, `tuple`, and `str` efficiently.

---

## The System Architecture Overview
Loglytics needs to ingest raw log strings, parse them, detect duplicate anomalies, track unique users, and surface the most severe system errors in real time.



---

## Core Tasks to Complete
Open `log_engine.py` and implement the sections marked with `TODO`. 

### Task 1: The Raw Parser (`str`, `tuple`, `list`)
* **Goal:** Ingest a raw log string formatted as `"TIMESTAMP | LEVEL | USER_ID | MESSAGE"` (e.g., `"14:00:01 | ERROR | user_101 | Database timeout"`).
* **Challenge:** Clean up whitespaces, extract elements, and store them in an immutable `tuple` format for safe downstream processing.

### Task 2: Unique Visitor Tracker (`set`)
* **Goal:** Instantly track how many unique users have interacted with the system.
* **Challenge:** Maintain a system where lookups and additions stay highly optimized ($O(1)$ time complexity).

### Task 3: Error Frequency Analyzer (`dict` as a Map ADT)
* **Goal:** Group and count occurrences of specific error messages to find systemic bugs.

### Task 4: The Real-Time Alert Triage (`list` as a Priority Queue ADT)
* **Goal:** Maintain a list of logs sorted *primarily* by severity (`CRITICAL` > `ERROR` > `WARNING`) so engineers can fix the worst bugs first.
* **Challenge:** You will implement this using a Python `list` but maintaining it dynamically like a Priority Queue.

---

## How to Run Tests
1. Install dependencies: `pip install -r requirements.txt`
2. Run the test suite: `pytest test_log_engine.py`
