
def readDataFile(dataFileName):
    """
    Read date file. Parse it. Return list of lists of data.
    """
    result = []
    # Regex for parse data lines and skeep header lines:
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    with open(dataFileName, 'r') as dataFile:
        for line in dataFile:
            match = regex.search(line)
            if match:
                result.append(match.groups())
    return result