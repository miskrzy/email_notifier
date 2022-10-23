import email_notifier
import azure.functions as afunc


class TestEmailNotifier:
    def test_email_notifier(self):
        req = afunc.HttpRequest(
                method='GET',
                body=None,
                url='email_notifier')
        
        resp = email_notifier.main(req)

        assert resp.get_body() == b"a"
