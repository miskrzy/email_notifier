from email_notifier.garbage_scraping.garbage_parser import GarbageParser

class TestGarbageParser:
    def test_get_street_id():
        street_name = "Monte Cassino"
        street_id = 1791
        garbage_parser = GarbageParser(0,0)
        street_id_received = garbage_parser._get_street_id(street_name)
        assert street_id_received == street_id

    def test_get_address_number_id():
        address_number = "35/1"
        address_number_id = 45429
        garbage_parser = GarbageParser(0,0)
        address_number_id_received = garbage_parser._get_address_number_id(address_number)
        assert address_number_id_received == address_number_id
