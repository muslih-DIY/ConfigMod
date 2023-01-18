# ConfigMod

This module can be used for get configuration using python configparser


# example

        ##conf.py

        from dataclasses import dataclass,field
        from pathlib import Path
        from ConfigMod import ClassConfig as config

        CONF_PATH = os.path.join(Path(__file__).resolve().parent,'config.ini')

        @dataclass
        class _postgresdb:
            class_type:str
            dbname  :str
            dbuser  :str
            host    :str
            password:str
            port    :str = '5432'

        conf = config(CONF_PATH)
        conf.register([_postgresdb])
        conf.load()
        assert conf.postgresdb.port == '1522'
        assert conf.glob.name == 'ABC'

        #config.ini

        [postgresdb]
        class_type = _postgresdb
        dbname = postgresDB
        dbuser = postgresUSER
        host   = 127.0.0.1
        password = 
        port    = 1522     

        [glob]
        name = ABC
        ip   = 127.0.0.1
