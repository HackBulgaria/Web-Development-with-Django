from tasks import add


result = add.delay(1, 2)
print(result)
