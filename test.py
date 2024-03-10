# from models import storage
# from models.base_model import BaseModel
# from models.user import User

# all_objs = storage.all()
# print("-- Reloaded objects --")
# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)

# print("-- Create a new User --")
# my_user = User()
# my_user.first_name = "Betty"
# my_user.last_name = "Bar"
# my_user.email = "airbnb@mail.com"
# my_user.password = "root"
# my_user.save()
# print(my_user)

# print("-- Create a new User 2 --")
# my_user2 = User()
# my_user2.first_name = "John"
# my_user2.email = "airbnb2@mail.com"
# my_user2.password = "root"
# my_user2.save()
# print(my_user2)


# string = 'show.all("something")'

# string = string.replace("(", " ")
# string = string.replace(")", "")
# dict = {"js": "mcndcn", "jm": "ndjsn"}
# string = string.replace(".", " ")
# print(string)
var = 'gsxfgxg, gxch, "jbbb"'
if "." in var:
    var = var.split(".")

var = var.replace(",", "")
print(var)
method_dict = {
    "all": "do_all",
    "show": "do_show",
    "destroy": "do_destroy",
    "update": "do_update"
}

# if var in method_dict.keys():
#     print(var)
# else:
#     print("this is shit")
#/usrbin/python
