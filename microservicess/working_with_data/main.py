dict = {"name1": 2, "name2": "joseph"}


def fun(**kwg):
    print(kwg)


fun(**dict)
for k in dict:
    print(k, dict[k])
