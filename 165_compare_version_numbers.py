class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1, lst2 = version1.split("."), version2.split(".")
        lst1= [int(part) for part in lst1]
        lst2 = [int(part) for part in lst2]
        if lst1 == lst2:
            return 0
        p1, p2 = 0, 0
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] > lst2[p2]:
                return 1
            elif lst1[p1] < lst2[p2]:
                return -1
            p1 += 1
            p2 += 1
        if p1 < len(lst1):
            for num in lst1[p1:]:
                if num != 0:
                    return 1
        if p2 < len(lst2):
            for num in lst2[p2:]:
                if num != 0:
                    return -1
        return 0
    
class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1, lst2 = version1.split("."), version2.split(".")
        lst1= [int(part) for part in lst1]
        lst2 = [int(part) for part in lst2]
        n1, n2 = len(lst1), len(lst2)
        for i in range(max(n1, n2)):
            num1 = lst1[i] if i < n1 else 0
            num2 = lst2[i] if i < n2 else 0
            if num1 != num2:
                return -1 if num1 < num2 else 1
        return 0
        