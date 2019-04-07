A = ('обладать', [('Способность к самообучению', 'Интеллектуальный робот'), ('Способность к самоорганизации', 'Интеллектуальный робот'), ('Способность к адаптации', 'Интеллектуальный робот')])
forms = {
    'обладать': {'н.в.':'обладает'},
    'способность': {'твор.':'способностью'},
    'способность к самообучению': {'твор.':'способностью к самообучению'},
}

def ядерное_предложение(data):
    # X y Z
    return "%s %s %s." % (
        data[1][0][1],
        forms[data[0]]['н.в.'],
        forms[data[1][0][0]]['твор.'])

def предложение_определение(data):
    # X это Y
    list_of_items = data[1]
    X = list_of_items[1][1]
    Y = list_of_items[1][0]
    out = ""
    out += X
    out += " это "
    n = 0
    for y in Y:
        out += "%s" % y
        n += 1
    out += '.'
    return out

def бессоюзное_предложение(data):
    # X - Y
    list_of_items = data[1]
    X = list_of_items[1][1]
    Y = list_of_items[1][0]
    out = ""
    out += X
    out += " - "
    n = 0
    for y in Y:
        out += "%s" % y
        n += 1
    out += '.'
    return out

def сложно_подчиненное_предложение(data):
    # X y Z, потому что F
    pass

def предолжение_с_перечислением(data):
    # X y Z, S, F
    # X обладает способностью к Y, Z и F
    list_of_items = data[1]
    X = list_of_items[1][1]
    Y = [ _[0] for _ in list_of_items ]
    Z = [ _[13:] for _ in Y]
    last = len(Z) - 1
    out = ""
    out += X
    out += " обладает способностью к " #делится на,
    n = 0
    for z in Z:
#        out += "%s " % y
        if n == last:
            out = out.strip(',') + " и " + z
        else:
            out += z + ", "
        n += 1
    out += '.'
    return out

#T = предолжение_с_перечислением
#T = предложение_определение
T = бессоюзное_предложение
#T = ядерное_предложение

def parse(answ):
    return T(answ)

print(parse(A))
