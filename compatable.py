from warnings import *
from typing import Any
from core.utils.commons.randomize import random_string
class DTYPE:
    def __init__(self,key: str,value: Any):
        self.key = key
        self.value = value
    def __repr__(self) -> str:
        return "<%s 0x%s = 0x%s >" % (self.__class__.__name__,self.key,self.value)

COMPAT_PARENT = DTYPE("COMPAT_PARENT",0x0)
COMPAT_CHILD = DTYPE("COMPAT_CHILD",0x1)
class Config:
    def __init__(self,src_key: dict,destination_dictionary: dict,out_dictionary: dict):
        self.src_dict = src_key
        self.dst_dict = destination_dictionary
        self.out_dict = out_dictionary
class SomeType:
    def __init__(self,name: str,value: Any,default: Any,required: bool):
        self.name = name
        self.val = value
        self.default = default
        self.required = required
    def __repr__(self) -> str:
        return "<%s name=%s value=%s required=%s >" % (self.__class__.__name__,self.name,self.val,self.required) 
class CompatizeInit:
    def __init__(self,**kwargs):
        opt = {}
        if kwargs != {}:
            if hasattr(self,"fields"):
                size = 0
                total = len(list(kwargs.keys()))
                """
                while size < total:
                    value = kwargs[list(kwargs.keys())[size]]
                    key = list(kwargs.keys())[size]
                    size = size+1
                    is_exist = opt.get(key)
                    if is_exist is None:
                        opt[key]=value
                    else:
                        size=size+1
                """
                r = Config(
                    self.fields,
                    kwargs,
                    self.option)
class Compat(CompatizeInit):
    name = None
    option = {}
    def __truediv__(self,other):
        IS_DIV_OBJ = any([hasattr(other,"COMPAT_PARENT") and isinstance(other.COMPAT_PARENT,DTYPE),hasattr(other,"COMPAT_CHILD") and isinstance(other.COMPAT_CHILD,DTYPE)])
        DIV_NAME = other.__class__.__name__ if other.__class__.__name__ != "type" else other.__name__
        if not IS_DIV_OBJ:
            raise TypeError("%s is not div object it's must be div object" % (DIV_NAME))
        self.name = DIV_NAME
        return self
    def __repr__(self) -> str: 
        return "< | %s -> %s | > " % (self.__class__.__name__,self.name)
class LCONF(Compat):
    COMPAT_PARENT = DTYPE("COMPAT_PARENT",0x0)
    fields = {
        "data":[
            int,
            4
        ]
    }
class OQCONF(Compat):
    COMPAT_CHILD = DTYPE("COMPAT_CHILD",0x0)
    fields = {
        "alperen":[
                int,
                4
            ]
        }
    