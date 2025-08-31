import logging
from typing import Dict

from fastapi import APIRouter, HTTPException, Request
import requests

from app.core.third_party_integrations.zillow_public_records.client import (
    ZillowPublicRecordsClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/zillow/public-records", tags=["zillow_public_records"])


# Utility

def fetch_resource(resource: str, params: Dict) -> Dict:
    client = ZillowPublicRecordsClient()
    return client.get(resource, params=params)


# Routes
@router.get("/{resource}")
async def zillow_public_records_get(resource: str, request: Request) -> Dict:
    try:
        return fetch_resource(resource, dict(request.query_params))
    except requests.HTTPError as e:
        status = e.response.status_code if getattr(e, "response", None) else 502
        detail = e.response.text if getattr(e, "response", None) else str(e)
        raise HTTPException(status_code=status, detail=detail)
    except Exception:
        logger.exception("Zillow Public Records request failed")
        raise HTTPException(status_code=500, detail="Internal server error")
