import pymorphy2
from constants import *

class Предложение():
    
    def build_matrix(self):
        data = []
        n = 0
        for part in self.pars_list:
            for var in part:
                try:
                    data[n] += [var]
                except IndexError:
                    data += [[var]]
            n += 1
        return data
    
    def get_candidates(self):
        max_h = max([ len(_) for _ in self.data ])
        rez = []
        for i in range(max_h):
            cand = []
            for j in range(len(self.data)):
                try:
                    cand += [self.data[j][i]]
                except IndexError:
                    cand += [self.data[j][0]]
            rez += [cand]
        return rez
    
    def get_sent_weight(self):
        rez = []
        for sent in self.sent_candidates:
            w = 1
            for pars in sent:
                w = w * pars.score 
            rez += [{'w':w, 'sent':sent}]
        return rez
    
    def get_max_w(self):
        rez = self.sent_candidates_w_weight[0]
        return rez
    
    def __init__(self, **kwargs):
        self.pars_list = kwargs['термы']
        self.morph = pymorphy2.MorphAnalyzer()
        self.tense = kwargs['время']

        self.data = self.build_matrix()
        self.sent_candidates = self.get_candidates()
        self.sent_candidates_w_weight = self.get_sent_weight()
        self.sentence = self.get_max_w()

class Простое_предложение(Предложение):
    def __str__(self):

        return str(self.sentence)
    
class Нераспространенное_предложение(Простое_предложение):
    pass

class Распространенное_предложение(Простое_предложение):
    pass 
    
class Сложное_бессоюзное_предложение(Нераспространенное_предложение,Распространенное_предложение):
    pass

class Сложно_сочиненное_предложение(Нераспространенное_предложение, Распространенное_предложение):
    pass

class Сложно_подчиненное_предложение(Нераспространенное_предложение, Распространенное_предложение):
    pass


def test():
    pm = pymorphy2.MorphAnalyzer()
    мама, мыть, рама = pm.parse('мама'),pm.parse('мыть'),pm.parse('рама'),
    мама_мыла_раму = Простое_предложение(
            термы = [мама, мыть, рама], 
            время = Прошедшее,
            числа = [1,1],
            вид = Несовершенный
        )
    print (мама_мыла_раму)

#    мама_мыла_белую_раму = Распространенное_предложение(
#            термы = [мама, мыть, белый, рама],
#            время = Прошедшее,
#            числа = [1,1],
#            вид = Несовершенный
#        )
#    мама_мыла_раму_подоконник_был_белый = Сложное_бессоюзное_предложение(
#            термы = [мама, мыть, рама, подоконник, быть, белый]
#            
#        )
#    мама_мыла_раму_и_подоконник_был_белый = Сложно_сочиненное_предложение(
#            термы = [мама, мыть, рама, подоконник, быть, белый],
#            режим_предложения = Согласие
#        )
#    мама_мыла_раму_потому_что_она_была_грязная = Сложно_подчиненное_предложение(
#            термы = [мама, мыть, рама, она, быть, грязный],
#            вид_придаточного_предложения = Причина
#        )
    
if __name__ == '__main__':
    test()