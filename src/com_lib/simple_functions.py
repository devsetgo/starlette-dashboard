# -*- coding: utf-8 -*-
from datetime import datetime


def get_current_datetime() -> datetime:
    """
    get the current datetime

    Returns:
        datetime.now()
    """
    current_time: datetime = datetime.now()
    return current_time
