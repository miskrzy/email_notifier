import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.garbage_scraping.garbage_scrapper import GarbageScrapper


class TestGarbageScrapper:
    _TEMP_STREET_NAME = "Monte Cassino"
    _TEMP_NUMBER = "35/1"
    _TEMP_STREET_ID = 1791
    _TEMP_NUMBER_ID = 45429

    def test_get_no_street_page(self):
        garbageScrapper = GarbageScrapper()
        no_street_page = garbageScrapper._get_no_street_page()
        assert isinstance(no_street_page, str)

    def test_get_numbers_for_street_response(self):
        garbageScrapper = GarbageScrapper()
        no_street_page = garbageScrapper._get_numbers_for_street_response(self._TEMP_STREET_ID)
        assert isinstance(no_street_page, dict)

    def test_get_waste_schedule_response(self):
        garbageScrapper = GarbageScrapper()
        no_street_page = garbageScrapper._get_waste_schedule_response(self._TEMP_STREET_ID, self._TEMP_NUMBER_ID)
        assert isinstance(no_street_page, dict)

    def test_get_street_id(self):
        garbageScrapper = GarbageScrapper()
        street_id = garbageScrapper._get_street_id(self._TEMP_STREET_NAME)
        assert street_id == self._TEMP_STREET_IDTEMP

    def test_get_number_id(self):
        garbageScrapper = GarbageScrapper()
        number_id = garbageScrapper._get_number_id(self._TEMP_NUMBER)
        assert number_id == self._TEMP_NUMBER_ID

    def test_get_get_waste_schedule(self):
        garbageScrapper = GarbageScrapper()
        waste_schedule = garbageScrapper.get_waste_schedule(self._TEMP_STREET_NAME, self._TEMP_NUMBER)
        assert isinstance(waste_schedule, dict)
        for k, v in waste_schedule.items():
            assert isinstance(k, str)
            assert isinstance(v, list)
            for i in v:
                assert isinstance(i, str)
