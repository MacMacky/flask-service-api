from typing import List


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
