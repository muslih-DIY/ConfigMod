import configparser
from pathlib import Path
import os


class config:


    _config_class = {}
        # '_oracledb':_oracledb,
        # '_postgresdb':_postgresdb
        # }

    def __init__(self,path: str=None) -> None:
        if path==None:
            self.PATH = os.path.join(Path(__file__).resolve().parent, 'config.ini')
        
        
    

    def load(self):
        configfile = self.readConfigDict()
        for conf_name,conf in configfile.items():
            setattr(self,conf_name,self._config_class[conf['class_type']](**conf))

    
    def register(self,confclasses:list):
        for confclass in confclasses:
            self._config_class.update({confclass.__name__:confclass})


    def readConfig(self,filename=None):
        if filename is None:filename=self.PATH
        config = configparser.ConfigParser()
        config.read(filename)
        return config

    def readConfigDict(self,filename=None):
        if filename is None:filename=self.PATH
        config:configparser.ConfigParser = configparser.ConfigParser()
        config.read(filename)
        return config._sections       

