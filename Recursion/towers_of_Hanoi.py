## SOLUTION: Focus on the case with 3 disks
# We can move N-1 disks from rod 1 to Aux
# Then move the 1 disk from rod 1 to 2
# And at last move the N-1 disks from Aux to rod 1

def towers_of_hanoi(n, from_rod, to_rod, aux_rod):
	if n == 1:
		print("Move disk 1 from rod {} to rod {}".format(from_rod, to_rod))
		return
	towers_of_hanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk {} from rod {} to rod {}".format(n,from_rod, to_rod))
	towers_of_hanoi(n-1, aux_rod, to_rod, from_rod)


n = 4
print("N = {}".format(n))
towers_of_hanoi(n, '1', '2', 'Aux')