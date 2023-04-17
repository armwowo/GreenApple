class Facility():
    def __init__(self,pets,ev_charger,salon,laudry,store,restaurant,security,cctv,finger_print,keycard,fitness,pool,lift,parking,smoking):
        self.__pets = pets
        self.__ev_charger = ev_charger
        self.__salon = salon
        self.__laudry = laudry
        self.__store = store
        self.__restaurant = restaurant
        self.__security = security
        self.__cctv = cctv
        self.__finger_print = finger_print
        self.__keycard = keycard
        self.__fitness = fitness
        self.__pool = pool
        self.__lift = lift
        self.__parking = parking
        self.__smoking = smoking

    def get_pets(self):
        return self.__pets
    
    def get_ev_charger(self):
        return self.__ev_charger
    
    def get_salon(self):
        return self.__salon
    
    def get_laudry (self):
        return self.__laudry
    
    def get_store(self):
        return self.__store
    
    def get_restaurant (self):
        return self.__restaurant
    
    def get_security (self):
        return self.__security
    
    def get_cctv (self):
        return self.__cctv
    
    def get_finger_print(self):
        return self.__finger_print
    
    def get_keycard (self):
        return self.__keycard
    
    def get_fitness (self):
        return self.__fitness
    
    def get_pool (self):
        return self.__pool
    
    def get_lift (self):
        return self.__lift
    
    def get_parking(self):
        return self.__parking
    
    def get_smoking(self):
        return self.__smoking