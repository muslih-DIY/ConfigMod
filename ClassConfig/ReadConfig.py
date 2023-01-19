import configparser
import warnings


class config:

    _config_class = {}
        # '_oracledb':_oracledb,
        # '_postgresdb':_postgresdb
        # }
    _config_paths: list = None

    def __init__(self,path:str|list|None=None) -> None:
        self.path = path

    @property
    def path(self):
        "return path"
        return self._config_paths

    @path.setter
    def path(self,path:str|list|None=None):
        if path is None:
            self._config_paths = []
        if isinstance(path,str):
            self._config_paths = [path]
        if isinstance(path,list):
            self._config_paths = path

    class DictClass(object):
        "create a class from dict"
        def __init__(self, **kwargs):
            self._kwargs = kwargs
            for key,value in kwargs.items():
                setattr(self, key, value)  

        def __repr__(self) -> str:
            kstr = ', '.join([f"{k}={i}" for  k,i in self._kwargs.items()])
            return f'DictClass({kstr})'

        def dict(self)-> dict:
            "return dict"
            return self._kwargs

    def load(self):
        """load all the configuration from file/files and
         create various configuration under different class object"""
        if not self._config_paths:
            warnings.warn('No configration file added :please use config.path=<some path>')
            return

        for path in self._config_paths:
            configfile = config.readConfigDict(path)
            for conf_name,conf in configfile.items():
                class_type = conf.pop('class_type',None)
                if class_type and self._config_class.get(class_type):
                    setattr(self,conf_name,self._config_class[class_type](**conf))
                    continue

                setattr(self,conf_name,self.DictClass(**conf))

    def register(self,confclasses:list):
        "register class type"
        for confclass in confclasses:
            self._config_class.update({confclass.__name__:confclass})

    @staticmethod
    def readConfig(filename=None):
        "Return config"
        configr = configparser.ConfigParser()
        configr.read(filename)
        return configr
    
    @staticmethod
    def readConfigDict(filename)->dict:
        "Return dict"
        configr:configparser.ConfigParser = configparser.ConfigParser()
        configr.read(filename)
        return configr._sections     

