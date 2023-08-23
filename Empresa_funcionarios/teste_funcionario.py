from funcionario import Funcionario

funcionario1 = Funcionario("Matheus", "matheus@blablabal.com.br")

funcionario1.cadastro_hora('Jan', 300)
funcionario1.cadastro_hora('Fev', 200)
funcionario1.cadastro_salario_hora('Jan', 30)
funcionario1.cadastro_salario_hora("Fev", 30)
print(funcionario1)
print(funcionario1.calcular_salario("Jan"))
print(funcionario1.calcular_salario("Fev"))