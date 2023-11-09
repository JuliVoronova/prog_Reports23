import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal
from new_design.main_window import Ui_MainWindow
from new_design.new_kss_window import Ui_new_kss
from new_design.new_metodology_window import Ui_new_metodology
from new_design.new_docs import Ui_new_docs
import protokols

# глобальные переменные
# количество нажатий на кнопку
count_clicked_add_kss = 0

class MainWindow(QMainWindow):

    new_protokol = protokols.CreateProt()

    #general_information_signal = pyqtSignal(list)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # создание экземпляра класса
        # self.new_protokol = protokols.CreateProt()
        #print(self.new_protokol.__dict__)

        self.ui.add_kss.clicked.connect(self.open_new_kss_window)
        self.ui.add_metodology.clicked.connect(self.open_new_metodology_window)
        self.ui.add_doc.clicked.connect(self.open_new_docs_window)

        # "стираю" всю введённую информацию
        #self.ui.create.clicked.connect(self.test_new)
        #self.ui.create.clicked.connect(self.count_kss)
        self.ui.create.clicked.connect(self.update)

    def default_date(self):
        self.new_protokol.set_date_control(date_control=protokols.CreateProt.DATE_CONTROL)
        self.new_protokol.set_date_welding(date_welding=protokols.CreateProt.DATE_WELDING)

    def update(self):
        print('Предварительный протокол сохранён')
        print(f'Добавлено КСС всего {count_clicked_add_kss}')
        self.default_count_kss()

    def default_count_kss(self):
        '''Возобновляет цикл добавления КСС'''
        global count_clicked_add_kss
        count_clicked_add_kss = 0

        self.update_new_protokol()

    @classmethod
    def update_new_protokol(cls):
        '''Присваивает экземпляру класса первоначальные значения аргументов'''
        cls.new_protokol = protokols.CreateProt()

    def open_new_docs_window(self):
        self.new_window_docs = Documents(self)
        self.new_window_docs.docs_signal.connect(self.save_docs_info)
        # также обновляю общую информацию при нажатии "Создать"
        self.new_window_docs.ui.add_docs.clicked.connect(self.save_general_information)
        # обновляю тип контроля при при нажатии "Создать"
        self.new_window_docs.ui.add_docs.clicked.connect(self.save_type_control)
        # проверка
        #self.new_window_docs.ui.add_docs.clicked.connect(self.test_new)
        #self.new_window_docs.ui.add_docs.clicked.connect(self.default_date)
        self.new_window_docs.exec_()

    def open_new_metodology_window(self):
        self.new_window_metod = Metodology(self)
        self.new_window_metod.metodology_info_signal.connect(self.save_metodology_info)
        # подготавливаю шаблон
        self.new_window_metod.ui.add_metodology.clicked.connect(self.create_template)
        # обновляю на дату по умолчанию
        self.new_window_metod.ui.add_metodology.clicked.connect(self.default_date)
        self.new_window_metod.exec_()

    def open_new_kss_window(self):
        self.new_window_kss = KssWindow(self)
        # сохраняем новое КСС
        self.new_window_kss.kss_info_signal.connect(self.save_kss_info)
        # сколько КСС на данный момент
        self.new_window_kss.ui.add_kss.clicked.connect(self.print_count_kss)
        self.new_window_kss.exec_()

    def save_general_information(self):
        '''Записывает новые значения в атрибуты экземпляра класса CreateProt'''
        self.new_protokol.set_number_prot(number_prot=self.ui.number_prot.text() or None)
        self.new_protokol.set_date_welding(date_welding=self.ui.date_welding.text() or None)
        self.new_protokol.set_date_control(date_control=self.ui.date_control.text() or None)
        self.new_protokol.set_program_for_customer(program=self.ui.num_programm.text() or None,
                                                   customer=self.ui.customer.text() or None)
        self.new_protokol.set_welder_info(ty_opo=self.ui.ty_opo.text() or None,
                                          fio_welder=self.ui.fio_welder.text() or None,
                                          stigma=self.ui.stigma.text() or None)

    def save_type_control(self):
        '''Отслеживает кнопки выбора метода контроля'''
        self.new_protokol.set_type_control(
            vt=self.ui.vt_button.isChecked(),
            ut=self.ui.ut_button.isChecked(),
            rt=self.ui.rt_button.isChecked(),
            mt=self.ui.mt_button.isChecked(),
            pt=self.ui.pt_button.isChecked())

    def save_metodology_info(self, metodology):
        '''Обновляет атрибут metodology в new_protokol'''
        self.new_protokol.set_metodology(metodology=metodology)

    def save_docs_info(self, docs_info):
        '''Добавляет документы в new_protokol'''
        self.new_protokol.set_docs(
            doc_1=docs_info[0],
            doc_2=docs_info[1],
            doc_3=docs_info[2],
            doc_4=docs_info[3]
        )
        self.new_protokol.set_quality_level(quality_level=docs_info[4])
        self.new_protokol.set_all_welding_types(all_welding_types=docs_info[5])

    def save_kss_info(self, list_info):
        '''Записывает значения окна "Новый образец" в локальные атрибуты экземпляра new_protokol'''
        self.new_protokol.set_new_kss(
            kss=list_info[0],
            diameter=list_info[1],
            thickness=list_info[2],
            standard_size=list_info[3],
            steel_grade=list_info[4],
            welding_method=list_info[5]
        )
        self.click_add_kss()


    def print_count_kss(self):
        print(f'Добавлено КСС: {count_clicked_add_kss}')

    def create_template(self):
        '''Формирует предварительный протокол'''
        self.new_protokol.get_template()

    def test_new(self):
        '''Обновились ли атрибуты экземпляра класса'''
        print(self.new_protokol.__dict__)

    def click_add_kss(self):
        '''Обновляет количество нажатий кнопки "Добавить КСС"'''
        global count_clicked_add_kss
        count_clicked_add_kss += 1
        self.save_count_kss()

    def save_count_kss(self):
        self.new_protokol.set_count_kss(count_clicked_add_kss=count_clicked_add_kss)

    def count_kss(self):
        print(count_clicked_add_kss)


    def create_protokol(self):
        '''
        Вызывает функ-ю формирования протоколов
        '''
        self.new_protokol.create()
        # При нажатии кнопки "Создать" количество добавленных в протокол КСС обнуляется


    def print_kss_info(self, kss_info):
        print(kss_info)

    def print_b(self):
        print(self.click_add_kss)

