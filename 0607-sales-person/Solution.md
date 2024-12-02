Originally posted on Leetcode [here](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/solutions/6105202/merging-on-the-original-dataframe-to-get-the-names).


# Problem
We want to find manager names that have at least 5 people reporting to them.

# Why its hard
`ManagerId` and `Id` are actually the same. Finding at least 5 counts is simple, but getting the name is tricky.

# Approach
We can use `value_counts(subset=['managerId']) >= 5` to find the eligible `managerId`'s. This produces a `Series` where `managerId` has become the index. Using `pd.merge` we can now join on the original dataframe to yield the names. 

We use the `Series` as the right dataframe, and we specify `how='inner'` so we do not get any `null` values. Next we specify `right_index=True` and `left_on='id` to get the correct merge. This approach also lets us avoid using `reset_index()` on the counts `Series`, avoiding some unneeded runtime and memory.

Now we have a dataframe with a new column named `count`, but since we performed a comparison on it, it is only boolean values if managers have more than 5 reports. We use this to filter the dataframe, and then we only return the `'name'` column.

# Code
```python
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # Find the manager counts by subsetting
    # Then merge on the original employee dataframe
    # Use an inner join to avoid null values
    at_least_5 = employee.merge(employee.value_counts(subset=['managerId']) >= 5 , how='inner', right_index=True, left_on='id')
    
    # subset using the count mask
    # only keep the name
    return at_least_5[at_least_5['count']][['name']]
```
