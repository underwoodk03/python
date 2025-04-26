import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1=Television()

    def teardown_method(self):
        del self.tv1


    def test_init(self):
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 0"

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__()== "Power = True, Channel = 0, volume = 0"

        self.tv1.power()
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 0"


    def test_mute(self):
        self.tv1.mute()
        assert self.tv1.__str__()== "Power = True, Channel = 0, volume = 1, muted"

        self.tv1.mute()
        assert self.tv1.__str__()== "Power = True, Channel = 0, volume = 1"

        self.tv1.mute()
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 1, muted"

        self.tv1.mute()
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 1"

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 0"

        self.tv1.channel_up()
        assert self.tv1.__str__()== "Power = true, Channel = 2, volume = 1"

        self.tv1.channel_up()
        assert self.tv1.__str__()== "Power = true, Channel = 3, volume = 1"


    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__()== "Power = False, Channel = 3, volume = 1"

        self.tv1.channel_down()
        assert self.tv1.__str__()== "Power = true, Channel = 0, volume = 1"


    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__()== "Power = False, Channel = 0, volume = 1"

        self.tv1.volume_up()
        assert self.tv1.__str__()== "Power = true, Channel = 0, volume = 1"

        self.tv1.volume_up()
        assert self.tv1.__str__()== "Power = true, Channel = 0, volume = 2, muted"

        self.tv1.volume_up()
        assert self.tv1.__str__()== "Power = true, Channel = 0, volume = 2, "


    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, volume = 1"

        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = true, Channel = 0, volume = 1"

        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = true, Channel = 0, volume = 2, muted"

