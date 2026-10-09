# Brainstorm: Skyline Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for
a small fictional online school client.

Task: Brainstorm analytical questions I should consider asking of the dataset
described below. I'm at the Define stage of the analytics lifecycle and need
a candidate list of questions before I start writing any code.

Context: The dataset is for Skyline Online Courses, a fictional online school.
100 rows, one row per student. Columns:

- enrollment_id: string, unique identifier per student (nominal)
- course_name: categorical, one of {Tableau Fundamentals, Python for Beginners, SQL Basics, Statistics 101, Introduction to Analytics} (nominal)
- enrollment_year: integer year between 2022 and 2025 inclusive (interval)
- final_grade: F, D, C, B, or A. Convert the letters to value. F=0, D=1, C=2, B=3, A=4 (ordinal)
- hours_studied: continuous, total hours the student has spent (ratio)
- completion_status: categorical, one of {Completed, Dropped, In Progress} (nominal)

The school is interested in understanding student behavior to inform
marketing and product decisions.

Constraints:
1. Only suggest questions that can be answered from the columns listed above.
   Don't invent additional columns.
2. For each suggested question, identify which columns would be used and
   what statistical method would be appropriate.
3. Make sure the statistical methods you propose are appropriate for the
   data type of each column (mean for ratio, mode for nominal, etc.).

Output Format: A numbered list of 8 to 12 analytical questions. For each:
- The question (one sentence)
- The columns involved
- The recommended statistical or visualization method

## Tool 1: Claude output

Here's a candidate list of 11 questions for Skyline Online Courses, ordered from descriptive to relational. With n = 100 across 5 courses (about 20 each) and 4 enrollment years, you have more room than in the 50-row version. Chi-square and ANOVA-type tests become more defensible, but cells are still small once you cross three variables, so I've kept nonparametric methods as the default and flagged where results are still exploratory.

**Two points about the 0-4 grade coding:**
- The letter-to-number mapping preserves order, but the gaps between levels aren't guaranteed to be equal. I use the median and mode as primary summaries and rank-based tests for comparisons. A GPA-style mean can be shown as a secondary, approximate figure.
- The schema doesn't say whether Dropped or In Progress students have a grade. Check for missing values early, since that affects Questions 4, 6, 7, and 10.

1. **How are students distributed across the five courses?**
   - Columns: `course_name`
   - Method: Frequency table and bar chart; mode as the measure of central tendency (nominal, so no mean or median).

2. **What share of students are Completed, Dropped, or In Progress?**
   - Columns: `completion_status`
   - Method: Frequency table with proportions and a bar chart; mode. Consider collapsing to Completed vs. Dropped for later tests, handling In Progress separately.

3. **How much time do students typically invest, and how skewed is it?**
   - Columns: `hours_studied`
   - Method: Histogram and boxplot; mean, median, SD, and IQR. Compare mean to median to gauge skew from heavy-study outliers.

4. **How are final grades distributed?**
   - Columns: `final_grade` (0-4)
   - Method: Ordered bar chart (F to A); median and mode as primary measures, with an approximate mean as secondary.

5. **Does the completion outcome differ by course?**
   - Columns: `course_name`, `completion_status`
   - Method: 100% stacked bar chart and cross-tabulation. Chi-square test of independence with Cramér's V as the effect size. Check that expected counts are at least 5 per cell (about 20 per course across 3 outcomes may still fall short); if not, use Fisher's exact test or collapse to Completed vs. Dropped.

6. **Do final grades differ by course?**
   - Columns: `course_name`, `final_grade`
   - Method: Boxplots or stacked bars of grade by course; median grade per course. Kruskal-Wallis test (suited to an ordinal outcome across 5 groups), with Dunn's post-hoc test if the omnibus result is significant.

7. **Do students who study more hours earn higher grades?**
   - Columns: `hours_studied`, `final_grade`
   - Method: Boxplots of hours by grade level, or a jittered scatterplot; Spearman rank correlation (one variable is ordinal, and the 0-4 scale has many ties).

