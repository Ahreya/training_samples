import requests

from requests_folder.get_token import generate_token


def submit_order(bookid, customer_name):
    body_request = {
                  "bookId": bookid,
                  "customerName": customer_name
                   }
    token = generate_token()
    header_params = {'Authorisation': token}
    response = requests.post("https://simple-books-api.glitch.me/orders", json=body_request, headers=header_params)
    return response

