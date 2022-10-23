import requests

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

    def __init__(self) -> None:
        pass

    def get_no_street_page(self) -> str:
        response_page = requests.get(self._NO_STREET_PAGE_URL).content
        return response_page

    def get_numbers_for_street_response(self, street_id: int) -> str:
        number_for_street_form = self._WASTE_SCHEDULE_FORM_TEMPLATE
        number_for_street_form["id_ulicy"] = street_id

        response_dict = requests.post(self._NUMBERS_FOR_STREET_URL, number_for_street_form).json()
        return response_dict

    def get_waste_schedule_response(self, street_id: int, number_id: int) -> dict:
        waste_schedule_form = self._WASTE_SCHEDULE_FORM_TEMPLATE
        waste_schedule_form["id_numeru"] = number_id
        waste_schedule_form["id_ulicy"] = street_id

        response_dict = requests.post(self._WASTE_SCHEDULE_URL, waste_schedule_form).json()
        return response_dict


# garbageScrapper = GarbageScrapper()
# print(garbageScrapper.get_no_street_page())
# print(garbageScrapper.get_numbers_for_street_response(1791))
# print(garbageScrapper.get_waste_schedule_response(1791,45429))