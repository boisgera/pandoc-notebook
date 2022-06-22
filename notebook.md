% My Notebook
% myself
% today

---

```python
%matplotlib inline
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
```

```python
#import matplotlib as mpl
#print(mpl.rcParams['figure.dpi'])
#mpl.rcParams['figure.dpi'] = 300
#print(mpl.rcParams['figure.dpi'])
#mpl.rcParams['savefig.dpi'] = 300
```

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

# Lorem ipsum

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.

```
print("hello")
```

```
print("hello")
```

```python
print("hello")
```

## Result

```python
>>> 1 + 1
```

## Pyout

```
from IPython.display import HTML
HTML("""
<script>
console.log("hello");
</script>
<b>HTML</b>
""")
```

## Image {.tag key=value #ididid}

This image ![images](images/howtoexplain.jpg) will be included as a cell attachment.

![images](images/howtoexplain.jpg)

---

```
1 + 1
```

```
print("Hello world!")
```

$$
\int_0^x f(t) \, dt
$$

sljdksjdksdj $a=1$

```
width = 345.0 / 72.27
height = width / (16/9)
print(width, height)
fig, axes = plt.subplots(figsize=(width, height))
axes.plot([0, 2, 1, 0, 3, 3, 0, 0])
```

```
width = 100 / 72 # target: 100 px. We assume a pixel = a dot. We convert that in inches.
dpi = 72 # and we define a consistent dpi.
height = width / (16/9)
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([0, 2, 1, 0, 3, 3, 0, 0])
```

```
width = 100
dpi = 100 # and we define a consistent dpi.
height = width / (16/9)
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([0, 2, 1, 0, 3, 3, 0, 0])
```

```python
width = 100
height = 100
dpi = 96 # my real dpi.
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([0, 2, 1, 0, 3, 3, 0, 0])
```

```python
width = 100
height = 100
dpi = 96 # my real (screen) dpi.
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([-1,1, -1, 1, -1, 1, -1, 1])
```

```python
width = height = 345 / 72.27
dpi = 72 # matplotlib default ?
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([-1,1, -1, 1, -1, 1, -1, 1])
```

```python
width = height = 345 / 72.27
dpi = 96 # my screen effective dpi
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([-1,1, -1, 1, -1, 1, -1, 1])
```

```python
width = height = 345 / 72.27
dpi = 117.5 # my screen experimental dpi
print(width, height)
fig, axes = plt.subplots(figsize=(width, height), dpi=dpi)
axes.plot([-1,1, -1, 1, -1, 1, -1, 1], color="red")
```
