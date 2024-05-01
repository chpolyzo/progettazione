import os
candidati = ['Pippo', 'Pluto', 'Paperino']

def clearConsole():
    """
    Funzione che ha il solo scopo di pulire il video
    """
    command = "clear"
    os.system(command)


'''
We define a class called Election.
'''


class Election:
    '''
    The __init__ method initializes the attributes representing the number of registered voters, total voters, yes votes, and no votes.
    '''

    def __init__(self):
        self.registered_voters = 0
        self.total_voters = 0
        self.yes_votes = 0
        self.no_votes = 0

    '''
    The input_results method prompts the user to input the relevant data.
    include a validation step within the input_results method to ensure that the number of voters 
    is not more than the number of registered voters.
    After taking input for the number of voters (self.total_voters), it enters a while loop.
    Inside the loop, it checks if the number of voters (self.total_voters) 
    is less than or equal to the number of registered voters (self.registered_voters).
    If the condition is met (i.e., the number of voters is not more than the number of registered voters), the loop breaks.
    If the condition is not met (i.e., the number of voters is more than the number of registered voters), 
    it displays an error message and prompts the user to enter the number of voters again until a valid input is provided.
    '''

    def input_results(self):
        self.registered_voters = int(input("Enter the number of registered voters: "))
        while True:
            self.total_voters = int(input("Enter the number of voters: "))
            if self.total_voters <= self.registered_voters:
                break
            else:
                print("Error: Number of voters cannot exceed the number of registered voters.")
        self.yes_votes = int(input("Enter the number of 'Yes' votes: "))
        self.no_votes = int(input("Enter the number of 'No' votes: "))

    '''
    The calculate_voter_percentage, calculate_yes_percentage, and calculate_no_percentage methods calculate the respective percentages.
    '''

    def calculate_voter_percentage(self):
        return (self.total_voters / self.registered_voters) * 100

    def calculate_yes_percentage(self):
        return (self.yes_votes / self.total_voters) * 100

    def calculate_no_percentage(self):
        return (self.no_votes / self.total_voters) * 100

    '''
    The display_results method prints the calculated percentages.
    '''

    def display_results(self):
        print("Percentage of voters out of total registered:", self.calculate_voter_percentage(), "%")
        print("Percentage of 'Yes' votes:", self.calculate_yes_percentage(), "%")
        print("Percentage of 'No' votes:", self.calculate_no_percentage(), "%")


'''
In the main program, we create an instance of the Referendum class, input the results, and display the calculated percentages.
'''

# Main program
if __name__ == "__main__":
    referendum = Election()
    referendum.input_results()
    referendum.display_results()
