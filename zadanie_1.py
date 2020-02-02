class Date_my:
    def __init__(self, us_date):
        self.us_date = us_date

    def pr_exmp(self):
        return self.us_date

    @classmethod
    def num_did(cls, us_date):
        x = us_date.split('-')
        return int(x[0]), int(x[1]), int(x[2])
    
    @staticmethod
    def vld_num(us_date):
        """ я так понимаю профи решил бы эо как то так?
        from datetime import date 
        def vld_num(y, m, d):
            try:
                date(y, m, d)
                return True
            except:
                return False"""
        date = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31 }
        x = us_date.split('-')
        d = ''
        n = int(x[0])
        if (x[1]) not in date:
            print("ошибка в месяце")
        
        d = date.get(x[1])
        if n < 0 or n > d:
            print("ошибка в дате ")
        
        if len(x[2]) > 4:
            print("ошибка в годе")
        s = ''.join(x)
        #print(type(s), x, us_date)
        if s.isdigit():
            print("дата введена верно")
        else:
            print("в дате должны быть только числа")

a = Date_my('15-01-1970')
print(a.pr_exmp())
print(Date_my.num_did('14-03-2015'))
print(Date_my.vld_num('14-03-r015'))
