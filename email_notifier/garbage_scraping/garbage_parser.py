import json
import requests
from bs4 import BeautifulSoup


class GarbageParser:
    def __init__(self,street_id:id,address_number_id:id) -> None:
        self._street_id = street_id
        self._number_id = address_number_id
        self._garbages_dict = self._get_garbage_type_dates_dict(self._street_id,self._number_id)

    @classmethod 
    def from_names(cls,street_name:str,address_number_str):
        street_id = cls._get_street_id(street_name)
        address_number_id = cls._get_number_id(address_number_str)
        return cls(street_id,address_number_id)

    def get_garbage_types_for_tomorrow(self) -> list:
        pass

    def _get_garbage_type_dates_dict(self,street_id:int,number_id:int) -> dict:
        pass

    @classmethod
    def _get_street_id(self,street_name:str):
        pass

    @classmethod
    def _get_address_number_id(self,address_number:str):
        pass



# soup = BeautifulSoup(page.content, "html.parser")

# result = soup.find(href=True)["href"]

# print(result)