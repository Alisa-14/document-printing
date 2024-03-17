from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_page(self):
        pass


class Document:
    @staticmethod
    def print_document(print_type):
        if print_type == "InkjetPrinter":
            return InkjetPrinter
        elif print_type == "LaserPrinter":
            return LaserPrinter
        else:
            raise ValueError("Принтер не найден")


class InkjetPrinter(Printer):
    def print_page(self):
        print(f'Страница распечатана на "Струйном принтере"')


class LaserPrinter(Printer):
    def print_page(self):
        print(f'Страница распечатана на "Лазерном принтере"')


if __name__ == "__main__":
    try:
        doc_1 = Document.print_document("InkjetPrinter")()
        doc_1.print_page()
        doc_2 = Document.print_document("LaserPrinter")()
        doc_2.print_page()
        doc_3 = Document.print_document("FalsePrinter")()
        doc_3.print_page()
    except ValueError as error:
        print(error)
