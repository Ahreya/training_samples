from requests_folder.get_all_books import get_all_books


class Test_Get_Books:
    def test_get_all_books_no_filter_check_response_status(self):
        response = get_all_books()
        assert response.status_code == 200, f"ERROR: status code is not correcr. Expected: 200, Actual: {response.status_code}"

    def test_get_all_books_no_filter_check_number_of_results(self):
        response = get_all_books()
        assert len(response.json()) == 6, f"EXPECTED: 6, ACTUAL: {len(response.json())}"

    def test_get_all_books_filter_non_fiction(self):
        response = get_all_books(type="non-fiction").json()
        assert len(response) == 2, f"ERROR, EXPECTED: 2, ACTUAL:{len(response)}"
        for i in range(len(response)):
            assert response[i]["type"] == "non-fiction", f"ERROR: EXPECTED: non-fiction, ACTUAL:{response[i]['type']}"

