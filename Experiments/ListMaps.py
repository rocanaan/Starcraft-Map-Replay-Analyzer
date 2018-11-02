	
import sc2reader

replays = sc2reader.load_replays('/Users/rodrigocanaan/Dev/SC2ReplayParser/test_replays/2.0.8.25604', load_map = True)

for replay in replays:
	map = replay.map
	print (map.name)
	print (map.map_info.width)
	print (map.map_info.height)