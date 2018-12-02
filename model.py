from dataclasses import dataclass
import json
import datetime


@dataclass
class Tibia:
    name: str
    extract_former_name: str
    sex: str
    vocation: str
    level: str
    achievement: str
    world: str
    residence: str
    last_login: str
    account_status: str
    deaths: dict
    created_at: datetime.datetime
