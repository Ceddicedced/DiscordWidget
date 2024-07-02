"""Tests for the DiscordWidget class."""

import pytest
from discordwidget.widget import Widget
from discordwidget.member import Member
from discordwidget.channel import Channel


@pytest.fixture
def widget():
    guild_id = 209559449533284352
    widget = Widget(guild_id)
    assert widget._guild_id == guild_id
    assert widget._url == f"https://discord.com/api/guilds/{guild_id}/widget.json"
    assert widget.id == 0
    assert widget.members == []
    assert widget.channels == []
    assert widget.presence_count == 0
    assert widget.name == ""
    assert widget.instant_invite == ""
    widget.get()
    return widget


def test_init(widget):
    assert widget.id == 209559449533284352
    assert widget.name == "Brotox-Community"
    assert widget.instant_invite == "https://discord.com/invite/T8EBPnvp"


def test_repr(widget):
    assert repr(widget) == f"<DiscordWidget {widget._guild_id}>"


def test_eq(widget):
    assert widget == Widget(widget._guild_id)
    assert widget != Widget(0)


def test_members(widget):
    assert len(widget.members) >= 1
    btx_bot = Member(
        id=0,
        username="Brotox Bot 🐼",
        status="online",
        avatar_url="https://cdn.discordapp.com/widget-avatars/0.png",
        discriminator="0000",
        avatar="",
    )  # Only username and discriminator are required to match
    assert btx_bot in widget.members


def test_channels(widget):
    assert len(widget.channels) >= 1
    afk_channel = Channel(id=286892988506832897, name="AFK", position=0)
    assert afk_channel in widget.channels


def test_presence_count(widget):
    assert widget.presence_count >= 1


if __name__ == "__main__":
    pytest.main()
