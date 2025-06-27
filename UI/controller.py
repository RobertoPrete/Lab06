import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillDD(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))

        brands = self._model.getBrands()
        retailers = self._model.getRetailers()
