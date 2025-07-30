######################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.itemGrabs = []
        self.grabDesc = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
        
    #I added these
    @property
    def itemGrabs(self):
        return self._itemGrabs
    @itemGrabs.setter
    def itemGrabs(self, value):
        self._itemGrabs = value
    @property
    def grabDesc(self):
        return self._grabDesc
    @grabDesc.setter
    def grabDesc(self, value):
        self._grabDesc = value

##############################################
    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)

    def addItem(self, item, desc, grabs, gd):
        self._items.append(item)
        self._itemDescriptions.append(desc)
        self._itemGrabs.append(grabs) #I added this
        self._grabDesc.append(gd) #I added this

    def addGrabbable(self, item):
        self._grabbables.append(item)
        
    def delGrabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        s = "You are in {}.\n".format(self.name)
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s
