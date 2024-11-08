<div style="background-color: #909190; padding: 40px;">

# **Geometry Nodes**
The editor can add a new subgroup of Sockets, the format of which is stored in the socket description.

![](./img/indent.png)

## Geometry Node Modifier Indentation Format

To use the Indentation Format, you need to add a semicolon at the beginning of the socket description.
```
;#0;sep(1);  Socket description..
```


### Indent
Indent to level 1.
```
;#1
```

### Unindent
Unindent to level 0.
```
;#0
```
---
### Header
Show title only when indented by default.

![](./img/indent_title.png)

- Header Alignment
  - Show Title and Value on Header
    ```
    ;align()
    ```
    ![](./img/indent_title_align.png)
  - Boolean
    ![](./img/indent_title_align_bool.png)

  - Show Title and Full Size Value
    ```
    ;align(fit)
    ```
    ![](./img/indent_title_align_fit.png)

  - Value Only
    ```
    ;align(full)
    ```
    ![](./img/indent_title_align_full.png)
---

### Separator
```
;sep(x)
    Parameters:
        x (float)
```

![](./img/indent3.png)

### Alignment
 - Boolean

   - Default / Title Right
        ```
        ;align(right)
        ```
        ![](./img/indent_bool_default.png)

   - Title Left
        ```
        ;align(left)
        ```
        ![](./img/indent_bool_left.png)

