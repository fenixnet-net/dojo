# note: use of max and min, and interating over the entire array, all come with cheap costs at this input size.
#       these would need to be rethought at larger data set sizes.

class Solution:
    def validateInput(self, height: List[int]) -> bool:
        valid = True
        if len(height) < 2:
            valid = False
            raise ValueError('height array too short ( {} < 2)'.format(len(height)))

        if len(height) > 10e5:
            valid = False
            raise ValueError('height array too long ( {} > 10e5)'.format(len(height)))

        if min(height) < 0:
            valid = False
            raise ValueError('minimum hight too small ( {} < 0 )'.format(min(height)))

        if max(height) > 10e4:
            valid = False
            raise ValueError('minimum hight too large ( {} > 10e4 )'.format(min(height)))

        return valid

    def maxArea(self, height: List[int]) -> int:
        if not self.validateInput(height):
            return -1

        l = 0
        r = len(height) -1 # mind the zero-index gap
        v = 0

        while(l < r):
            vol = min(height[l], height[r]) * (r - l)
            if vol > v:
                v = vol

            # bias toward moving left pointer in a tie
            # only look for edges/heights taller than existing ones
            #    anything same or shorter will have less volume on a shorter base length
            if height[l] <= height[r]:
                left = height[l]
                while(height[l] <= left and l < r):
                    l+=1
            else:
                right = height[r]
                while(height[r] <= right and r > l):
                    r-=1

        return v
