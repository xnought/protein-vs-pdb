import fire
import sys
import os
import time

DATA_DIR = "./data"
TOTAL = 214_791
KILO = 2**10
MEGA = KILO * KILO
GIGA = MEGA * KILO


def num_files_in_dir(dir_name: str):
    total = 0
    file_size = 0
    for path, _, files in os.walk(dir_name):
        total += len(files)
        for file in files:
            file_size += os.path.getsize(os.path.join(path, file))
    return total, file_size


def progress(delay=0.2):
    while True:
        num_files, _bytes = num_files_in_dir(DATA_DIR)
        fmt = f"{num_files}/{TOTAL} ({100*num_files/TOTAL:.2f}%), [B={_bytes}, KiB={_bytes/KILO:.2f}, MiB={_bytes/MEGA:.2f}, GiB={_bytes/GIGA:.2f}]"
        print(fmt, end="\r")
        time.sleep(delay)


if __name__ == "__main__":
    fire.Fire(progress)
