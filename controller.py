from scr.models.vendas import Vendas
from scr.dals.vendas import VendasDal
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
import util.PyNumBR as pnb
import util.PyUtilTerminal as put


class VendasController:

    @classmethod
    def buscar(cls, id=None, data_i=None, data_f=None, invisiveis=False
               ) -> list:
        vendas = VendasDal()
        if id is not None:
            listas = list(filter(lambda venda: venda.id == id,
                                 vendas.listar()))
        elif data_i is not None and data_f is None:
            listas = list(filter(lambda venda: venda.data == data_i,
                                 vendas.listar()))
        elif data_i is not None and data_f is not None:
            
        else:
            listas = vendas.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def cadastrar(cls, funcionario: str, cliente: str, compra: list,
                  valor: float, visivel=1) -> str:
        vendas = VendasDal()
        n_cupom = vendas.gera_cupom()
        venda = Vendas(n_cupom, funcionario, pnb.pega_data(), cliente, compra,
                       valor, visivel)
        if vendas.salvar(venda, 'a'):
            return 'Venda cadastrada com sucesso'
        else:
            return 'Erro não foi possível realizar o cadastro'


if __name__ == '__main__':
    pass
