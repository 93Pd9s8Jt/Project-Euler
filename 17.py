digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
sum = 0
def getLetterCount(i):
    #print(sum)
    sum=0
    num = i%100
    if num < 1:
        sum+=0 # do nothing
    elif num < 10:
        sum+=len(digits[num-1])
    elif num < 20:
        sum+=len(teens[num-10])
    elif num < 100:
        t = len(tens[num//10-2])
        if num%10!=0:
            o = len(digits[num%10-1])
        else:
            o=0
        sum += (t+o)
    if i > 99:
        sum+= len(digits[i//100-1])
        sum+= len('hundred')
        if num != 0:
            sum+= len('and')
    return sum
for i in range(1,1000):
    sum += getLetterCount(i)
sum+= len('onethousand')
print(sum)
