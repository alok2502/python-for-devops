# 🧠 Understanding Data Types in Python

## 📌 What Are Data Types?
Everything we write in a program is **data**.  
To process this data correctly, the programming language needs to understand **what type of data** it is.  
That’s why every programming language, including Python, has **data types**.

## 🐍 Python Data Types Overview
In Python, some commonly used data types are:

- **String** → e.g., `"Alok"` or `'Alok'`
- **Numeric**
  - `int` → Integer numbers (e.g., `10`)
  - `float` → Decimal numbers (e.g., `10.5`)
- **Sequence**
  - `list` → e.g., `[1, 2, 3]`
  - `tuple` → e.g., `(1, 2, 3)`
- **Mapping**
  - `dict` → e.g., `{"name": "Alok"}`
- **Boolean**
  - `True` or `False`

There are more data types, but these are the ones we use most frequently.

## ⚙️ Python Is Dynamically Typed
In Python, we **don’t need to declare data types explicitly**.  
The interpreter figures it out based on the **syntax**.

For example:
```python
name = "Alok"  # Python understands this is a string
```

This is why Python is called a **dynamically typed language**.

## 🧰 Built-in Functions for Data Types
Every data type in Python comes with **built-in functions** that help us work with data easily.

### Example: Working with Strings
Let’s say we have a string:
```python
full_name = "Alok Kumar"
```
If we want to extract just the first name, we can use the `split()` function:
```python
first_name = full_name.split()[0]
print(first_name)  # Output: Alok
```

### DevOps Example: Extracting Username from an ARN
Let’s say we get a list of IAM user ARNs and we want to extract the username:
```python
arn = "arn:aws:iam::123456789012:user/johndoe"
username = arn.split("/")[-1]
print(username)  # Output: johndoe
```

This is how Python’s built-in string functions can help in real-world DevOps tasks.

