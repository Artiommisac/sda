class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        suma = 0
        rezultat = []

        for numar in nums:
            suma = suma + numar
            rezultat.append(suma)

        return rezultat