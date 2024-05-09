# Generator
def producer():
    yield "Introduction"
    yield "to"
    yield "Cybrom"
print(producer())

for i in producer():
    print(i)

# def rangerr(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
# for i in rangerr(5):
#     print(i)

next(producer)