from configparser import InterpolationMissingOptionError
from categorias import Categorias
from fornecedores import Fornecerdores
from produtos import Produtos
from pessoas import Clientes, Funcionarios
from cargos import Cargos
from vendas import Vendas
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
