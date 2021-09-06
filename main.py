import json

# Change color of messages
class colors:
  OKGREEN = "\033[92m"
  FAIL    = "\033[91m"

print("###################################################")
print("# __          _______ _  _______   _______     __ #")
print("# \ \        / /_   _| |/ /_   _| |  __ \ \   / / #")
print("#  \ \  /\  / /  | | | ' /  | |   | |__) \ \_/ /  #")
print("#   \ \/  \/ /   | | |  <   | |   |  ___/ \   /   #")
print("#    \  /\  /   _| |_| . \ _| |_ _| |      | |    #")
print("#     \/  \/   |_____|_|\_\_____(_)_|      |_|    #")
print("#                                                 #")
print("###################################################")
print("")
print("Welcome to wiki.py! The revolutionary wiki made entirely from")
print("Python, and does not use anything else! Created by @roc0ast3r")
print("on September 5, 2021, we have gone so far since our first")
print("creation. Type viewPage(\"Help\") for more info on this wiki.")
print(colors.FAIL + "                     PLEASE NOTE!")
print("This is still a heavy WIP! Do not be surprised when")
print("you see bugs.")

wikiInfo      = open("wikiInfo.json")
pagesDatabase = open("database.json")
pages         = json.load(pagesDatabase)

bannedWords   = ["fuck", "Fuck"]
item          = bannedWords[0]

#############
# Main Code #
#############
# Add page code
def addPage(pageName):
  for i in pages["wikiPage"]:
    if pageName == item in bannedWords:
      print(colors.FAIL + "Page title contains a banned word.")
    elif pageName == i["wikiPageName"]:
      print(colors.FAIL + "Page already exists.")
    else:
      print("Now creating page:", pageName, "\n")
      pageContent = input("")
      if pageContent == "":
        print(colors.FAIL + "Page not created. You did not put any content.")
      else:
        print(colors.OKGREEN + "Page created.")
        # Code from https://www.geeksforgeeks.org/append-to-json-file-using-python/
        def writePage(newData, filename="database.json"):
          with open(filename, "r+") as file:
            file_data = json.load(file)
            file_data["wikiPage"].append(newData)
            file.seek(0)
            json.dump(file_data, file, indent=2)
        y = {
              "wikiPageName": pageName,
              "wikiPageContent": pageContent,
              "isLocked": "False"
        }
        writePage(y)

# Edit page code
def editPage(pageName):
  for i in pages["wikiPage"]:
    if i["isLocked"] == "False":
      if i["wikiPageName"] == pageName:
        # Print the first part of edit message
        print("Now editing page:", pageName, "\n")
        pageContent = input()

        # Change the content once done
        with open("database.json") as infile:
          data = json.load(infile)
        for elem in data["wikiPage"]:
          elem["wikiPageContent"]=elem["wikiPageContent"].replace(i["wikiPageContent"], pageContent)
        with open("database.json", "w") as outfile:
          json.dump(data, outfile, indent=2)

    elif i["isLocked"] == "True":
      if i["wikiPageName"] == pageName:
        print("Page is currently locked. You can still view it though!\n")
        print(i["wikiPageContent"])

# View page code
def viewPage(pageName):
  for i in pages["wikiPage"]:
    if pageName == i["wikiPageName"]:
      print("Now viewing page:", pageName, "\n")
      print(i["wikiPageContent"])
