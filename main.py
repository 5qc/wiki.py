import json

# Change color of messages
class colors:
  FAIL    = "\033[91m"
  MESSAGE = "\033[93m"
  NORMAL  = "\033[0m"
  OKGREEN = "\033[92m"

siteInfo      = open("wikiInfo.json")
site          = json.load(siteInfo)
pagesDatabase = open("database.json")
pages         = json.load(pagesDatabase)
bannedWords   = open("bannedWords.json")
banned        = json.load(bannedWords)

for i in site["wikiInfo"]:
  if i["wikiName"] == "wiki.py":
    print(colors.NORMAL + "###################################################")
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
    print("creation. Type viewPage(\"Help\") for more info on this software.")
  else:
    print(colors.NORMAL + "Welcome to", i["wikiName"])

#############
# Main Code #
#############
# Add page code
def addPage(pageName):
  for bannedWord in banned["bannedWords"]:
    if bannedWord in pageName:
      return print(colors.FAIL + "Pagename contains a banned word.")
  if pageName != bannedWord:
    for i in pages["wikiPage"]:
      if pageName == i["wikiPageName"]:
        return print(colors.FAIL + "Page already exists.")
    if pageName != i["wikiPageName"]:
      print(colors.MESSAGE + "Now creating page:", pageName)
      print(colors.NORMAL)
      pageContent = input("")

  if pageContent == "":
    print(colors.FAIL + "Page not created. You did not put any content.")
  else:
    print(colors.OKGREEN + "Page created.")
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
        print(colors.MESSAGE + "Now editing page:", pageName)
        print(colors.NORMAL + "")
        pageContent = input(i["wikiPageContent"])

        # Change the content once done
        with open("database.json") as infile:
          data = json.load(infile)
        for elem in data["wikiPage"]:
          elem["wikiPageContent"] = elem["wikiPageContent"].replace(i["wikiPageContent"], pageContent)
        with open("database.json", "w") as outfile:
          json.dump(data, outfile, indent=2)

        return print(colors.OKGREEN + "Successfully edited page.")
    elif i["isLocked"] == "True":
      if i["wikiPageName"] == pageName:
        print(colors.MESSAGE + "Page is currently locked. You can still view it though!\n")
        return print(colors.NORMAL + i["wikiPageContent"])
  if i["wikiPageName"] != pageName:
    print(colors.FAIL + "Page doesn't exist.")
def edit(pageName): # Alias for "editPage"
  editPage(pageName)

# View page code
def viewPage(pageName):
  for i in pages["wikiPage"]:
    if pageName == i["wikiPageName"]:
      print(colors.MESSAGE + "Now viewing page:", pageName, "\n")
      return print(colors.NORMAL + i["wikiPageContent"])
  if pageName != i["wikiPageName"]:
    print(colors.FAIL + "Page doesn't exist.")

#######################################
## THESE ARE NOT MEANT TO BE EDITED. ##
##   PLEASE DO EDIT ANY OF THESE!!   ##
#######################################

# Special pages
def specialPage(pageName):
  if pageName == "AllPages":
    for i in pages["wikiPage"]:
      print(i["wikiPageName"])
  elif pageName == "SiteInfo":
    for i in site["wikiInfo"]:
      print("Wikiname:", i["wikiName"])
  else:
    print(colors.FAIL + "Special page doesn't exist.")
