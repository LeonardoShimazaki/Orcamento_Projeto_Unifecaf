# Orcamento_Projeto_Unifecaf

# 🏠 Sistema de Orçamento de Locação

## 📌 Descrição
Este projeto consiste em um sistema desenvolvido em Python para simulação de orçamento de locação de imóveis. A aplicação permite ao usuário selecionar o tipo de imóvel, adicionar melhorias, calcular valores e gerar um arquivo com os dados finais.

---

## 🧠 Lógica do Sistema

A aplicação segue um fluxo lógico baseado na interação do usuário, conforme descrito abaixo:

### 1. Coleta de dados do cliente
- O sistema solicita o nome do cliente
- O nome é armazenado para ser utilizado no orçamento final

### 2. Verificação de filhos
- O sistema pergunta se o cliente possui filhos
- Caso **não possua filhos** e escolha **apartamento**, é aplicado **desconto de 5%**

### 3. Escolha do tipo de locação
O usuário escolhe entre:

- Casa → R$ 900,00  
- Apartamento → R$ 700,00  
- Estúdio → R$ 1200,00  

---

### 4. Escolha de quartos (Casa/Apartamento)
- 1 quarto → sem alteração  
- 2 quartos → acréscimo no valor:

| Tipo        | Acréscimo |
|------------|----------|
| Casa       | + R$ 250,00 |
| Apartamento| + R$ 200,00 |

---

### 5. Vaga de garagem

#### Para Casa e Apartamento:
- + R$ 300,00

#### Para Estúdio:
- Até 2 vagas → + R$ 250,00  
- Acima de 2 vagas → + R$ 60,00 por vaga adicional  

---

### 6. Valor do contrato
- Valor fixo: **R$ 2000,00**
- Parcelamento em até **5x sem juros**

---

### 7. Cálculo das parcelas
- O sistema calcula os valores mensais para os próximos **12 meses**
- Durante o período de parcelamento:
  - Valor = aluguel + parcela do contrato
- Após o parcelamento:
  - Valor = apenas aluguel

---

### 8. Exportação de dados
- O sistema pergunta se deseja gerar um arquivo `.csv`
- Caso sim:
  - O arquivo é gerado com todos os dados do orçamento

---

## ⚙️ Tecnologias Utilizadas

- Python
- Biblioteca `colorama`
- Biblioteca `csv`

---
