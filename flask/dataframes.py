import pandas as pd

def get_dataframe():
    df = pd.read_csv("static/docs/students_scores.csv")
    return df

def get_students_grades():
    df = get_dataframe()
    df["grade"] = df[["score 1", "score 2", "score 3"]].mean(axis=1)
    df['grade'] = df['grade'].apply(lambda x: f"{x:.2f}")
    df['grade'] = pd.to_numeric(df['grade'])
    return df

def get_students_status():
    df = get_students_grades()
    df['status'] = df['grade'].apply(lambda x: "passed" if x >= 60 else "failed")
    return df

def get_highest_grade():
    df = get_students_grades()
    return df['grade'].max()

def get_lowest_grade():
    df = get_students_grades()
    return df['grade'].min()

def get_average_grade():
    df = get_students_grades()
    return df['grade'].mean()

def passed_students():
    df = get_students_status()
    return df[df['status'] == 'passed']

def passed_students_count():
    df = get_students_status()
    return df[df['status'] == 'passed'].shape[0]

def failed_students():
    df = get_students_status()
    return df[df['status'] == 'failed']

def failed_students_count():
    df = get_students_status()
    return df[df['status'] == 'failed'].shape[0]