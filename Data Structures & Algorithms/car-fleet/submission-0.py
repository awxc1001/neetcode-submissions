class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combine pos and speed in one list
        #zip combine multiple list index to a iterator
        #need to covert to list
        pos_speed = list(zip(position, speed))
        #sort the car like racing by their position
        pos_speed = sorted(pos_speed)
        #pos_speed = [(1,3), (4,2), (7,1)]

        # because cars cannot overtake, the front car / front fleet determines the 
        #cars behind it
        #they are the rightest of array,  so we process from right to left
        # when checking a car, the fleet in front has already been determined

        #initilise one outside loop, so first can compare
        #the stack stores inidivual fleet
        fleet_stack = []
        fleet_count = 0
        for i in range(len(pos_speed) - 1, -1 , -1):
            pos, spd = pos_speed[i]
            #we use / to get deciaml
            time_to_dst = (target - pos) / spd
            #start from right, put one first if empty because
            #its definitely a fleet
            if not fleet_stack:
                fleet_count += 1
                fleet_stack.append(time_to_dst)
            #now we check if next car time can catch up fleet_stack
            #smaller time means faster and can catch up from left
            #bigger times means cannot catch up and have to make a new fleet
            if time_to_dst > fleet_stack[-1]:
                fleet_count += 1
                fleet_stack.append(time_to_dst)

            elif time_to_dst < fleet_stack[-1]:
                continue
        
        return fleet_count

            

