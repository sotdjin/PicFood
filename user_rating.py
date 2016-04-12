import FP_user
import os
import sys
import re
import math
import json


def main():
    food_ratings = {}
    username = raw_input("username:")
    password = raw_input("password:")
    user = FP_user.PFUser(username, password)
    print "Please enter a type of food you like: "
    answer = raw_input()
    print "Please enter a rating for " + answer + "from 1 to 10: "
    rating = int(input())
    food_ratings[answer] = rating
    for food in food_ratings:
        user.add_ratings(food, food_ratings[food])
    user.print_food_ratings()
    
if __name__ == '__main__':
    main()
