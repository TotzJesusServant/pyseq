import math
import numpy as np

class geometricsequence:
    def __init__(self,sequence,r=None,a1=None):
        
        if sequence != None:
            if r != None or a1 != None:
                raise Exception("Correct group of value entered is wrong. Enter each group of value correctly for different method, either: Group 1). Enter sequence value only or group 2). Enter only enter (r, an, a1, n values)")
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
            if r != None or a1 != None:
                self.a1 = a1
                self.r = r
                self.method = "2"
                self.sequence = []
                for i in range(5):
                    self.sequence.append(a1 * self.r**(i-1))
            else:
                raise Exception("Correct group of value is wrong. Enter each group of value correctly for different method, either: Group 1). Enter sequence value only or group 2). Enter only enter (r, an, a1, n values)")

    def getr(self):
        if self.method == "1":
            return self.r
        if self.method == "2":
            return self.r
            
    def getan(self,n):
        if self.method == "1" or self.method == "2":
            return self.a1 * self.r**(n-1)

    def getn(self,an):
        if self.method == "1" or self.method == "2":
            ans = (math.log(an/self.a1) / math.log(self.r))+1
            if float(ans):
                return (math.floor(ans), ans, math.ceil(ans))
            else:
                return ans

    def getnforbigger(self,an):
        if self.method == "1" or self.method == "2":
            return math.ceil((math.log(an/self.a1) / math.log(self.r))+1)

    def getnforlower(self,an):
        if self.method == "1" or self.method == "2":
            return math.floor((math.log(an/self.a1) / math.log(self.r))+1)

    def getnforrange(self,anlower,anhigher):
        if self.method == "1" or self.method == "2":
            return (self.getnforbigger(anlower),self.getnforlower(anhigher))

myseq = geometricsequence([2,4,8,16],None,None)
print(myseq.getr()) # memasukkan nilai rasio
print(myseq.getan(5)) # mengembalikan nilai an untuk nilai n yang dimasukkan
print(myseq.getn(16.5)) # mengembalikan nilai n untuk nilai an yang dimasukkan
print(myseq.getnforbigger(17)) # memngembalikan nilai n untuk nilai an yang lebih besar dari an yang diberikan
print(myseq.getnforlower(2.3)) # memngembalikan nilai n untuk nilai an yang lebih kecil dari an yang diberikan 
print(myseq.getnforrange(2.3,17)) #mengembalikan range n untuk range an yang diberikan




