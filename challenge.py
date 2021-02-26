def counter(name):
    if name == None:
        raise ValueError("You cannot add None value.")
    if name.isalpha() and (not None):
        return len(name)
    else:
        raise ValueError("please add english alphabetical name.")


#print(counter("ra  jni"))
