def generate_diff(file1, file2):
    key1 = set(file1.keys())
    key2 = set(file2.keys())
    keys = set(key1).union(set(key2))
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

    return "\n".join(diff)
