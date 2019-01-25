def open_liste_interdite():
	liste_interdite = []
	with open("liste_interdite.txt", "r") as f:
		for line in f.read().splitlines():
			liste_interdite.append(line)

	f.close()
	return liste_interdite
