# Brainstorm: Crescent Bakery Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for
a small fictional bakery client.

Task: Brainstorm analytical questions I should consider asking of the dataset
described below. I'm at the Define stage of the analytics lifecycle and need
a candidate list of questions before I start writing any code.

Context: The dataset is for Crescent Bakery, a fictional regional bakery.
50 rows, one row per customer. Columns:

- customer_id: string, unique identifier per customer (nominal)
- region: categorical, one of {Downtown, North Side, South Side, West End} (nominal)
- first_visit_year: integer year between 2018 and 2025 inclusive (interval)
- satisfaction: integer 1 to 5, customer satisfaction rating (ordinal)
- total_spent_usd: continuous, total dollars the customer has spent (ratio)
- visits_last_year: integer, number of visits in the last year (ratio)

The bakery is interested in understanding customer behavior to inform
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

Here's a candidate list of 10 questions, ordered roughly from descriptive to relational. Given n = 50 (and only ~12 per region on average), I've leaned toward nonparametric methods and flagged where results should be treated as exploratory.

1. **How are customers distributed across the four regions?**
   - Columns: `region`
   - Method: Frequency table and bar chart; mode as the measure of central tendency (nominal data, so no mean or median).

2. **What does a typical customer's spending look like, and how skewed is it?**
   - Columns: `total_spent_usd`
   - Method: Histogram and boxplot; report mean, median, SD, and IQR. Compare mean to median to gauge skew from high-spend outliers.

3. **How satisfied are customers overall?**
   - Columns: `satisfaction`
   - Method: Frequency table and bar chart of the 1-5 ratings; report median and mode (ordinal, so avoid treating the mean as meaningful, or flag it as approximate if shown).

4. **Does total spending differ by region?**
   - Columns: `region`, `total_spent_usd`
   - Method: Side-by-side boxplots; group means and medians. Kruskal-Wallis test (or one-way ANOVA if the distributions look roughly normal), with the caveat of small group sizes.

5. **Does visit frequency differ by region?**
   - Columns: `region`, `visits_last_year`
   - Method: Boxplots by region; group means and medians. Kruskal-Wallis as the default test; use a Poisson-style view of counts if exploring further.

6. **Do customers who visit more often spend more?**
   - Columns: `visits_last_year`, `total_spent_usd`
   - Method: Scatterplot with a trend line; Pearson correlation if the relationship is linear, Spearman if skewed or outlier-driven. Consider total spend per visit as a derived metric, though note that total spend covers lifetime while visits cover only the last year, so interpret carefully.

7. **Is satisfaction associated with spending?**
   - Columns: `satisfaction`, `total_spent_usd`
   - Method: Boxplots of spending by satisfaction level; Spearman rank correlation (appropriate because one variable is ordinal).

8. **Is satisfaction associated with visit frequency?**
   - Columns: `satisfaction`, `visits_last_year`
   - Method: Boxplots of visits by satisfaction level; Spearman rank correlation.

9. **Does satisfaction vary by region?**
   - Columns: `region`, `satisfaction`
   - Method: Stacked bar chart of rating proportions by region; median satisfaction per region. Chi-square test of independence is likely unreliable here because of sparse cells (n = 50 across 4 × 5 categories), so use Fisher's exact test or collapse ratings (e.g., 1-3 vs. 4-5) and treat results as exploratory.

10. **Do longer-tenured customers differ in spending, visits, or satisfaction from newer ones?**
    - Columns: `first_visit_year`, `total_spent_usd`, `visits_last_year`, `satisfaction`
    - Method: Scatterplots or boxplots by cohort (e.g., group years into 2018-2020, 2021-2022, 2023-2025); Spearman correlations with `first_visit_year`. Since the year is interval data, differences between years are meaningful, but ratios (e.g., "twice as recent") are not. Note that total spend naturally accumulates with tenure, so this partly reflects time as a customer.

11. **How are customers distributed across acquisition cohorts, and did acquisition trend by region?**
    - Columns: `first_visit_year`, `region`
    - Method: Bar chart of new customers per year; cross-tabulation or faceted bars of year by region. Descriptive only, because counts per cell will be very small.

