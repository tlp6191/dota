heroes={}
heroes2={}
with open('parsed') as f:
    for l in f.readlines():
        hero=l.split("|")[0]
        if hero not in heroes:
            heroes[hero]=len(heroes)
            print hero+"1,",
with open('parsed') as f:
    for l in f.readlines():
        hero=l.split("|")[0]
        if hero not in heroes2:
            heroes2[hero]=len(heroes2)
            print hero+"2,",
print "winrate"
print heroes
with open('parsed') as f:
    for l in f.readlines():
        (hero1,hero2,advantage,win_rate,plays)=l.split("|")
        h1="0,"*heroes[hero1]+"1,"+"0,"*(len(heroes)-heroes[hero1]-1)
        h2="0,"*heroes[hero2]+"1,"+"0,"*(len(heroes)-heroes[hero2]-1)
        wr = float(win_rate)
        print "{0}{1}{2}".format(h1,h2,wr)
