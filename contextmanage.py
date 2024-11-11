from contextlib import contextmanager

# Define a function-based context manager using the @contextmanager decorator
@contextmanager
def file_manager(filename, mode):
    file = None
    try:
        # Open the file in the specified mode
        file = open(filename, mode)
        yield file  # Yield the file object to be used within the with block
    finally:
        # Ensure the file is closed after the block ends
        print("\nfile_closing")
        if file is not None:
            file.close()


# Usage of the function-based context manager
with file_manager('test.txt', 'w') as f:
    f.write('Test')

# Check if the file is closed after the with block
print(f.closed)
