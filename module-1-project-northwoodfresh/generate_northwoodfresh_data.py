# Generate synthetic monthly sales data for NorthwoodFresh

import numpy as np
import pandas as pd

np.random.seed(42)

# Define base revenue for each region (in dollars)
REGIONS = {
    "Northeast": 520000,
    "Midwest": 510000,
    "West": 590000,
    "Southeast": {"first": 480000, "second": 370000},
}

# Define standard deviation for revenue generation
standard_deviation = 0.05  # 5% of the base revenue
# Define months
MONTHS = range(1, 13)

# Generate synthetic sales data
rows = []
for region, base_revenue in REGIONS.items():
    # Generate revenue for each month
    for month in MONTHS:
        # Determine the base revenue based on the region and month
        if isinstance(base_revenue, dict):  # Southeast: two-period structure
            base = base_revenue["first"] if month <= 6 else base_revenue["second"]
        else:
            base = base_revenue
        # Generate revenue using a normal distribution around the base revenue
        revenue = np.random.normal(loc=base, scale=standard_deviation * base)
        # Round revenue to two decimal places and ensure it's non-negative
        revenue = np.round(revenue, 2)
        revenue = np.maximum(revenue, 0)
        # Append the generated data to the rows list
        rows.append({"region": region, "month": month, "revenue": revenue})

# Create a DataFrame from the generated data
df = pd.DataFrame(rows)

# Save the DataFrame to a CSV file
output_path = "northwoodfresh_sales.csv"
df.to_csv(output_path, index=False)
print(f"\nDataset saved to {output_path}")