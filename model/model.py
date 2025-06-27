from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAnni(self):
        return DAO.getAnni()

    def getBrands(self):
        return DAO.getBrands()

    def getRetailers(self):
        return DAO.getRetailers()
