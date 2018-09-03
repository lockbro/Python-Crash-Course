def make_car(manufacturer, model, **other_info):
    car_dict = {}
    car_dict["manufacturer"] = manufacturer
    car_dict["model"] = model
    for key, value in other_info.items():
        car_dict[key] = value
    return car_dict


def add_ingredient(*add_list):
    print("you add : " + ",".join(add_list))


def make_shirt(size, word):
    print("The T-shirt's size is " + size +
          " and the word in the T-shirt is " + word)
