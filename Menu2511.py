'''
Objetivo:
Desenvolver uma aplicação em Python que aborde uma solução ao tema proposto.
'''

# Menu de códigos
print("\n-----FUNCIONALIDADES-----\n"
      "\nPROBLEMA -------------- 1"
      "\nSOLUÇÃO --------------- 2"
      "\nEXEMPLOS -------------- 3")

# Input do código escolhido
op = int(input("\nInsira o código equivalente a funcionalidade desejada: "))

# Descrições
match op:
    case 1:
        print("\nPROBLEMA\n"
              "\nO nosso dia a dia é cheio de coisas e datas a se lembrar, \nresponsabilidades no trabalho, datas de provas, aniversário \ndos amigos, o que comprar no mercado entre outros mil. Nessa \ncorreria, quando sobra tempo para lembrarmos que a nossa \nconsulta no odontologista faz algum tempo? Ou então quanto \ntempo atrás compramos uma nova escova de dente e precisamos \ntrocá-la?"
              "\nA não ser que setenha tudo bem anotado em uma agenda, fica \ndifícil acompanhar essas datas no meio de tantas outras, o \nque compromete em muito a saúde que deveria ser cuidada no \ndia a dia para uma prevenção adequada ou mesmo tratamentos    \nque não deveriam ser esquecidos.")
    case 2:
        print("\nSOLUÇÃO\n"
              "\nFoi pensando nisso que desenvolvemos Raquel, a sua scretária \nda saúde!"
              "\nA Raquel é uma aplicação que busca auxiliar o usuário com \nlembretes voltados tanto para a prevenção com cuidados \nbásicos de saúde quanto para o acompanhamento de tratamentos \ncontínuos."
              "\nO aplicativo alivia a necessidade de ficar recordando de \ncabeça a questão da saúde, deixando mais espaço para cuidar \nde outras coisas no dia a dia."
              "\nApós um pequeno cadastro rápido, que pode ser feito no ponto \nde ônibus, a Raquel já retorna notificações de tratamentos já \niniciados com o histórico do paciente caso esse seja cliente \nde um plano de saúde da Hapvida NotraDame Intermédica ou \nentão após selecionar o primeiro módulo o qual deseja que a \nRaquel tome conta."
              "\nUtilizando módulos para cada cuidado, o usuário seleciona \nquais deseja que a Raquel cuide e de acordo com planos pré \nfeitos que podem ser customizados pelo usuário, a Raquel vai \nnotificar o usuário quando for horário ou época de tomar uma \nmedicação ou agendar uma consulta.")
    case 3:
        print("\nEXEMPLOS\n"
              "\nODONTOLOGIA"
              "\nAo selecionar o módulo de odontologia, a Raquel irá perguntar \nao usuário quando foi a sua última consulta ao odontologista \ne quando foi a última vez que comprou uma escova de dentes \nnova."
              "\nDe início a Raquel irá notificar para lembrar o usuário a \nagendar uma consulta ao odontologista a cada 6 meses e a \ncompra de uma escova nova a cada 3 meses, seguindo \nrecomendações do Conselho Federal de Odontologia (CFO), mas \nque podem ser customizados de acordo com a necessidade do \nusuário."
              
              "\n\nOFTAMOLOGIA"
              "\nAo selecionar o módulo de oftamologia, a Raquel irá perguntar \nao usuário qual foi a sua última consulta ao oftamologista e \nirá recordá-lo a agendar uma nova consulta 1 ano após a \nanterior, seguindo recomendação do Conselho Brasileiro de \nOftalmologia (CBO), mas que pode ser customizado de acordo \ncom a necessidade do usuário"
              
              "\n\nTRATAMENTOS CONTÍNUOS"
              "\nAo validar seu plano de saúde da Hapvida NotreDame \nIntermédica, a Raquel reconhece o tratamento que o usuário \npossui no banco de dados e retorna notificações para realizar \nseu tratamento de acordo com a recomendação médica recebida, \nque pode ser customizado dentro dos limites estabelecidos \npelo médico."
              "\nEx.: Medicação antes de dormir apenas poderá ser customizada \npara notificar durante a noite.")