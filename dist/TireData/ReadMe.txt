Vorbereitungen:
Datenstruktur wie folgt:
- Skript in Hauptordner
- Darin in ein Ordner "Data"
- Darin zwei Ordner "Braking" und "Cornering"
- Darin so viele Ordner, wie Reifen analysiert werden sollen
- Bennenung der Ordner: tire0, tire1, tire2, ....
- Bennenung der Daten ist egal, aber sie müssen wie folgt sortiert sein: 12PSI, 10PSI, 14PSI, 8PSI (Entspricht der Reihenfolge, wie sie das TTC auch nummeriert)
- Es muss eine Datei "Grenzen.txt" vorhanden sein. Dort werden die Grenzwerte zur Sortierung eingetragen. Eigentlich sollte man die nicht ändern müssen
- Es muss eine Datei "Druck.txt" vorhanden sein. Dort werden die eingestellten Drücke hinterlegt. Eigentlich sollte man die nicht ändern müssen.
- Ordner "Figures" in Hauptordner

Braking:
index	ia	fz	sa
0	0	0	0
1	1	0	0
2	2	0	0
3	0	1	0
4	1	1	0
5	2	1	0
6	0	2	0
7	1	2	0
8	2	2	0
9	0	3	0
10	1	3	0
11	2	3	0
12	0	0	1
13	1	0	1
14	2	0	1
15	0	1	0
...
35	2	3	2

Cornering
index	ia	fz
0	0	0
1	1	0
2	2	0
3	0	1
4	1	1
5	2	1
6	0	2
7	1	2
8	2	2
9	0	3
10	1	3
11	2	3


Grenzwerte:
ia 0 = 0°
ia 1 = 2°
ia 2 = 4°

fz 0 = -1557 N
fz 1 = -667 N 
fz 2 = -222 N 
fz 3 = -1112 N

sa 0 = 0°
sa 1 = 3°
sa 2 = 6°


Beispieldaten:
Aus Runde 4:

Hoosier 20.5x6.0-13 R25B (43128) [C2500]: 

8	10	12		14	psi
38	36	34,39		37	cornering
116	114	112w,113,117	115	Drive/Brake/combined

