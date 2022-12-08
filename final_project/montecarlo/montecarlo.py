import pandas as pd
import numpy as np

class Die: 
    """ Die class that has N sides/faces,and W Weights, 
    which can be rolled to select a face"""

    def __init__(self, faces_array):
        """
        Takes an array of faces 
        Internally initializes weights to 1.0 for each face
        Saves faces & weights to a private dataframe
        """
        self.faces_array = faces_array
        self.weight_array = np.ones_like(faces_array)
        self.faces_weight_df = pd.DataFrame({'faces': self.faces_array, 'weight': self.weight_array})

    def weight_change(self, face_value, new_weight):
        """
        A method to change weight of a single side 
        Checks to see if the face passed is valid
        Checks to see if the weight is valid
        """

        if face_value in self.faces_weight_df['faces'].values:
            if isinstance(new_weight, float):
                self.faces_weight_df.at[self.faces_weight_df['faces'] == face_value, 'weight'] = new_weight
            else:
                np.float32(new_weight)
                self.faces_weight_df.at[self.faces_weight_df['faces'] == face_value, 'weight'] = new_weight
                #raise TypeError('New Weight must be a float -- Automatically Converted' )
        else:
            raise IndexError('Face is not in the Dataframe')
        

    def roll(self, rolls = 1):
        """
        A method to roll the die one or more times
        Takes a parameter of how many rolls
        Random Sample from the vector of faces according to the weights
        Returns a list of outcomes
        """
        rolled_outcomes = self.faces_weight_df.sample(n = rolls, weights = 'weight', replace = True)
        return list(rolled_outcomes['faces'])

    def show(self):
        """Returns the dataframe with all its glory: Intialized and/or Updated."""
        return self.faces_weight_df

class Game:
    """
    A game consists of rolling of one or more dice of the same kind one or more times
    Each game is initialized with a list of one or more of similarly defined dice (Die objects)
    By “same kind” and “similarly defined” we mean that each die in a given game has the same number of sides and set of faces,
    but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to roll all of the dice a given number of times.
    The class keeps the results of its most recent play.
    
    """

    def __init__(self, Dice):
        """Takes a single parameter, a list of already instantiated similar Die objects"""
        self.Dice = Dice

    def play(self, rolls):
        """Takes a parameter to specify how many times the dice should be rolled
        Saves the result of the play to a private dataframe of shape N rolls by M dice"""
        self._play_outcome = pd.DataFrame()
        self.rolls = rolls
        M_Dice = 1

        for die in self.Dice:
            dice_results = die.roll(rolls=rolls)
            M_Dice += 1
            series = pd.Series(dice_results, name = f'Die Number {M_Dice}')
            self._play_outcome = pd.concat([self._play_outcome,series], axis =1)
        
        self._play_outcome['Roll'] = self._play_outcome.index + 1
        self._play_outcome = self._play_outcome.set_index('Roll')
        return self._play_outcome
        
    def show(self, form = 'wide'):
        """A method to show the user the results of the most recent play.
        This method just passes the private dataframe to the user.
        Takes a parameter to return the dataframe in narrow or wide form"""

        if form == 'wide':
            #making it public: 
            self.play_outcome = self._play_outcome
            return(self.play_outcome)
        elif form == 'narrow':
            self.narrow_play_outcome = self._play_outcome.stack()
            return(self.narrow_play_outcome)
        else: 
            raise TypeError('wide or narrow inputs only' )

class Analyzer:
    """An analyzer takes the results of a single game 
    Computes various descriptive statistical properties about it"""

    def __init__(self, game):
        """Takes a game object as its input parameter
        Initialization time, it also infers the data type of the die faces used."""
        self.game_df = game.show()
    
    def face_counts_per_roll(self):
        """Stores the results as a dataframe in a public attribute
        Dataframe has an index of the roll number and face values as columns """
        
        self.face_counts_per_roll = self.game_df.apply(lambda x: x.value_counts(), axis = 1)
        return self.face_counts_per_roll


    def jackpot(self):
        """A jackpot method to compute how many times the game resulted in all faces being identical"""
        
        df = self.face_counts_per_roll()
        jackpot_df = df[df.nunique(1) == 1]
        winners = len(jackpot_df)
        return winners
       
    def combo(self):
        """A combo method to compute the distinct combinations of faces rolled, along with their counts"""
        
        self.combo = self.game_df.apply(lambda x: x.sort_values().transpose(), axis=1).value_counts().to_frame('Count')
        self.combo = self.combo.sort_values(by='Count',ascending=False)
        return(self.combo)


