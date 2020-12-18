from Problema import Problema


class Estado:
    def __init__(self, problema):
        self.current_state = Problema()

    def update(self):
        if self.current_state.time == 23:
            self.current_state.time == 0
        else:
            self.current_state.tiempo += 1;

    def op1(self):
        self.current_state.sat1.do_nothing()
        self.current_state.sat2.do_nothing()

