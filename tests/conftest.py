from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_initial_activities = deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(_initial_activities))
    yield
    activities.clear()
    activities.update(deepcopy(_initial_activities))
