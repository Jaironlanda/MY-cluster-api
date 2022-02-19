from malaysia.state import states_list

# state = {"sabah": 12, "sarawak": 14, "kedah": 1}
# print(states_list())
my_input = "saRawaK"

for x in states_list():
    # print(states_list()[x])
    if my_input.capitalize() == x:
        print("The code is:")
        print(states_list()[x])
