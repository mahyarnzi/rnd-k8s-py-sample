########################################################################################################
#                                           Library
########################################################################################################
from sqlalchemy.orm import Session
from .models import Test


########################################################################################################
#                                           Functions
########################################################################################################
def db_get_message(db: Session):
    return db.query(Test).all()