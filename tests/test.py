from dataclasses import dataclass,field
from pathlib import Path

import sys,os

project_path = os.path.abspath(Path(__file__).resolve().parent.parent)
sys.path.append(project_path)
CONF_PATH = os.path.join(Path(__file__).resolve().parent,'config.ini')

from ClassConfig import config


@dataclass
class _oracledb:
    dbname  :str 
    dbuser  :str 
    host    :str 
    password:str 
    port    :str = '1521'
    sid     :str =field(init=False)

    def __post_init__(self):
        self.sid = f"{self.host}:{self.port}/{self.dbname}"

@dataclass
class _postgresdb:
    dbname  :str
    dbuser  :str
    host    :str
    password:str
    port    :int = 5432

print(CONF_PATH)
conf = config(CONF_PATH)
conf.register([_oracledb,_postgresdb])
conf.load()

assert conf.postgresdb.port == '1522'
assert conf.postgresdb.dbname == 'postgresDB'
assert conf.postgresdb.dbuser == 'postgresUSER'
assert conf.postgresdb.host == '127.0.0.1'
assert conf.postgresdb.password == ''


assert conf.oracledbsdc.port == '1521'
assert conf.oracledbsdc.dbname == 'Fdd'
assert conf.oracledbsdc.dbuser == 'ivrs'
assert conf.oracledbsdc.host ==  '10.33.22.22'
assert conf.oracledbsdc.password == '33#123'
assert conf.oracledbsdc.sid == "10.33.22.22:1521/Fdd"

assert conf.glob.name == 'ABC'
assert conf.glob.wait ==  'possstgres'
assert conf.glob.ip == '127.0.0.1'
print("test success")
