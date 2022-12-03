import mock
from src.checkers.reporter import ReportChecker
from tests.testutils import *


def setup_module(module):
    from dotenv import load_dotenv

    load_dotenv("bot.env")


class TestReportChecker:
    def test_check_message(self):
        rc = ReportChecker()
        assert rc.check_message("!report word Aang") == True
        assert rc.check_message("!rep word Aang") == False
        assert rc.check_message("report word Aang") == False

    def test_parse_message(self):
        rc = ReportChecker()
        assert rc.parse_message("!report word Aang") == ("word", "Aang")
        assert rc.parse_message("!report word Aang 123") == ("word", "Aang")
