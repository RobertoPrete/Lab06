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
        """
        Questo metodo del modello permette di recuperare dal database il top delle vendite (massimo 5) in base ai filtri selezionati nei dropdown di anno, brand e retailer.
        Recupera dati diversi in base ai filtri selezionati e non. Per questo differenziamo le top vendite nel seguente modo:
        TopVendite1: le top vendite date nel caso in cui non viene selezionato nessun filtro tra anno, brand e retailer (o viene selezionato in tutti i casi "Nessune filtro")
        TopVendite2: le top vendite date nel caso in cui viene selezionato solo il filtro dell'anno
        TopVendite3: le top vendite date nel caso in cui vengono selezionati tutti i filtri (anno, brand e retailer)

        """
        if (anno is None or anno == "" or anno == "Nessun filtro") and (brand is None or brand == "" or brand == "Nessun filtro") and (retailer is None or retailer == "" or retailer == "Nessun filtro"):
            topVendite = DAO.getTopVendite1()
        return topVendite



