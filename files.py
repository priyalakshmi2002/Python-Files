import os

# Specify the path
path = "c:/Users/DELL/Desktop"

# Specify the file name
file = 'file.txt'

# 1. Writing to the file (this will overwrite existing content)
with open(os.path.join(path, file), 'w') as fp:
    fp.write("This is a new line of text.\n")
    fp.write("This is another line of text.\n")
fp.close()

# 2. Appending to the file (this will add content to the end)
with open(os.path.join(path, file), 'a') as fp:
    fp.write("This line is appended to the file.\n")
fp.close()

# 3. Reading the file content
with open(os.path.join(path, file), 'r') as fp:
    content = fp.read()
fp.close()

# Print the file content
print("Content of the file after writing and appending:")
print(content)

file_path = os.path.join(path, file)
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file}' has been deleted.")
else:
    print(f"File '{file}' does not exist.")  