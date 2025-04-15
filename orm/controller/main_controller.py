from view.view import View
from model.model_dao import OrderDAO

class Controller:
    def __init__(self):
        self.view = View()
        self.dao = OrderDAO()

    def start(self):
        while True:
            opcao = self.view.show_menu()
            if opcao == '1':
                self.add_order()
            elif opcao == '2':
                self.infos_order()
            elif opcao == '3':
                self.ranking_funcionarios()
            elif opcao == '4':
                print("Saindo...")
                break
            else:
                self.view.display_message("Opção inválida, tente novamente.")

            input("Pressione Enter para continuar")
            self.view.clear_screen()

    def add_order(self):
        order_data = self.view.get_order_data()
        order_details = self.view.get_order_details()
        self.dao.create_order(order_data, order_details)
        self.view.display_message("Order inserido com sucesso!")

    def infos_order(self):
        order_id = self.view.get_order_id()  
        order_info = self.dao.get_order_info(order_id)
        if order_info:
            self.view.display_order_info(order_info)
        else:
            self.view.display_message("Order não encontrado.")

    def ranking_funcionarios(self):
        start_date = input("Data inicial (YYYY-MM-DD): ")
        end_date = input("Data final (YYYY-MM-DD): ")
        ranking = self.dao.employee_ranking(start_date, end_date)
        self.view.display_employee_ranking(ranking)

if __name__ == '__main__':
    controller = Controller()
    controller.start()