class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        invalid = []
        n = len(transactions)

        for i in range(n):
            tran1 = transactions[i].split(',')
            if int(tran1[2]) > 1000:
                invalid.append(",".join(tran1))
                continue
            for j in range(n):
                if i == j:
                    continue
                tran2 = transactions[j].split(',')
                if tran1[0] == tran2[0] and tran1[3] != tran2[3] and (((int(tran1[1]) - 60) <= int(tran2[1]) <= int(tran1[1]) + 60)):
                    invalid.append(",".join(tran1))
                    break

        return invalid
                
