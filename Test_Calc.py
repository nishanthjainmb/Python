import unittest
import Calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Calc.add(50,50),100)
        self.assertEqual(Calc.add(20,-50),-30)
        self.assertEqual(Calc.add(-20,10),-10)

        self.assertRaises(ValueError,Calc.div,10,0)

if __name__=='__main__':
    unittest.main()
