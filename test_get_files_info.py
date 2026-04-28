from functions.get_files_info import get_files_info

def test_get_files_info():
    # Test 1: List current directory
    print("get_files_info(\"calculator\", \".\")\n")
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(f"  {result}\n")
    
    # Test 2: List subdirectory
    print("get_files_info(\"calculator\", \"pkg\")\n")
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(f"  {result}\n")
    
    # Test 3: Try to access outside directory
    print("get_files_info(\"calculator\", \"/bin\")\n")
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(f"  {result}\n")
    
    # Test 4: Try to access parent directory
    print("get_files_info(\"calculator\", \"../\")\n")
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(f"  {result}\n")

if __name__ == "__main__":
    test_get_files_info()
