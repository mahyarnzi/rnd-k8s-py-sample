########################################################################################################
#                                           Library
########################################################################################################
from fastapi import APIRouter
from app.test import core as core_test

########################################################################################################
#                                           Main
########################################################################################################
router = APIRouter()
router.include_router(core_test.router)