## Student Performance Analysis System

A data analysis project built using Python, Pandas, and Excel to evaluate and analyze student academic performance.

This system processes student marks, calculates performance metrics, identifies top performers, and generates a structured Excel report for easy review.

## Features

✔ Data cleaning and preprocessing
✔ Automatic calculation of Total and Average marks
✔ Grade assignment based on performance
✔ Identification of Top 3 performing students
✔ Subject-wise performance analysis
✔ Pass percentage calculation
✔ Export of results into a multi-sheet Excel report

##Technologies Used
Python
Pandas
Excel (OpenPyXL)

## Project Structure
Student_Performance_Analysis/
│
├── student_performance_analysis.py   # Main Python script
├── students.csv                      # Input dataset
└── Student_Performance_Report.xlsx   # Generated output report

## Input Dataset

The system reads student data from a CSV file containing subject marks.

Sample Format:

Name	Maths	Science	English	History
Amit	85	78	92	74
Neha	90	88	95	91

## How It Works
Loads student data from CSV

Cleans missing values (if any)

Calculates:

Total Marks

Average Marks

Assigns Grades:

A (90+)

B (75–89)

C (60–74)

Needs Improvement (<60)

Identifies top performers

Analyzes subject-wise averages

Generates an Excel report with multiple sheets

## How to Run the Project
Step 1: Install Required Libraries
pip install pandas openpyxl

Step 2: Run the Script
python student_performance_analysis.py

## Output

The program generates an Excel file:

Student_Performance_Report.xlsx

It contains:

Sheet Name	Description
Full Report	Complete student performance data
Top Performers	Top 3 students based on average marks
Subject Averages	Average marks per subject

##Learning Outcomes

Through this project, I practiced:

Data cleaning using Pandas

Data analysis and aggregation

Applying conditional logic for grading

Exporting structured reports to Excel

Writing clean, real-world Python scripts

## Future Improvements

Add data visualizations (charts & graphs)

Create a performance dashboard

Add ranking system

Build a simple GUI interface

## Author

Sourabh Panchal
Aspiring Data Analyst | Python & SQL Learner
