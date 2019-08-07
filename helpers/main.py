from typing import List,Tuple,Type
from flask import jsonify

def slice(listo: List = [], start: int = 0, stop: int = 1) -> []:
    result: List = []
    lengtho: int = len(listo)
    if lengtho is None or lengtho == 0 or start > stop:
        return result
    else:
        for i in range(lengtho):
            if start == stop:
                break
            else:
                result.append(listo[i])
                start += 1
    return result


def resJson(**kwargs):
   resp = {}
   for key in kwargs:
       resp[key] = kwargs[key]     
   return jsonify(resp)


def result_dict(column_names:Tuple[str], datas:List[str]) -> List[dict]:
    result : List[dict] = []
    for i in range(len(datas)):
      result.append({column_names[z] : datas[i][z] for z in range(len(datas[i]))})
    return result
   
def is_none(val:Type):
    return val == None
