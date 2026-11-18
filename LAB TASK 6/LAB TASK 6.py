def vacuum_cleaner(room):
    position = 0

    for i in range(len(room)):
        position = i

        if room[position] == 1:
            print("Room", position, "is Dirty")
            room[position] = 0
            print("Cleaning room", position)
        else:
            print("Room", position, "is Clean")

    print("All rooms are clean")

room = [1, 0, 1, 1]
vacuum_cleaner(room)
