import json

file1 = json.load(open('gendiff/file1.json'))
file2 = json.load(open('gendiff/file2.json'))


def generate_diff(file1, file2):
    keys = set(file1.keys()).union(set(file2.keys()))
    diff = ["{"]

    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff.append(f"  {key}: {file1[key]}")
            else:
                diff.append(f"  - {key}: {file1[key]}")
                diff.append(f"  + {key}: {file2[key]}")
        elif key in file1:
            diff.append(f"  - {key}: {file1[key]}")
        elif key in file2:
            diff.append(f"  + {key}: {file2[key]}")
    diff.append("}")

    return str("\n".join(diff))


print(generate_diff(file1, file2))







