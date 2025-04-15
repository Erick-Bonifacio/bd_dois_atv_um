import os

class View:
    
    def show_menu(self):
        print('\n' + '=' * 40)
        print('        [ORM] SISTEMA DE PEDIDOS NORTHWIND')
        print('=' * 40)
        print('1️⃣  Inserir novo pedido')
        print('2️⃣  Consultar informações de um pedido')
        print('3️⃣  Ver ranking de funcionários')
        print('4️⃣  Sair do sistema')

        print('=' * 40)
        opcao = input('🔸 Escolha uma opção: ')
        return opcao

    def get_order_data(self):
        order_id = self.ask_for_order_id()
        customer_id = input("ID do cliente: ")
        employee_id = input("ID do funcionário: ")
        order_date = input("Data do pedido (YYYY-MM-DD): ")
        required_date = input("Data necessária (YYYY-MM-DD): ")
        shipped_date = input("Data de envio (YYYY-MM-DD): ")
        freight = input("Valor do frete: ")
        ship_name = input("Nome do destinatário: ")
        ship_address = input("Endereço do destinatário: ")
        ship_city = input("Cidade do destinatário: ")
        ship_region = input("Região do destinatário: ")
        ship_postal_code = input("CEP do destinatário: ")
        ship_country = input("País do destinatário: ")
        shipper_id = input("ID da transportadora: ")

        return {
            "orderid": order_id,
            "customerid": customer_id,
            "employeeid": employee_id,
            "orderdate": order_date,
            "requireddate": required_date,
            "shippeddate": shipped_date,
            "freight": freight,
            "shipname": ship_name,
            "shipaddress": ship_address,
            "shipcity": ship_city,
            "shipregion": ship_region,
            "shippostalcode": ship_postal_code,
            "shipcountry": ship_country,
            "shipperid": shipper_id
        }

    def get_order_details(self):
        quantity = int(input("Quantidade de itens no pedido: "))
        details = []

        for _ in range(quantity):
            product_id = input("ID do produto: ")
            unit_price = input("Preço unitário: ")
            quantity = input("Quantidade: ")
            discount = input("Desconto: ")
            details.append({"productid": product_id, "unitprice": unit_price, "quantity": quantity, "discount": discount})

        return details

    def get_order_id(self):
        return input("ID do pedido: ")

    def ask_for_order_id(self):
        while True:
            order_id = input("Digite um novo ID para o pedido: ")
            if order_id.isdigit():
                return int(order_id)
            else:
                print("Insira um número válido.")
                
    def display_order_info(self, order_info):
        print("\n***** Relatório do Pedido *****\n")
        for key, value in order_info.items():
            print(f"{key}: {value}")

    def display_employee_ranking(self, ranking):
        print("\n***** Ranking dos Funcionários *****\n")
        for employee in ranking:
            print(f"Nome do funcionário: {employee[0]} {employee[1]} - Total de pedidos realizados: {employee[2]}, Soma dos valores vendidos: R$ {employee[3]:.2f}")

    def display_message(self, message):
        print(message)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')