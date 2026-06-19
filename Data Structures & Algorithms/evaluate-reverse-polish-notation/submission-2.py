class Solution:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def evalRPN(self, tokens: List[str]) -> int:
        se = {'+':self.add,'-':self.sub,'/':self.div,'*':self.mul}
        stck=[]
        for x in tokens:
            if x in se:
                b=stck.pop()
                a=stck.pop()
                stck.append(int(se[x](a,b)))
            else:
                stck.append(int(x))
        return stck[0]


        