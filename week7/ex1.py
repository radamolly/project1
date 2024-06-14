class Home:
    def __init__(self):
        print("Home is calling")
    def furnish(self, furniture):
        return "I'm furnish " + furniture
    
    def cleaning(self, thing):
        return "I'm cleaning the : " + thing
    
home = Home()
print(home.furnish('Sofar'))
print(home.furnish('TV'))
print(home.furnish('Lightings'))

print(home.cleaning('Bedroom'))
print(home.cleaning('Bathroom'))
