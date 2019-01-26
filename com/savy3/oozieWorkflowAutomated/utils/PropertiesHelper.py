import xmltodict, os, logging

resourceFilePath = os.path.abspath("../../../../resources.xml")
logging.info("Reading parameters from the path : %s",resourceFilePath)

with open(resourceFilePath) as fd:
    properties = xmltodict.parse(fd.read())["properties"]
    oozieProperties = properties["oozieProperties"]
    envProperties = properties["envProperties"]

def getSourceProperties(source):
    return properties["sourceProperties"][source]