class KssWindow(QDialog):

    kss_info_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_kss()
        self.ui.setupUi(self)
        self.setWindowTitle('Новый образец')

        self.ui.add_kss.clicked.connect(self.add_kss_information)

    def add_kss_information(self):
        '''Передача введённых данных окна "Новый образец"'''
        kss = self.ui.kss.text()
        diameter = self.ui.diameter.value()
        thickness = self.ui.thickness.value()
        standard_size = self.ui.standard_size.text()
        steel_grade = self.ui.steel_grade.currentText()
        welding_method = self.ui.welding_metod.currentText()
        list_kss_information = [kss, diameter, thickness, standard_size, steel_grade, welding_method]
        self.kss_info_signal.emit(list_kss_information)
        self.accept()

class Metodology(QDialog):

    metodology_info_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_metodology()
        self.ui.setupUi(self)
        self.setWindowTitle('Методика')

        self.ui.add_metodology.clicked.connect(self.add_metodology)

    def add_metodology(self):
        '''Передача введённых данных окна "Метод"'''
        metodology = self.ui.comboBox.currentText()
        self.metodology_info_signal.emit(metodology)
        self.accept()

class Documents(QDialog):

    docs_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_docs()
        self.ui.setupUi(self)
        self.setWindowTitle('Документы')

        self.ui.add_docs.clicked.connect(self.add_docs)

    def add_docs(self):
        '''Передача введённых данных окна "Документы"'''
        doc_1 = self.ui.doc_1.currentText()
        doc_2 = self.ui.doc_2.currentText()
        doc_3 = self.ui.doc_3.currentText()
        doc_4 = self.ui.doc_4.currentText()
        quality_level = self.ui.quality_level.currentText()
        all_welding_types = self.ui.all_welding_type.text()
        documents_info = [doc_1, doc_2, doc_3, doc_4, quality_level, all_welding_types]
        self.docs_signal.emit(documents_info)
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


