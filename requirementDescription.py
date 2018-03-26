

class RequirementDescription:
    def __init__(self, number, title, asA, wantTo, soThat):
        self.number = int(number)
        self.title = title
        self.asA =  asA
        self.wantTo = wantTo
        self.soThat = soThat

    def __str__(self):
        string = str(self.number) + " " + self.title + "\n"
        string += "As a " + self.asA + " I want to " + self.wantTo
        string += " so that " + self.soThat + "\n"
        return string

    def get_full_description(self):
        return self.wantTo +  self.soThat

