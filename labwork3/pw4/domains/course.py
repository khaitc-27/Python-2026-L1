class Course:

    def init(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def input(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")
        self.credit = int(input("Enter credits: "))

    def list(self):
        print(
            "ID:", self.id,
            "| Name:", self.name,
            "| Credit:", self.credit
        )