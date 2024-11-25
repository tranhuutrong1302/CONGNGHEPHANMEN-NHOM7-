class Pet:
  def__init__(self,name,species,owner=None):
     self.name =name
     self.species= species
     self.owner= owner
  def__str__(self)
     return f"{self.name}({self.species})-Owner:{self.owner.user if self.owner else 'No owner'}"
class User:
  def__init__(self,username,password):
     self.username= username
     self.password= password
     self.pets=[]
  def__add_pet__(self,pet):
     self.pets.append(pet)
     pet.owner = self
  def remove_pet (self,pet):
      if pet in self.pets:
        self.pets.remove(pet)
        pet.owner= None
      else:
        print(f"{self.username} không sở hữu thú cưng này!")
  def list_pets(self):
      if not self.pets:
        print(f"{self.username} không có thú cưng nào!")
      else:
        print(f"{self.username}'s Pets:")
        for pet in self.pets:
           print (f"-{pet}")
class Manager:
  def__init__(self):
     self.users=[]
     self.pets=[]
     self.logged_in_user =None
     self.admin_username="admin"
     self.admin_password="123"
  def register_user(self):
     username=input("Nhập tên người dùng: ")
     password=input("Nhập mật khẩu: ")
     if self.find_user(username):
       print(f"Người dùng{username} đã tồn tại. Vui lòng chọn tên khác!")
       return None
     user=User(username,password)
     self.Users.append(user)
     print(f"Đăng ký người dùng {username} thành công !")
     return user
  def login_user(self):
     username=input("Nhập tên người dùng : ")
     password=input("Nhập mật khẩu: ")
     user = self.find__user(username)
     if user and user.password==password:
         self.logged_in_user=user
         print (f"Đăng nhập thành công !..Chào mừng{username} (^__^)")
         return user
     else:
         print("Tên người dùng hoặc mật khẩu không đúng (T_T)")
         return None
  def login_admin(self):
     username=input("Nhập tài khoản quản trị viên bạn được cấp : ")
     password=inpuut("Vui lòng nhập mật khẩu")
     if username==self.admin_username and password==self.admin_password:
         print("Bạn đã đăng nhận với tư cách quản trị viên.")
         return True
     else:
         print ("Tài khoản mật khẩu quản trị viên không chính xác !")
         return False
  def find_user(self,username):
      for user in self.users:
        if user.username==username:
             return user
      return None
  def adopt_pet(self,adopter_username,pet_name):
      adopter = self.find_user(adopter_username)
      if not adopter:
           print (f"Không tìm thấy người dùng {adopter_username}.")
           return
      pet= next((pet for pet in self.pets if pet.name==pet_name and pet.owner is None),None)
      if pet:
          adopter.add_pet(pet)
          print(f"{adopter.username} đã nhận {pet_name} !")
      else:
          print (f"Thú cưng {pet_name} không có hoặc đã được nhận nuôi")
def give_away_pet(self,giver_username,pet_name):
    if not self.logged_in_user
       print("Vui lòng đăng nhập trước khi cho đi thú cưng.")
       return
    giver=self.logged_in_user
    pet=next((pet for pet in giver.pets if pet.name==pet_name),None)
    if pet:
      giver.remove_pet(pet)
      self.pets.append(pet)
      print(f"{giver.username} đã cho đi {pet_name}.")
    else:
      print (f"{giver.username}  không sở hữu thú cưng {pet_name}.")
def add_new_pet(self):
    if not self.logged_in_user:
        print("Vui lòng đăng nhập để thêm thú cưng.")
        return
    name=input("nhập tên thú cưng: ")
    new_pet=Pet(name,species)
    self.logged_user.add__pet(new_pet)
    print(f"self.logged_in_user.username} đã thêm thú cưng {new_pet} vào tài khoản.")
