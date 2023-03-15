
class ClacMaster(object):
    def __init__(self, choice, *argv):
        self.name = "Calc Master Class"
        self.description = "Calc Master class to perform arithmetic functions"
        self.choice = choice
        self.argv = argv
        self.choices = ['addition', 'subtraction', 'multiplication', 'division']

        self.result_message = "Unsupported Choice"
        self.result_value = 0
        self.result_status = False

    def validate_choice(self):
        if self.choice not in self.choices:
            return False
        return True

    def validate_values(self):
        all_value = True
        if len(self.argv) > 0:
            for each_val in self.argv:
                if type(each_val).__name__ not in ['int', 'float', 'int64', 'float64']:
                    all_value = False
                    self.result_message = "Please submit all values are numeric"
        return all_value

    def perform_addition(self):
        result_value = 0
        if len(self.argv) > 0:
            for each_val in self.argv:
                result_value = result_value + each_val

            self.result_value = result_value
            self.result_status = True
            self.result_message = "Addition is successful"

    def perform_multiplication(self):
        if len(self.argv) > 0:
            result_value = self.argv[0]
            for val_index in range(len(self.argv))[1:]:
                result_value = result_value * self.argv[val_index]

            self.result_value = result_value
            self.result_status = True
            self.result_message = "Multiplication is successful"

    

