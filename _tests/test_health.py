from backend.app.core.third_party_integrations.zillow_public_records.client import ZillowPublicRecordsClient

def test_health():
    client = ZillowPublicRecordsClient(api_key="test")
    assert client.health() is True
