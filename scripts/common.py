"""Shared configuration for the project.

Add common settings here as they are introduced.
"""

from typing import Any


COMMON_CONFIG: dict[str, Any] = {
    "project_name": "test-git",
    "debug": False,
    "log_level": "INFO",
    "default_timeout": 30,
    "allowed_hosts": ["localhost", "127.0.0.1"],
}
