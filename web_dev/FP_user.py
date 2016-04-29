class PFUser:
    username = ""
    password = ""
    food_ratings = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def display_user(self):
        print "username:", self.username, "     password:", self.password
        
    def add_ratings(self, key, rating):
        self.food_ratings[key] = rating
    
    def user_food_ratings(self):
        return self.food_ratings
        
    def print_food_ratings(self):
        print self.food_ratings
