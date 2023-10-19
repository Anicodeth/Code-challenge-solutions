class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairings = {}
        unhappy_set = set()

        # Create a dictionary to store the pairings
        for x, y in pairs:
            pairings[x] = y
            pairings[y] = x

        unhappy_count = 0
        for person in pairings:
            partner_x = pairings[person]
            partner_y = pairings[partner_x]

            # Check if they are unhappy
            preferences_x = preferences[person]
            for friend in preferences_x:
                if friend == partner_x:
                    break
                else:
                    preferences_friend = preferences[friend]
                    for partner in preferences_friend:
                        if partner == pairings[friend]:
                            break
                        elif partner == person and person not in unhappy_set:
                            unhappy_set.add(person)
                            unhappy_count += 1
                            break

        return unhappy_count

        
