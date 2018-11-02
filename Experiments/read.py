	
import sc2reader
# sys.path.append('/Users/rodrigocanaan/Dev/ggpyjobs')
# sys.path.append('/Users/rodrigocanaan/Dev/sc2reader')

# Old version, does not support tracker events
# replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2reader/test_replays/1.0.0.16117/1.SC2Replay', load_map=True)

# Error 504
# replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2reader/test_replays/2.0.8.25446/ggtracker_3024127.SC2Replay', load_map=True)


replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2readerStoic/sc2reader/download_replays/Blizzard2.SC2Replay', load_map = True)



print(replay.players[0])
print(replay.players[1])
print(replay.map.name)
print(replay.map.hash)

print (replay.build)
# print (replay.events)


# print (replay.tracker_events)

# for e in replay.tracker_events:
# 	print(e)

# for i,e in enumerate(replay.tracker_events):
# 	print(i,e)

# for e in replay.events:
# 	print(e)


for event in replay.events:
    if event.name == 'UnitDiedEvent':
        print(str(event.unit) + ' was killed by ' + str(event.killer) + ' at ' + str(event.second) + ' at  position (' + 
        	str(event.x)+','+str(event.y)+')')

print (replay.winner.lineup) #Race of the winner
print (replay.length) #Length of the replay


# print (replay.map.minimap)

# replay.load_map()

# print (replay.map.map_info)
# for unit in p1.units:
# 	print (unit)