student_info = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}

# Accessing values
print(student_info["name"])  # Output: John Doe
print(student_info["age"])   # Output: 20
print(student_info["courses"])  # Output: ['Math', 'Science', 'History']
# Adding a new key-value pair
student_info["grade"] = "A"
print(student_info)  # Output: {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'Science', 'History'], 'grade': 'A'}
# Updating an existing key-value pair
student_info["age"] = 21
print(student_info)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'Science', 'History'], 'grade': 'A'}