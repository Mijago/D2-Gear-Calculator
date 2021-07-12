import pandas as pd
import networkx as nx
import numpy as np

from armor import ArmorFilterSettings
from armor.enums import Slot, Stat


class ArmorFilter:
    startNode = 'START'
    endNode = 'END'

    def __init__(self, settings: ArmorFilterSettings):
        self.G = None
        self.data = None
        self.allPaths = []
        self.allScores = []
        self.settings = settings

    def __getClassItemNodeData(self):
        return {
            Stat.Mobility.value: 2, Stat.Resilience.value: 2, Stat.Recovery.value: 2,
            Stat.Discipline.value: 2, Stat.Intellect.value: 2, Stat.Strength.value: 2,
        }

    def __getEmptyNodeData(self):
        return {
            Stat.Mobility.value: 0, Stat.Resilience.value: 0, Stat.Recovery.value: 0,
            Stat.Discipline.value: 0, Stat.Intellect.value: 0, Stat.Strength.value: 0,
        }

    def buildPaths(self):
        # Find Paths
        paths = nx.all_simple_paths(self.G, source=self.startNode, target=self.endNode)

        self.allPaths = []
        self.allNames = []
        self.allScores = []
        for path in paths:
            itemIndices = self.__getItemIndicesFromPath(path)
            itemNames = self.__getItemNamesFromData(itemIndices, path)
            # print(itemNames)

            values = self.__getPathValues([self.startNode, self.endNode] + list(itemIndices.values()))
            # apply filters
            _valid = True
            for filter in self.settings.itemFilters:
                if not filter.apply(self.G, itemIndices, values, itemNames):
                    _valid = False
            if _valid:
                self.allPaths.append(itemIndices)
                self.allNames.append(itemNames)
                self.allScores.append(values)

    def __getItemIndicesFromPath(self, path):
        return {
            Slot.Helmet.value: path[2],
            Slot.Gauntlet.value: path[5],
            Slot.Chest.value: path[8],
            Slot.Legs.value: path[11],
        }

    def __getItemNamesFromData(self, idc, path):
        return {
            Slot.Helmet.value: self.data["Name"][idc[Slot.Helmet.value]],
            Slot.Gauntlet.value: self.data["Name"][idc[Slot.Gauntlet.value]],
            Slot.Chest.value: self.data["Name"][idc[Slot.Chest.value]],
            Slot.Legs.value: self.data["Name"][idc[Slot.Legs.value]],
        }

    def __getPathValues(self, path):
        values = {}
        for nodeId in path:
            node = self.G.nodes.get(nodeId)
            for key in node:
                if key != "subset":
                    if key not in values:
                        values[key] = 0
                    values[key] += node[key]
        return values

    def buildGraphForFile(self, path):
        data = pd.read_csv(path)
        data = data[data["Equippable"] == self.settings.clazz].set_index(["Id"])

        self.data = data

        G = nx.DiGraph()
        G.add_node(self.startNode, **self.settings.staticStats)
        G.add_node(self.endNode, **self.__getClassItemNodeData())

        types = ["Helmet", "Gauntlets", "Chest Armor", "Leg Armor"]
        previousLegendaryNode = self.startNode
        for k, type in enumerate(types):
            df_sub = data[data["Type"] == type]
            df_sub_exo = df_sub[df_sub["Tier"] == "Exotic"]
            df_sub_leg = df_sub[df_sub["Tier"] != "Exotic"]

            newLegendaryNodeIn = type + "_leg_in"
            G.add_node(newLegendaryNodeIn, **self.__getEmptyNodeData())
            newLegendaryNodeOut = type + "_leg_out"
            G.add_node(newLegendaryNodeOut, **self.__getEmptyNodeData())

            G.add_edge(previousLegendaryNode, newLegendaryNodeIn)

            for item in df_sub.T.iteritems():
                G.add_node(item[0], **{
                    Stat.Mobility.value: 2 + item[1]["Mobility (Base)"],
                    Stat.Resilience.value: 2 + item[1]["Resilience (Base)"],
                    Stat.Recovery.value: 2 + item[1]["Recovery (Base)"],
                    Stat.Discipline.value: 2 + item[1]["Discipline (Base)"],
                    Stat.Intellect.value: 2 + item[1]["Intellect (Base)"],
                    Stat.Strength.value: 2 + item[1]["Strength (Base)"],
                }, exotic=item[1]["Tier"] == "Exotic" and 1 or 0)

            for item in df_sub_leg.T.iteritems():
                G.add_edge(newLegendaryNodeIn, item[0])
                G.add_edge(item[0], newLegendaryNodeOut)

            # Draw exotic paths

            if len(df_sub_exo) > 0:
                newExoticNodeIn = type + "_exo_in"
                G.add_node(newExoticNodeIn)
                newExoticNodeOut = type + "_exo_out"
                G.add_node(newExoticNodeOut)

                G.add_edge(previousLegendaryNode, newExoticNodeIn)
                for item in df_sub_exo.T.iteritems():
                    G.add_edge(newExoticNodeIn, item[0])
                    G.add_edge(item[0], newExoticNodeOut)

                if k < 3:
                    nextSubtype = types[k + 1]
                    if not G.has_node(nextSubtype + "_leg_only_in"):
                        for k2 in range(k + 1, 4):
                            subtype = types[k2]
                            G.add_node(subtype + "_leg_only_in", **self.__getEmptyNodeData())
                            G.add_node(subtype + "_leg_only_out", **self.__getEmptyNodeData())
                            for item in df_sub_leg.T.iteritems():
                                G.add_node(item[0] + "_leg", **{
                                    Stat.Mobility.value: 2 + item[1]["Mobility (Base)"],
                                    Stat.Resilience.value: 2 + item[1]["Resilience (Base)"],
                                    Stat.Recovery.value: 2 + item[1]["Recovery (Base)"],
                                    Stat.Discipline.value: 2 + item[1]["Discipline (Base)"],
                                    Stat.Intellect.value: 2 + item[1]["Intellect (Base)"],
                                    Stat.Strength.value: 2 + item[1]["Strength (Base)"],
                                }, exotic=item[1]["Tier"] == "Exotic" and 1 or 0)

                                G.add_edge(subtype + "_leg_only_in", item[0] + "_leg")
                                G.add_edge(item[0] + "_leg", subtype + "_leg_only_out")

                            df_sub2 = data[data["Type"] == subtype]
                            df_sub2_leg = df_sub2[df_sub2["Tier"] != "Exotic"]

                            G.add_edge(subtype + "_leg_only_in", subtype + "_leg_only_out")  # TODO: REMOVE AND INSERT ALL LEG NODES HERE
                            if k2 > 1:
                                G.add_edge(types[k2 - 1] + "_leg_only_out", subtype + "_leg_only_in")
                            if k2 == 3:
                                G.add_edge(subtype + "_leg_only_out", self.endNode)

                    G.add_edge(newExoticNodeOut, nextSubtype + "_leg_in")
                else:
                    G.add_edge(newExoticNodeOut, self.endNode)
            previousLegendaryNode = newLegendaryNodeOut

        G.add_edge(previousLegendaryNode, self.endNode)
        self.G = G
        return self

    def getScores(self):
        df2 = pd.DataFrame(self.allScores)
        print("Total Paths", len(df2))

        df2['tiers'] = (
                + df2[Stat.Mobility.value].values // 10
                + df2[Stat.Resilience.value].values // 10
                + df2[Stat.Recovery.value].values // 10
                + df2[Stat.Discipline.value].values // 10
                + df2[Stat.Intellect.value].values // 10
                + df2[Stat.Strength.value].values // 10
        )

        df2['score'] = 0
        df2['score'] = (
                + 2 * df2["tiers"].values
                + self.settings.weights[Stat.Mobility.value] * (df2[Stat.Mobility.value].values - 18)
                + self.settings.weights[Stat.Resilience.value] * (df2[Stat.Resilience.value].values - 18)
                + self.settings.weights[Stat.Recovery.value] * (df2[Stat.Recovery.value].values - 18)
                + self.settings.weights[Stat.Discipline.value] * (df2[Stat.Discipline.value].values - 18)
                + self.settings.weights[Stat.Intellect.value] * (df2[Stat.Intellect.value].values - 18)
                + self.settings.weights[Stat.Strength.value] * (df2[Stat.Strength.value].values - 18)

                # Penalties! every score from 1-4 and 6-9 is lost!
                - self.settings.wastedStatPenaltyWeight[Stat.Mobility.value] * (df2[Stat.Mobility.value].values % 5 > 0)
                - self.settings.wastedStatPenaltyWeight[Stat.Resilience.value] * (df2[Stat.Resilience.value].values % 5 > 0)
                - self.settings.wastedStatPenaltyWeight[Stat.Recovery.value] * (df2[Stat.Recovery.value].values % 5 > 0)
                - self.settings.wastedStatPenaltyWeight[Stat.Discipline.value] * (df2[Stat.Discipline.value].values % 5 > 0)
                - self.settings.wastedStatPenaltyWeight[Stat.Intellect.value] * (df2[Stat.Intellect.value].values % 5 > 0)
                - self.settings.wastedStatPenaltyWeight[Stat.Strength.value] * (df2[Stat.Strength.value].values % 5 > 0)
                # stats over 100 are bad
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Mobility.value] * np.maximum(df2[Stat.Mobility.value].values - 100, 0)
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Resilience.value] * np.maximum(df2[Stat.Resilience.value].values - 100, 0)
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Recovery.value] * np.maximum(df2[Stat.Recovery.value].values - 100, 0)
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Discipline.value] * np.maximum(df2[Stat.Discipline.value].values - 100, 0)
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Intellect.value] * np.maximum(df2[Stat.Intellect.value].values - 100, 0)
                - self.settings.wastedStatPenaltyWeightOver100[Stat.Strength.value] * np.maximum(df2[Stat.Strength.value].values - 100, 0)
        )

        self.scored = df2

    def saveScored(self, path, num=100):
        print(self.scored.sort_values(by=["score"], ascending=False).head(25))
        with open(path, 'w') as f:
            for k, m in self.scored.sort_values(by=["score"], ascending=False).head(num).T.iteritems():
                print('Collection', k, file=f)
                scores = self.allScores[k]
                print("  tiers", int(m["tiers"]), file=f)
                print("  mobility", scores[Stat.Mobility.value], "  resilience", scores[Stat.Resilience.value], "  recovery", scores[Stat.Recovery.value], file=f)
                print("  discipline", scores[Stat.Discipline.value], " intellect", scores[Stat.Intellect.value], "  strength", scores[Stat.Strength.value], file=f)
                dfHelm = self.data.T[self.allPaths[k][Slot.Helmet.value]]
                dfGauntlet = self.data.T[self.allPaths[k][Slot.Gauntlet.value]]
                dfChest = self.data.T[self.allPaths[k][Slot.Chest.value]]
                dfLegs = self.data.T[self.allPaths[k][Slot.Legs.value]]
                print("  Helmet:\t" + dfHelm["Name"] + " "
                      + str(dfHelm[["Mobility (Base)", "Resilience (Base)", "Recovery (Base)", "Discipline (Base)", "Intellect (Base)", "Strength (Base)"]].values + 2)
                      , file=f)
                print("  Gauntlets:\t" + dfGauntlet["Name"] + " " +
                      str(dfGauntlet[["Mobility (Base)", "Resilience (Base)", "Recovery (Base)", "Discipline (Base)", "Intellect (Base)", "Strength (Base)"]].values + 2)
                      , file=f)
                print("  Chest:\t" + dfChest["Name"] + " " +
                      str(dfChest[["Mobility (Base)", "Resilience (Base)", "Recovery (Base)", "Discipline (Base)", "Intellect (Base)", "Strength (Base)"]].values + 2)
                      , file=f)
                print("  Legs:\t\t" + dfLegs["Name"] + " "
                      + str(dfLegs[["Mobility (Base)", "Resilience (Base)", "Recovery (Base)", "Discipline (Base)", "Intellect (Base)", "Strength (Base)"]].values + 2)
                      , file=f)
                print("", file=f)
                print("", file=f)
