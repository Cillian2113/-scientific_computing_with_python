import math

class Category:
    def __init__(self, name):
        self.name=name
        self.ledger = []

    def get_balance(self):
        balance = 0
        for i in range(0,len(self.ledger)):
            balance+= self.ledger[i]["amount"]
        return float("%.2f" %balance)

    def deposit(self,amount,description= ""):
        x = {"amount": amount, "description": description}
        self.ledger.append(x)

    def withdraw(self,amount,description= ""):
        if self.check_funds(amount):
            x = {"amount": -amount, "description": description}
            self.ledger.append(x)
            return True
        return False

    def transfer(self, AMOUNT,category):
        if self.check_funds(AMOUNT):
            self.withdraw(AMOUNT, "Transfer to "+ str(category.name))
            category.deposit(AMOUNT, "Transfer from "+str(self.name))
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() - amount >= 0:
            return True
        return False

    def __str__(self):
        asterisks = (30 - len(self.name))/2
        transactions = ""
        if asterisks.is_integer():
            title = ('*'*(int(asterisks))+self.name+int(asterisks)*'*')
        else:
            title = ('*' * math.floor(asterisks) + self.name + math.ceil(asterisks)*'*')
        for x in self.ledger:
            desc = x["description"][:23]
            amount = str("%.2f" % x["amount"])
            transactions += "\n"+(desc+" "*(30-len(desc)-len(amount))+amount)
        return title+transactions+"\n"+"Total: "+str(self.get_balance())

    def money_spent(self):
        spent = 0
        for i in range(0,len(self.ledger)):
            if self.ledger[i]["amount"]<0:
                spent+= self.ledger[i]["amount"]
        spent = abs(spent)
        return float("%.2f" %spent)


def create_spend_chart(categories):
    total=0
    percents = [0 for x in range(len(categories))]
    names = [0 for x in range(len(categories))]
    for x in categories:
        total += x.money_spent()
    i = 0
    for x in categories:
        percents[i] = (x.money_spent()/total)*100
        percents[i] = int(math.floor(percents[i] / 10.0)) * 10
        names[i] = x.name
        i+=1
    Lines = [None for x in range(13+len(max(names, key=len)))]
    Lines[0]="Percentage spent by category"
    for i in range(1,12):
        mark = (11-i)*10
        Lines[i] = (3-len(str(mark)))*" "+str(mark)+"|"
        for j in range (len(names)):
            if percents[j] >= mark:
                Lines[i]+=" o "
            else:
                Lines[i]+="   "
        Lines[i]+=" "
    Lines[12]="    "+"---"*len(names)+"-"
    for i in range(13,len(Lines)):
        Lines[i]="    "
        for j in range(len(names)):
            if len(names[j])>i-13:
                Lines[i]+=" "+names[j][i-13]+" "
            else:
                Lines[i]+="   "
        Lines[i]+=" "
    output = ""

    for x in range(len(Lines)-1):
        output+=Lines[x]+'\n'
    output+=Lines[-1]

    return output
