# Sales Data Analysis

A retail **Sales Data Analysis** project built with **PostgreSQL, SQL,
Python, and Pandas**. The project processes a raw retail sales dataset
containing **500K+ records**, performs data cleaning, loads the usable
data into PostgreSQL, and provides a Python-based CLI application for
sales, customer, and product analytics.

## Project Overview

The project follows this workflow:

``` text
Raw Retail Sales Dataset
        │
        ▼
Data Cleaning
        │
        ├── Missing values
        ├── Duplicate records
        └── Inconsistent data
        │
        ▼
Cleaned Dataset
        │
        ▼
PostgreSQL Database
        │
        ▼
Python Analytics Application
        │
        ├── Data Overview
        ├── Sales Analytics
        ├── Customer Analytics
        ├── Product Analytics
        └── Report Export
        │
        ▼
CSV Reports
```

The cleaned PostgreSQL database currently contains **172,782 sales
records** available for analysis.

## Objectives

-   Clean and prepare a large retail sales dataset.
-   Store and manage cleaned data using PostgreSQL.
-   Analyze sales and revenue performance using SQL.
-   Analyze customer purchasing behavior.
-   Identify top-performing and low-demand products.
-   Analyze sales trends over time.
-   Build a reusable Python CLI analytics application.
-   Export analytical results into CSV reports.

## Tech Stack

  Technology   Purpose
  ------------ -------------------------------------------
  PostgreSQL   Database and SQL analysis
  Python       Application and analytics logic
  psycopg2     PostgreSQL database connectivity
  Pandas       Data processing and CSV report generation
  Tkinter      File-save dialog for report exports
  SQL          Data aggregation and analytical queries

## Database Structure

The PostgreSQL database contains the following main tables:

### `sales`

The primary transaction table.

  Column          Description
  --------------- -------------------------
  `sales_id`      Sales record identifier
  `invoiceno`     Invoice/order number
  `product_id`    Product identifier
  `description`   Product description
  `quantity`      Quantity sold
  `invoicedate`   Invoice date and time
  `unitprice`     Unit selling price
  `customerid`    Customer identifier
  `country`       Customer country
  `country_id`    Country identifier

### `product`

Product reference table.

  Column          Description
  --------------- ---------------------
  `product_id`    Product identifier
  `description`   Product description
  `unitprice`     Unit price

### `customer`

Customer reference table.

  Column          Description
  --------------- ---------------------
  `customer_id`   Customer identifier
  `country`       Customer country

### `country`

Country reference table.

  Column         Description
  -------------- --------------------
  `country_id`   Country identifier
  `country`      Country name

## Analytics Features

The Python CLI provides the following modules.

### 1. Data Overview

Provides:

-   Total sales records
-   Total customers
-   Total products
-   Dataset date range
-   Database connection management

Example output:

``` text
==== Data Overview ====

1. Total Sales Records
2. Total Customers
3. Total Products
4. Dataset Date Range
5. Close Database Connection
6. Back to Main Menu
```

The current cleaned database returns **172,782 sales records**.

### 2. Sales Analytics

The application provides:

-   Monthly revenue trends
-   Top 10 selling products
-   Country-wise revenue
-   Daily revenue analysis for a selected date range
-   Average order value

Revenue is calculated from:

``` sql
quantity * unitprice
```

Example monthly revenue analysis:

``` sql
SELECT
    DATE_TRUNC('month', invoicedate) AS month,
    SUM(quantity * unitprice) AS revenue
FROM sales
GROUP BY month
ORDER BY month;
```

### 3. Customer Analytics

The application provides:

-   Top customers by revenue
-   Customer order activity
-   Customer lifetime value
-   Country-wise customer distribution

Customer lifetime value is calculated using:

``` sql
SUM(quantity * unitprice)
```

Customer analysis also uses a JOIN between the sales and customer
tables.

### 4. Product Analytics

The application provides:

-   Best-performing products
-   Low-demand products
-   Product sales trends
-   Product revenue trends

Example:

``` sql
SELECT
    product_id,
    description,
    SUM(quantity) AS total
FROM sales
GROUP BY product_id, description
ORDER BY total DESC;
```

### 5. Report Export

The application can export analytical results as CSV files.

Available reports:

-   Monthly Revenue Report
-   Top Product Report
-   Detailed Sales Report

The reports are generated using **Pandas**.

Example output structure:

``` text
report.csv
```

## SQL Analysis

The project uses SQL for:

-   Aggregation
-   GROUP BY analysis
-   JOIN operations
-   Subqueries
-   Date-based analysis
-   Revenue calculations
-   Customer analysis
-   Product analysis

Examples of analytical metrics include:

``` text
Revenue = Quantity × Unit Price

Customer Lifetime Value = Sum of Customer Revenue

Average Order Value = Average Order Revenue
```

## Python Application Architecture

The application is separated into modules:

``` text
Sales Data Analysis/
│
├── main.py
├── Analytics.py
├── database.py
├── Sales.sql
└── README.md
```

