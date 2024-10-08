S = """When I got the call one day asking whether I’d be interested in spending some time in Guinea, I wiped the dust off my well-used atlas and carefully identified the correct Guinea, separating it from its namesakes.

Let’s call it the Africa problem. No, not a problem with Africa itself. Rather, a problem of ignorance and bias that can so often come in the way of responsible reporting on the continent and its people. The burden of this responsibility hangs over writers and photographers who have an Africa assignment handed to them on a platter. One has to swim against the current to avoid adding more “ooga-booga” imagery to the vast archives that already exist. With an open mind and an honest intent to connect with the contemporary culture of Guinea, I would spend 10 days in its capital city, Conakry. The idea was to discover Guinea on my own terms and create a personal memory of the place from scratch.

The nation of Guinea is 60 years old this year! And yet, since their tryst with democracy in 2010, the kinder part of history has only just begun. I set about looking for the vision of a better world reflected in the eyes of those whom I encountered on the streets of Conakry. Everybody's a star. Within our imagination, they form the constellation that is Guinea."""
D = {}

wordlist = sorted(S.lower().replace(",", "").replace("'", "").replace(".", "").split())

for s in wordlist:
    if s.isalpha() and len(s)>3:
        D[s] = wordlist.count(s)

D2 = {}

for f in sorted(list(D.values()), reverse=True):
    D2[f] = ""
    for j in D:
        if D[j] == f:
            if D2[f] == "":
                D2[f] = j
            else:
                D2[f] += ", " + j

max_count = max(D2.keys())
print(f"These words occur {max_count} times each: {D2[max_count]}")
