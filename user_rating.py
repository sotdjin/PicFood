import FP_user
import os
import sys
import re
import math
import json
import user_filtering
def main():
    foods=["Mexican","Asian","Thai","Pasta","Steak","Barbeque","Soul Food","Italian","Pizza","Chicken"]
    print "new user"
    username=raw_input("username:")
    password=raw_input("password:")
    user=FP_user.FP_user(username,password)
    for food in foods:
        print "Do you like ", food, " ?"
        answer=raw_input("yes or no")
        if(answer=="yes"):
            rating=int(input("rate from 1 to 10"))
            user.add_ratings(food,rating)
    user.print_food_ratings()
    
if __name__ == '__main__':
  main()
