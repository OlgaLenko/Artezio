class Student:
    name = None
    marks = {}

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.marks = {n: 0 for n in range(self.conf['lab_num'])}
        self.limit = {}

    def make_lab(self, m, n=None):

        last_try = 3
        if n not in self.limit:
            self.limit[n] = 1
        elif self.limit[n] < last_try:
            self.limit[n] += 1
        else:
            return

        m = float(m)
        if n is None:
            n = 0
            if n in self.marks:
                n += 1
            self.marks[n] = m
        elif 0 <= n <= self.conf['lab_num'] - 1:
            if 0 <= m <= float(self.conf['lab_max']):
                self.marks[n] = m
            elif m > float(self.conf['lab_max']):
                self.marks[n] = float(self.conf['lab_max'])
        return self

    def make_exam(self, m):
        m = float(m)
        if 0 <= m <= float(self.conf['exam_max']):
            self.marks['exam_mark'] = m
            return self
        elif m > float(self.conf['exam_max']):
            self.marks['exam_mark'] = float(self.conf['exam_max'])
            return self

    def is_certified(self):
        max_mark = self.conf['exam_max'] \
                   + self.conf['lab_max'] * self.conf['lab_num']
        final_mark = sum(self.marks.values())
        if (final_mark / max_mark) >= self.conf['k']:
            return final_mark, True
        else:
            return final_mark, False


conf = {
    'exam_max': 30,
    'lab_max': 7,
    'lab_num': 10,
    'k': 0.61
}

vasya = Student('Vasya', conf)
vasya.make_lab(5, 4)
vasya.make_lab(1, 2)
vasya.make_lab(11, 0)
vasya.make_lab(5, 25)
vasya.make_lab(2, 0)
vasya.make_lab(6, 0)
vasya.make_lab(7, 0)
vasya.make_lab(5)
vasya.make_exam(35)
vasya.is_certified()
