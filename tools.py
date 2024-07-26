import requests

# Base URL of the API
base_url = 'http://localhost:5000/api'

def get_top_selling_products(start_date, end_date):
    url = f"{base_url}/sales/top-products"
    params = {'start_date': start_date, 'end_date': end_date}
    response = requests.get(url, params=params)
    return response.json()

def get_top_categories(start_date, end_date):
    url = f"{base_url}/sales/top-categories"
    params = {'start_date': start_date, 'end_date': end_date}
    response = requests.get(url, params=params)
    return response.json()

def get_sales_trends(start_date, end_date):
    url = f"{base_url}/sales/trends"
    params = {'start_date': start_date, 'end_date': end_date}
    response = requests.get(url, params=params)
    return response.json()

def get_revenue_by_category(start_date, end_date):
    url = f"{base_url}/sales/revenue-by-category"
    params = {'start_date': start_date, 'end_date': end_date}
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Top Selling Products:")
    print(get_top_selling_products('2023-04-01', '2023-06-30'))

    print("\nTop Categories:")
    print(get_top_categories('2023-04-01', '2023-06-30'))

    print("\nSales Trends:")
    print(get_sales_trends('2023-04-01', '2023-06-30'))

    print("\nRevenue by Category:")
    print(get_revenue_by_category('2023-04-01', '2023-06-30'))