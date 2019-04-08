
        
class Предложение_определение():
    # X это Y
    def __init__(self, data):
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
        self.s = out

class Бессоюзное_предложение():
    # X - Y
    def __init__(self, data):
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
        self.s = out

class Сложно_подчиненное_предложение():
    # X y Z, потому что F
    pass 
    
class Предолжение_с_перечислением():
    # X y Z, S, F
    # X обладает способностью к Y, Z и F
    def __init__(self, data):
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
#           out += "%s " % y
            if n == last:
                out = out.strip(',') + " и " + z
            else:
                out += z + ", "
            n += 1
        out += '.'
        self.s = out
