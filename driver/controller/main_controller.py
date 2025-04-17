from View.main_view import MainView
from Model.model_dao.pedido_dao import PedidoDAO

class Controlador:
    def __init__(self):
        self.view = MainView()
        self.orderDAO = PedidoDAO()

    def iniciar(self):
        if not self.orderDAO.testar_conexao():
            self.view.display_message("ERRO 500 - Falha na conexão com o banco de dados")
            return

        opcao = self.view.start()

        while opcao != '4':

            if opcao == '1':
                pedido = self.view.insert_order()
                try:
                    self.orderDAO.inserir_pedido(pedido)
                    self.view.display_message("✅ Pedido inserido com sucesso!")
                except Exception as e:
                    mensagem_erro = "❌ Erro ao inserir pedido. Detalhes: " + str(e)
                    self.view.display_message(mensagem_erro)

            elif opcao == '2':
                id_pedido = self.view.get_order()
                resultado = self.orderDAO.buscar_pedido_completo(id_pedido)
                if resultado[2]:
                    registros = resultado[2]
                    self.view.display_information(registros)
                else:
                    self.view.display_message("❗ Nenhum pedido encontrado com esse ID!")

            elif opcao == '3':
                id_pedido = self.view.get_order()
                resultado = self.orderDAO.buscar_pedido_completo_inseguro(id_pedido)
                print(resultado)
                if resultado[2]:
                    registros = resultado[2]
                    self.view.display_information(registros)
                else:
                    self.view.display_message("❗ Nenhum pedido encontrado com esse ID!")

            elif opcao == '4':
                resultado = self.orderDAO.ranking_funcionarios()
                if resultado[2]:
                    registros = resultado[2]
                    self.view.display_rank(registros)
                else:
                    self.view.display_message("❌ Não foi possível gerar o ranking")

            elif opcao == '5':
                self.view.exit_program()
                return

            else:
                self.view.valid_entry()

            opcao = self.view.menu()

if __name__ == '__main__':
    principal = Controlador()
    principal.iniciar()
