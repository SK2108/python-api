"""Module providing requests"""
import requests

response = requests.get("https://fakestoreapi.com/products", timeout=5)
print(response)
print(response.text)
