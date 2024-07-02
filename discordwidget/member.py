"""This module contains the Member class, which represents a member in a Discord guild."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Member:
    """Represents a member in a Discord guild.

    Attributes:
        id (int): The ID of the member.
        username (str): The username of the member.
        discriminator (str): The discriminator of the member.
        avatar_url (str): The URL of the member's avatar.
        status (str): The status of the member.
        avatar (str): The avatar of the member.

        Optional Attributes:
        game (str): The game the member is playing (optional).
        deaf (bool): Whether the member is deafened (optional).
        mute (bool): Whether the member is muted (optional).
        self_deaf (bool): Whether the member has self-deafened (optional).
        self_mute (bool): Whether the member has self-muted (optional).
        suppress (bool): Whether the member is suppressed (optional).
        channel_id (int): The ID of the voice channel the member is in (optional).
    """

    id: int
    username: str
    discriminator: str
    avatar_url: str
    status: str
    avatar: str
    game: Optional[str] = None
    deaf: Optional[bool] = None
    mute: Optional[bool] = None
    self_deaf: Optional[bool] = None
    self_mute: Optional[bool] = None
    suppress: Optional[bool] = None
    channel_id: Optional[int] = None

    def __str__(self) -> str:  # noqa: D105
        if self.discriminator is None:
            return self.username
        return f"{self.username}#{self.discriminator}"

    def __repr__(self) -> str:  # noqa: D105
        return f"<Member {self.__str__()}>"

    def __eq__(self, other) -> bool:  # noqa: D105
        if isinstance(other, Member):
            return self.id == other.id
        return False

    def __lt__(self, other) -> bool:  # noqa: D105
        if isinstance(other, Member):
            return self.id < other.id
        # Can't compare if not a Member
        raise TypeError(
            f"'<' not supported between instances of 'Member' and '{type(other).__name__}'"
        )

    @property
    def isInVoice(self) -> bool:
        """Checks if the member is in a voice channel."""
        return self.channel_id is not None

    @property
    def isPlaying(self) -> bool:
        """Checks if the member is playing a game."""
        return self.game is not None
