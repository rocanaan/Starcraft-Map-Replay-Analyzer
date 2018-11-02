	
import sc2reader
import numpy as np
import cv2


# replays = sc2reader.load_replays('/Users/rodrigocanaan/Dev/SC2ReplayParser/test_replays/2.0.8.25604', load_map = True)
# replays = sc2reader.load_replays('/Users/rodrigocanaan/Downloads/2018 WCS Montreal/Day 1/Group Stage 1/Group A/Rhizer vs. PengWin', load_map = True)

# replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2readerStoic/sc2reader/download_replays/Acid Plant.SC2Replay', load_map = True)
# replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2readerStoic/sc2reader/download_replays/Blizzard.SC2Replay', load_map = True)
replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2readerStoic/sc2reader/download_replays/Blizzard2.SC2Replay')

# replay = sc2reader.load_replay('http://ggtracker.com/matches/7229933/replay',load_map = True)

# replays = sc2reader.load_replays('/Users/rodrigocanaan/Dev/sc2readerStoic/sc2reader/download_replays', load_map = True)


i=0

# for replay in replays:
map = replay.map
w = map.map_info.width
h = map.map_info.height



deathMap = np.zeros((w,h))

max = 0
count = 0

for event in replay.events:
	if event.name == 'UnitDiedEvent':
		count += 1
		x = event.x
		y = event.y
		deathMap[x,y] += 1
		if (deathMap[x,y]) > max:
			max +=1

print(max)
print(count)
deathMap = deathMap

img = np.zeros([w,h,3])

img[:,:,0] = np.multiply(np.ones((w,h)),deathMap)*255
img[:,:,1] = np.multiply(np.ones((w,h)),deathMap)*255
img[:,:,2] = np.multiply(np.ones((w,h)),deathMap)*255
cv2.imwrite('replay' + str(i) + 'deathMap.jpg', img)

i=i+1
