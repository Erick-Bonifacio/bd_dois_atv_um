from view import View
from dao import PedidoDAO

class Controller:
    def __init__(self):
        self.view = View()
        self.dao = PedidoDAO()

    def start(self):
        while True:
            opcao = self.view.show_menu()
            if opcao == '1':
                self.add_pedido()
            elif opcao == '2':
                self.infos_pedido()
            elif opcao == '3':
                self.ranking_funcionarios()
            elif opcao == '4':
                print("Saindo...")
                break
            else:
                self.view.display_message("Opção inválida, tente novamente.")

            input("Pressione Enter para continuar")
            self.view.clear_screen()

    def add_pedido(self):
        pedido_data = self.view.get_pedido_data()
        pedido_details = self.view.get_pedido_details()
        self.dao.create_pedido(pedido_data, pedido_details)
        self.view.display_message("Pedido inserido com sucesso!")

    def infos_pedido(self):
        pedido_id = self.view.get_pedido_id()  
        pedido_info = self.dao.get_pedido_info(pedido_id)
        if pedido_info:
            self.view.display_pedido_info(pedido_info)
        else:
            self.view.display_message("Pedido não encontrado.")

    def ranking_funcionarios(self):
        start_date = input("Data inicial (YYYY-MM-DD): ")
        end_date = input("Data final (YYYY-MM-DD): ")
        ranking = self.dao.employee_ranking(start_date, end_date)
        self.view.display_employee_ranking(ranking)

if __name__ == '__main__':
    controller = Controller()
    controller.start()