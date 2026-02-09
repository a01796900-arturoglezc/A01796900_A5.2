"""
Compute total sales from a price catalogue and a sales record.

Results are printed on screen and written to SalesResults.txt
"""

import json
import sys
import time


def load_json_file(filename):
    """
    Loads a JSON file and returns its content.

    :param filename: JSON file name
    :return: Parsed JSON data
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON.")
        sys.exit(1)


def build_price_catalogue(products):
    """
    Builds a dictionary with product names as keys and prices as values.

    :param products: List of product dictionaries
    :return: Dictionary {product_name: price}
    """
    catalogue = {}

    for product in products:
        try:
            name = product["title"]
            price = float(product["price"])
            catalogue[name] = price
        except (KeyError, ValueError, TypeError):
            print(f"Invalid product entry skipped: {product}")

    return catalogue


def compute_total_sales(catalogue, sales):
    """
    Computes the total sales cost.

    :param catalogue: Dictionary of product prices
    :param sales: List of sales records
    :return: Total cost
    """
    total = 0.0

    for sale in sales:
        try:
            product_name = sale["Product"]
            quantity = int(sale["Quantity"])

            if product_name not in catalogue:
                print(f"Product not found in catalogue: {product_name}")
                continue

            total += catalogue[product_name] * quantity

        except (KeyError, ValueError, TypeError):
            print(f"Invalid sale entry skipped: {sale}")

    return total


def write_results(total, elapsed_time):
    """
    Writes the results to SalesResults.txt.

    :param total: Total sales amount
    :param elapsed_time: Execution time
    """
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write("SALES RESULTS\n")
        file.write("====================\n")
        file.write(f"Total Sales: {total:.2f}\n")
        file.write(f"Execution Time (seconds): {elapsed_time}\n")


def main():
    """
    Main execution function.
    """
    if len(sys.argv) != 3:
        print(
                "Usage: python compute_sales.py "
                "priceCatalogue.json salesRecord.json"
            )

        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    products = load_json_file(price_file)
    sales = load_json_file(sales_file)

    catalogue = build_price_catalogue(products)
    total_sales = compute_total_sales(catalogue, sales)

    elapsed_time = time.time() - start_time

    print("SALES RESULTS")
    print("====================")
    print(f"Total Sales: {total_sales:.2f}")
    print(f"Execution Time (seconds): {elapsed_time}")

    write_results(total_sales, elapsed_time)


if __name__ == "__main__":
    main()
