from flask import Flask, request, jsonify
import mysql.connector
from decimal import Decimal
from flask.json import JSONEncoder
import os

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Read MySQL configuration from environment variables
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_database = os.environ.get('MYSQL_DATABASE')
mysql_host = os.environ.get('MYSQL_HOST', 'localhost')

# MySQL database connection configuration
db_config = {
    'user': 'root',
    'password': mysql_password,
    'host': mysql_host,
    'database': mysql_database
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/sales/top-products', methods=['GET'])
def top_selling_products():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = """
        SELECT p.product_id, p.name, SUM(o.quantity) AS total_quantity_sold, SUM(o.total_amount) AS total_revenue
        FROM products p
        JOIN orders o ON p.product_id = o.product_id
        WHERE o.order_date BETWEEN %s AND %s
        GROUP BY p.product_id, p.name
        ORDER BY total_quantity_sold DESC;
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(results)

@app.route('/api/sales/top-categories', methods=['GET'])
def top_categories():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = """
        SELECT c.category_id, c.name, SUM(o.quantity) AS total_quantity_sold, SUM(o.total_amount) AS total_revenue
        FROM categories c
        JOIN products p ON c.category_id = p.category_id
        JOIN orders o ON p.product_id = o.product_id
        WHERE o.order_date BETWEEN %s AND %s
        GROUP BY c.category_id, c.name
        ORDER BY total_quantity_sold DESC;
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(results)

@app.route('/api/sales/trends', methods=['GET'])
def sales_trends():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = """
        SELECT DATE(o.order_date) AS date, SUM(o.total_amount) AS total_revenue
        FROM orders o
        WHERE o.order_date BETWEEN %s AND %s
        GROUP BY DATE(o.order_date)
        ORDER BY DATE(o.order_date);
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(results)

@app.route('/api/sales/revenue-by-category', methods=['GET'])
def revenue_by_category():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = """
        SELECT c.category_id, c.name, SUM(o.total_amount) AS total_revenue
        FROM categories c
        JOIN products p ON c.category_id = p.category_id
        JOIN orders o ON p.product_id = o.product_id
        WHERE o.order_date BETWEEN %s AND %s
        GROUP BY c.category_id, c.name
        ORDER BY total_revenue DESC;
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)