from locale import setlocale, LC_ALL
from datetime import datetime, timedelta
from dao import CategoriasDao, FornecedoresDao, ProdutosDao, ClientesDao, CargosDao, VendedoresDao, VendasDao
import PyNumBR as numbr


setlocale(LC_ALL, 'pt_BR.UTF-8')
MASCARA_DATA = '%d/%m/%Y'
MASCARA_DATA_HORA = '%d/%m/%Y %H:%M:%S'
FUSO = timedelta(hours=-3)
