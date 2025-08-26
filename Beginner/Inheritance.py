"""
Beginner Task 9: Inheritance – MobilePhone -> Apple, Samsung
"""
class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=True,
                 front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number}..."
    def receive_call(self, number):
        return f"Receiving call from {number}..."
    def take_a_picture(self):
        return "Picture taken!"

class Apple(MobilePhone):
    def __init__(self, model="iPhone", **kwargs):
        super().__init__(**kwargs)
        self.brand = "Apple"
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model="Galaxy", **kwargs):
        super().__init__(**kwargs)
        self.brand = "Samsung"
        self.model = model

if __name__ == "__main__":
    iphone = Apple(model="iPhone 14", front_camera="12MP", rear_camera="48MP", ram="6GB", storage="128GB")
    galaxy = Samsung(model="Galaxy S23", front_camera="12MP", rear_camera="50MP", ram="8GB", storage="256GB")

    for phone in (iphone, galaxy):
        print(f"{phone.brand} {phone.model} | {phone.screen_type} | {phone.network_type} | Dual SIM: {phone.dual_sim} | Cameras: {phone.front_camera}/{phone.rear_camera} | RAM: {phone.ram} | Storage: {phone.storage}")
        print(phone.make_call("+1-202-555-0175"))
        print(phone.take_a_picture())
