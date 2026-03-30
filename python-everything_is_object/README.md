
###  Introduction

As a beginner learning Python, I recently explored a topic: how Python handles different types of objects in memory, and how this affects our programs. This post summarizes what I’ve learned about object identity, mutability, and function argument behavior in Python. I include simple examples and clear explanations so anyone new to programming can follow along.

---

### `id()` and `type()`

In Python, every object has a unique identifier, which we can see using the `id()` function. You can also check what kind of object something is using `type()`. These tools help understand what’s happening under the hood.

```python
x = 10
print(id(x))
print(type(x))

y = "hello"
print(id(y))
print(type(y))
```

Even though `x` and `y` are different types, they both have IDs. This tells us they are objects stored in memory.

---

### Mutable Objects

Mutable objects can be changed after they are created. Common mutable types include lists, dictionaries, and sets.

```python
my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
print(my_list)
print(id(my_list))
```

Notice that the list’s `id` did not change even after we modified it. That means the object itself was changed — not replaced. This is what “mutable” means in Python.

---

###  Immutable Objects

Immutable objects cannot be changed once they’re created. If you try to change them, Python creates a new object instead. Examples include `int`, `float`, `str`, and `tuple`.

```python
a = 5
print(id(a))
a += 1
print(a)
print(id(a))
```

Here, `a` went from 5 to 6, but Python actually created a new object and assigned it to `a`. This is how Python handles immutability.

---

### Why It Matters: Mutable vs Immutable

Understanding mutability helps you avoid unexpected behavior in your code. Python treats mutable and immutable objects differently when it comes to memory and functions.

For example:

```python
def modify_list(l):
    l.append(100)

lst = [1, 2, 3]
modify_list(lst)
print(lst)
```

But with immutable objects:

```python
def modify_number(n):
    n += 100

num = 10
modify_number(num)
print(num)
```

Mutable objects are changed in place, while immutable ones are effectively copied when passed around.

---

### How Python Passes Arguments

Python always passes arguments by object reference, sometimes called "pass-by-assignment." But what happens depends on mutability.

```python
def add_item(my_list):
    my_list.append("new")

x = ["old"]
add_item(x)
print(x)

def change_str(s):
    s = s.upper()

name = "alice"
change_str(name)
print(name)
```

This shows that with mutable types, the function can change the original object. With immutable types, the function works on a copy, leaving the original unchanged.

---

### Advanced Insights (Optional)

If you're diving deeper, you'll find that Python sometimes reuses immutable objects for efficiency (like small integers or short strings), which explains why some `id()` values appear the same. Also, mutable default arguments in functions can cause bugs if not handled properly:

```python
def buggy_func(x=[]):
    x.append(1)
    return x

print(buggy_func())
print(buggy_func())
```

Python reused the same list between calls. That’s why default arguments should use `None` and create the list inside the function:

```python
def fixed_func(x=None):
    if x is None:
        x = []
    x.append(1)
    return x
```
