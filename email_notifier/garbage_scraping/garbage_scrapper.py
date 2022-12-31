import requests
from bs4 import BeautifulSoup


# TODO: add headers and cookies to requests
class GarbageScrapper:

    _NO_STREET_PAGE_URL = "https://ekosystem.wroc.pl/gospodarowanie-odpadami/harmonogram-wywozu-odpadow/"

    _NUMBERS_FOR_STREET_URL = "https://ekosystem.wroc.pl/wp-admin/admin-ajax.php"
    _NUMBERS_FOR_STREET_FORM_TEMPLATE = {
        "action": "waste_disposal_form_get_street_numbers",
        "id_ulicy": None
    }

    _WASTE_SCHEDULE_URL = "https://ekosystem.wroc.pl/wp-admin/admin-ajax.php"
    _WASTE_SCHEDULE_FORM_TEMPLATE = {
        "action": "waste_disposal_form_get_schedule_direct",
        "id_numeru": None,
        "id_ulicy": None
    }

    def _get_no_street_page(self) -> str:
        response_page = requests.get(self._NO_STREET_PAGE_URL).content
        return str(response_page)

    def _get_numbers_for_street_response(self, street_id: int) -> str:
        number_for_street_form = self._WASTE_SCHEDULE_FORM_TEMPLATE
        number_for_street_form["id_ulicy"] = street_id

        response_dict = requests.post(self._NUMBERS_FOR_STREET_URL, number_for_street_form).json()
        return response_dict

    def _get_waste_schedule_response(self, street_id: int, number_id: int) -> dict:
        waste_schedule_form = self._WASTE_SCHEDULE_FORM_TEMPLATE
        waste_schedule_form["id_numeru"] = number_id
        waste_schedule_form["id_ulicy"] = street_id

        response_dict = requests.post(self._WASTE_SCHEDULE_URL, waste_schedule_form).json()
        return response_dict

    def _get_street_id(self, street_name: str) -> int:
        pass

    def _get_number_id(self, number: str) -> int:
        pass

    def get_waste_schedule(self, street_name: str, street_number: str) -> dict:
        pass
