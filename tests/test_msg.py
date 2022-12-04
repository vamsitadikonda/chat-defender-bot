#!/usr/bin/python
from src.utils.msg import *


class TestMessageFunctions:
    def test_clean_message(self):
        assert clean_message("QWerTYUGFBDG12143t543") == "qwertyugfbdg12143t543"

    def test_clean_message1(self):
        assert clean_message("Déjà vu") == "dj vu"

    def test_get_msg_template_no_warning(self):
        assert (
            get_msg_template("user_id", "reason", warning=False)
            == """ User:<@user_id> has been banned for reason."""
        )
        assert (
            get_msg_template("user_id", ["reason1", "reason2"], warning=False)
            == """ User:<@user_id> has been banned for reason1,reason2."""
        )

    def test_get_msg_template(self):
        assert (
            get_msg_template("user_id", "reason", warning=True)
            == """ Warning user:<@user_id> for reason.\n Another attempt will result in a ban!"""
        )
        assert (
            get_msg_template("user_id", ["reason1", "reason2"], warning=True)
            == """ Warning user:<@user_id> for reason1,reason2.\n Another attempt will result in a ban!"""
        )

    def test_get_help_message(self):
        assert isinstance(get_help_message(), str)
