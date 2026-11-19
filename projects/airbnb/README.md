# Toronto Airbnb Rental Market Analysis

An analysis of Toronto Airbnb listings: data cleaning in Python, an interactive Power BI dashboard, and regression models that predict nightly price.

## Data

- **Source:** [Inside Airbnb](https://insideairbnb.com/get-the-data/), Toronto summary listings file (`listings.csv`)
- **Snapshot:** July 2026. Each row is one listing as it appeared on the date the data was collected. The file is a snapshot, not one month of activity.
- **Size:** 22,256 listings, 19 columns (neighbourhood, room type, price, minimum nights, reviews, availability, host listing count, license, and more)

## Tools

- **Python (Pandas, NumPy)** in **Jupyter Notebook**: data cleaning and preparation
- **Matplotlib** and **Seaborn**: charts for exploring the data and checking models
- **SciPy**: ANOVA tests
- **scikit-learn**: linear and polynomial regression models
- **Power BI**: interactive dashboard

## What I Did

### 1. Data cleaning ([`toronto_airbnb_summary_analysis.ipynb`](toronto_airbnb_summary_analysis.ipynb))
- Checked the share of missing values in each column (price was 21% missing, license 46%)
- Dropped an empty column (`neighbourhood_group`) and checked for duplicate listings (none found)
- Filled missing prices with the median price for the same room type and neighbourhood, and used the overall median if a group had no prices
- Filled missing review rates and host listing counts with 0
- Turned the license text into a simple licensed / not licensed flag (1 / 0)
- Exported a clean CSV for the dashboard

### 2. Dashboard ([`airbnb-dashboard.pdf`](airbnb-dashboard.pdf))
Built a multi-page Power BI dashboard with filters for room type and neighbourhood. It covers:
- Key numbers: total listings, average and median price, average monthly reviews
- Price by neighbourhood, room type, and minimum-stay rule
- A map of listings by room type and price
- Reviews by neighbourhood, room type, and host
- Single-listing hosts vs. multi-listing hosts
- Licensed vs. unlicensed listings
- Year-round, seasonal, and short-term availability

### 3. Price prediction model ([`toronto_airbnb_summary_model.ipynb`](toronto_airbnb_summary_model.ipynb))
- Removed listings with no price (17,592 listings left) and split the data 80% training / 20% testing
- Used one-way ANOVA tests to confirm that neighbourhood and room type both have a significant effect on price (p < 0.001)
- Turned neighbourhood and room type into numbers using the average training price for each group
- Applied a log transform to skewed columns (price, minimum nights, reviews, availability, host listing count)
- Compared linear regression with polynomial regression (degrees 3, 4, and 5) using R² and mean squared error

## Key Findings

**Market**
- 22,256 listings. Average price is $250 per night and median price is $184.
- 68% of listings are entire homes or apartments and 31% are private rooms. Hotel and shared rooms are under 1%.
- Hotel rooms have the highest average price ($473), followed by entire homes ($312). Private and shared rooms average $115-$123.
- Bridle Path-Sunnybrook-York Mills has the highest average price ($651). Waterfront Communities-The Island has by far the most reviews (145K).
- Most listings require a minimum stay of 7 nights or more. Listings that allow short stays (1-6 nights) have higher average prices.
- 54% of listings belong to hosts with only one property. 19% belong to hosts with 5 or more.
- 54% of listings show a license number and 46% do not.

**Model**

| Model | R² (train) | R² (test) | MSE (test, log price) |
|-------|-----------|-----------|----------------------|
| Linear regression | 0.60 | 0.58 | 0.305 |
| Polynomial, degree 3 | 0.65 | **0.63** | **0.269** |
| Polynomial, degree 4 | 0.67 | -144.37 | 105.60 |
| Polynomial, degree 5 | 0.68 | -1460.05 | 1061.36 |

- **Polynomial regression of degree 3 performed best.** It explains about 63% of the variation in (log) price on unseen data.
- Degrees 4 and 5 fit the training data slightly better but failed on the test data. This is a clear case of overfitting.

## Limitations

- The data is one snapshot (July 2026), so it can't show seasonal or month-to-month trends.
- About 21% of prices were missing. The dashboard fills them with group medians, so its price numbers are partly estimates.
- The model uses only the columns in the summary file. Details like number of bedrooms or amenities are not included, which limits how well it can predict price.

