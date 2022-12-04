#!/usr/bin/python
from src.checkers.bully import BullyChecker


class TestBullyChecker:
    def test_load_model(self):
        bc = BullyChecker()
        assert bc.model is not None

    def test_check_message(self):
        bc = BullyChecker()
        assert len(bc.check_message("Rot in Hell")) > 0
        assert len(bc.check_message("You are a Pig woman!")) > 0
        assert len(bc.check_message("How are you?")) == 0
