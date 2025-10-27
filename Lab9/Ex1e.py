import os
from collections import Counter

filename = "names.txt"   # switch back to the real file to append and print

# --- Safe read of the file contents ---
if os.path.exists(filename) and os.access(filename, os.R_OK):
    try:
        with open(filename, "r") as file_object:
            lines = file_object.readlines()          # read all lines into a list
            names = [line.strip() for line in lines if line.strip()]  # strip newline and ignore blank lines

        # print each name
        for name in names:
            print(name)

        # build a dictionary of name -> occurrence count
        name_counts = dict(Counter(names))
        print("Counts:", name_counts)

        # build a dictionary of name -> first line index (1-based)
        name_index = {name: idx for idx, name in enumerate(names, start=1)}
        print("Indices:", name_index)

    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading '{filename}': {e}")
else:
    if not os.path.exists(filename):
        print(f"File not found: '{filename}'")
    else:
        print(f"File exists but is not readable: '{filename}'")

# --- Safe append of a new name and print entire file contents ---
append_name = "French, Micah"

# Ensure file exists and is writable before attempting to append
if os.path.exists(filename) and os.access(filename, os.W_OK):
    # Use a+ mode to allow reading and appending; read current contents to check trailing newline
    with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0)
        data = f.read()
        # If file has content and doesn't end with newline, add one before appending
        if data and not data.endswith("\n"):
            f.write("\n")
        f.write(append_name + "\n")

    # Re-open for reading and print full contents
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

else:
    if not os.path.exists(filename):
        print(f"Cannot append: file not found: '{filename}'")
    else:
        print(f"Cannot append: file exists but is not writable: '{filename}'")