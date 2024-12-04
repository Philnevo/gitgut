
def open_file(n:str) -> list[list[int]]:
    """ Opens file and makes lists of lists for each row """

    v = []
    
    with open(n) as x:
        v = [list(map(int, row.split())) for row in x]

    return v

def is_safe(v:list) -> bool:
    """ takes a list of ints and checks if they are 'safe' """

    safe = True
    
    if v[0] > v[1]:
        safe = _is_safe_desc(f_is_safe_desc(v)) or _is_safe_desc(s_is_safe_desc(v))

    elif v[0] < v[1]:
        safe = _is_safe_asc(f_is_safe_asc(v)) or _is_safe_asc(s_is_safe_asc(v))

    else:
        safe = _is_safe_desc(f_is_safe_desc(v)) or _is_safe_desc(s_is_safe_desc(v)) or _is_safe_asc(f_is_safe_asc(v)) or _is_safe_asc(s_is_safe_asc(v))

    return safe

def f_is_safe_asc(v:list) -> list[int]:
    """
    Checks if there is an 'unsafe' combination of values and
    removes the first element of the troublesome combination.
    """

    i = 0
    j = 0
    w = v

    while i + 1 < len(v) and j < 1 :

        if  v[i] >= v[i+1] or (v[i+1]-v[i]) > 3:
           j = j + 1
           del w[i]
        i = i + 1

    return w

def s_is_safe_asc(v:list) -> list[int]:
    """
    Checks if there is an 'unsafe' combination of values and
    removes the second element of the troublesome combination.
    """

    i = 0
    j = 0
    w = v

    while i + 1 < len(v) and j < 1 :

        if  v[i] >= v[i+1] or (v[i+1]-v[i]) > 3:
           j = j + 1
           del w[i+1]
        i = i + 1

    return w

def _is_safe_asc(v:list) -> bool:
    """ aux function to check if a list is safe ascendingly """

    i = 0
    safe = True
 

    while i + 1 < len(v) and safe:

        if  v[i] > v[i+1] or (v[i+1]-v[i]) > 3:
           safe = False
        i = i + 1

    return safe

def f_is_safe_desc(v:list) -> list[int]:
    """
    Checks if there is an 'unsafe' combination of values and
    removes the first element of the troublesome combination.
    """
    
    i = 0
    j = 0
    w = v

    while i + 1 < len(v) and j < 1 :

        if  v[i] <= v[i+1] or (v[i]-v[i+1]) > 3:
           j = j + 1
           del w[i]
        i = i + 1

    return w

def s_is_safe_desc(v:list) -> list[int]:
    """
    Checks if there is an 'unsafe' combination of values and
    removes the second element of the troublesome combination.
    """
    
    i = 0
    j = 0
    w = v

    while i + 1 < len(v) and j < 1 :

        if  v[i] <= v[i+1] or (v[i]-v[i+1]) > 3:
           j = j + 1
           del w[i+1]
        i = i + 1

    return w

def _is_safe_desc(v:list) -> bool:
    """ aux function to check if a list is safe descendingly """

    i = 0
    safe = True

    while i + 1 < len(v) and safe:

        if  v[i] < v[i+1] or (v[i]-v[i+1]) > 3:
           safe = False
        i = i + 1

    return safe

def count_safe(v:list[list[int]]) -> int:
    """ Counts the number of safe lists in a list """

    i = 0

    while v != []:
        if is_safe(v[0]):
            i = i + 1
        v = v[1:]

    return i

getlists = open_file("data.txt")
#print(getlists)
print(len(getlists))

#getlists = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]

countsafe = count_safe(getlists)
print(countsafe)