8. **Do students who complete a course study more hours than those who drop?**
   - Columns: `hours_studied`, `completion_status`
   - Method: Boxplots by status; group medians and means. Mann-Whitney U for Completed vs. Dropped, or Kruskal-Wallis if In Progress is included. Hours may partly result from persisting, so this shows association, not cause.

9. **Does time investment differ by course?**
   - Columns: `course_name`, `hours_studied`
   - Method: Side-by-side boxplots; group means and medians. Kruskal-Wallis as the default; one-way ANOVA (or Welch's) is more defensible at about 20 per group if distributions look roughly normal.

10. **Are grades associated with completion status?**
    - Columns: `final_grade`, `completion_status`
    - Method: Boxplots of grade by status or a cross-tabulation; Kruskal-Wallis, or a chi-square/Fisher's exact test on a collapsed grade scale (e.g., A-B vs. C-F). First check how many non-completers have a recorded grade.

11. **Has enrollment volume, completion, or study time shifted across enrollment years?**
    - Columns: `enrollment_year`, `completion_status`, `hours_studied`, `course_name`
    - Method: Bar chart of enrollments per year (faceted by course); completion proportions by year; boxplots of hours by year; Spearman correlation between year and hours. Year is interval data, so differences between years are meaningful but ratios are not. Keep course-by-year views descriptive, since cells will be small.

**Scoping notes for the Define stage**

- **Sample size:** n = 100 supports single-variable comparisons reasonably well, but any breakdown by course × year × status will have tiny cells. Prioritize effect sizes and visualizations alongside p-values.
- **Exposure bias:** 2025 enrollees have had less time to study and finish than 2022 enrollees, and many may be In Progress. Year comparisons (Question 11) and any In Progress comparisons can be skewed by this.
- **Survivorship in grades:** If only completers have grades, grade-based questions (4, 6, 7, 10) describe completers only, not all students. State this scope explicitly.
- **Association, not causation:** Hours, grades, and completion move together, but the data can't show that studying more causes better outcomes.
- **Multiple comparisons:** With this many tests, consider adjusting (e.g., Holm or Benjamini-Hochberg) or designating a few primary questions up front.
- **Suggested priority:** Questions 5, 6, 7, and 8 map most directly to marketing and product decisions (which courses retain students, which underperform, and whether engagement tracks success).
- **Out of scope:** The data has no pricing, acquisition channel, demographics, or satisfaction measure, so channel effectiveness and satisfaction questions can't be answered here. Worth flagging to the client as a gap.

## Tool 2: Gemini output

Here is a list of targeted analytical questions aligned with Skyline Online Courses' goals, constrained strictly to the provided dataset and appropriate for each column's data type.

1. **Which course commands the highest average student study time?**
* **Columns Involved:** `course_name` (nominal), `hours_studied` (ratio)
* **Recommended Method:** Grouped mean / median calculation by course, visualized via a horizontal bar chart or box plot.


2. **What is the overall completion rate across all enrolled students, and which completion status is most common?**
* **Columns Involved:** `completion_status` (nominal)
* **Recommended Method:** Frequency distribution, mode, and percentage breakdown visualized via a pie chart or donut chart.


3. **Does total study time significantly correlate with a student's final grade?**
* **Columns Involved:** `hours_studied` (ratio), `final_grade` (ordinal numeric: 0–4)
* **Recommended Method:** Spearman rank correlation coefficient ($r_s$) and a scatter plot with a non-parametric trend line.


4. **How have course enrollment volumes shifted year-over-year from 2022 to 2025?**
* **Columns Involved:** `enrollment_year` (interval), `enrollment_id` (nominal / count)
* **Recommended Method:** Frequency counts per year, formatted as percentage change and visualized via a line chart or stacked column chart.


5. **Which course yields the highest proportion of students who drop out vs. complete?**
* **Columns Involved:** `course_name` (nominal), `completion_status` (nominal)
* **Recommended Method:** Two-way cross-tabulation (contingency table) with Chi-Square Test of Independence ($\chi^2$) and a 100% stacked bar chart.


6. **What is the distribution of final letter grades across the entire student population?**
* **Columns Involved:** `final_grade` (ordinal numeric: 0–4)
* **Recommended Method:** Median, Interquartile Range (IQR), and mode, visualized via a histogram or bar chart of grade frequencies.


7. **Do average final grades differ significantly depending on the course taken?**
* **Columns Involved:** `course_name` (nominal), `final_grade` (ordinal numeric: 0–4)
* **Recommended Method:** Kruskal-Wallis H Test (non-parametric ANOVA equivalent for ordinal outcomes), visualized using side-by-side box plots.


8. **How does the average hours spent differ between students who complete a course versus those who drop?**
* **Columns Involved:** `completion_status` (nominal), `hours_studied` (ratio)
* **Recommended Method:** Two-sample independent t-test (or Mann-Whitney U test) comparing the mean/median hours of "Completed" vs. "Dropped" groups, visualized using overlapping density plots.


9. **Which individual course accounts for the largest share of total course enrollments?**
* **Columns Involved:** `course_name` (nominal), `enrollment_id` (nominal / count)
* **Recommended Method:** Mode and frequency distribution, visualized via a Pareto chart or bar chart.

## Verification

1. How are students distributed across the five courses? (Both)
    ✓ Verified: passes all three checks; ready to use.

2. What share of students are Completed, Dropped, or In Progress? Which is most common? (Both)
    ✓ Verified: passes all three checks; ready to use.


3. How much time do students typically invest, and how skewed is it? (Claude)
    ✓ Verified: passes all three checks; ready to use.

4. How are final grades distributed? (Both)
    ✓ Verified: passes all three checks; ready to use.


5. Does the completion outcome differ by course? (Both)
    ✗ Hallucinated column or method: discard.

6. Do final grades differ by course? (Claude)
    ✓ Verified: passes all three checks; ready to use.


7. Do students who study more hours earn higher grades? (Both)
    ✓ Verified: passes all three checks; ready to use.


8. Do students who complete a course study more hours than those who drop? (Claude)
    ✓ Verified: passes all three checks; ready to use.


9. Does time investment differ by course? (Claude)
    ✓ Verified: passes all three checks; ready to use.


10. Are grades associated with completion status? (Claude)
    ✓ Verified: passes all three checks; ready to use.


11. Has enrollment volume, completion, or study time shifted across enrollment years? (Claude)
    ✓ Verified: passes all three checks; ready to use.

12. Which course commands the highest average student study time? (Gemini)
    ✓ Verified: passes all three checks; ready to use.

13. How have course enrollment volumes shifted year-over-year from 2022 to 2025?
    ✓ Verified: passes all three checks; ready to use.

14. Which course yields the highest proportion of students who drop out vs. complete?
    ✓ Verified: passes all three checks; ready to use.


## Verified question list

 Course performance
    How are final grades distributed? (Both)
    Do final grades differ by course? 
    Do students who complete a course study more hours than those who drop? 
    Are grades associated with completion status?
    Which course commands the highest average student study time?
    Which course yields the highest proportion of students who drop out vs. complete?
    Does time investment differ by course? 
 
 Student behavior
    How are students distributed across the five courses?
    Has enrollment volume, completion, or study time shifted across enrollment years?
    How much time do students typically invest, and how skewed is it?
    Do students who study more hours earn higher grades?
 
 Ccompletion patterns
    What share of students are Completed, Dropped, or In Progress? Which is most common?
    Does the completion outcome differ by course
 
 Time trends
    How have course enrollment volumes shifted year-over-year from 2022 to 2025?