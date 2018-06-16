countries = ["Alaska", "Alberta" ,"Central America",
           "Eastern United States",
           "Greenland", "Northwest Territory",
           "Ontario", "Quebec", "Western United States",
           "Argentina", "Brazil", "Peru", "Venezuela",
           "Great Britain", "Iceland", "Northern Europe",
           "Scandinavia", "Southern Europe", "Ukraine", "Western Europe",
           "Central Africa", "East Africa", "Egypt", "Madagascar",
           "North Africa", "South Africa","Afghanistan", "China", "India", "Irkutsk","Japan","Kamchatka", "Middle East", 
           "Mongolia", "Siam", "Siberia", "Ural", "Yakutsk",
           "Eastern Australia","Indonesia", "New Guinea","Western Australia"]

continents = ["North America","North America","North America","North America","North America","North America","North America","North America","North America",
                                "South America","South America","South America","South America",
                                "Europe","Europe","Europe","Europe","Europe","Europe","Europe",
                                "Africa","Africa","Africa","Africa","Africa","Africa",
                                "Asia","Asia","Asia","Asia","Asia","Asia","Asia","Asia","Asia","Asia","Asia","Asia",
                                "Australia", "Australia", "Australia", "Australia"]

sources = [0,0,1,1,1,2,2,3,3,3,4,4,4,5,6,6,12,12,12,10,10,11,13,13,13,13,14,14,15,15,15,16,17,17,15,
                               20,20,20,21,21,21,21,22,23,20,24,24,22,
                               26,26,26,26,27,27,27,27,28,28,29,29,29,29,30,30,31,31,33,35,35,27,27,
                               32,32,32,32,26,36,31,
                               38,38,39,39,40,34]

targets = [1,5,5,6,8,8,3,6,7,8,5,6,7,6,7,8,2,10,11,11,9,9,14,16,15,19,4,16,17,18,19,18,18,19,16,
                               21,24,25,22,23,24,25,24,25,10,17,19,17,
                               27,28,32,36,28,34,33,36,34,32,35,33,37,31,33,31,33,37,35,36,37,33,35,
                               22,17,18,21,18,18,0,
                               40,41,41,40,41,40]

def get_edge_list():
	edge_list = {}
	for i, _ in enumerate(sources):
		s = sources[i]
		t = targets[i]
		if (not countries[s] in edge_list):
			edge_list[countries[s]] = []
		if (not countries[t] in edge_list):
			edge_list[countries[t]] = []
		edge_list[countries[s]].append(countries[t])
		edge_list[countries[t]].append(countries[s])
	return edge_list

class Country:
	def __init__(self, neighbors, continent):
		self.neighbors = neighbors
		self.continent = continent

class Board:
	def __init__(self):
		self.edge_list = get_edge_list()
		self.countries = countries


b = Board()
print b.edge_list
