   def make_agree(self):
        word1, word2, word3, word4 = self.sentence['sent']
        x = word1.tag.gender
        y = word4.tag.gender
        rez = ( word1.inflect({'nomn'}), 
                word2.inflect({x, self.tense, self.aspect, self.voice}), 
                word3.inflect({'neut', 'accs'}),
                word4.inflect({y, self.case, self.gender}) )
        print(rez, word1, word2, word3, word4)
        assert None not in rez
        return rez