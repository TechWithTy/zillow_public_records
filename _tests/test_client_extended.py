from backend.app.core.third_party_integrations.zillow_public_records.client import ZillowPublicRecordsClient


class _Resp:
    def __init__(self, status=200, json_data=None):
        self.status_code = status
        self._json = json_data if json_data is not None else {"ok": True}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def test_get_injects_access_token_and_header(monkeypatch):
    client = ZillowPublicRecordsClient(api_key="ZTK", base_url="https://api.bridgedataoutput.com/api/v2/publicRecords")

    def fake_get(url, headers=None, params=None, timeout=None):
        assert url == "https://api.bridgedataoutput.com/api/v2/publicRecords/parcels"
        assert headers.get("Authorization") == "Bearer ZTK"
        # client also appends access_token if not present
        assert params.get("access_token") == "ZTK"
        assert params.get("limit") == 5
        return _Resp(json_data={"bundle": []})

    monkeypatch.setattr(
        "backend.app.core.third_party_integrations.zillow_public_records.client.requests.get",
        fake_get,
    )

    out = client.get("parcels", params={"limit": 5})
    assert "bundle" in out
