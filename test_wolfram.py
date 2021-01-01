from . import wolfram_language_functions as wlf

fake_messages = ["bla I love math",
                 "bla I love math thingy bla",
                 "thingy bla I love math",
                 "I love math bla bla thingy",
                 "bla I love math bla"]
name = "user"
wrapper_dict = {name: fake_messages}

print(wlf.predict_next_word(wrapper_dict, name, "I love", True))
print("done")
