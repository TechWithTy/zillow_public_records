import os
from typing import Any, Dict, Optional

import requests


class ZillowPublicRecordsClient:
    """
    Zillow Bridge Public Records API client.
    Docs: https://www.zillowgroup.com/developers/api/public-data/public-records-api/

    Note: Access is invite-only; endpoints and scopes depend on your account.
    This client exposes a generic GET method to call specific resources under
    the Public Records API once enabled.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
    ):
        # Bridge typically uses an access token; provide via ZILLOW_PUBLIC_RECORDS_API_KEY
        self.api_key = api_key or os.getenv("ZILLOW_PUBLIC_RECORDS_API_KEY")
        self.base_url = (base_url or os.getenv("ZILLOW_PUBLIC_RECORDS_BASE_URL") or "https://api.bridgedataoutput.com/api/v2/publicRecords").rstrip("/")
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.api_key:
            # Bridge often uses token or api_key in query; support header if configured
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generic GET for a Public Records resource.
        Example path: "parcels", "transactions", "assessments" (depends on your access).
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        query: Dict[str, Any] = dict(params or {})
        # Some Bridge configurations expect an 'access_token' query param instead of Authorization header.
        if self.api_key and "access_token" not in query and "apikey" not in query:
            query["access_token"] = self.api_key
        resp = requests.get(url, headers=self._headers(), params=query, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def health(self) -> bool:
        return bool(self.api_key)
