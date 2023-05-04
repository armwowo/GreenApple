from abc import ABC,abstractmethod
from Backend.Room import *

class Payment(ABC):
    
    @abstractmethod
    def pay(self):
        pass

class CreditPayment(Payment):
    def __init__(self,card_name,card_number):#("armcard","11045","2022-02-05","112")
        self.card_name = card_name
        self.card_number = card_number
        # self.card_expire = card_expire
        # self.cvv = cvv
        self.status = False

    def pay(self):
        # self.status = True
        # return str([{"payment status":self.status}])
        pass

class DebitPayment(Payment):
    def __init__(self,card_name,card_number):
        self.card_name = card_name
        self.card_number = card_number
        # self.card_expire = card_expire
        # self.cvv = cvv
        self.status = False

    def pay(self):
        self.status = True
        return "payment complete"

class PromtPayment(Payment):
    def __init__(self,tel_no):
        self.tel_no = tel_no

    def pay(self):
        pass

    # def __init__(self,price,payment_detail,payment_status):
    #     self._price = price
    #     self._payment_detail = payment_detail
    #     self._payment_status = payment_status

    # def get_detail_reserved(self):
    #     pass
    # def get_detail_creditpayment(self):
    #     pass
    
    # def get_detail_debitpayment(self):
    #     pass