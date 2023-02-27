from requests_folder.submit_order import submit_order


class TestSubmitOrder:
    def test_submit_order(self):
        # apelam metoda submit si ii dam parametrii
        response = submit_order(1, "Alin Cernavoda")
        # s-a generat un rezultat care s-a salvat in response
        # verificam urmatoarele:
        # - order creation : True
        # - status code trebuie sa 201
        # - order id length > 0
        assert response.json()["created"] == True, f"Error: Order creation status is not correct. EXPECTED: True, ACTUAL:{response.json()['created']}"
        assert response.status_code == 201, f"ERROR: Status code is not valid. EXPECTED: 201, ACTUAL: {response.status_code}"
        assert len(response.json()["orderId"]) > 0, f"Error: Order ID is invalid. EXPECTED: length > 0, ACTUAL:{len(response.json()['orderId'])}"
