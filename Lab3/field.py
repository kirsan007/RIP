

#def countdown(num):
#   while num > 0:
#       yield num
 #       num -= 1

#cd = countdown(10)

#for i in range(10):
#    print(next(cd))

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'foo': 'bar'},
    {'title': None}
]



#goods[0]['foo'] = 'bar'
#print(goods[0])


def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for obj in items:
            if args[0] in obj and obj[args[0]] is not None:
                yield obj[args[0]]
    else:
        for obj in items:
            res = {}
            for prop in args:
                if prop in obj and obj[prop] is not None:
                    res[prop] = obj[prop]
            if len(res) > 0:
                yield res


f = field(goods, 'title', 'price')

print(next(f))
print(next(f))
print(next(f))

