from collections import deque, defaultdict

class ResWaitlist:
    def __init__(self):
        self.waitlist = defaultdict(deque)
        self.wentOut = set()
        self.seats = { i : None for i in range(1, 10 + 1)}

    def book(self, name, number) -> None:
        if not self.seats[number]:
            self.seats[number] = name
        else:
            self.waitlist[number].append(name) 

    def free(self, seatNumber):
        
        self.seats[seatNumber] = None
        waitlist = self.waitlist[seatNumber]

        if waitlist:
            while waitlist and waitlist[0] in self.wentOut:
               name =  waitlist.popleft()
               self.wentOut.remove(name)

            nextCus = waitlist.popleft()
            self.seats[seatNumber] = nextCus


    def getOut(self, name):
        self.wentOut.add(name)
