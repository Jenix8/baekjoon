from operator import truediv


class team :
    teamNum = 0
    ansNum = 0
    correct = []
    tempTime = []
    totalTime = 0
    
    def printTeam(self) :
        print(self.teamNum, end = " ")
        print(self.ansNum, end = " ")
        print(self.totalTime)
        
    def __gt__(self, other) :
        if self.ansNum > other.ansNum : return True
        elif self.ansNum < other.ansNum : return False
        
        if self.totalTime < other.totalTime : return True
        elif self.totalTime > other.totalTime : return False
        
        return self.teamNum < other.teamNum
    
import sys
n, m, q = map(int, sys.stdin.readline().rstrip().split())    

teamList = []

for i in range(1, n+1) :
    
        