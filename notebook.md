% My Notebook
% myself
% today

``` {.code .python}
import matplotlib_inline.backend_inline

matplotlib_inline.backend_inline.set_matplotlib_formats("svg")
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

# Lorem ipsum

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.

``` code
print("hello")
```

```
print("hello")
```

```python
print("hello")
```

## Pyout

``` code
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

If you want to add cell attributes, group cells differently, 
or add output to code cells, 
then you need to include divs to indicate the structure. 
You can use either fenced divs or native divs for this. Here is an example:

:::::: {.cell .markdown .other}
# Lorem {.ipsum}

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.
::::::

:::::: {.cell .code execution_count=1}
``` {.python}
print("hello")
```

::: {.output .stream .stdout}
```
hello
```
:::
::::::

:::::: {.cell .code execution_count=2}
``` {.python}
from IPython.display import HTML
HTML("""
<script>
console.log("hello");
</script>
<b>HTML</b>
""")
```

::: {.output .execute_result execution_count=2}
```{=html}
<script>
console.log("hello");
</script>
<b>HTML</b>
hello
```
:::
::::::