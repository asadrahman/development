import re

class WriteCheque():
    word_numbers = {
        '0':'', '1': 'one', '2':'two', '3':'three', '4':'four', 
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', 
        '9': 'nine', '10':'ten', '12': 'twelve', '30': 'thirty', 
        '100': 'hundred', '1000' : 'thousand', '10000': 'ten thousand'
    }
    
    
    def translate_number(self, number_to_translate):
        
        size = len(number_to_translate)
        number_list = list(number_to_translate)
        number_list2 = list( number_to_translate[i] for i in range(0,size -2))
        number_list2.append(number_to_translate[-2:])
        size2 = len(number_list2)
   
        output_str = ''        
        for idx in range(0,len(number_list2)):
            
            word = number_list2[idx]
            if word == '0':
                continue
                
            base_power = size2 - idx
            number_wd = self.translate_number_size(word, base_power)
            output_str += number_wd

            if idx == 0 and size2 != 1:
                output_str += ' and'
  
        return re.sub("\s\s+", " ", output_str).strip()
        

    def translate_number_size(self, number, base):
        
        power = 10 ** base
        str_size, remainder = divmod(int(number), power)
        print("BASE " +str(base))
        print("DIVIDEND " +str(str_size))
        print("REMAINDER " +str(remainder))
        print("POWER " +str(self.word_numbers[str(power)]))
        
        if base == 1:
            if str_size == 1:
                number_str = ' ' + self.word_numbers[number]
            else:
                tens = str_size * power
                number_str = ' ' + self.word_numbers[str(tens)] + ' ' + str(self.word_numbers[str(remainder)])
        else:
            number_str = self.word_numbers[str(remainder)] + ' ' + str(self.word_numbers[str(power)])
               
        return number_str
