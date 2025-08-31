import logging
from typing import Dict

from fastapi import APIRouter
from app.core.third_party_integrations.zillow_public_records.api.resources import (
    router as resources_router,
)

logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(resources_router)

