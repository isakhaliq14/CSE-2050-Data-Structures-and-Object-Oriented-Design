def trib(k):
    return _trib(k, {})

def _trib(k, solved):
    if k == 0:
        return 0
    if k == 1 or k == 2:
        return 1
    if k in solved:
        return solved[k]
    
    solved[k] = _trib(k - 1, solved) + _trib(k - 2, solved) + _trib(k - 3, solved)
    return solved[k]