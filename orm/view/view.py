import os

class View:
    
    def show_menu(self):
        print("1. Inserir novo pedido")
        print("2. Relatório de pedido")
        print("3. Exibir ranking dos funcionários")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        return opcao

    def get_order_data(self):
        order_id = self.ask_for_order_id()
        customer_id = input("ID do Cliente: ")
        employee_id = input("ID do Empregado: ")
        order_date = input("Data do Pedido (YYYY-MM-DD): ")
        required_date = input("Data Requerida (YYYY-MM-DD): ")
        shipped_date = input("Data de Envio (YYYY-MM-DD): ")
        freight = input("Frete: ")
        ship_name = input("Nome do Destinatário: ")
        ship_address = input("Endereço do Destinatário: ")
        ship_city = input("Cidade do Destinatário: ")
        ship_region = input("Região do Destinatário: ")
        ship_postal_code = input("CEP do Destinatário: ")
        ship_country = input("País do Destinatário: ")
        shipper_id = input("ID do Transportador: ")

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
        details = []
        print("\nDigite os itens do pedido (deixe em branco para finalizar e pressione Enter):")
        while True:
            product_id = input("ID do Produto: ")
            if not product_id:
                break
            quantity = input("Quantidade: ")
            unit_price = input("Preço: ")
            details.append({"productid": product_id, "quantity": quantity, "unitprice": unit_price})
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
            print(f"{employee[0]} {employee[1]} - Pedidos: {employee[2]}, Vendas: R$ {employee[3]:.2f}")

    def display_message(self, message):
        print(message)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')