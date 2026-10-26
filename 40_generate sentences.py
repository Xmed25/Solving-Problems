# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].


verbs=["Play", "Love"]
objects=["Hockey","Football"]
subjects=["I", "You"]

for s in range(len(subjects)):
    for v in range(len(verbs)):
        for o in range(len(objects)):
            print(f"{subjects[s]} {verbs[v]} {objects[o]}")
