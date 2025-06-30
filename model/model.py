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

    def top_vendite(self, anno, brand, retailer_code):
        """
        Questo metodo del modello permette di recuperare dal database il top delle vendite (massimo 5) in base ai filtri selezionati nei dropdown di anno, brand e retailer.
        Recupera dati diversi in base ai filtri selezionati e non. Per questo differenziamo le top vendite nel seguente modo:
        TopVendite1: le top vendite date nel caso in cui non viene selezionato nessun filtro tra anno, brand e retailer (o viene selezionato in tutti i casi "Nessune filtro")
        TopVendite2: le top vendite date nel caso in cui viene selezionato solo il filtro dell'anno
        TopVendite3: le top vendite date nel caso in cui vengono selezionati tutti i filtri (anno, brand e retailer)

        """
        topVendite = []
        if (anno is None or anno == "" or anno == "Nessun filtro") and (brand is None or brand == "" or brand == "Nessun filtro") and (retailer_code is None or retailer_code == "" or retailer_code == "Nessun filtro"):
            topVendite = DAO.getTopVendite1()
        if (anno is not None and anno != "" and anno != "Nessun filtro") and (brand is None or brand == "" or brand == "Nessun filtro") and (retailer_code is None or retailer_code == "" or retailer_code == "Nessun filtro"):
            topVendite = DAO.getTopVendite2(anno)
        if (anno is not None and anno != "" and anno != "Nessun filtro") and (brand is not None and brand != "" and brand != "Nessun filtro") and (retailer_code is not None and retailer_code != "" and retailer_code != "Nessun filtro"):
            topVendite = DAO.getTopVendite3(anno, brand, int(retailer_code))
        return topVendite

    def analizzaVendite(self, anno, brand, retailer_code):
        """
        Questo metodo del modello permette di recuperare dal database i dati riguardanti le statistiche delle vendite (compreso i ricavi) in base ai filtri selezionati e non.\n
        Divideremo i dati statistici in due tipi: \n
        StatisticheVendite1: le statistiche delle vendite derivati dal fatto di non aver selezionato nessun filtro di anno, brand e retailer. \n
        StatisticheVendite2: le statistiche delle vendite derivanti dal fatto di aver selezionato tutti e tre i filtri di anno, brand e retailer.\n
        :param anno: anno delle vendite
        :param brand: brand delle vendite
        :param retailer_code: il codice che identifica il retailer delle vendite (viene passata come stringa, quindi importante prima di contattare il db fare un parsing per renderlo un intero)
        :return: restituisce il giro d'affari (il volume totale dei ricavi, ottenuto dalla somma dei ricavi), il numero di vendite, il numero dei retailer coinvolti e il numero di prodotti coinvolti
        """
        giro_affari = 0
        numero_vendite = 0
        numero_retailers = 0
        lista_retailers = []
        numero_prodotti = 0
        lista_prodotti = []
        vendite = []

        if (anno is None or anno == "" or anno == "Nessun filtro") and (brand is None or brand == "" or brand == "Nessun filtro") and (retailer_code is None or retailer_code == "" or retailer_code == "Nessun filtro"):
            vendite = DAO.getStatisticheVendite1()
        elif (anno is not None and anno != "" and anno != "Nessun filtro") and (brand is not None and brand != "" and brand != "Nessun filtro") and (retailer_code is not None and retailer_code != "" and retailer_code != "Nessun filtro"):
            vendite = DAO.getStatisticheVendite2(anno, brand, int(retailer_code))

        for vendita in vendite:
            giro_affari = giro_affari + vendita.Ricavo
            numero_vendite += 1
            if vendita.Retailer_code not in lista_retailers:
                lista_retailers.append(vendita.Retailer_code)
            if vendita.Product_number not in lista_prodotti:
                lista_prodotti.append(vendita.Product_number)
        numero_retailers = len(lista_retailers)
        numero_prodotti = len(lista_prodotti)

        return giro_affari, numero_vendite, numero_retailers, numero_prodotti



