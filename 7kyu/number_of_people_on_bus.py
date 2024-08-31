def number(bus_stops):
    got_on, got_off = 0, 0
    arrive, depart = [], []
    for a, d in bus_stops:
        arrive.append(a)
        depart.append(d)
    for a in range(0, len(arrive)):
        got_on = got_on + arrive[a]
    for d in range(0, len(depart)):
        got_off = got_off + depart[d]
    final = got_on - got_off
    return final
