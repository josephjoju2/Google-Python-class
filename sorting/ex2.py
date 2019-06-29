silent=['hello','and','goodbye']
shouting=[s.upper()+'!!!' for s in silent if len(s)>3]
print(shouting)
