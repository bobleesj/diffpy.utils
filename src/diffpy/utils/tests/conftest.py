import json
from importlib.resources import as_file, files
from pathlib import Path

import pytest


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = Path(tmp_path)
    home_dir = base_dir / "home_dir"
    home_dir.mkdir(parents=True, exist_ok=True)
    cwd_dir = base_dir / "cwd_dir"
    cwd_dir.mkdir(parents=True, exist_ok=True)

    home_config_data = {"username": "home_username", "email": "home@email.com"}
    with open(home_dir / "diffpyconfig.json", "w") as f:
        json.dump(home_config_data, f)

    yield tmp_path


def get_datafile(filename):
    """Helper function to retrieve the file path for test data."""
    ref = files(__package__) / f"testdata/{filename}"
    with as_file(ref) as rv:
        return rv


@pytest.fixture
def datafile():
    """Fixture to dynamically load any test file."""

    def _load(filename):
        return get_datafile(filename)

    return _load
