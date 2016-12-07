import unittest
from cheque import WriteCheque

class writeCheque(unittest.TestCase):
    def setUp(self):
        self.WriteCheque = WriteCheque()
        
    def test_translate_12(self):
       output_str = self.WriteCheque.translate_number('12')
       self.assertEqual(output_str, 'twelve')
       
       output_str = self.WriteCheque.translate_number('10')
       self.assertEqual(output_str, 'ten')
    
    def test_translate_hundreds(self):
        output_str = self.WriteCheque.translate_number('439')
        self.assertEqual(output_str, 'four hundred and thirty nine')

    def test_translate_thousands(self):
        output_str = self.WriteCheque.translate_number('9007')
        self.assertEqual(output_str, 'nine thousand and seven')
    
    def test_translate_thousands(self):
        output_str = self.WriteCheque.translate_number('16001')
        self.assertEqual(output_str, 'sixteen thousand and one')
    

if __name__ == '__main__':
    unittest.main()


'''12
439
9007
123,000,000,001
'''
