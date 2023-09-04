from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Server:
    """A data class to represent server configuration."""

    host: str
    port: int


@dataclass
class Config:
    """A data class to represent the configuration for the main application."""

    server: Server
    allowed_objects: List[Dict]


# one of config
main_config: Config = Config(
    server=Server(
        host='',
        port=0,
    ),
    allowed_objects=[],
)