# Day 2 - Student Data Analysis Notes

# Objective
Practice Python data handling and introduce Pandas for data analysis.

# What I Learned
- How to create a dataset using a list of dictionaries
- How to convert data into a Pandas DataFrame using `pd.DataFrame()`
- How to filter rows using conditions, e.g. `df[df["Marks"] > 70]`
- How to calculate statistics using `.mean()`, `.idxmax()`, `.idxmin()`
- How to use `.loc[]` to retrieve a specific row by index

# Key Pandas Methods Used
| Method | Purpose |
|---|---|
| `pd.DataFrame()` | Convert list of dictionaries into a table |
| `df["Marks"] > 70` | Create a boolean filter |
| `.mean()` | Calculate average of a column |
| `.idxmax()` / `.idxmin()` | Find index of highest/lowest value |
| `.loc[]` | Retrieve a row using its index |
| `len(df)` | Count total number of rows |

# Result Summary
- Average Marks: 73.30
- Top Student: Zara (95 marks)
- Lowest Scoring Student: Hamza (45 marks)
- Total Students: 10