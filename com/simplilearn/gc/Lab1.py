import gc

print(gc.isenabled()) # True
gc.disable()
print(gc.isenabled()) # False
gc.enable()
print(gc.isenabled()) # True