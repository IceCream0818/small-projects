pi = 3.141592653589793238462643383279502

#rounds down float arguments
#input: int or int in string
def factorial(num):
    try:
        num = int(float(num))
        if num < 0:
            print('enter a positive number to factorial')
            return
        n = 0
        final = 1
        while n < num:
            final *= num - n
            n += 1
        return final
    except:
        print('enter a valid number for factorial')

#print(factorial(input('type a number: ')))

def sine(num):
    try:
        num %= (2*pi)
 #    degree parameter (work on this later)
 #       if degree == True:
 #           num = num/180*pi
        temp = 0
        for x in range(10):
            temp += (-1)**x /factorial(2*x+1) * num**(2*x+1)
        return temp
    except:
        print("error with sine")

#abandoned idea 
#ifDegree = input('calculate in degree?(True/False): ')

#testing
#radian = float(input('enter the angle: '))
#print(f"sine of {radian} = {sine(radian):.10f}")


def cosine(num):
    try:
        num %= (2*pi)
        temp = 0
        for x in range(10):
            temp += (-1)**x /factorial(2*x) * num**(2*x)
        return temp
    except:
        print("error with cosine")
  
#print(f"cosine of {radian} = {cosine(radian):.10f}")

def tangent(num):
    try:
        if abs(cosine(num)) < 0.0000000001:
            return(f"asymptote at this point")
        elif abs(sine(num)) < 0.0000000001:
            return(0)
        else:    
            return round(sine(num)/cosine(num),10)
    except:
        print("error with tangent")

#print(f"tangent of {radian} = {tangent(radian)}")

inverseNumber = float(input('type a number: '))

def arcsin(num):
        temp = 0
#if abs(num) >= 0.8
#new function model
        if abs(num) <= 1:
            for x in range(20):
                temp += factorial(2*x)/((4**x)*((factorial(x))**2)*(2*x + 1)) * num**(2*x + 1)
            return temp
        else:
            return(f'{num} is not in domain of arcsin')

print(f"arcsin of {inverseNumber} = {arcsin(inverseNumber)}")
        
def arccos(num):
    try:
        if abs(num) <= 1:
            return pi/2 - arcsin(num)
        else:
            return(f'{num} is not in domain of arccos')
    except: 
        print('error with arccos')
    
print(f"arccos of {inverseNumber} = {arccos(inverseNumber)}")

def arctan(num):
    try:
        temp = 0
        #approximation when close to 1
        if abs(num) > 0.940 and abs(num) < 1.06:
            return(0.5*num + 0.2854)
        elif abs(num) < 1:
            for x in range(20):
                temp += (-1)**(x) * num**(2*x+1)/(2*x+1)
            return(temp)
        else:
            for x in range (20):
                temp += (-1)**(x+1) / (num**(2*x+1)*(2*x+1))
            if(num<0):
                return(temp - pi/2)
            else:
                return(temp + pi/2)
    except:
        print('error with arctan')

print(f"arctan of {inverseNumber} = {arctan(inverseNumber)}")
#input: number or number in string