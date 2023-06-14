def doubler_killer(videos: list=[]):
    no_double = []
    for i in range(len(videos)):
        if videos[i] in no_double:
            pass
        else:
            no_double.append(videos[i])
    return no_double