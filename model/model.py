from database.DAO import DAO


class Model:
    def __init__(self):
        self.listaAnni = None
        self.listaBrands = None
        self.listaRetailers = None

        self.getAnni()
        self.getBrands()
        self.getRetailers()

    def getAnni(self):
        self.listaAnni = DAO.getAnni()

    def getBrands(self):
        self.listaBrands = DAO.getBrands()

    def getRetailers(self):
        self.listaRetailers = DAO.getRetailers()
