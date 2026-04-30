from functions.run_python_file import run_python_file

# Test 1: run_python_file("calculator", "main.py")
print("Test 1: run_python_file('calculator', 'main.py')")
result1 = run_python_file("calculator", "main.py")
print(result1)
print()

# Test 2: run_python_file("calculator", "main.py", ["3 + 5"])
print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(result2)
print()

# Test 3: run_python_file("calculator", "tests.py")
print("Test 3: run_python_file('calculator', 'tests.py')")
result3 = run_python_file("calculator", "tests.py")
print(result3)
print()

# Test 4: run_python_file("calculator", "../main.py")
print("Test 4: run_python_file('calculator', '../main.py')")
result4 = run_python_file("calculator", "../main.py")
print(result4)
print()

# Test 5: run_python_file("calculator", "nonexistent.py")
print("Test 5: run_python_file('calculator', 'nonexistent.py')")
result5 = run_python_file("calculator", "nonexistent.py")
print(result5)
print()

# Test 6: run_python_file("calculator", "lorem.txt")
print("Test 6: run_python_file('calculator', 'lorem.txt')")
result6 = run_python_file("calculator", "lorem.txt")
print(result6)
