# Retail Database Analytics

A command-line tool for analyzing retail sales data stored in PostgreSQL. Explore sales trends, customer insights, product performance, and export analytics reports with ease.

## Features

- **Data Overview** - View total sales records, customers, products, and dataset date range
- **Sales Analytics** - Analyze monthly revenue trends, top-selling products, country-wise revenue, daily running revenue, and average order value
- **Customer Analytics** - Identify top customers, track repeat vs new customers, calculate customer lifetime value, and view customer distribution by country
- **Product Analytics** - Discover best and low-performing products, analyze product sales and revenue trends
- **Export Reports** - Generate and download CSV reports for monthly revenue, top products, and detailed sales data

## Requirements

- Python 3.7+
- PostgreSQL database
- Required packages: `psycopg2`, `pandas`

## Installation

1. **Clone or download the project**
   ```bash
   git clone <your-repo-url>
   cd retail-analytics
   ```

2. **Install dependencies**
   ```bash
   pip install psycopg2-binary pandas
   ```

3. **Set up your PostgreSQL database**
   Ensure you have a PostgreSQL database with the following tables:
   - `sales` - Contains transaction records with fields: invoiceno, invoicedate, product_id, customerid, quantity, unitprice, country, description
   - `customer` - Contains customer information with fields: customer_id, country
   - `product` - Contains product information with fields: product_id, description

## Quick Start

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Connect to your database**
   When prompted, enter:
   - Database name
   - Database user
   - Database password

3. **Navigate the menu**
   ```
   ==== Retail Database Analytics ====
   1. Data Overview
   2. Sales Analytics
   3. Customer Analytics
   4. Product Analytics
   5. Export Reports
   6. Exit
   ```

## Usage Examples

### View Data Overview
- Check total sales records, customers, and products
- See the date range of your dataset

### Analyze Sales
- View monthly revenue trends
- Find top 10 best-selling products
- Analyze revenue by country
- Get average order value

### Export a Report
- Export monthly revenue as CSV
- Export top products list
- Export complete sales report with all transaction details

## File Structure

- `main.py` - Entry point and main menu logic
- `database.py` - PostgreSQL database connection and query handler
- `Analytics.py` - Analytics functions and export functionality

## Notes

- Date inputs in Daily Running Revenue should be in `YYYY-MM-DD` format
- CSV exports use a file dialog for saving location
- All analytics are performed directly on the database for optimal performance with large datasets

## Support

For issues or questions, please open an issue on the repository.
