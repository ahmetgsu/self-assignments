
# Find the biggest quadrangle in (nxn) matrix


def make_list(list,a,b,c,d):
    _list = []
    for i in range(len(list)):
        for j in range(len(list)):
            if a <= i <= c and b <= j <= d:
                _list.append(list[i][j])
    return _list

def rectangle(p):
    _max = 0
    _value = None
    for a in range(len(p)):
        for b in range(len(p)):
            for c in range(len(p)-1,-1,-1):
                for d in range(len(p)-1,-1,-1):
                    first = p[a][b]
                    last = p[c][d]
                    if a == c and b == d:
                        break
                    else:
                        if p[a][b] == p[c][d]: #p01 == p31
                            new_list = make_list(p,a,b,c,d)
                            counter = 0
                            for elem in new_list:
                                if elem == p[a][b]:
                                    counter += 1
                                    if counter == len(new_list):
                                        if counter > _max:
                                            _max = counter
                                            _value = elem

    return [_value, _max]

r = [[1,2,2,4,3], [3,2,2,1,0], [3,1,0,4,4], [3,2,1,4,4], [3,0,1,4,4]]
print(rectangle(r))