12. **Are there distinct customer segments (e.g., high-spend/high-frequency vs. low-spend/low-frequency)?**
    - Columns: `total_spent_usd`, `visits_last_year` (optionally `satisfaction`)
    - Method: Scatterplot with quartile-based or k-means grouping (standardize variables first); profile segments by region and satisfaction afterward. Exploratory, since 50 points won't support stable clusters.

**Scoping notes for the Define stage**

- **Sample size:** With 50 customers, treat all inferential results as directional. Effect sizes and visualizations will be more informative than p-values.
- **Time mismatch:** `total_spent_usd` is cumulative over the customer's lifetime, while `visits_last_year` is a one-year window. Questions combining them (6, 10) need that caveat stated upfront.
- **Measurement levels:** Keep the nominal/ordinal/interval/ratio distinction in your documentation. It drives which summaries (mode, median, mean) and tests you can defend.
- **Suggested priority:** Questions 4, 6, 7, and 12 are the most directly tied to marketing and product decisions (where to focus, whether loyalty drives spend, whether satisfaction matters commercially, and who to target).
- **Out of scope:** The data has no product, time-of-day, or purchase-level detail, so product-mix questions can't be answered from this dataset. You may want to flag that to the client as a gap.

## Tool 2: Gemini output

Here is a candidate list of 10 analytical questions designed for the Define stage, tailored specifically to the schema of Crescent Bakery's 50-customer dataset.

1. **Which regions generate the highest average customer spend?**
* **Columns involved:** `region`, `total_spent_usd`
* **Recommended method:** Grouped summary statistics (mean, median) per region and a bar chart comparison (or a One-Way ANOVA / Kruskal-Wallis test if checking for statistical significance across region groups).


2. **Is there a relationship between customer satisfaction ratings and total spend?**
* **Columns involved:** `satisfaction`, `total_spent_usd`
* **Recommended method:** Spearman rank correlation coefficient (since `satisfaction` is ordinal) and a grouped boxplot or scatter plot showing spend distributions across satisfaction levels 1 through 5.


3. **How is overall customer satisfaction distributed across the customer base?**
* **Columns involved:** `satisfaction`
* **Recommended method:** Frequency distribution table, median, mode, interquartile range (IQR), and a bar chart or bar histogram of ratings.


4. **Do long-tenured customers visit the bakery more frequently than newer customers?**
* **Columns involved:** `first_visit_year`, `visits_last_year`
* **Recommended method:** Grouped summary statistics (mean/median visits by `first_visit_year`) and Spearman rank correlation or a line plot of median visits across cohort years.


5. **Which bakery region has the largest share of the customer base?**
* **Columns involved:** `region`
* **Recommended method:** Frequency counts, mode, percentage breakdown, and a bar plot.


6. **Are frequent visitors higher-spending customers overall?**
* **Columns involved:** `visits_last_year`, `total_spent_usd`
* **Recommended method:** Pearson correlation coefficient (both are ratio variables) and a scatter plot with an estimated linear trend line.


7. **What is the average spend per visit across different regions?**
* **Columns involved:** `region`, `total_spent_usd`, `visits_last_year`
* **Recommended method:** Computed metric calculation ($\frac{\text{total\_spent\_usd}}{\text{visits\_last\_year}}$ per customer), followed by region-level mean/median comparison and a bar chart.


8. **How does customer satisfaction vary across geographical regions?**
* **Columns involved:** `region`, `satisfaction`
* **Recommended method:** Cross-tabulation (contingency table) with cell percentages, group medians/modes per region, and a stacked bar chart or grouped boxplot.


9. **Has customer acquisition (first visit year) changed over time from 2018 to 2025?**
* **Columns involved:** `first_visit_year`
* **Recommended method:** Annual frequency count, percentage distribution, and a time-series line chart or column chart showing cohort size by year.


10. **Do earlier customer cohorts (2018–2020) have higher total lifetime spend compared to recent cohorts (2024–2025)?**
* **Columns involved:** `first_visit_year`, `total_spent_usd`
* **Recommended method:** Summary statistics (mean, median, standard deviation) grouped by tenure cohort year, supplemented by a boxplot across tenure years.

## Verification

