class Solution:
    def validateInput(self, intervals: List[List[int]]) -> bool:
        valid = True

        if len(intervals) < 1:
            valid = False
            raise ValueError('intervals list is too short ({} < 1)'.format(len(intervals)))
        if len(intervals) > 10e4:
            valid = False
            raise ValueError('intervals list is too long ({} > 10e4)'.format(len(intervals)))

        lengths=[len(x) for x in intervals]
        if max(lengths)!=min(lengths)!=2:
            valid = False
            raise ValueError('incorrect tuple length found (min: {}, max: {})'.format(min(lengths), max(lengths)))

        for x in intervals:
            if not 0<=x[0]<=x[1]<=10e4:
                valid = False
                raise ValueError('invalid tuple value found ( 0 <= {} <= {} <= 10e4 fails )'.format(x[0],x[1]))

        return valid

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not self.validateInput(intervals):
            return None

        intervals.sort() #guarantee order
        merged = [ intervals.pop(0) ]

        while(len(intervals) > 0):
            left = merged.pop()
            right = intervals.pop(0)

            if left[1] >= right[0]:
                merged += [ [left[0],right[1]] ]
            else:
                merged += [ left, right ]

        return merged
