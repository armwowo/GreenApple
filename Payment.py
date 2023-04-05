class Payment:
    def __init__(self,price,name,email,phone_number):
        self.__price = price
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__payment_status = False

    def get_detail_reserved(self):
        pass

    def get_detail_creditpayment(self):
        pass
    
    def get_detail_debitpayment(self):
        pass

    @property
    def payment_status(self):
        return self.__payment_status
    
    def set_payment_status(self,changed):
        self.__payment_status = changed
        return self.__payment_status
    
