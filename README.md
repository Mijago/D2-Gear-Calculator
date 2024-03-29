
# What it does
This tool takes your destinyArmor.csv from DIM and generates optimal gear-combinations depending on certain rules. 
You basically tell the tool which stats are important for you and it will give you (hopefully) nice gear permutations.

Note 1: It thinks all your armor is masterworked!

Note 2: It does not add any armor mods - so you can freely distribute the five mod slots to further increase the builds.

Note 3: Please try around before you ask me stuff (like installation - if it doesn't work, it's probably user error). If you find an issue, open a Gitlab issue.

# How to use
1. Download this repository, either with `git clone https://github.com/Mijago/D2-Gear-Calculator.git` or by downloading the ZIP-archive from github.
2. Install python 3.8 or higher (tested with 3.8 and 3.9).
3. Install the packages: numpy, pandas, matplotlib, networkx with `py -m pip install numpy pandas matplotlib networkx`
4. Open DIM, go to Settings and download the armor spreadsheet (at the end of the page). Put your destinyArmor.csv from DIM in the same folder as the `main.py`.
5. Modify main.py to your liking. Set the Weights high (~1.5) for perks you like and low (~0.4) for perks you dont care about.
6. Execute main.py with `py main.py`.
7. `???`
8. Profit. It does **not** add any stat mods into account, so that's up to you!


## Very detailed instructions...
Example for Windows with **example Paths**.
1) Go to https://www.python.org/downloads/release/python-396/ and download `Windows embeddable package (64-bit)`. Unpack it and note down the path, for example `C:/Downloads/python39/`.
2) Download this repository https://github.com/Mijago/D2-Gear-Calculator/archive/refs/heads/master.zip
3) Unzip the master.zip and note the path, for example `C:/Downloads/master/D2-Gear-Calculator-master/`.
4) Open a command line by pressing Win+R and type "cmd".
5) In the command line, navigate to the directory of the repository, for example using `cd C:/Downloads/master/D2-Gear-Calculator-master/`. Using the `dir` command you should now see the "main.py".
6) Install the dependencies with `C:/Downloads/python39/python.exe -m pip install numpy pandas matplotlib networkx`
7) Edit `main.py` to your liking
8) Execute it in the command line with `C:/Downloads/python39/python.exe main.py`

# Configuration
Adapt the following configuration to your liking. 
A high weight means it is an important stat, if you don't like a stat, use a lower number. 
I'd not recommend using negative weights. 
```python
af = ArmorFilter(
    ArmorFilterSettings()
        # Prepare Settings
        .setClass("Titan")
        .setStatWeight(Stat.Mobility, 0.3)
        .setStatWeight(Stat.Resilience, 1.5)
        .setStatWeight(Stat.Recovery, 1.2)
        .setStatWeight(Stat.Discipline, 1.5)
        .setStatWeight(Stat.Intellect, 0.6)
        .setStatWeight(Stat.Strength, 0.3)
        # You can also modify the penalty weights
        .setWastedStatPenaltyWeight(Stat.Mobility, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Resilience, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Recovery, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Discipline, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Intellect, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Strength, weight=4, over100=1.1)
        ## add base mods; you can also add stasis here manually, or use the shortcuts below
        # .addStaticStat(Stat.Mobility, 20)     # Powerful Friends
        # .addStaticStat(Stat.Strength, 20)     # Radiant Light
        ## As a shortcut, you can also use the following commands
        .addStaticPowerfulFriends()           # +20 mobility
        .addStaticRadiantLight()              # +20 strength
        ## STASIS
        .addStaticStasisWhisperOfChains()     # +10 recovery
        .addStaticStasisWhisperOfConduction() # +10 resilience, +10 intellect
        .addStaticStasisWhisperOfDurance()    # +10 strength
        .addStaticStasisWhisperOfShards()     # +10 resilience

        # Add filters
        .addFilter(MinimumStatValueFilter(Stat.Mobility, 70)) # Mobility MUST be >= 70
        .addFilter(MaximumStatValueFilter(Stat.Mobility, 80)) # Mobility MUST be <= 80
        .addFilter(NamedItemFilter(Slot.Legs, "Dunemarchers"))# Only builds with Dunemarchers in the leg slot
)
```


# Example Output
Example output for my titan armor with the following weights:
```py
    ArmorFilterSettings()
        # Prepare Settings
        .setClass("Titan")
        .setStatWeight(Stat.Mobility, 0.3)
        .setStatWeight(Stat.Resilience, 1.5)
        .setStatWeight(Stat.Recovery, 1.2)
        .setStatWeight(Stat.Discipline, 1.5)
        .setStatWeight(Stat.Intellect, 0.6)
        .setStatWeight(Stat.Strength, 0.3)
        .addStaticStat(Stat.Mobility, 20)  # Powerful Friends
        .addStaticStat(Stat.Strength, 20)  # Radiant Light
```


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
