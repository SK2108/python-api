"""Module providing requests"""
import requests


def get_products():
    """Create your function"""
    url = "https://fakestoreapi.com/products"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            products = response.json()
            return products
    except requests.exceptions.RequestException as e:
        print('Your request has failed:', e)
        return None


def main():
    """The main function"""
    products = get_products()

    if products:
        print(products)
    else:
        print('Failed to get products from the API.')


if __name__ == '__main__':
    main()
