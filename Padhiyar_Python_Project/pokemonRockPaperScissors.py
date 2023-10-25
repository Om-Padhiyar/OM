import random

#allows a random selection to be made


#defines a function used whenever the result is a tie
def tie():
  print(
      "Nobody Wins. The types are either neutral, not very effective, of immune (Or super effective on each other if dragon or ghost). Play Again."
  )


#creates a list that data will be pulled from
PokemonTypes = [
    "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison",
    "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark",
    "Steel", "Fairy", "Normal"
]
#Creates the variable to see who wins
PlayerWin = ("Tie")
#Has the computer select a random value from the above list
computerSelection = random.choice(PokemonTypes)
#prints the introduction to the game
print(
    "Hello! Welcome to Pokemon Rock Paper Scissors! Here, you say a pokemon type, then a random type is generated, and it shows the matchup. If the matchup is super effective, then the game will end and a winner will be declared."
)

print("The types are:")
print("Fire")
print("Water")
print("Grass")
print("Electric")
print("Ice")
print("Fighting")
print("Poison")
print("Ground")
print("Flying")
print("Psychic")
print("Bug")
print("Rock")
print("Ghost")
print("Dragon")
print("Dark")
print("Steel")
print("Fairy")
print("Normal")

#Sets a boolean to validate if the type is on the list
ValidateType = False
#Is the type is not valid, it loops
while ValidateType == False:
  YourPokemonType = input("Pick a Pokemon Type: ")
  #Determines if the type is valid by comparing it to each type on the list and then prints your corresponding selection
  for element in PokemonTypes:
    if YourPokemonType.lower() == PokemonTypes[0].lower():
      ValidateType = True
      print("You Chose the Fire Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[1].lower():
      ValidateType = True
      print("You Chose the Water Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[2].lower():
      ValidateType = True
      print("You Chose the Grass Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[3].lower():
      ValidateType = True
      print("You Chose the Electric Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[4].lower():
      ValidateType = True
      break
      print("You Chose the Ice Type!")
    elif YourPokemonType.lower() == PokemonTypes[5].lower():
      ValidateType = True
      print("You Chose the Fighting Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[6].lower():
      ValidateType = True
      print("You Chose the Poison Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[7].lower():
      ValidateType = True
      print("You chose the Ground Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[8].lower():
      ValidateType = True
      print("You Chose the Flying Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[9].lower():
      ValidateType = True
      print("You Chose the Psychic Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[10].lower():
      ValidateType = True
      print("You Chose the Bug Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[11].lower():
      ValidateType = True
      print("You Chose the Rock Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[12].lower():
      ValidateType = True
      print("You Chose the Ghost Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[13].lower():
      ValidateType = True
      print("You Chose the Dragon Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[14].lower():
      ValidateType = True
      print("You Chose the Dark Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[15].lower():
      ValidateType = True
      print("You Chose the Steel Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[16].lower():
      ValidateType = True
      print("You Chose the Fairy Type!")
      break
    elif YourPokemonType.lower() == PokemonTypes[17].lower():
      ValidateType = True
      print("You Chose the Normal Type!")
      break
    else:
      print("Invalid Pokemon Type")
      YourPokemonType = input("Try Again: ").lower()
  #Else statement makes it loop if not a valid type

print("The computer has chosen " + computerSelection + "!")
#Displays the random selection from the list
print("The matchup is " + YourPokemonType + " against " +
      computerSelection.lower() + "!")
#Displays the matchup between the two pokemon types

#Every super effective type matchup is shown here except for those that are super effective on each other, which I will count as a tie. When one matchup is seen, then the corresponding value will be set for the PlayerWin variable - either to win, lose, or tie.

if YourPokemonType.lower() == "fire" and computerSelection == "Water":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fire" and computerSelection == "Rock":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fire" and computerSelection == "Ground":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "water" and computerSelection == "Grass":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "water" and computerSelection == "Electric":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "grass" and computerSelection == "Fire":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "grass" and computerSelection == "Flying":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "grass" and computerSelection == "Poison":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "grass" and computerSelection == "Bug":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "grass" and computerSelection == "Ice":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "electic" and computerSelection == "Ground":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "normal" and computerSelection == "Fighting":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fairy" and computerSelection == "Poison":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fairy" and computerSelection == "Steel":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "dragon" and computerSelection == "Ice":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "dragon" and computerSelection == "Fairy":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Flying":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Psychic":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Fairy":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "psychic" and computerSelection == "Dark":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "psychic" and computerSelection == "Ghost":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "psychic" and computerSelection == "Bug":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "steel" and computerSelection == "Fighting":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "steel" and computerSelection == "Fire":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "steel" and computerSelection == "Ground":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ice" and computerSelection == "Fire":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ice" and computerSelection == "Rock":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ice" and computerSelection == "Fighting":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ice" and computerSelection == "Steel":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "dark" and computerSelection == "Bug":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "dark" and computerSelection == "Fairy":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "dark" and computerSelection == "Fighting":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ghost" and computerSelection == "Dark":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ground" and computerSelection == "Ice":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ground" and computerSelection == "Grass":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "ground" and computerSelection == "Water":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "rock" and computerSelection == "Steel":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "rock" and computerSelection == "Grass":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "rock" and computerSelection == "Water":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "rock" and computerSelection == "Fighting":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "rock" and computerSelection == "Ground":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "flying" and computerSelection == "Electric":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "flying" and computerSelection == "Rock":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "flying" and computerSelection == "Ice":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "poison" and computerSelection == "Psychic":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "poison" and computerSelection == "Ground":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "bug" and computerSelection == "Flying":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "bug" and computerSelection == "Rock":
  PlayerWin = ("Lose")
elif YourPokemonType.lower() == "bug" and computerSelection == "Fire":
  PlayerWin = ("Lose")
elif computerSelection.lower() == "fire" and YourPokemonType.lower == "water":
  PlayerWin = ("Win")
elif computerSelection.lower() == "fire" and YourPokemonType.lower() == "rock":
  PlayerWin = ("Win")
elif computerSelection.lower() == "fire" and YourPokemonType.lower(
) == "ground":
  PlayerWin = ("Win")
elif computerSelection.lower() == "water" and YourPokemonType.lower(
) == "grass":
  PlayerWin = ("Win")
elif computerSelection.lower() == "water" and YourPokemonType.lower(
) == "electric":
  PlayerWin = ("Win")
elif computerSelection.lower() == "grass" and YourPokemonType.lower(
) == "fire":
  PlayerWin = ("Win")
elif computerSelection.lower() == "grass" and YourPokemonType.lower(
) == "flying":
  PlayerWin = ("Win")
elif computerSelection.lower() == "grass" and YourPokemonType.lower(
) == "poison":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "bug" and computerSelection == "Grass":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ice" and computerSelection == "Grass":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ground" and computerSelection == "Electric":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Normal":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "poison" and computerSelection == "Fairy":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "steel" and computerSelection == "Fairy":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ice" and computerSelection == "Dragon":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fairy" and computerSelection == "Dragon":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "flying" and computerSelection == "Fightng":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Fighting":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fairy" and computerSelection == "Fighting":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "dark" and computerSelection == "Psychic":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ghost" and computerSelection == "Psychic":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "bug" and computerSelection == "Psychic":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Steel":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fire" and computerSelection == "Steel":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ground" and computerSelection == "Steel":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fire" and computerSelection == "Ice":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "rock" and computerSelection == "Ice":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Ice":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "steel" and computerSelection == "Ice":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "bug" and computerSelection == "Dark":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fairy" and computerSelection == "Dark":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Dark":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "dark" and computerSelection == "Ghost":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ice" and computerSelection == "Ground":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "grass" and computerSelection == "Ground":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "water" and computerSelection == "Ground":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "steel" and computerSelection == "Rock":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "grass" and computerSelection == "Rock":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "water" and computerSelection == "Rock":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fighting" and computerSelection == "Rock":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ground" and computerSelection == "Rock":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "electric" and computerSelection == "Flying":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "rock" and computerSelection == "Flying":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ice" and computerSelection == "Flying":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "pyschic" and computerSelection == "Poison":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "ground" and computerSelection == "Poison":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "flying" and computerSelection == "Bug":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "rock" and computerSelection == "Bug":
  PlayerWin = ("Win")
elif YourPokemonType.lower() == "fire" and computerSelection == "Bug":
  PlayerWin = ("Win")
else:
  PlayerWin = ("Tie")

#Declares who won and the matchup
if PlayerWin == "Win":
  print("You win! " + YourPokemonType.lower() + " is super effective on " +
        computerSelection + "!")
elif PlayerWin == "Lose":
  print("You Lost! " + computerSelection + " is super effective on " +
        YourPokemonType.lower() + "!")
else:
  tie()

#Asks for a number value of how much they enjoyed playing.
Enjoyment = int(input("Rate your experience on a scale of 1-10: "))

while Enjoyment < 1 or Enjoyment > 10:
  Enjoyment = int(input("Please enter a valid response: "))
#If they put a number that is outside the range of 1-10, then it loops
print("Your response was: " + str(Enjoyment) +
      ". Thank you for your response.")
#finishes off with a print statement using the value previoussly taken from the user input and put into the string.
