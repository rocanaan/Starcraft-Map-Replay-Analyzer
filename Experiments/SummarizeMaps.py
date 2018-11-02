	
import sc2reader
from collections import Counter

replays = sc2reader.load_replays('/Users/rodrigocanaan/Dev/SC2ReplayParser/test_replays/2.0.8.25604', load_map = True)

d = {}
c = Counter()

for replay in replays:
	map = replay.map
	name = map.name
	h = replay.map_hash
	width = map.map_info.width
	heigth = map.map_info.height
	key = (name,h)
	info = (width, heigth)
	d[key] = info
	c[key] +=1
	
for (key, count) in c.most_common():
	info = d[key]
	print('Map: ' + str(key) + ' Count: ' + str(count) + ' Info: ' + str(info)  )
