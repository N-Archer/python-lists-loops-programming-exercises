parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(my_list):
    state = {"total_slots": 0, "available_slots": 0, "occupied_slots": 0}
    for ele in my_list:
        print("ele:", ele)
        for elm in ele:
            print("elm:", elm)
            if elm == 1:
                state["occupied_slots"] += 1
                state["total_slots"] += 1
            elif elm == 2:
                state["available_slots"] += 1
                state["total_slots"] += 1
    return state



print(get_parking_lot(parking_state))

