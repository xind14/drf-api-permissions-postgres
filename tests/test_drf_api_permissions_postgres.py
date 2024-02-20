
import pytest
from drf_api_permissions_postgres.drf_api_permissions_postgres import drf_api_permissions_postgres 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = drf_api_permissions_postgres()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = drf_api_permissions_postgres(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

