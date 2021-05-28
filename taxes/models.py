from django.db import models


class Tax(models.Model):
    begin = models.FloatField(default=0)
    end = models.FloatField(null=True)
    percent = models.PositiveSmallIntegerField(default=0)

    def calculate_tax(self, salary):
        if salary > self.begin - 1:
            if salary > (self.end or salary):
                return round((self.end - (self.begin - 1)) * (self.percent / 100), 2)
            else:
                return round((salary - (self.begin - 1)) * (self.percent / 100), 2)
        else:
            return 0

    @classmethod
    def calculate_total_tax(cls, salary):
        return sum(map(lambda tax: tax.calculate_tax(salary), cls.objects.all()))