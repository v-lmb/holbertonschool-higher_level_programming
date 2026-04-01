# Python: Mutable, Immutable… and How Memory Really Works

---

## Introduction

In Python, everything is an object. Whether it's an integer, string, list, or function, each object has:

- an identity (memory address)
- a type
- a value

Understanding how Python handles objects in memory is essential to avoid subtle bugs, especially when working with mutable objects and function arguments.

---

## id() and type()

Every object has:

- an identity → accessed with `id()`
- a type → accessed with `type()`

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # memory address
```
Two variables can reference the same object:

```python
a = 89
b = 89
print(a is b)  # True (CPython optimization)
```

---

## Mutable Objects

Mutable objects can be modified in place after creation.

### Main mutable types:
list
dict
set
bytearray
```python
l = [1, 2, 3]
l.append(4)
```

#### Memory schema:
```python
l ─────► [1, 2, 3]
             │
append(4)
             ▼
l ─────► [1, 2, 3, 4]
(same object)
```

#### Aliasing (very important)
```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)
print(l2)  # [1, 2, 3, 4]
```

l1 and l2 are aliases (same object in memory)
 
---

## Immutable Objects

Immutable objects cannot be modified after creation.

### Main immutable types:
int, float, complex
str
tuple
frozenset
bytes
bool

```python
s = "hello"
s += " world"
```

#### Memory behavior:
```python
s ─────► "hello"

s += " world"

s ─────► "hello world"
(new object created)
```

#### Special Case: Tuple and Frozenset

Even though they are immutable, they can contain mutable objects:
```python
t = ([1, 2],)
t[0].append(3)

print(t)  # ([1, 2, 3],)
```

--- 

## Passing Arguments to Functions

Python uses pass-by-object-reference (or pass-by-assignment).

### Immutable example:
```python
def increment(n):
    n += 1

a = 1
increment(a)

print(a)  # 1
```

A new object is created inside the function.

### Mutable example:
```python
def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)

print(l)  # [1, 2, 3, 4]
```

The original object is modified.

### Reassignment does NOT affect original:
```python
def reset(lst):
    lst = [0]

l = [1, 2, 3]
reset(l)

print(l)  # [1, 2, 3]
```

Only the local reference changed.

---

### Difference Between + and +=
```python
l = [1, 2, 3]
l = l + [4]   # new object
```

```python
l = [1, 2, 3]
l += [4]      # in-place modification
```

---

### Conclusion

Understanding Python memory behavior is critical:

- Mutable objects can change in place → dangerous with aliases
- Immutable objects are safe but create new objects
- Always distinguish between:
  - identity (is)
  - equality (==)
