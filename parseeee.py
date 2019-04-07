import pymorphy2

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
        

    def __init__(self, pars_list, tense = 'pres', number=0):
        self.pars_list = pars_list
        self.morph = pymorphy2.MorphAnalyzer()
        self.tense = tense

        self.data = self.build_matrix()
        self.sent_candidates = self.get_candidates()
        self.sent_candidates_w_weight = self.get_sent_weight()
        self.sentence = self.get_max_w()
    

   # 'мама' 'мыть' 'рама'
    #              'рама'
        
    def __str__(self):

        return str(self.sentence) #' '.join(out).capitalize()

class Ядерное_предложение(Предложение):
    # X y Z
     pass

def main():
    morph = pymorphy2.MorphAnalyzer()
    мама = morph.parse("мама")
    мыть = morph.parse("мыть")
    рама = morph.parse("рама")
    a = Ядерное_предложение([мама, мыть, рама], tense='past')
    катя = morph.parse("катя")
    ехать = morph.parse("ехать")
    мир = morph.parse("мир")
    a = Ядерное_предложение([катя, ехать, мир], tense='past')
    print (a)
    data = ""
#    predl = Предложение_с_перечислением(data)
    
#    print(predl.s)

if __name__ == '__main__':
    main()
