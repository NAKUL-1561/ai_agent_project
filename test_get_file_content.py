from functions.get_file_content import get_file_content

def test_get_file_content():
    # Test 1: Large file with truncation
    print("get_file_content(\"calculator\", \"lorem_ipsum.txt\")\n")
    result = get_file_content("calculator", "lorem_ipsum.txt")
    print(f"Content length: {len(result)} characters")
    if "[...File" in result and "truncated" in result:
        print("✓ Truncation message found")
    print(f"Last 100 characters: ...{result[-100:]}\n")
    
    # Test 2: Regular Python file
    print("get_file_content(\"calculator\", \"main.py\")\n")
    result = get_file_content("calculator", "main.py")
    print(f"Content length: {len(result)} characters")
    print(f"First 200 characters:\n{result[:200]}\n")
    
    # Test 3: File in subdirectory
    print("get_file_content(\"calculator\", \"pkg/calculator.py\")\n")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Content length: {len(result)} characters")
    print(f"Content:\n{result}\n")
    
    # Test 4: File outside permitted directory
    print("get_file_content(\"calculator\", \"/bin/cat\")\n")
    result = get_file_content("calculator", "/bin/cat")
    print(f"Result:\n  {result}\n")
    
    # Test 5: Non-existent file
    print("get_file_content(\"calculator\", \"pkg/does_not_exist.py\")\n")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result:\n  {result}\n")

if __name__ == "__main__":
    test_get_file_content()