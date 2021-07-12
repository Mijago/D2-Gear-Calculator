
# What it does
This tool takes your destinyArmor.csv from DIM and generates optimal gear-combinations depending on certain rules. 
You basically tell the tool which stats are important for you and it will give you (hopefully) nice gear permutations.

Note: It thinks all your armor is masterworked!

# How to use
1. Install packages: numpy, pandas, matplotlib, networkx 
2. Put your destinyArmor.csv from DIM in this folder
3. Modify main.py to your liking. Set the Weights high (~1.5) for perks you like and low (~0.4) for perks you dont care about.
4. Execute main.py
5. `???`
6. Profit

# Example Output
```
Collection 275015
  tiers 33
  mobility 38   resilience 88   recovery 51
  discipline 90  intellect 40   strength 46
  Helmet:	Mask of the Quiet One [4 18 15 22 12 4]
  Gauntlets:	Lightkin Gauntlets [4 24 10 22 8 8]
  Chest:	Plate of the Great Hunt [4 26 8 24 4 8]
  Legs:		Greaves of the Great Hunt [4 18 16 20 14 4]


Collection 272423
  tiers 34
  mobility 42   resilience 93   recovery 45
  discipline 83  intellect 40   strength 50
  Helmet:	An Insurmountable Skullfort [8 26 5 23 10 4]
  Gauntlets:	Kabr's Brazen Grips [4 21 14 14 10 12]
  Chest:	Plate of the Great Hunt [4 26 8 24 4 8]
  Legs:		Greaves of the Great Hunt [4 18 16 20 14 4]


Collection 271126
  tiers 33
  mobility 55   resilience 70   recovery 55
  discipline 95  intellect 28   strength 50
  Helmet:	An Insurmountable Skullfort [8 26 5 23 10 4]
  Gauntlets:	Mimetic Savior Gauntlets [4 4 31 18 8 12]
  Chest:	Plate of the Great Hunt [4 26 8 24 4 8]
  Legs:		Mimetic Savior Greaves [17 12 9 28 4 4]
```