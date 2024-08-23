def menu():
    while True:
        print("\nMenu de Operações:")
        print("1. União")
        print("2. Intersecção")
        print("3. Diferença")
        print("4. Produto cartesiano")
        print("5. Verificar se A é subconjunto de B")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        conjunto_A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
        conjunto_B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())
        
        if escolha == '1':
            print(f"A ∪ B = {conjunto_A | conjunto_B}")
        elif escolha == '2':
            print(f"A ∩ B = {conjunto_A & conjunto_B}")
        elif escolha == '3':
            print(f"A - B = {conjunto_A - conjunto_B}")
            print(f"B - A = {conjunto_B - conjunto_A}")
        elif escolha == '4':
            produto_cartesiano = {(a, b) for a in conjunto_A for b in conjunto_B}
            print(f"Produto cartesiano A x B = {produto_cartesiano}")
        elif escolha == '5':
            print(f"A ⊆ B : {conjunto_A.issubset(conjunto_B)}")
            print(f"A ⊂ B : {conjunto_A.issubset(conjunto_B) and conjunto_A != conjunto_B}")
        elif escolha == '6':            
            break
            print("Encerrando o programa.")
        else:
            print("Opção inválida. Tente novamente.")



menu()