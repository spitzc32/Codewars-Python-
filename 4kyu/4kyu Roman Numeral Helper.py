
class RomanNumerals:

    @staticmethod
    def to_roman(input):
        rnl = [ { '4' : 'MMMM', '3' : 'MMM', '2' : 'MM', '1' : 'M', '0' : '' }, { '9' : 'CM', '8' : 'DCCC', '7' : 'DCC',
          '6' : 'DC', '5' : 'D', '4' : 'CD', '3' : 'CCC', '2' : 'CC', '1' : 'C', '0' : '' }, { '9' : 'XC',
          '8' : 'LXXX', '7' : 'LXX', '6' : 'LX', '5' : 'L', '4' : 'XL', '3' : 'XXX', '2' : 'XX', '1' : 'X',
          '0' : '' }, { '9' : 'IX', '8' : 'VIII', '7' : 'VII', '6' : 'VI', '5' : 'V', '4' : 'IV', '3' : 'III',
          '2' : 'II', '1' : 'I', '0' : '' }]
        return reduce(lambda x, y: x + y, map(lambda x, y: rnl[x][y], range(4), str( input).zfill(4))) if -1 < input < 5000 else None
    
    @staticmethod
    def from_roman(input):
        numeral = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        nums = [numeral[i] for i in input.upper() if i in numeral]
        return sum([i if i>=nums[min(j+1, len(nums)-1)] else -i for j,i in enumerate(nums)])
