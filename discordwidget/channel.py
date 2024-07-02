"""This module contains the Channel class."""

from dataclasses import dataclass


@dataclass
class Channel:
    """Represents a channel in a Discord guild."""

    id: int
    name: str
    position: int

    def __str__(self) -> str:  # noqa: D105
        return self.name

    def __repr__(self) -> str:  # noqa: D105
        return f"<Channel {self.__str__()}>"

    def __eq__(self, other) -> bool:  # noqa: D105
        return self.id == other.id

    def __hash__(self) -> int:  # noqa: D105
        return hash(self.id)

    def __lt__(self, other) -> bool:  # noqa: D105
        return self.position < other.position
