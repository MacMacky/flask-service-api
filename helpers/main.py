from typing import List,Tuple,Type
from flask import jsonify
from datetime import date

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


def generate_token_db_name() -> str:
    now = date.today()
    year = now.year
    day = now.day
    month = now.month
    len_m = len(str(month)); len_d = len(str(day))
    day = f"0{day}" if len_d == 1 else str(day)
    month = f"0{month}" if len_m == 1 else str(month)
    return f"shopsession{year}{month}{day}.sessiondetails"