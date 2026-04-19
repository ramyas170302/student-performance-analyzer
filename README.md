# Student Performance Analyzer

A data analysis project built using Python and Pandas to analyse
academic performance of 2000 students.

## Problem Statement
Educational institutions have large amounts of student data but
no quick way to identify who is performing well and who needs help.
This project automatically cleans, analyses, and summarises student
performance data to find meaningful patterns.

## Key Findings
- Total students analysed: 2000
- Average final exam marks: 64.86 / 100
- Average attendance: 84.89%
- Average daily study hours: 2.82 hours
- High performers: 377 students
- Medium performers: 1435 students
- Low performers: 188 students
- At-risk students (low marks + low attendance): 2 students
- Topper: S2007 with 100/100 in final exam
- Lowest scorer: S2564 with 25/100 in final exam

## What this project does
- Loads and explores real student dataset (2000 rows)
- Cleans missing values across all columns
- Creates new columns — Total Internal, Total Score, Performance category
- Groups students by performance level using groupby
- Filters high performers and at-risk students
- Ranks students by total score and attendance
- Prints a complete summary report

## Concepts used
- Pandas — read_excel, fillna, groupby, merge, query, sort_values
- Feature engineering — creating new columns using existing data
- Conditional categorisation using lambda functions
- Data filtering using single and multiple conditions

## Tech used
- Python 3
- Pandas

## How to run
1. Clone this repo
2. Install pandas: `pip install pandas openpyxl`
3. Run: `python analyzer.py`

## Dataset
- 2000 student records
- Columns: Student ID, Attendance, Internal Test 1,
  Internal Test 2, Assignment Score, Daily Study Hours,
  Final Exam Marks

## What is coming next
- Matplotlib and Seaborn visualisations (currently learning)
- Streamlit dashboard for interactive analysis