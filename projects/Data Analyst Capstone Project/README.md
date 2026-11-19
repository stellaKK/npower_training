# Data Analyst Capstone Project: Developer Technology Trends

Capstone project for the **IBM Data Analyst Professional Certificate**, completed during the **NPower Canada AI & Data Analytics** program (2026).

**Live dashboard:** [View the interactive dashboard in Google Data Studio](https://datastudio.google.com/s/qBfhstIqbfc)
Note: You need to login to a Google account.

## Overview

This project looks at which technology skills developers use today and which ones they want to learn next. It is written for a business audience: leadership, HR, and learning and development teams who need to plan training and hiring.

Questions answered:
- Which programming languages are most in demand?
- Which databases are most used and most wanted?
- Which development tools (IDEs) are most popular?
- How do pay and work arrangements (remote, hybrid, in-person) vary?

## Data

- **2024 Stack Overflow Developer Survey** (main dataset)
- A job-postings dataset (postings by US city)
- A table of average salaries by programming language (IBM Skills Network course dataset)

## Tools

- **Python (Pandas)** in **Jupyter Notebook**: data cleaning and analysis (the cleaning steps were later saved as a single Python script)
- **Matplotlib** and **Seaborn**: charts for the analysis
- **Google Data Studio** (called Looker Studio until April 2026): 3-page interactive dashboard

The report uses charts from both Python and the dashboard, so the chart styles in it look different.

## What I Did

1. **Collected data** from the survey CSV and the other sources above.
2. **Cleaned the data**: removed duplicates, handled missing values (filled with mean or median, or dropped rows), standardized country names, and shortened long labels.
3. **Reshaped multi-answer fields**: survey answers like "JavaScript;SQL;Python" were split into separate values, then counted to get the top 10 languages, databases, platforms, and web frameworks, for both "used now" and "want to use next year". See [`data_cleaning.py`](data_cleaning.py).
4. **Analyzed the data with Matplotlib and Seaborn**: salary distributions by age and experience, work-arrangement counts, and comparisons across the top 5 countries.
5. **Built the dashboard** with three pages:
   - **Current Technology Usage**: top 10 languages, databases, platforms, and web frameworks in use
   - **Future Technology Trends**: top 10 of each that developers want to use next year
   - **Demographics**: respondents by age, country, and education level
6. **Wrote a report** with findings and recommendations for the business audience.

## Key Findings

- **Languages:** JavaScript, SQL, HTML/CSS, and TypeScript are the top 4 in both current use and future interest. Go and Rust enter the "want to use" top 10. PHP and PowerShell drop out of it.
- **Databases:** PostgreSQL is #1 for both current use and future interest. Redis moves from 6th to 2nd on the wish list. Supabase enters the top 10 and Oracle drops out.
- **Tools:** Visual Studio Code is the most popular development tool (30.3%).
- **Work arrangements:** Hybrid (23,015 respondents) and remote (20,831) are both far more popular than in-person (10,960).
- **Pay:** Median pay rises from about $60k (USD) for ages 25-34 to nearly $100k for ages 45-54. It grows fastest in the first 10-15 years of experience, then levels off around 20 years.
- **Demographics:** Most respondents are 25-34 years old (41.3%), and a bachelor's degree is the most common education level.

**Recommendations:** focus training on JavaScript, TypeScript, SQL, Python, and PostgreSQL; test Go, Rust, and Redis with small pilot projects; and offer hybrid or remote options to attract developers.

**Limitation:** survey interest shows what developers want to learn. It does not guarantee future hiring demand.

