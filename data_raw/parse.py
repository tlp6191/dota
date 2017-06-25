import re
with open("m") as f:
    for l in f.readlines():
        m = re.search('.*?fa-space.*?r-none-mobile\">(.*?)<(.*)',l)
        if m:
            for matchup in re.findall("cell-icon\" data-value=\"(.*?)\">.*?data-value=\"(.*?)\">.*?segment-advantage.*?data-value=\"(.*?)\".*?segment-win.*?data-value=\"(.*?)\">.*?segment-match",m.group(2)):
                print "{0}|{1}|{2}|{3}|{4}".format(m.group(1),matchup[0],matchup[1],matchup[2],matchup[3])
