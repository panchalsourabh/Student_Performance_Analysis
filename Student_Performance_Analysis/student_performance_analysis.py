import pandas as pd

# Load student data
df = pd.read_csv("students.csv")

print("Original Data:\n")
print(df)


# -----------------------------
# DATA CLEANING
# -----------------------------

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing marks with subject average (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)


# -----------------------------
# CALCULATIONS
# -----------------------------

# Calculate Total Marks
df["Total"] = df[["Maths", "Science", "English", "History"]].sum(axis=1)

# Calculate Average Marks
df["Average"] = df["Total"] / 4


# -----------------------------
# GRADE ASSIGNMENT
# -----------------------------

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Needs Improvement"

df["Grade"] = df["Average"].apply(assign_grade)


# -----------------------------
# TOP PERFORMERS
# -----------------------------

top_performers = df.sort_values(by="Average", ascending=False).head(3)

print("\nTop Performers:\n")
print(top_performers[["Name", "Average", "Grade"]])


# -----------------------------
# SUBJECT-WISE AVERAGES
# -----------------------------

subject_averages = df[["Maths", "Science", "English", "History"]].mean()

print("\nSubject Wise Averages:\n")
print(subject_averages)


# -----------------------------
# PERFORMANCE INSIGHTS
# -----------------------------

highest_subject = subject_averages.idxmax()
lowest_subject = subject_averages.idxmin()

print(f"\nHighest Scoring Subject: {highest_subject}")
print(f"Lowest Scoring Subject: {lowest_subject}")

pass_percentage = (df["Grade"] != "Needs Improvement").mean() * 100
print(f"Pass Percentage: {pass_percentage:.2f}%")


# -----------------------------
# EXPORT TO EXCEL REPORT
# -----------------------------

with pd.ExcelWriter("Student_Performance_Report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Full Report", index=False)
    top_performers.to_excel(writer, sheet_name="Top Performers", index=False)
    subject_averages.to_frame(name="Average Marks").to_excel(writer, sheet_name="Subject Averages")

print("\nExcel report generated: Student_Performance_Report.xlsx")