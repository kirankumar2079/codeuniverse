state = {
    'monkey' : 'A' ,
    'box' : 'B' ,
    'banana'  : 'C' ,
    'on_box' : False,
    'has_banana' : False
}

def move(position):
    print(f"Monkey moves from {state['monkey']} to {position}")
    state['monkey'] = position

def push_box(position):
    if state['monkey'] == state['box']:
        print(f"Monkey pushes the box from {state['box']} to {position}")
        state['box'] = position
        state['monkey'] = position
    else:
        print("Monkey is not near the box")

def climb_box():
    if state['monkey'] == state['box']:
        print("Monkey climbs onto the box")
        state['on_box'] = True
    else:
        print('Box is not at the monkeys position')

def grab_banana():
    if state['on_box'] and state['box'] == state['banana']:
        print("Monkey grabs the banana")
        state['has_banana'] = True
    else:
        print('Cannot reach the banana')



print("Initial State: " , state)
print("-------------")

move('B')

push_box('C')

climb_box()

grab_banana()


print("---------")
print("Final State : " , state)