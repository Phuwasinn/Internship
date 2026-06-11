class Camera:
    def take_photo(self):
        print("Taking photo..")

class Phone:
    def calling(self):
        print("Calling..")

class SmartPhone(Camera,Phone):
    pass

phone = SmartPhone()
phone.take_photo()  
phone.calling()