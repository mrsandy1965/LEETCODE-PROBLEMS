class ATM:

    def __init__(self):
        self.denominations = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx,coin in [(0,20),(1,50),(2,100),(3,200),(4,500)]:
            self.denominations[coin] += banknotesCount[idx]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0 for _ in range(5)]
        for idx , coin in [(0,500),(1,200),(2,100),(3,50),(4,20)]:
            if amount >= coin :
                ans[4-idx] = min(self.denominations[coin] , amount//coin)
                amount -= ans[4-idx] * coin 
        if amount : return [-1]
        for idx , coin in [(0,20),(1,50),(2,100),(3,200),(4,500)]:
            self.denominations[coin] -= ans[idx] 
        return ans 


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)