f = open('input.txt')

class Raindeer:
    def __init__(self, name, speed, speed_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.speed_time = int(speed_time)
        self.rest_time = int(rest_time)
        self.time = 0
        self.position = 0
        self.points = 0
    def tick(self):
        if self.time < self.speed_time:
            self.position += self.speed

        self.time += 1
        if self.time == self.speed_time + self.rest_time:
            self.time = 0


deer = []
for line in f.readlines():
    line = line.strip().split(" ")
    deer.append(Raindeer(line[0], line[3], line[6], line[-2]))

for i in range(2503):
    max_dist = 0
    for d in deer:
        d.tick()
        max_dist = max(max_dist, d.position)

    for d in deer:
        if d.position == max_dist:
            d.points += 1

max_points = 0
for d in deer:
    max_points = max(max_points, d.points)

print(max_points)