### `main.py`

Controls the application flow and main menu.

``` text
Connect to Database
        │
        ▼
Main Menu
 ┌──────┼────────┬──────────┬──────────┐
 ▼      ▼        ▼          ▼          ▼
Data   Sales   Customer   Product    Export
```

### `database.py`

Handles the PostgreSQL connection and database operations using
`psycopg2`.

The database layer provides functions for:

-   Connecting to PostgreSQL
-   Executing SELECT queries
-   Fetching results
-   Executing database changes
-   Closing the connection

### `Analytics.py`

Contains the analytical functions for:

-   Data overview
-   Sales analytics
-   Customer analytics
-   Product analytics
-   CSV report generation

## Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd sales-data-analysis
```

### 2. Create a Python environment

Using Conda:

``` bash
conda create -n sales-analysis python=3.11
conda activate sales-analysis
```

Or using a standard Python virtual environment:

``` bash
python -m venv venv
```

### 3. Install dependencies

``` bash
pip install psycopg2-binary pandas
```

Tkinter is normally included with standard Python installations on
Windows.

## PostgreSQL Setup

Install PostgreSQL and pgAdmin.

Create a database, for example:

``` sql
CREATE DATABASE sales;
```

Then restore the provided `Sales.sql` dump into the database.

Using PostgreSQL command line:

``` bash
psql -U postgres -d sales -f Sales.sql
```

Or restore/open the SQL dump through pgAdmin.

The SQL dump contains the database schema and data for the project.

## Running the Application

Run:

``` bash
python main.py
```

The application asks for PostgreSQL credentials:

``` text
==== Connect to Retail Database ====

Enter database name: SALES
Enter user name: postgres
Enter password: ********
```

After a successful connection:

``` text
==== Retail Database Analytics ====

===== MAIN MENU =====
1. Data Overview
2. Sales Analytics
3. Customer Analytics
4. Product Analytics
5. Export Reports
6. Exit
```

## Example Workflow

### Step 1 --- Connect

Connect the Python application to the PostgreSQL database.

### Step 2 --- Check Data Overview

Review:

-   Number of sales records
-   Number of customers
-   Number of products
-   Date range

### Step 3 --- Analyze Sales

Use the Sales Analytics module to investigate:

-   Revenue trends
-   Top products
-   Country performance
-   Daily revenue
-   Average order value

### Step 4 --- Analyze Customers

Investigate:

-   Highest-value customers
-   Customer order activity
-   Customer lifetime value
-   Customer distribution by country

### Step 5 --- Analyze Products

Investigate:

-   Best-performing products
-   Low-demand products
-   Product sales trends
-   Product revenue trends

### Step 6 --- Export Reports

Export results to CSV for further analysis in Excel, Power BI, or other
reporting tools.

## Data Cleaning

The raw dataset contains **500K+ records/values**, with substantial
missing and inconsistent data.

The data preparation stage focuses on:

-   Handling missing values
-   Removing duplicate records
-   Addressing inconsistent data
-   Preparing usable records for PostgreSQL analysis

After cleaning, the PostgreSQL sales table contains **172,782 sales
records** used by the analytics application.

> Note: The exact cleaning rules and transformation scripts should be
> documented separately if this repository includes the original
> data-cleaning code.

## Key Business Questions

The project is designed to answer questions such as:

1.  How does revenue change over time?
2.  Which products have the highest sales volume?
3.  Which products generate the most revenue?
4.  Which countries generate the most revenue?
5.  Who are the highest-value customers?
6.  How many orders are associated with each customer?
7.  What is the average order value?
8.  Which products have relatively low demand?
9.  How do individual products perform over time?
10. How is the customer base distributed geographically?

## Project Highlights

-   Processed a **500K+ raw retail dataset**.
-   Cleaned missing, duplicate, and inconsistent records.
-   Loaded cleaned data into PostgreSQL.
-   Built a Python CLI analytics application.
-   Used SQL for business-oriented analysis.
-   Connected Python directly to PostgreSQL using `psycopg2`.
-   Used Pandas to generate CSV reports.
-   Created separate analytical modules for sales, customers, and
    products.

## Future Improvements

Possible extensions include:

-   Add SQL CTE-based analysis.
-   Add SQL window functions for ranking and running totals.
-   Add parameterized SQL queries for safer user input.
-   Add automated data-cleaning scripts to the repository.
-   Add query-performance benchmarking using `EXPLAIN ANALYZE`.
-   Add Power BI dashboard integration.
-   Add automated Excel report generation.
-   Add configuration through environment variables instead of entering
    database credentials.
-   Add logging and error handling.
-   Add unit tests for analytical functions.

## Security

Do **not** store PostgreSQL passwords directly in source code or commit
them to GitHub.

Use environment variables instead:

``` text
DB_NAME=SALES
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Also avoid uploading screenshots containing database credentials.

## Author

**Your Name**

Data Analyst \| SQL \| PostgreSQL \| Python \| Excel \| Power BI
