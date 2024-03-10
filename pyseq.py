import math
import numpy as np

class geometricsequence:
    def __init__(self,sequence=None,r=None,an=None,a1=None,n=None):
        if sequence != None:
            if r == 1 or an == 1 or a1 == 1 or n == 1:
                raise Exception("Method not valid. Enter the correct method either: 1). Enter sequence (only enter sequence) or 2). Enter method (only enter r, an, a1, n values)")
            else:
                self.method = "1"
                self.sequence = sequence
                self.r_between2 = 0
                self.r_array = []
                self.r = 0
                
                self.a1 = sequence[0]
                self.r_total = 0
                self.meanr = 0

                for i in range(len(self.sequence)-1):
                    self.r_between2 = self.sequence[i+1]/self.sequence[i]
                    self.r_array.append(self.r_between2)
                    self.r_total = self.r_total + self.r_between2
                self.r = self.r_total/(len(self.sequence)-1)
        else:
            if r == 1 or an == 1 or a1 == 1 or n == 1:
                self.a1 = a1
                self.r = r
                self.n = n
                self.method = "2"
            else:
                raise Exception("Method not valid. Enter the correct method either: 1). Enter sequence (only enter sequence) or 2). Enter method (only enter r, an, a1, n values)")

    def getr(self):
        if self.method == "1":
            return self.r
        if self.method == "2":
            return self.r
            


    def getan(self,n):
        if self.method == "1":
            return self.a1 * self.r**(n-1)

    def getn(self,an):
        if self.method == "1":
            return (math.log(an/self.sequence[0]) / math.log(self.r))+1

##    def findnupper(self,an):
####        if self.method == "1":
####            return (math.
            


##    def finda1(self):
##        
##
##    def showsequence(self,number):
##        if len(self.sequence) = 0:
##            return self.sequence
##
##        else:
##            for i = 1 to number :
##                self.sequence[i] = self.a1*math.power(r,i-0)
##            return self.sequence
        

myseq = geometricsequence([2,4,8,16])
print(myseq.getr())
print(myseq.getan(5))
print(myseq.getn(16.5))


