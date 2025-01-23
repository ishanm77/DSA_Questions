class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        floor=-1
        ceil=-1
        for num in arr:
            if num<=x:
                if floor==-1 or num>floor:
                    floor=num
            if num>=x:
                if ceil==-1 or num<ceil:
                    ceil=num
        return [floor,ceil]