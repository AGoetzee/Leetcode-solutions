Originally posted as `Solution` on Leetcode, where it lives [here](https://leetcode.com/problems/students-and-examinations/solutions/6094874/using-multiindex-to-fill-zero-count-values)


# What to do

We want to get the exam attempts of all students on all study subjects in a sorted dataframe.
# Why its hard

We can't just use `value_counts(subset=['student_id','subject_name'])` because `value_counts()` does not include zero values. They need to be added afterwards, but how do you make that efficient?
# Approach

We can use pandas' MultiIndex feature to reindex the dataframe after calling `value_counts()` on examinations, we can fill missing indices with a default value, which in our case will be `0`. The method call will look as follows: counts_df.reindex(my_multi_index, fill_value=0).

Only thing left to do is to create the multindex. We grab the unique student ids using `students['student_id'].unique()` and subject names are just from the `subjects` dataframe. Next we use these unique values to create a cartesian product as the multiIndex and add names using `pd.MultiIndex.from_product([students['student_id'].unique(), subjects['subjects']], names=['student_id','subject_name'])`

After that I reset the index to get a normal dataframe again, which I merge with students to obtain the student names. After that its just sorting and reordering the columns.

Hope this is helpful!
# Code
```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # we are going to need a multindex, which is the cartesian product of students and subjects
    multi_index = pd.MultiIndex.from_product([students['student_id'].unique(),subjects['subject_name']], names=['student_id','subject_name'])

    # get the grouped counts, 
    # then reindex to add zero counts
    # reset index to get a regular df and rename 
    attended_exams = examinations.value_counts(subset=['student_id','subject_name']).reindex(multi_index, fill_value=0).reset_index(name='attended_exams')

    # merging here to add the student_name
    # next we sort on student_id first and then subject_name
    # and then reorder the columns
    attended_exams = pd.merge(attended_exams, students, on='student_id').sort_values(['student_id','subject_name'], ascending=True)[['student_id','student_name','subject_name','attended_exams']]


    return attended_exams
```
