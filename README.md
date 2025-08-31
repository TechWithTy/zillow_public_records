# Zillow Public Records SDK (skeleton)

Minimal placeholder; add usage examples after full implementation.

## Quick start

```python
from backend.app.core.third_party_integrations.zillow_public_records.client import ZillowPublicRecordsClient

client = ZillowPublicRecordsClient(api_key="YOUR_API_KEY")
assert client.health() is True
```

Note: Access to Zillow Bridge APIs may require approval/invite per their site.

## Environment

- ZILLOW_PUBLIC_RECORDS_API_KEY
- ZILLOW_PUBLIC_RECORDS_BASE_URL (default: https://api.bridgedataoutput.com/api/v2/publicRecords)
- ZILLOW_TIMEOUT (default: 15)

## References

- Zillow Public Records API: https://www.zillowgroup.com/developers/api/public-data/public-records-api/
