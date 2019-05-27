import pymorphy2
from constants import *

morph = pymorphy2.MorphAnalyzer()

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
    
    def get_candidates(self): #нужны все комбинации всех элементов списка
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
    
    def make_agree(self):
        word1, word2, word3 = self.sentence['sent']
        #mama = self.pars_list
        #myt = self.pars_list
        #rama = self.pars_list
        x = word1.tag.gender
        rez = word1.inflect({'nomn'}), word2.inflect({x, self.tense, self.aspect, self.voice}), word3.inflect({'accs'})
        assert None not in rez
        return rez      
        
    def __init__(self, **kwargs):
        self.pars_list = kwargs['термы']
        self.morph = pymorphy2.MorphAnalyzer()
        try:
            self.tense = kwargs['время']
        except KeyError:
            self.tense = 'pres'
        self.number = kwargs['число']
        self.aspect = kwargs['вид']
        self.voice = kwargs['залог']
        
        self.data = self.build_matrix()
        self.sent_candidates = self.get_candidates()
        self.sent_candidates_w_weight = self.get_sent_weight()
        self.sentence = self.get_max_w()
        self.sentence_agree = self.make_agree()

class Простое_предложение(Предложение):
    def __str__(self):
        return str([ _.word for _ in self.sentence_agree ])
    
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
    мама, мыть, рама = morph.parse('мама'),morph.parse('мыть'),morph.parse('рама'),
    мама_мыла_раму = Простое_предложение(
            термы = [мама, мыть, рама], 
            время = Настоящее,
            число = Множественное,
            вид = Несовершенный,
            залог = Действительный
        )
    print (мама_мыла_раму)
    папа, мыть, мама = morph.parse('папа'),morph.parse('мыть'),morph.parse('мама'),
    папа_мыл_маму = Простое_предложение(
            термы = [папа, мыть, мама], 
            время = Прошедшее,
            число = Множественное,
            вид = Несовершенный,
            залог = Действительный
        )
    print (папа_мыл_маму)
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