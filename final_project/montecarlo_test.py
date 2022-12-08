import unittest
from montecarlo import Die, Game, Analyzer
import pandas as pd 
import numpy as np

class MontecarloTestSuite(unittest.TestCase):
    """Unit tests to test if the methods return valid outputs"""
    
    def test_die(self):
        # Test if weights is created properly: 
        faces_array = [1,2,3,4,5,6]
        test1 = Die(faces_array)
        x = 1
        if x not in test1.faces_weight_df['weight'].values:
            raise AssertionError
   
   
    def test_weight_change(self):
        # Test the change_change() method: 
        faces_array = [1,2,3,4,5,6]
        test2 = Die(faces_array)
        test2.weight_change(5,5)
        assert (test2.faces_weight_df[test2.faces_weight_df['faces']==5]
        ['weight'],5)

    def test_roll(self):
        #Test to see if roll method works 5 rolls:
        faces_array = [1,2,3,4,5,6]
        test3 = Die(faces_array)
        roll = test3.roll(5)
        self.assertEqual(len(roll),5)

    def test_show(self): 
        #Tests if the roll is saved to df:
        faces_array = [1,2,3,4,5,6]
        test4 = Die(faces_array)
        test4_df = test4.show()
        test4_type = type(test4_df)
        x = pd.DataFrame()
        pd_type = type(x) 
        self.assertEqual(test4_type, pd_type)
        

    def test_play(self):
        # Tests if Dice is rolled at specified shape:
        faces_array = ([1,2,3,4,5])
        test4_1 = Die(faces_array)
        test4_2 = Die(faces_array)
        test4_3 = Die(faces_array)
        test4_4 = Die(faces_array)
        test4_5 = Die(faces_array)

        test4_dice_list = ([test4_1,test4_2,test4_3,test4_4,test4_5])
        test4_game = Game(test4_dice_list)
        test4_game.play(4)
        #show = public df
        test4_df = test4_game.show()
        expected_df = (4,5)
        actual_df = test4_df.shape
        self.assertEqual(actual_df, expected_df)
    
    def test_show(self):
        # Tests if Dice is rolled at specified shape:
        faces_array = ([1,2,3])
        test5_1 = Die(faces_array)
        test5_2 = Die(faces_array)
        
        test5_dice_list = ([test5_1,test5_2])
        test5_game = Game(test5_dice_list)
        test5_game.play(2)
        
        #show = public df
        test5_df = test5_game.show()
        expected_df = (2,2)
        actual_df = test5_df.shape
        self.assertEqual(actual_df, expected_df) 

    def test_face_counts_per_roll(self): 
        #checks to see if counts faces into a df: 
        faces_array = ([1,2,3])
        test6_1 = Die(faces_array)
        test6_2 = Die(faces_array)
        test6_dice_list = ([test6_1,test6_2])

        test6_game = Game(test6_dice_list)
        test6_game.play(2)
        test6_analyzer = Analyzer(test6_game)
        test6_df = test6_analyzer.face_counts_per_roll()
        shape = test6_df.shape[0]
        expected = 2
        self.assertEqual(shape, expected) 
        


    def test_jackpot(self):
        #checks if it gets winner number
        faces_array = ([1,2,3])
        test7_1 = Die(faces_array)
        test7_2 = Die(faces_array)
        test7_dice_list = ([test7_1,test7_2])

        test7_game = Game(test7_dice_list)
        test7_game.play(2)
        test7_analyzer = Analyzer(test7_game)
        test7_df = test7_analyzer.jackpot()
        self.assertIsInstance(test7_df, int)

    def test_combo(self): 
        #checks if combo returns df: 
        faces_array = ([1,2,3])
        test8_1 = Die(faces_array)
        test8_2 = Die(faces_array)
        test6_dice_list = ([test8_1,test8_2])

        test8_game = Game(test6_dice_list)
        test8_game.play(2)
        test8_analyzer = Analyzer(test8_game)
        test8_df = test8_analyzer.combo().size
        self.assertGreater(test8_df, 0)

if __name__ == '__main__':
    unittest.main(verbosity=3)