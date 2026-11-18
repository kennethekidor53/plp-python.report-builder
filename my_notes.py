# Write three notes to a new file
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n")
    # Write a second note
    # Write a third note

# Read the file back and print each line with no blank lines between
print("--- My notes ---")
with open("my_notes.txt", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

# Count the lines
with open("my_notes.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))