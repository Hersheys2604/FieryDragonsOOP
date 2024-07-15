import json

class SaveManager:
    '''
    Class for the Save manager. Responsible for calling each of the elements within the game and saving the relevant string data to a JSON file
    '''
    def __init__(self) -> None:
        pass

    def saveAll(self, chitCards, volcanos, playerManager, caves, fileName):
        '''
        saveAll method calls the respective save method on each of these entities which returns the string data needed to write to the JSON  
        
        Inputs:
        - chitCard, volcanos, PlaterManager, caves, fileName

        '''
        # Load existing data from the file if it exists
        try:
            with open('data.json', 'r') as json_file:
                json_dict = json.load(json_file)

            json_dict[fileName] = {
                "playerManager": {},
                "volcanos": [],
                "chitCards": [],
                "caves": []
                }
            json_dict = self.writeToDict(json_dict, chitCards, volcanos, playerManager, caves, fileName)
                
        except FileNotFoundError:
            # If the file doesn't exist yet, initialize an empty list
            # all_data = []

            # need to initialise a new dict, since we don't have one initially set up
            json_dict = {
                fileName: {
                "playerManager": {},
                "volcanos": [],
                "chitCards": [],
                "caves": []
                }
            }

            json_dict = self.writeToDict(json_dict, chitCards, volcanos, playerManager, caves, fileName)


        # Save the updated data back to the file
        with open('data.json', 'w') as json_file:
            json.dump(json_dict, json_file, indent=4)


    def writeToDict(self, dict, chitCards, volcanos, playerManager, caves, fileName):
        '''
        writeToDict method: called by the saveAll method. Responsible for assigning valued in a formatted manner to the JSON file
        
        '''
        for chitCard in chitCards:
            dict[fileName]["chitCards"].append(chitCard.save())

        for volcano in volcanos:
            dict[fileName]["volcanos"].append(volcano.save())

        for cave in caves:
            dict[fileName]["caves"].append(cave.save())

        dict[fileName]["playerManager"] = playerManager.save()

        return dict