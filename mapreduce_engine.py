from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import re


def process_chunk(lines):
    results = []

    for line in lines:

        error_match = re.search(r'\s(404|500)\s', line)
        hour_match = re.search(r':(\d{2}):\d{2}:\d{2}', line)

        if error_match:
            results.append((f"HTTP_{error_match.group(1)}", 1))

        if hour_match:
            results.append((f"HOUR_{hour_match.group(1)}", 1))

    return results


def mapreduce_log_analysis(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    chunk_size = max(1, len(lines) // 4)

    chunks = [
        lines[i:i + chunk_size]
        for i in range(0, len(lines), chunk_size)
    ]

    mapped = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(process_chunk, chunks)

        for r in results:
            mapped.extend(r)

    grouped = defaultdict(list)

    for key, value in mapped:
        grouped[key].append(value)

    reduced = {}

    for key, values in grouped.items():
        reduced[key] = sum(values)

    return reduced