class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)

    def print_contact_info(self):
        print("%s's email: %s" % (self.name, self.email))
        print("%s's phone number: %s" % (self.name, self.phone))

    def add_friend(self, other_friend):
        self.friends.append(other_friend)
        print("%s has been added to %s's friend list." % (self.name, other_friend.name))

    def num_friends(self):
        friend_count = len(self.friends)
        if friend_count == 1:
            print(self.name + " has " + str(friend_count) + " friend right now.")
        else:
            print(self.name + " has " + str(friend_count) + " friends right now.")

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")      
bill = Person("Bill", "billbader@mail.com", "555-555-5555")

# sonny.greet(jordan)
# jordan.greet(sonny)

# sonny.print_contact_info()
# jordan.print_contact_info()

# sonny.add_friend(jordan)

# sonny.num_friends()

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

sonny.add_friend(jordan)
jordan.add_friend(sonny)
jordan.add_friend(bill)
#print(sonny.friends)
#print(jordan.friends)

# Count number of friends
sonny.num_friends()
jordan.num_friends()

sonny.greet(jordan)
sonny.greet(jordan)

# Count number of greetings
print(sonny.greeting_count)
print(jordan.greeting_count)

# Convert object to string
print(sonny)
print(jordan)

# Number of unique people greeted
sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()