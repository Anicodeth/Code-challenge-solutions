class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        deadline = 0
        days = 0
        people = deque([(1,1)])
        for i in range(1,n + 1):
            while people and i - people[0][1] == forget:
                people.popleft()
            count = 0
            for a,b in people:
                if i - b >= delay:
                    count += a
            people.append((count, i))

        sumi = 0
        for a,b in people:
            sumi += a
        return sumi % (10**9 + 7)
