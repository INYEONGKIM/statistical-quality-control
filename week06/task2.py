import pandas as pd
import os

input = __import__('sys').stdin.readline

raw_data = []
for _ in range(495//11):
    tmp = [""] * 11
    for i in range(10):
        tmp[i] = float(input())
    tmp[-1] = input().strip()

    raw_data.append(tmp)

for x in raw_data:
    print(x)
print(len(raw_data))


try:
    dir_path = os.path.abspath(__file__) + "/data/"
    file_name = "task2.xlsx"

    df = pd.DataFrame.from_records(raw_data)

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    df.to_excel(dir_path + file_name, sheet_name="Sheet1", index=False)

    print("fin")

except OSError as e:
    print(e.__traceback__)