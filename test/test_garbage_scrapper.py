import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.garbage_scraping.garbage_scrapper import GarbageScrapper
from email_notifier.email_logging import EmailLogger


class TestGarbageScrapper:
    _TEMP_STREET = {"name": "Monte Cassino, ul.", "id": 1791}
    _TEMP_NUMBER = {"name": "35/1", "id": 45429}
    _TEMP_INPUT = (_TEMP_STREET["name"], _TEMP_NUMBER["name"])
    _TEMP_OUTPUT = (_TEMP_STREET["id"], _TEMP_NUMBER["id"])


    def test_retrieve_streets(self):
        logger = EmailLogger()
        garbageScrapper = GarbageScrapper([self._TEMP_INPUT], logger)
        garbageScrapper.retrieve_streets()
        assert isinstance(garbageScrapper._streets_ids, dict)
        assert isinstance(list(garbageScrapper._streets_ids.keys())[0], str)
        assert isinstance(list(garbageScrapper._streets_ids.values())[0], int)
        assert isinstance(list(garbageScrapper._streets_ids.values())[0], int)
        assert len(garbageScrapper._streets_ids) == len([self._TEMP_INPUT])
        assert garbageScrapper._streets_ids[self._TEMP_STREET["name"]] == self._TEMP_STREET["id"]

    def test_retrieve_numbers(self):
        logger = EmailLogger()
        garbageScrapper = GarbageScrapper([self._TEMP_INPUT], logger)
        garbageScrapper._streets_ids = {self._TEMP_STREET["name"]: self._TEMP_STREET["id"]}
        garbageScrapper.retrieve_numbers()
        assert isinstance(garbageScrapper._streets_numbers_ids, dict)
        assert garbageScrapper._streets_numbers_ids
        assert isinstance(list(garbageScrapper._streets_numbers_ids.keys())[0], tuple)
        assert isinstance(list(garbageScrapper._streets_numbers_ids.values())[0], tuple)
        assert garbageScrapper._streets_numbers_ids[self._TEMP_INPUT] == self._TEMP_OUTPUT

    def test_get_waste_schedules(self):
        logger = EmailLogger()
        garbageScrapper = GarbageScrapper([self._TEMP_INPUT], logger)
        garbageScrapper._streets_numbers_ids = {self._TEMP_INPUT: self._TEMP_OUTPUT}
        waste_schedules = garbageScrapper.get_waste_schedules()
        assert isinstance(waste_schedules, dict)
        assert self._TEMP_INPUT in waste_schedules.keys()
        waste_schedule = waste_schedules[self._TEMP_INPUT]
        assert isinstance(waste_schedule, dict)
        for k, v in waste_schedule.items():
            assert isinstance(k, str)
            assert isinstance(v, list)
            for i in v:
                assert isinstance(i, str)
