import copy
import random
# Consider using the modules imported above.
random.seed(95)
class Hat:
    def __init__(self,**data):
        if len(data) < 1:
            print("Error must have at least one ball")
            return
        self.split = data
        self.contents = []
        keys = []
        values = []
        for i in self.split:
            keys.append(i)
            values.append(self.split[i])
        for i in range(len(keys)):
            for j in range(values[i]):
                self.contents.append(keys[i])


    def draw(self, num):
        output = []
        if len(self.contents) <= num:
            return self.contents
        for i in range(num):
            rand = random.randrange(len(self.contents))
            output.append(self.contents[rand])
            self.contents.remove(self.contents[rand])
        return output



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range (num_experiments):
        out = copy.deepcopy(hat).draw(num_balls_drawn)
        if checksuccess(out, expected_balls):
            successes+=1
    return successes/num_experiments


def checksuccess(out, expected_balls):
    for name in expected_balls:
        if expected_balls[name]>out.count(name):
            return False
    return True
