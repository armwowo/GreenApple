class Review():
    def __init__(self,rating,comment) :
        self.__rating = rating
        self.__comment = comment

    def add_review_to_list(self,rating,comment):
        pass

    def get_rating(self):
        return self.__rating
    
    def get_comment(self):
        return self.__comment