# DEFINE 2 COMMONLY USED SUBROUTINES
def isYes(prompt):
    answer = input(prompt + '\nAnswer y for yes, any other key for no: ')
    if answer == 'y':
        return True
    else:
        return False


def chooseInteger(a, b):
    while True:  # indefinite loop until acceptable value returned
        answer = input('Enter an option between {a} and {b}: ')
        try:
            answer = int(answer)
            if answer in range(a, b + 1):
                return answer  # VALIDATION and return integer
            else:
                print('Error: number out of bounds, try again')  # NEW!!!!!
        except:
            print('Error: enter a numerical answer only')  # an error message


# MAIN BODY OF PROGRAM
import datetime

# Define blank databases for members and sponsors and some constants
loading = True  # loading, a CONSTANT, to keep a loop running until exited
today = datetime.date.today()  # the date today
members = []  # an empty array which will contain arrays, one row for each member
sponsorName = []  # An array to contain the names of sponsors NEW!!!!!!!
sponsorMessage = []  # An array to contain the messages of each sponsor NEW!!!!!!!
# NOTE that a sponsor's name and message will have the same index value
# SponsorNames is a 2-D array, each row contains an array of firstname and surname
# sponsorMessage is a simple array, each entry is a sponsor's message

while loading:  # INDEFINITE LOOP
    # TASK 1 OR 3
    print('MAIN MENU\n1 : Membership Registration\n2 : Plank Sponsorship')
    service = chooseInteger(1, 2)

    # GET NAMES (RELEVANT TO TASK 1 AND 3) WOULD NEED TO BE INCLUDED IN DESCRIPTION OF EITHER TASK!
    while True:  # Obtain forename and surname, repeat until two names given
        answer = input('Enter forename and surname of customer: ')
        try:
            forename, surname = answer.split();  break  # leave when 2 names given
        except:
            print('Error: enter two names only')

    if service == 1:  # TASK 1

        if isYes('Does member wish to volunteer?'):  # Get volunteer status
            print('volunteer at?\n1 : Pier Entrance Gate \n2 : Gift Shop \n3 : Painting and Decorating')
            volunteer = chooseInteger(1, 3)  # will be a VARIABLE
        else:
            volunteer = 0

        while True:  # Get date of joining
            joined = input('Input the date of joining, YYYY-MM-DD: ')
            try:  # VALIDATION
                join_date = datetime.date.fromisoformat(joined)
                if (today - join_date).days < 0:
                    print('Error: join date cannot be in the future')
                else:
                    break  # Leave date loop once satified requirements
            except:
                print('Error: not a valid date')

        paid = isYes('Has member paid $75 fee?')
        members.append([forename, surname, volunteer, join_date, paid])
        # Note: a whole new row has been appended to members
    # END OF TASK 1
    else:  # TASK 3

        while True:  # message loop
            message = input('Please enter sponsor\'s message (max 255 char): ')
            if len(message) > 255:
                print('Error: message too long')  # VALIDATION (length check)
            else:
                break  # if fine, exit message loop

        print('Name:', forename, surname, '\nMessage:', message)  # VERIFICATION (Proofreading)
        if isYes('Are the details correct?'):
            sponsorName.append([forename, surname])  # add name to array NEW!!!
            sponsorMessage.append(message)  # add corresponding message to different array NEW!!!
            print('PLEASE CHARGE SPONSOR $200')
        else:
            continue  # go back to start of main loop and try again

    loading = isYes('Would you like to begin a new sale?')  # if done, set loading to False, will then escape loop

# END OF TASKS 1 & 3
# START OF TASK 2
print(members);
print(sponsorName);
print(sponsorMessage)

print('\nMEMBERS WHO VOLUNTEER')
for record in members:  # Members without 0 in volunteer column
    # NOTE: record represents a row in members array, each row is visited in this loop
    if record[2] != 0: print(record[0], record[1])

locations = ['Pier Entrance Gate', 'Gift Shop', 'Painting and Decorating']  # a constant and an array
for i in range(3):  # sequentially lists all 3 working areas and their members
    print('\nMEMBERS WHO VOLUNTEER TO WORK AT ' + locations[i])
    for record in members:  # LOOP THROUGH EACH ROW IN ARRAY
        # NOTE: i+1 matches index of location to corresponding value in 'record'
        if record[2] == i + 1: print(record[0], record[1])

print('\nEXPIRED MEMBERSHIPS')
for record in members:  # find time difference, is it more than 365 days?
    if (today - record[3]).days > 365: print(record[0], record[1])

print('\nMEMBERS WHO HAVE NOT YET PAID $75')
for record in members:  # NOT paid - very important, prints if record[4] is 'False'
    if not record[4]: print(record[0], record[1])
# END OF TASKS
