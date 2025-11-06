"""
Squirrel Research Problem.
"""
from typing import Dict, List
class SquirrelResearch:
    def __init__(self, locations: Dict[str, int]):
        """
        Initialize the SquirrelResearch object.
        Args:
            locations: A dictionary of location IDs and the number of levels in each location.

        Returns:
            None
        """
        self.locations = {}
        self.nuts = {}
        for location, num in locations.items():
            self.locations[location] = {}
            self.locations[location]["levels"] = [[] for _ in range(num)]
            self.locations[location]["capacity"] = self.fib(num)
    
    def fib(self, n: int) -> list[int]:
        """
        Calculate the capacity of each level in the locations.
        Args:
            n: The number of levels in the locations.

        Returns:
            A list of the capacity of each level in the locations.
        """
        if n == 0:
            return [1]
        if n == 1:
            return [1, 2]
        fib_list = [1, 2]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list

    def HideNut(self, timestamp: float, location_id: str, nut_id: str, nut_weight: float, time_to_expire: float) -> bool:
        """
        Hide a nut in a location.
        Args:
            timestamp: The timestamp when the nut is hidden.
            location_id: The ID of the location where the nut is hidden.
            nut_id: The ID of the nut.
            nut_weight: The weight of the nut.
            time_to_expire: The time to expire of the nut.

        Returns:
            True if the nut is hidden successfully, False otherwise.
        """

        if location_id not in self.locations:
            return False
        if nut_id in self.nuts:
            return False
        levelNum = -1
        for i in range(len(self.locations[location_id]["levels"])):
            if len(self.locations[location_id]["levels"][i]) < self.locations[location_id]["capacity"][i]:
                self.locations[location_id]["levels"][i].append((nut_id, nut_weight, timestamp + time_to_expire))
                levelNum = i
                break
        if levelNum == -1:
            return False
        return True

    def RetrieveNut(self, timestamp: float, location_id: str, max_squirrel_capacity_in_nuts: int) -> list[str]:
        if location_id not in self.locations:
            return []
        res = []
        for i in range(len(self.locations[location_id]["levels"]) - 1, -1, -1):
            if len(res) >= max_squirrel_capacity_in_nuts:
                break
            levelLength = len(self.locations[location_id]["levels"][i])
            if levelLength == 0:
                continue
            
            # Track which level each nut comes from
            availableNuts = [(nut, i) for nut in self.locations[location_id]["levels"][i]]
            if levelLength < self.locations[location_id]["capacity"][i] * 0.5 and i - 1 >= 0:
                availableNuts.extend([(nut, i - 1) for nut in self.locations[location_id]["levels"][i - 1]])
            
            # Sort by weight in descending order, then by nut_id in ascending order
            availableNuts.sort(key=lambda x: (-x[0][1], x[0][0])) 
            
            # Process nuts from this level
            for nut, level_idx in availableNuts:
                if len(res) >= max_squirrel_capacity_in_nuts:
                    break
                if nut[2] <= timestamp:
                    # Expired nut, remove it
                    if nut in self.locations[location_id]["levels"][level_idx]:
                        self.locations[location_id]["levels"][level_idx].remove(nut)
                else:
                    # Valid nut, collect it
                    res.append(nut[0])
                    if nut in self.locations[location_id]["levels"][level_idx]:
                        self.locations[location_id]["levels"][level_idx].remove(nut)
        return res



if __name__ == "__main__":
    locations = {
        "pineTree": 3,
        "oakTree": 1
    }
    squirrel_research = SquirrelResearch(locations)
    print(squirrel_research.HideNut(100, "pineTree", "nut1", 0.3, 600))
    print(squirrel_research.HideNut(101, "pineTree", "nut2", 0.5, 600))
    print(squirrel_research.HideNut(115, "pineTree", "nut4", 0.3, 600))
    print(squirrel_research.HideNut(115, "pineTree", "nut5", 0.4, 600))
    print(squirrel_research.RetrieveNut(142, "pineTree", 5))