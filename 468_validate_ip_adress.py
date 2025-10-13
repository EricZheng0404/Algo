class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        elements = queryIP.split(".")
        if self.ipv4(elements):
            return "IPv4"

        elements = queryIP.split(":")
        if self.ipv6(elements):
            return "IPv6"
        return "Neither"
    
    def ipv4(self, elements):
        if len(elements) != 4:
            return False
        for element in elements:
            for char in element:
                if char.isdigit() is False:
                    return False
            if len(element) < 1 or len(element) > 3:
                return False
            if int(element) > 255:
                return False
            if len(element) > 1 and element[0] == "0":
                return False
        return True
        
    def ipv6(self, elements):
        if len(elements) != 8:
            return False
        for element in elements:
            if len(element) > 4 or len(element) < 1:
                return False
            for char in element:
                if char.isalnum() is False:
                    return False
                if not ((char >= "a" and char <= "f") or (char >= "A" and char <= "F") or ("0" <= char <= "9")):
                    return False
        return True
                