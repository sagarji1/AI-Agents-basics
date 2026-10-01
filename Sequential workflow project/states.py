#now we r creating a graph 
#first thing we create is a state

import os

# 1) typed disc (most common approach)
from typing import TypedDict
class State(TypedDict):
    topic:str
    summary:str
    score:int 
    
# 2)pydantic approach : good at data validation and type checking at runtype

from pydantic import BaseModel, field_validator
class State(BaseModel):
    topic:str
    score:int
    summary:str=""
    @field_validator
    def score_postive(cls,v):
        if(v<0):
            raise ValueError("Score must be postive")
        
# 3)python dataclasses : standard data classes bit it is used rarely

from dataclasses import dataclass,field

@dataclass
class State:
    topic:str =""
    summary:str
    message:list = field(default_factory=list)


     