class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            count += 1
            return count >= n
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i == 0 and flowerbed[i + 1] == 0:
                count +=1 
                flowerbed[i] = 1
            if flowerbed[i] == 0 and i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                count += 1
                flowerbed[i] = 1
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1 
        print(flowerbed)
        print(count)
        return count >= n