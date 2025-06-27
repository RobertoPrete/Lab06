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

    def top_vendite(self, anno, brand, retailer):
        if (anno is None or anno == "" or anno == "Nessun filtro") and (brand is None or brand == "" or brand == "Nessun filtro") and (retailer is None or retailer == "" or retailer == "Nessun filtro"):
            topVendite = DAO.getTopVendite1()
        return topVendite



