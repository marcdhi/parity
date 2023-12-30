from django.db import models
import string
import random

# Generating the unique joining code
def generate_unique_code():
    # Creating the unique code
    length = 6

    # Creating the while loop
    while True:

        # Creating the code
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        #####
        # Now we must check if the code is unique, and is not assigned to any other room already in the database
        # If the code is unique, then we can break out of the loop
        # The logic to check if the code is unique is to check if the code is in the database
        #####

        if Room.objects.filter(code=code).count() == 0:
            break

    return code

#####
# Adding all the models for the database
#####

class Room(models.Model):
    # Creating the room code
    code = models.CharField(max_length=8, default="", unique=True)
    # Creating the host of the room
    host = models.CharField(max_length=50, unique=True)
    # Creating the guest can pause
    guest_can_pause = models.BooleanField(null=False, default=False)
    # Creating the vote to skip
    votes_to_skip = models.IntegerField(null=False, default=1)
    # Creating the created at time
    created_at = models.DateTimeField(auto_now_add=True)
