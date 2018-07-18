# Given an instance of the gasup problem, efficiently compute an ample city

def find_ample_city(gallons, distances, MPG):
	remaining_gallons = 0

	num_cities = len(gallons)
	city_rem_gas_pair = (0, 0) # (city_id, remaining_gallons)

	# Get the city with th e lowest/minimum remaining gallons
	for i in range(1, num_cities):
		remaining_gallons += gallons[i-1] - distances[i-1]//MPG
		if remaining_gallons < city_rem_gas_pair[1]:
			city_rem_gas_pair = (i, remaining_gallons)

	return city_rem_gas_pair[0]


MPG = 20
gallons = [50,20,5,30,25,10,10]
distances = [900, 600, 200, 400, 600, 200, 100]

print("Gallons:	{}".format(gallons))
print("Distances:	{}".format(distances))

print("Ample city:	{}".format(find_ample_city(gallons, distances, MPG)))

