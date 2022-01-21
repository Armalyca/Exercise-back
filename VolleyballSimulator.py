from random import randint
from decimal import Decimal

# Ask the user for the probabilities of T1 winning when T1 is serving and converting to integer
p1 = Decimal(input("Enter p1 (as a decimal between 0.0 and 1.0) : "))

# Ask the user for the probabilities of T2 winning when T2 is serving and converting to integer
p2 = Decimal(input("Enter p2 (as a decimal between 0.0 and 1.0) : "))


###### VARIABLES ######
pts1 = 0  # Number of points earned in a set for T1
pts2 = 0  # Number of points earned in a set for T2
listScores = []  # List of scores we display at the end
winSet1 = 0  # Number of sets won by T1
winSet2 = 0  # Number of sets won by T2
toAddResult = ""  # The score of previous set we show in the list at each line


###### FUNCTIONS ######

# Function to compute a point with the probabilities given
#
def compute_points(s, p1, p2, pts1, pts2):
    # Simulation of a random number to see if it is in the probability that the team win
    randomNb = randint(0, 100)
    if s == 1:  # If T2 served this time
        # We give add the point to T1 or T2 depending on the random number compared to the p1
        pts1 += 1 if randomNb < p1 else 0
        pts2 += 1 if randomNb > p1 else 0
        # Determine who serve next time (except new set)
        s = 1 if randomNb < p1 else 2
    elif s == 2:  # If T2 served this time
        # We give add the point to T1 or T2 depending on the random number compared to the p2
        pts2 += 1 if randomNb < p2 else 0
        pts1 += 1 if randomNb > p2 else 0
        # Determine who serve next time (except new set)
        s = 2 if randomNb < p2 else 1

    # Return (as a tuple) a string of the score of this set at this point and the points of T1 and T2
    return str(pts1) + '-' + str(pts2), pts1, pts2

# Function to compute a set with the probabilities given
#
def compute_set(maxPts, s, p1, p2, pts1, pts2, listScores, toAddResult):
    winnerSet = 0  # Value use to return who won the set

    while True:  # Do...while loop to compute the whole set
        # Use the text returned by the compute_points function to add a new string to the list we return at the end
        scoreToAdd, pts1, pts2 = compute_points(s, p1, p2, pts1, pts2)

        # Add the part of the string before the new score with 'toAddResult' string
        if len(toAddResult) == 0:
            listScores.append(scoreToAdd)
        else:
            listScores.append(toAddResult + " " + scoreToAdd)

        # Check if one of the team won (score superior to 25 or 15 + a 2 points difference between 2 teams)
        if pts1 >= maxPts and pts1 - pts2 >= 2:
            winnerSet = 1
            # When a team win, we add the final score of the set into the 'toAddResult' string (with space if it is not the first set)
            toAddResult += scoreToAdd if len(
                toAddResult) == 0 else " " + scoreToAdd
            break
        elif pts2 >= maxPts and pts2 - pts1 >= 2:
            winnerSet = 2
            # When a team win, we add the final score of the set into the 'toAddResult' string (with space if it is not the first set)
            toAddResult += scoreToAdd if len(
                toAddResult) == 0 else " " + scoreToAdd
            break

    # Return (as a tuple) who won, a string of previous set's score and the list of all scores
    return winnerSet, toAddResult, listScores


# For loop for the 5 possible sets
for i in range(1, 6):
    s = 1 if i % 2 == 1 else 2  # Variable to determine who will serve the point
    maxPts = 0

    # If one of the teams won 3 sets, they won the match so we exit the loop
    if winSet1 == 3 or winSet2 == 3:
        break
     # If there is a 5th set, the number of points to win is 15, else it is 25
    maxPts = 25 if i < 5 else 15

    # We update the number of sets won by each team with the result of the compute_set function
    resultSet, toAddResult, listScores = compute_set(
        maxPts, s, p1*100, p2*100, pts1, pts2, listScores, toAddResult)
    winSet1 += 1 if resultSet == 1 else 0
    winSet2 += 1 if resultSet == 2 else 0

# We display all the scores at the end
print(str(listScores))
