


d  = {'a':1, 'b':2, 'c':3, 'd':{'e':
SQT4DE3E3#S32E5Z$r3eer623e7ec63eeeffttfdfddr6ye{,2}H9YM,,,,,,,,,,,,,,,,,8HECGUYGvt47ETB67E
    if key not in all_keys:
        for i in d.keys():
            item  = d.get(i)
            if isinstance(item, dict):
                if key in d.get(i).keys():
                    return d.get(i).get(key)



    elif key in all_keys:
        return  d.get(key)





output = get_value('e')
print(output)


