# generate_skyline_data.py
# Lesson 1.2: Types of Data and Where to Find It
# Author: John Ko
# Date: 10/05/26
#
# Generates a synthetic dataset of 100 fictional Skyline Tower enrollments
# illustrating the four scales of measurement (nominal, ordinal, interval,
# ratio). Saves the result as skyline_enrollments.csv.

import random
import numpy as np
import pandas as pd
from datetime import date

random.seed(123)
np.random.seed(123)

n_enrollments = 100

# Enrollment ID (nominal: numerical-looking labels with no order)
enrollment_ids = [f"ENR-{random.randint(100000, 999999)}" for _ in range(n_enrollments)]

# Course Name (nominal scale: categorical with no order)
course_names = np.random.choice(
    ["Introduction to Analytics", "Python for Beginners", "SQL Basics", "Tableau Fundamentals", "Statistics 101"],
    size=n_enrollments,
    p=[0.20, 0.20, 0.20, 0.20, 0.20],
)

# Completion Status (nominal scale: categorical with no order)
completion_status = np.random.choice(
    ["Completed", "In Progress", "Dropped"],
    size=n_enrollments,
    p=[0.50, 0.30, 0.20],
)

# Enrollment Year (interval scale: ordered with equal gaps, no true zero)
enrollment_year = np.random.randint(2022, 2026, size=n_enrollments)

# Final Grade (ordinal scale: ordered categories with unequal gaps)
final_grade = np.random.choice(
    ["F", "D", "C", "B", "A"],
    size=n_enrollments,
    p=[0.05, 0.10, 0.30, 0.35, 0.20],
)

# Total hours spent studying (ratio scale: ordered, equal gaps, true zero)
hours_studied = np.random.normal(loc=30, scale=15, size=n_enrollments)
hours_studied = np.round(hours_studied, 2)
hours_studied = np.maximum(hours_studied, 0)

skyline_enrollments = pd.DataFrame({
    "enrollment_id": enrollment_ids,
    "course_name": course_names,
    "enrollment_year": enrollment_year,
    "final_grade": final_grade,
    "hours_studied": hours_studied,
    "completion_status": completion_status,
})

print(skyline_enrollments.head(10))
print(f"\nShape: {skyline_enrollments.shape}")
print(f"\nColumn types:\n{skyline_enrollments.dtypes}")

output_path = "skyline_enrollments.csv"
skyline_enrollments.to_csv(output_path, index=False)
print(f"\nDataset saved to {output_path}")