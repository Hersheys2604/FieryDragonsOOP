import json
import os
from AnimalFactory.BatFactory import BatFactory
from AnimalFactory.BabyDragonFactory import BabyDragonFactory
from AnimalFactory.SalamanderFactory import SalamanderFactory
from AnimalFactory.SpiderFactory import SpiderFactory
from AnimalFactory.PirateDragonFactory import PirateDragonFactory
from AnimalFactory.CarFactory import CarFactory
from Volcanos.CaveCutVolcano import CaveCutVolcano
from Volcanos.NonCaveCutVolcano import NonCaveCutVolcano
from Tiles.VolcanoTile import VolcanoTile
from Tiles.CaveTile import CaveTile
from AnimalType import AnimalType
from ChitCard import ChitCard
from GameProgression import GameProgression
from Players.Player import Player
from Players.Player import Player
import json

class LoadManager:

    def __init__(self, file_name) -> None:
        self.load_data(file_name)

    def load_data(self, file_name):
        with open('data.json', 'r') as json_file:
            all_data = json.load(json_file)

        # Find the entry with the given file name
        # data = next((entry for entry in all_data if file_name in entry["fileName"]), None)
        # if data:
        try:
            self.player = all_data[file_name]["playerManager"]
            # self.caveCut = all_data[file_name]["caveCut"]
            # self.nonCaveCut = all_data[file_name]["nonCaveCut"]
            self.volcanos = all_data[file_name]["volcanos"]
            self.caves = all_data[file_name]["caves"]
            self.chitCards = all_data[file_name]["chitCards"]
            # else:
        except:
            raise ValueError(f"No data found for file name: {file_name}")

    def initialiseClasses(self):
        salamanderFactory = SalamanderFactory()
        batFactory = BatFactory()
        spiderFactory = SpiderFactory()
        babyDragonFactory = BabyDragonFactory()
        pirateDragonFactory = PirateDragonFactory()
        carFactory = CarFactory()
        volcanos = []    # this is all the volcanos that have a cave cut
        for volcano in self.volcanos:
            volcanosTiels = [] # this is the tiles inside each volcano

            for animal in volcano["saveList"]:
                if animal == "Spider":
                    volcanosTiels.append(VolcanoTile(spiderFactory.new(AnimalType.TILE)))
                if animal == "Bat":
                    volcanosTiels.append(VolcanoTile(batFactory.new(AnimalType.TILE)))
                if animal == "BabyDragon":
                    volcanosTiels.append(VolcanoTile(babyDragonFactory.new(AnimalType.TILE)))
                if animal == "Salamander":
                    volcanosTiels.append(VolcanoTile(salamanderFactory.new(AnimalType.TILE)))

            if volcano["type"] == "nonCaveCut":
                volcanos.append(NonCaveCutVolcano(volcanosTiels))
            if volcano["type"] == "caveCut":
                caveCut = CaveCutVolcano(volcanosTiels)
                volcanos.append(caveCut)
                caveCut.set_cave_cut_tile(volcano["caveCutTileIndex"])


        cavesList = []
        for animal in self.caves:  # this is the caves inside JSON file
            if animal == "Spider":
                cavesList.append(CaveTile(spiderFactory.new(AnimalType.CAVE)))
            if animal == "Bat":
                cavesList.append(CaveTile(batFactory.new(AnimalType.CAVE)))
            if animal == "BabyDragon":
                cavesList.append(CaveTile(babyDragonFactory.new(AnimalType.CAVE)))
            if animal == "Salamander":
                cavesList.append(CaveTile(salamanderFactory.new(AnimalType.CAVE)))

        chitCardsList = []
        openChitCards = []
        for chitCard in self.chitCards:
            chitCardType = chitCard[2]
            flipped = chitCard[1]
            animal = chitCard[0]
            if animal == "Spider":
                chitInstantiated = ChitCard(spiderFactory.new(AnimalType[chitCardType]))
            if animal == "Bat":
                chitInstantiated = ChitCard(batFactory.new(AnimalType[chitCardType]))
            if animal == "Pirate Dragon":
                chitInstantiated = ChitCard(pirateDragonFactory.new(AnimalType[chitCardType]))
            if animal == "Salamander":
                chitInstantiated = ChitCard(salamanderFactory.new(AnimalType[chitCardType]))
            if animal == "BabyDragon":
                chitInstantiated = ChitCard(babyDragonFactory.new(AnimalType[chitCardType]))
            if animal == "Car":
                chitInstantiated = ChitCard(carFactory.new(AnimalType[chitCardType]))

            if flipped == "True":
                chitInstantiated.flip()
                openChitCards.append(chitInstantiated)

            chitCardsList.append(chitInstantiated)

        playerList = []
        angles = []
        isHomeList = []
        currentPlayer = None
        for player_name, value in self.player.items(): 
            player = Player(player_name, GameProgression(), value["data"]["img_path"])
            player.ratioNum = value["data"]["player_num"]
            player.ratioDen = value["data"]["player_den"]
            playerList.append(player)

            angles.append(value["data"]["angle"])
            isHomeList.append(value["data"]["isHome"])
            if value["current"]:
                currentPlayer = player

        return volcanos, cavesList, chitCardsList, playerList, angles, isHomeList, currentPlayer, openChitCards

