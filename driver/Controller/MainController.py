from driver.View.mainView import MainView
from driver.Model.ModelDAO.PedidoDAO import PedidoDAO
from driver.Model.Connection import Connection
from datetime import datetime


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

            elif opcao == "3":
                print("📊 Ranking de Funcionários por intervalo de contratação")

                def solicitar_data(prompt):
                    while True:
                        data_input = input(prompt)
                        try:
                            # Valida o formato e se a data existe
                            datetime.strptime(data_input, "%Y-%m-%d")
                            return data_input
                        except ValueError:
                            print("❌ Data inválida. Use o formato YYYY-MM-DD e verifique se a data existe.")

                data_inicio = solicitar_data("📅 Digite a data inicial (YYYY-MM-DD): ")
                data_fim = solicitar_data("📅 Digite a data final (YYYY-MM-DD): ")

                erro, _, resultado = self.orderDAO.ranking_funcionarios(data_inicio, data_fim)

                if erro:
                    print("❌ Erro ao consultar ranking:", erro)
                else:
                    print("\n🏆 Ranking de Funcionários:")
                    for nome, hiredate, total_pedidos, total_vendas in resultado:
                        print(f"👤 {nome} | Contratado em: {hiredate} | Pedidos: {total_pedidos} | Total em vendas: ${total_vendas:.2f}")


            elif opcao == '4':
                self.view.exit_program()
                return

            else:
                self.view.valid_entry()

            opcao = self.view.menu()

if __name__ == '__main__':
    principal = Controlador()
    principal.iniciar()
