#Class variable is the same for All objects


class HebrewWord():
    gematria_dict = {"א":1 , "ב":2, "ג":3,"ד":4  ,"ה":5 ,"ו":6
     ,"ז":7,"ח":8 ,
"ט":9,"י":10 ,"כ":20 ,"ל":30 ,"מ":40 , "נ":50,
"ס":60,"ע":70,"פ":80,"צ":90,"ק":100,"ר":200,"ש":300,"ת":400}

    def __init__(self,word ):
        self.word = word  


    def gematria(self):
        sum =0
        for i in self.word:
            sum= sum + HebrewWord.gematria_dict[i]

        return sum
    def _gematria(hebrew_word):
        sum =0
        for i in hebrew_word:
            sum = sum + HebrewWord.gematria_dict[i]

        return sum

    def gematria_katan(self):
        current_gematria_katan = HebrewWord.gematria(self)

        while current_gematria_katan > 9:
           current_gematria_katan = HebrewWord._add_digits(current_gematria_katan)

        return current_gematria_katan


    def _add_digits(a):
        a = str(a)
        sum = 0
        for i in a:
            i=int(i)
            sum = sum+i
        return sum

    def list_of_similar_gematrias(self):


        ramban = ""
        list_of_hebrew_words = ["רר","ככ","יי","כ","ס","לל"]
        list_of_similars = []
        
        for i in list_of_hebrew_words:
            #get gemtria of i
            gematria_of_i = HebrewWord._gematria(i)

            #see if its the same as the selfs gematria
            if gematria_of_i == HebrewWord.gematria(self):


                # if its the same, add it to the list_of_similars
                list_of_similars.append(i) 

        return list_of_similars





        

#word1 = HebrewWord("גדול") 
word2 = HebrewWord("הההה")
#object.function()
#Class.function(object)

#word1.gematria()
#SAME AS: HebrewWord.gematria(word1) 
#word1.gematria_katan()

similar_gematrias = word2.list_of_similar_gematrias()
