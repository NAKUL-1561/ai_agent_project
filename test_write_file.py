from functions.write_file import write_file

def test_write_file():
    # Test 1: Write to a file in the root of the working directory
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")\n')
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {result}\n")
    
    # Test 2: Write to a file in a subdirectory (should create directories as needed)
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")\n')
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {result}\n")
    
    # Test 3: Try to write to a file outside the permitted directory
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed")\n')
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {result}\n")

if __name__ == "__main__":
    test_write_file()
