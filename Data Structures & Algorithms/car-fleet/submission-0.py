class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hmap = {}

        for i in range(len(position)):
            distance = target - position[i]
            hours = distance / speed [i]
            hmap[position[i]] = hours 
        
        position.sort(reverse=True)

        curr = hmap[position[0]]
        fleets = 1
        for i in range(1, len(position)):
            if hmap[position[i]] > curr:
                curr = hmap[position[i]]
                fleets += 1
        
        return fleets
            


        