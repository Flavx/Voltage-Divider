global board


class VoltageDivider:
    def __init__(self):
        self.menu = "1. Serie\n" \
                    "2. Serie & Parallel\n" \
                    "0. Exit"
        self.result_intro = "The result is: "
        self.resistances = None  # Total number of resistances
        self.r_values = []       # Values of each resistance
        self.v_out = None        # Number indicating the the resistance after which the voltage is calculated
        self.voltage = None      # Voltage
        self.exit = False

    def get_n_resistances(self):
        x = int(input("Number of resistances:\n> "))
        self.resistances = x
        return self.resistances

    def get_r_values(self):  # Creates a sublist for each resistance in series
        values = []          # those that are in parallel are within the same sublist
        for n in range(self.resistances):
            x = float(input(f"R.{n + 1} value:\n> "))
            y = input(f"Is R.{n + 1} in series(s) or parallel(p):\n> ")
            if y == "s":
                values.append([x])
            elif y == "p":
                parall_ind = len(values) - 1
                values[parall_ind].append(x)  # Value appended within the last sublist
        self.r_values = values                # because resistance is in parallel
        return self.r_values

    def get_v_out(self):
        x = int(input("Voltage out location:\n"
                      "(type the corresponding number of R "
                      "after which the voltage output is calculated):\n"
                      "> "))
        self.v_out = x
        return self.v_out

    def get_voltage(self):
        x = float(input("Voltage value:\n> "))
        self.voltage = x
        return self.voltage

    def create_board(self):  # Creates and empty board with x
        x = "  x  "          # with appropriate number
        global board         # of rows and columns
        board = []
        for n in range(len(self.r_values)):
            board.append([])
            for _ in range(len(self.r_values)):
                board[n].append(x)

    def r_in_board(self):  # Replaces the "x" with "R"
        global board       # where "R" = resistance
        count = 0
        for row, group in list(enumerate(self.r_values)):
            for col, item in list(enumerate(group)):
                count += 1
                r = f"|R{count}|"
                if count == self.v_out:        # places a "v" indicating where v_out is
                    board[row][col] = r + "v"  # within the board
                elif len(str(count)) == 1:
                    board[row][col] = r + " "
                else:
                    board[row][col] = r

    def print_board(self):
        global board
        self.create_board()
        self.r_in_board()
        score = "-" * (len(self.r_values) * 6)
        print(f"{score}\n")
        for item in board:
            print(*item)
        print(f"\n{score}")

    def calc_serie(self):
        return round((sum(self.r_values[self.v_out:]) / sum(self.r_values)) * self.voltage, 3)

    def reco_v_out(self):  # Recognises where v_out is
        count = 0
        actual = 0
        for group in self.r_values:
            actual += 1
            if count >= self.v_out:
                return actual - 1
            elif len(group) == 1:
                count += 1
            elif len(group) > 1:
                for _ in group:
                    count += 1

    def mixed(self):  # Calculates the voltage
        pars = []     # for resistance in series and parallel
        for group in self.r_values:
            x = 0
            if len(group) == 1:
                pars.append(group[0])
            elif len(group) > 1:
                for item in group:
                    x += 1 / item
                pars.append(1 / x)
        return round((sum(pars[self.reco_v_out():]) / sum(pars)) * self.voltage, 3)

    def user_interface(self):
        while not self.exit:
            choice = int(input(self.menu + "Please select:\n> "))
            if choice == 1:
                self.get_n_resistances()
                self.get_r_values()
                self.get_v_out()
                self.get_voltage()
                self.create_board()
                print(self.result_intro, self.calc_serie(), "\n")
            if choice == 2:
                self.get_n_resistances()
                self.get_r_values()
                self.get_v_out()
                self.get_voltage()
                self.print_board()
                print(self.result_intro, self.mixed(), "\n")
            if choice == 0:
                self.exit = True


if __name__ == '__main__':
    voltage_divider = VoltageDivider()
    voltage_divider.user_interface()
