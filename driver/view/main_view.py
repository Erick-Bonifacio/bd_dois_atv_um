import os

class MainView:

    def start(self):
        return self.menu()

    def menu(self):
        print('\n' + '=' * 40)
        print('        SISTEMA DE PEDIDOS NORTHWIND')
        print('=' * 40)
        print('1  Inserir novo pedido')
        print('2  Consultar informações de um pedido')
        print('3  Consultar informações de um pedido (inseguro)')
        print('4  Ver ranking de funcionários')
        print('5  Sair do sistema')

        print('=' * 40)
        opcao = input('🔸 Escolha uma opção: ')
        return opcao
    
    def insert_order(self):
        print('\nPreencha os dados do novo pedido:\n')

        pedido_id = input('Código do pedido: ')
        cliente_id = input('ID do cliente: ')
        funcionario_id = input('ID do funcionário: ')
        data_pedido = input('Data do pedido (YYYY-MM-DD): ')
        data_necessaria = input('Data necessária (YYYY-MM-DD): ')
        data_envio = input('Data de envio (YYYY-MM-DD): ')
        frete = input('Valor do frete: ')
        nome_entrega = input('Nome da entrega: ')
        endereco_entrega = input('Endereço de entrega: ')
        cidade_entrega = input('Cidade de entrega: ')
        regiao_entrega = input('Região de entrega: ')
        cep_entrega = input('CEP de entrega: ')
        pais_entrega = input('País de entrega: ')
        transportadora_id = input('ID da transportadora: ')

        qtd_itens = int(input("Quantidade de itens no pedido: "))
        detalhes = []
        for _ in range(qtd_itens):
            produto_id = input("ID do produto: ")
            preco_unitario = input("Preço unitário: ")
            quantidade = input("Quantidade: ")
            desconto = input("Desconto: ")
            detalhes.append((pedido_id, produto_id, preco_unitario, quantidade, desconto))

        return {
            'order': [
                pedido_id, cliente_id, funcionario_id, data_pedido, data_necessaria, data_envio,
                frete, nome_entrega, endereco_entrega, cidade_entrega, regiao_entrega,
                cep_entrega, pais_entrega, transportadora_id
            ],
            'order_details': detalhes
        }

    def get_order(self):
        return input('Informe o código do pedido: ')

    def display_information(self, registros):
        print("\nInformações do Pedido:")
        for linha in registros:
            print("----------------------------")
            print("Código do Pedido:", linha[0])
            print("Data do Pedido:", linha[1])
            print("Cliente:", linha[2])
            print("Funcionário:", linha[3])
            if linha[4] is not None:
                print("Produto:", linha[4])
                print("Preço Unitário:", linha[5])
                print("Quantidade:", linha[6])
            else:
                print("⚠️  Esse pedido não possui itens cadastrados.")
        input('\nPressione ENTER para continuar.')

    def display_rank(self, registros):
        for i, linha in enumerate(registros, start=1):
            print("----------------------------")
            print("Posição:", i)
            print("Funcionário:", linha[0])
            print("Data de Admissão:", linha[1])
            print("Total de Pedidos:", linha[2])
            print("Soma das Vendas:", linha[3])
        input('\nPressione ENTER para continuar.')

    def display_message(self, mensagem):
        print(mensagem)
        input('\nPressione ENTER para continuar.')

    def valid_entry(self):
        print('Opção inválida. Por favor, escolha uma opção válida.')
        input('\nPressione ENTER para voltar ao menu.')

    def exit_program(self):
        os.system('cls' if os.name == 'nt' else 'clear')