1.  How are customers distributed across the four regions? (Both)
    Columns: `region`
    ✓ Verified: passes all three checks; ready to use.

2.  What does a typical customer's spending look like, and how skewed is it? (Claude)
    Columns: `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

3.  How satisfied are customers overall? (Claude)
    Columns: `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

4.  Does total spending differ by region? (Claude)
    Columns: `region`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

5.  Does visit frequency differ by region? (Claude)
    Columns: `region`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

6.  Do customers who visit more often spend more? (Both)
    Columns: `visits_last_year`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

7.  Is satisfaction associated with spending? (Both)
    Columns: `satisfaction`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

8.  Is satisfaction associated with visit frequency? (Claude)
    Columns: `satisfaction`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

9.  Does satisfaction vary by region? (Both)
    Columns: `region`, `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

10. Do longer-tenured customers differ in spending, visits, or satisfaction from newer ones? (Both)
    Columns: `first_visit_year`, `total_spent_usd`, `visits_last_year`, `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

11. How are customers distributed across acquisition cohorts, and did acquisition trend by region?
    Columns: `first_visit_year`, `region`
    ✓ Verified: passes all three checks; ready to use.

12. Are there distinct customer segments (e.g., high-spend/high-frequency vs. low-spend/low-frequency)?
    Columns: `total_spent_usd`, `visits_last_year` (optionally `satisfaction`)
    ✓ Verified: passes all three checks; ready to use.

13. Which regions generate the highest average customer spend? (Gemini)
    Columns: `region`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

14. What is the average spend per visit across different regions? (Gemini)
    Columns: `region`, `total_spent_usd`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

15. Has customer acquisition (first visit year) changed over time from 2018 to 2025? (Gemini)
    Columns: `first_visit_year`
    ✓ Verified: passes all three checks; ready to use.

16. Do earlier customer cohorts (2018–2020) have higher total lifetime spend compared to recent cohorts (2024–2025)? (Both)
    Columns: `first_visit_year`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

## Verified question list

1.  How are customers distributed across the four regions? (Both)
    Columns: `region`
    ✓ Verified: passes all three checks; ready to use.

2.  What does a typical customer's spending look like, and how skewed is it? (Claude)
    Columns: `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

3.  How satisfied are customers overall? (Claude)
    Columns: `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

4.  Does total spending differ by region? (Claude)
    Columns: `region`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

5.  Does visit frequency differ by region? (Claude)
    Columns: `region`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

6.  Do customers who visit more often spend more? (Both)
    Columns: `visits_last_year`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

7.  Is satisfaction associated with spending? (Both)
    Columns: `satisfaction`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

8.  Is satisfaction associated with visit frequency? (Claude)
    Columns: `satisfaction`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

9.  Does satisfaction vary by region? (Both)
    Columns: `region`, `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

10. Do longer-tenured customers differ in spending, visits, or satisfaction from newer ones? (Both)
    Columns: `first_visit_year`, `total_spent_usd`, `visits_last_year`, `satisfaction`
    ✓ Verified: passes all three checks; ready to use.

11. How are customers distributed across acquisition cohorts, and did acquisition trend by region?
    Columns: `first_visit_year`, `region`
    ✓ Verified: passes all three checks; ready to use.

12. Are there distinct customer segments (e.g., high-spend/high-frequency vs. low-spend/low-frequency)?
    Columns: `total_spent_usd`, `visits_last_year` (optionally `satisfaction`)
    ✓ Verified: passes all three checks; ready to use.

13. Which regions generate the highest average customer spend? (Gemini)
    Columns: `region`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.

14. What is the average spend per visit across different regions? (Gemini)
    Columns: `region`, `total_spent_usd`, `visits_last_year`
    ✓ Verified: passes all three checks; ready to use.

15. Has customer acquisition (first visit year) changed over time from 2018 to 2025? (Gemini)
    Columns: `first_visit_year`
    ✓ Verified: passes all three checks; ready to use.

16. Do earlier customer cohorts (2018–2020) have higher total lifetime spend compared to recent cohorts (2024–2025)? (Both)
    Columns: `first_visit_year`, `total_spent_usd`
    ✓ Verified: passes all three checks; ready to use.