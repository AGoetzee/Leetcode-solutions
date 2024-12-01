Originally posted on leetcode [here](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/solutions/6100813/3-solutions-using-joins)

# What to do
We need to join two DataFrames based on a shared `id` column. After joining, the `id` column should be removed. Missing `unique_id`s in the second DataFrame should be filled with `null`.

# Approach
There are multiple ways to achieve this using Pandas:
1. Using the `on='id'` parameter in `pd.merge`.
2. Merging the DataFrames by setting `id` as the index.
3. Directly joining the DataFrames on their indices.

Each approach has trade-offs in runtime and memory usage. We aim to compare the methods and evaluate their performance for typical scenarios.

To ensure missing values are handled correctly, we use a **left join**, which keeps all rows from the left DataFrame (`employees`) and fills in `null` where no match is found in the right DataFrame (`employee_uni`).

---

# Method 1: Merging without indices (Simple and Readable)

Here, we directly use the `id` column to merge the two DataFrames. After merging, the `id` column is dropped. This method is simple and avoids any additional steps to manipulate the DataFrame structure.

Runtime: `356 ms` beats 97.08%  
Memory: `67.5 MB` beats 98.75%

## Code:

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    # Use a left join to keep all employee names and fill missing ids with null
    # Next drop the id column
    return pd.merge(employees, employee_uni, on='id', how='left', copy=False).drop(columns=['id'])
```

---

# Method 2: Merging with indices (🏁 Fastest 🏁)

In this approach, we first set `id` as the index for both DataFrames. Using `inplace=True` ensures no copies are created, saving memory and speeding up the process. The merge is then performed on the indices, and the resulting DataFrame is returned.

Runtime: `300 ms` beats 99.93%  
Memory: `67.35 MB` beats 99.11%

## Code:

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Set indexes for easy joinging
    # Use inplace for memory optimization
    employees.set_index('id', inplace=True)
    employee_uni.set_index('id', inplace=True)

    # Now join the dfs on the index
    # Use a left merge to keep all employee names and fill missing ids with null
    return pd.merge(employees, employee_uni, left_index=True, right_index=True, how='left', copy=False, sort=False)
```

---

# Method 3: Joining with indices (✅ Lowest memory ✅)

This method directly uses the `join` function, which is optimized for merging DataFrames based on indices. Like the previous method, we set `id` as the index for both DataFrames. However, `join` is slightly slower than `merge` for this specific task but uses marginally less memory.

Runtime: `382 ms` beats 89.04%  
Memory: `67.09 MB` beats 99.60%

## Code:

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    # Set indexes for easy joinging
    # Use inplace for memory optimization
    employees.set_index('id', inplace=True)
    employee_uni.set_index('id', inplace=True)

    # Now join the dfs on the index
    # Use a left join to keep all employee names and fill missing ids with null
    return employees.join(employee_uni, how='left')
```

---

# Summary

| Method                  | Runtime (ms) | Memory (MB) | Description                         |
|-------------------------|--------------|-------------|-------------------------------------|
| Merging without indices | `356`        | `67.5`      | Simplest method; drop `id` column manually. |
| Merging with indices    | `300`        | `67.35`     | Fastest; merge on indices after setting them. |
| Joining with indices    | `382`        | `67.09`     | Lowest memory; uses `join` on indices.       |

---


