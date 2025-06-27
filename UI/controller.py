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
            self._view.dd_anno.options.append(ft.dropdown.Option(anno, on_click=self.read_anno))

        brands = self._model.listaBrands
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand, on_click=self.read_brand))

        retailers = self._model.listaRetailers
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code,
                                                                     text=retailer.Retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))

    def read_retailer(self, e):
        self._retailer = e.control.data

    def read_brand(self, e):
        self._anno = e.control.data

    def read_anno(self, e):
        self._brand = e.control.data
