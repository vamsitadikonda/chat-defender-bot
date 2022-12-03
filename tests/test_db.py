import mock
from src.utils.db import DbConnector
from tests.testutils import *


def setup_module(module):
    from dotenv import load_dotenv

    load_dotenv("bot.env")
    assert True


@mock.patch("time.sleep", mock.MagicMock())
class TestDbConnector:
    def test_connect(self):
        with mock.patch("mysql.connector.connect") as mc:
            mc.return_value = MockConnector()
            db = DbConnector()
            db.connect()

    def test_create_tables(self):
        with mock.patch("mysql.connector.connect") as mc:
            mc.return_value = MockConnector()
            db = DbConnector()
            db.connect()
            db.create_tables()

    def test_executequery(self):
        with mock.patch("mysql.connector.connect") as mc:
            mc.return_value = MockConnector()
            db = DbConnector()
            db.connect()
            db.executequery("mock_query", "mock_cond")

    def test_close(self):
        with mock.patch("mysql.connector.connect") as mc:
            mc.return_value = MockConnector()
            db = DbConnector()
            db.connect()
            db.close()
