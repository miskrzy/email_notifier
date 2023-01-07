from __future__ import annotations
import os
import requests
import sys
from typing import List, Tuple

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_logging import EmailLogger


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
        "action": "waste_disposal_form_get_schedule",
        "id_numeru": None
    }

    def __init__(self, streets_numbers: List[Tuple[str]], logger: EmailLogger) -> None:
        self._logger = logger
        self._streets_numbers = streets_numbers
        self._number_for_a_street = dict(self._streets_numbers)
        self._streets = [street_number[0] for street_number in self._streets_numbers]

    def retrieve_streets(self) -> GarbageScrapper:
        self._logger.info("Starting of streets retrieval")
        try:
            self._logger.debug(f"Retrieveing main page with url: {self._NO_STREET_PAGE_URL}")
            main_page = str(requests.get(self._NO_STREET_PAGE_URL).content)
            self._logger.info("Sucessfully retrieved the main garbage page")
        except Exception as e:
            self._logger.error(f"Error while retrieving the main garbage page: {e}")
            raise e

        try:
            soup = BeautifulSoup(main_page, 'html.parser')
            select_tag = soup.find('select', class_='waste-disposal-form__input waste-disposal-form__input--first')
            option_tags = select_tag.find_all('option')
            self._streets_ids = {option_tag.text: int(option_tag.get('value')) for option_tag in option_tags if (option_tag.get('value') is not None) and (option_tag.text in self._streets)}
            self._logger.info("Successfully retrieved ids for all streets")
            self._logger.debug("Retrieved streets and ids: {self._streets_ids}")
        except Exception as e:
            self._logger.error(f"Error while retrieving ids for street names: {e}")
            raise e
        return self
        
    def retrieve_numbers(self) -> GarbageScrapper:
        self._logger.info("Starting of numbers for streets retrieval")
        if not hasattr(self, '_streets_ids'):
            err = "No streets were retrieved yet. Try calling retrieve_streets() first"
            self._logger.error(err)
            raise Exception(err)

        self._streets_numbers_ids = {}
        for street, street_id in self._streets_ids.items():
            number = self._number_for_a_street[street]
            number_for_street_form = self._NUMBERS_FOR_STREET_FORM_TEMPLATE
            number_for_street_form["id_ulicy"] = street_id
            try:
                self._logger.debug(f"Retrieveing main page with url: {self._NUMBERS_FOR_STREET_URL} and content: {number_for_street_form}")
                response_content = requests.post(self._NUMBERS_FOR_STREET_URL, number_for_street_form).content
                self._logger.info("Sucessfully retrieved numbers for a street: {street}")
                self._logger.debug("Response after retrieving numbers for a streeet: {response_content}")
            except Exception as e:
                self._logger.warning(f"Probelm occoured while trying to retrieve numbers for street: {street}. Error messge: {e}")
                continue
            soup = BeautifulSoup(response_content, 'html.parser')
            option_tags = soup.find_all('option')
            numbers_ids = {option_tag.text: int(option_tag.get('value')) for option_tag in option_tags if (option_tag.get('value') is not None)}
            searched_number_id = numbers_ids.get(number)
            if(searched_number_id):
                self._logger.info(f"Successfully retrieved number id: {searched_number_id} for street: {street} and number: {number}")
                self._streets_numbers_ids[(street, number)] = (street_id, searched_number_id)
            else:
                self._logger.warning(f"Did not find a number: {number} for a street: {street}")
                continue
        return self

    def get_waste_schedules(self) -> dict:
        self._logger.info("Starting of schedules for streets and numbers retrieval")
        for names, ids in self._streets_numbers_ids.items():
            waste_schedule_form = self._WASTE_SCHEDULE_FORM_TEMPLATE  
            waste_schedule_form["id_numeru"] = ids[1]
            print(waste_schedule_form)
            response_dict = requests.post(self._WASTE_SCHEDULE_URL, waste_schedule_form).json()
            print(response_dict)


# _TEMP_STREET = {"name": "Monte Cassino, ul.", "id": 1791}
# _TEMP_NUMBER = {"name": "35/1", "id": 45429}
# _TEMP_INPUT = (_TEMP_STREET["name"], _TEMP_NUMBER["name"])
# _TEMP_OUTPUT = (_TEMP_STREET["id"], _TEMP_NUMBER["id"])
# logger = EmailLogger()
# garbageScrapper = GarbageScrapper([_TEMP_INPUT], logger)
# garbageScrapper.retrieve_streets().retrieve_numbers().get_waste_schedules()

_NUMBERS_FOR_STREET_URL = "https://ekosystem.wroc.pl/wp-admin/admin-ajax.php"
_NUMBERS_FOR_STREET_FORM_TEMPLATE = {
    "action": "waste_disposal_form_get_street_numbers",
    "id_ulicy": 1791
}
import json
response_dict = requests.post(_NUMBERS_FOR_STREET_URL, json.dumps(_NUMBERS_FOR_STREET_FORM_TEMPLATE))#.json()
print(response_dict)