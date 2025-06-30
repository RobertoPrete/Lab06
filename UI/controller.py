import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None
        self._anno = None
        self._brand = None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillDD(self):
        anni = self._model.listaAnni
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))

        brands = self._model.listaBrands
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))

        retailers = self._model.listaRetailers
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code,
                                                                     text=retailer.Retailer_name,
                                                                     data=retailer))

    def setRetailer(self, e):
        self._retailer = e.control.value

    def read_brand(self, e):
        self._brand = self._view.dd_brand.value = e.control.value

    def read_anno(self, e):
        self._anno = self._view.dd_anno.value = e.control.value

    def handleTopVendite(self, e):
        topvendite = self._model.top_vendite(self._anno, self._brand, self._retailer)
        self._view.txt_result.controls.clear()
        for x in topvendite:
            self._view.txt_result.controls.append(ft.Text(x.__str__()))
        self._view.update_page()

    def handleAnalizzaVendite(self, e):
        self._view.txt_result.controls.clear()
        (giro_affari, numero_vendite, numero_retailer, numero_prodotti) = self._model.analizzaVendite(self._anno, self._brand, self._retailer)
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {giro_affari}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {numero_vendite}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {numero_retailer}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {numero_prodotti}"))
        self._view.update_page()



