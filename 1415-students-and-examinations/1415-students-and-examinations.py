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