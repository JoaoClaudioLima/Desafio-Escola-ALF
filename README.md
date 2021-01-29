# Desafio Escola ALF
Repositório do Desafio Escola ALF
## Índice
* [Informações Gerais](###Informações-Gerais)
* [Tecnologias](###Tecnologias)
* [Setup](###Setup)
* [Tutorial de Utilização](###Tutorial-de-Utilização)
* [Limitações e Futuro](###Limitações-e-Futuro)

## Informações Gerais
O presente projeto é uma API simples de geração de relatório de alunos aprovados, com base em dados cadastrados pelos administradores.

## Tecnologias
O projeto foi criado utilizando as tecnologias presentes no arquivo 'requirements.txt'.

## Setup
Para executar a API, favor copiar todo o conteúdo deste repositório para um diretório a sua escolha.
Feito isto, acessar o diretório pelo terminal e executar 'python main.py'. A API será hosteada localmente.

Favor notar que existem arquivos de database vazios no diretório '/db'. Estas databases serão manipuladas pelos métodos presentes no diretório 'db_handling' e, caso seja a intenção, alteradas. As funcionalidades do app encontram no arquivo 'Documentação API Escola ALF', no presente repositório.

Caso seja intenção executar o app para databases outras, subistituir respeitando ambos os nomes dos arquivos e keys de cada database (encontradas também no arquivo 'Documentação API Escola ALF'.

## Tutorial de Utilização
Para o cadastro de novos dados na db, algumas regras devem ser observadas:
### Cadastro de Alunos
Para o cadastro de novos Alunos, deve ser informado o "nome" do aluno para a KEY "nome".
Onde:
* "nome" deve ser um string com o nome a ser inserido. Este aluno receberá o ID de onde ele será inserido. Assim, o primeiro aluno cadastrado terá o ID 1, o segundo terá o ID 2 e assim sucessivamente.

### Cadastro de Respostas
Para o cadastro de Respostas, devem ser informados o "ID da Prova", "ID do Aluno" e "Resposta" para as KEYS "id_prova", "id_aluno" e "resposta", respectivamente.
Onde:
* "resposta" deve ser um string com as respostas do aluno "id_aluno" para a prova "id_prova". Esta resposta deve ser cadastrada da forma "abcd", onde "a" é a resposta da primeira questão, "b" da segunda questão e assim sucessivamente. Favor notar que, para o funcionamento da API, a string "resposta" deve ter o mesmo comprimento das strings "peso" e "gabarito", a serem definidas no tópico a seguir. Para o caso de o aluno não ter resolvido uma das questões, por exemplo a segunda, cadastrar da forma: "aXcd" Em situações que o aluno não realizou uma prova que deveria ter feito, cadastrar as respostas da forma "XXXX".
* "id_aluno" deve ser um inteiro que se refira a um aluno cadastrado na database de cadastro de alunos.
* "id_prova" deve ser um inteiro que se refira a uma prova feita por um aluno, onde seu gabarito foi cadastrado na database de cadastro de gabaritos.

### Cadastro de Gabaritos
Para o cadastro de Gabaritos, devem ser informados o "ID da Prova", "Peso" e "Gabarito" para as KEYS "id_prova", "peso" e "gabarito", respectivamente.
Onde:
* "gabarito" deve ser um string com o gabarito da prova "id_prova". Este gabarito deve ser cadastrado da forma "abcd", onde "a" é o gabarito da primeira questão, "b" da segunda questão e assim sucessivamente. Favor notar que, para o funcionamento da API, a string "gabarito" deve ter o mesmo comprimento das strings "peso" e "resposta", a serem definidas no a seguir e no tópico anterior.
* "id_prova" deve ser um inteiro que se refira a uma prova feita por um aluno, onde o ID do aluno e suas respostas foram cadastrados na database de cadastro de respostas.
* "peso" deve ser um string com o peso da prova "id_prova". Este peso deve ser cadastrado da forma "1234", onde "1" é o peso da primeira questão, "2" da segunda questão e assim sucessivamente. Favor notar que, para o funcionamento da API, a string "peso" deve ter o mesmo comprimento das strings "resposta" e "gabarito", definidas anteriormente. Por motivos de limitações da atual versão do projeto, somente pesos com valor menor que 10 podem ser tratados pela API. Esta limitação será abordada em versões futuras.

### Observações
Para facilitação de visualização, um exemplo de como devem ser as databases tratadas pela API pode ser encontrado no diretório '/testes'. De forma semelhante, estas informações podem ser encontradas em 'Documentação API Escola ALF'.

## Limitações e Futuro

Existem atualmente algumas limitações no projeto. É de interesse do desenvolvedor adaptar futuramente a API para melhor atender o cliente. Os principais tópicos a serem atacados em seguida se encontram listados:

* Cadastro de pesos: no momento, o cadastro de pesos somente permite cadastrar um valor inteiro menor que 10. Nas próximas versões serão feitas modificações que permitam uma escolha mais abrangente de pesos.
* Atualização de cadastros: no momento o cadastro não pode ser alterado ou deletado. Conforme o prosseguimento do projeto, estes métodos serão implementados.
* Cálculo mais preciso de notas: atualmente o projeto se baseia na hipótese que todos os alunos fizeram todas as provas para a geração da nota. Portanto, no caso de um aluno não fazer uma prova que deveria ter feito, essa prova não é incluída no cálculo de nota (a menos que seja tratada da forma especificada no tópico "Tutorial de Utilização"). Pretende-se implementar uma forma de discernir alunos que não realizaram alguma prova que deveriam fazer, além da especificada no tópico "Tutorial de Utilização".
