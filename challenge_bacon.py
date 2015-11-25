# Create "Should you eat that Bacon" or "Should you eat that Vegan Bacon" game
# Write code as functions
# Use raw_input()for global scope
# Use conditionals to move throught the game
# Validate user responses from global variable from raw_input() within function

print "Game: Should you eat that bacon?"
print
print "It feels like angels are frolicking on your taste buds."
answer = raw_input("Do you like bacon? Type yes, maybe or no: ")
def eatBacon(answer):
    if (answer == "yes") or (answer == "Yes") or (answer == "YES"):
        return "Eat it darling !"
    elif (answer == "maybe") or (answer == "Maybe") or (answer == "MAYBE"):
        print "You are afraid bacon will kill you."
        coward = raw_input ("Are you a coward? Type yes or no: ")
        if (coward == "no") or (coward == "No") or (coward == "NO"):
            return "You are not a coward. Then eat it sweetheart."
        else:
            return "You are a coward.  Bacon will turn you into a true warrior."
    else:
        return "You've clearly never eaten bacon.  So eat it !"


print eatBacon(answer)
