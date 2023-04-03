class Payment:
    def __init__(self,price,payment_detail,payment_status):
        self._price = price
        self._payment_detail = payment_detail
        self._payment_status = payment_status

    def get_detail_reserved(self):
        pass
    
    def get_detail_creaditpayment(self):
        pass
    
    def get_detail_debitpayment(self):
        pass