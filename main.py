import json

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

wikiInfo      = open("wikiInfo.json")
pagesDatabase = open("database.json")
pages         = json.load(pagesDatabase)

bannedWords   = ["fuck", "Fuck"]
item          = bannedWords[0]

# Change color of messages
class colors:
  OKGREEN = "\033[92m"
  FAIL    = "\033[91m"

#############
# Main Code #
#############
# Add page code
def addPage(pageName):
  if pageName == item in bannedWords:
    print(colors.FAIL + "Page not created. You entered a banned word.")
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
          json.dump(file_data, file, indent = 4)
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
        pageContent = input(i["wikiPageContent"])

        # Change the content once done
        
        
        # Will display message
        if pageContent == i["wikiPageContent"]:
          print(colors.OKGREEN + "Page edited.")
        else:
          print(colors.FAIL + "Page wasn't edited. Please try again later.")
      else:
        print(colors.FAIL + "Page not found.")
    elif i["isLocked"] == "True":
      if i["wikiPageName"] == pageName:
        print("Page is currently locked. You can still view it though!\n")
        print(i["wikiPageContent"])

# View page code
def viewPage(pageName):
  for i in pages["wikiPage"]:
    if i["wikiPageName"] == pageName:
      print("Now viewing page:", pageName, "\n")
      print(i["wikiPageContent"])
