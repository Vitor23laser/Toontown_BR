import string

# To make sure the language checker is working
# DO NOT TRANSLATE THIS
ExtraKeySanityCheck = "Ignore me"

# common names
Mickey = "Mickey"
Minnie = "Minnie"
Donald = "Donald"
Daisy  = "Margarida"
Goofy  = "Pateta"
Pluto  = "Pluto"
Flippy = "Flippy"

MickeyMouse = "Mickey Mouse"

AIStartDefaultDistrict = "Vila dos Idiotas"

Cog  = "Cog"
Cogs = "Cogs"
ACog = "um Cog"
TheCogs = "os Cogs"
Skeleton = "Esqueletocogs"
SkeletonP = "Esqueletocogs"
ASkeleton = "um Esqueletocog"
Foreman = "Supervisor da fábrica"
ForemanP = "Supervisores da fábrica"
AForeman = "um Supervisor da fábrica"
CogVP = Cog + " VP"
CogVPs = "VPs Cogs"
ACogVP = ACog + " VP"
Supervisor = "Supervisor da Casa da Moeda"
SupervisorP = "Supervisores da Casa da Moeda"
ASupervisor = "um Supervisor da Casa da Moeda"
CogCFO = Cog + "Diretor Financeiro"
CogCFOs = "Diretores Financeiros Cogs"
ACogCFO = ACog + "Diretor Financeiro"

# Quests.py
TheFish = "o Peixe"
AFish = "um peixe"
Level = "nível"
QuestsCompleteString = "Concluir"
QuestsNotChosenString = "Não escolhido"

# _avName_ gets replaced with the avatar (player's) name
# _toNpcName_ gets replaced with the npc's name we are being sent to
# _where_ gets replaced with a description of where to find the npc, with a leading \a
QuestsDefaultGreeting = ("Olá, _avName_!",
                         "Oi, _avName_!",
                         "E aí, _avName_?",
                         "Diga aí, _avName_!",
                         "Bem-vindo, _avName_!",
                         "Tudo certo, _avName_?",
                         "Como vai você, _avName_?",
                         "Olá _avName_!",
                         )
QuestsDefaultIncomplete = ("Como está indo aquela tarefa, _avName_?",
                           "Parece que você ainda tem mais trabalho a fazer naquela tarefa!",
                           "Continue com o bom trabalho, _avName_!",
                           "Continue tentando concluir aquela tarefa. Eu sei que você consegue!",
                           "Continue tentando concluir a tarefa. Contamos com você!",
                           "Continue trabalhando naquela Tarefa Toon!",
                           )
QuestsDefaultIncompleteProgress = ("Você veio ao lugar certo, mas, primeiramente, precisa concluir sua Tarefa Toon.",
                                   "Ao terminar a Tarefa Toon, volte aqui.",
                                   "Volte quando tiver terminado sua Tarefa Toon.",
                                   )
QuestsDefaultIncompleteWrongNPC = ("Bom trabalho naquela Tarefa Toon. Você deveria visitar _toNpcName_._where_",
                                   "Parece que você está pronto para concluir sua Tarefa Toon. Vá ver _toNpcName_._where_.",
                                   "Vá ver _toNpcName_ para concluir sua Tarefa Toon._where_",
                                   )
QuestsDefaultComplete = ("Bom trabalho! Aqui está a sua recompensa...",
                         "Ótimo trabalho, _avName_! Tome esta recompensa...",
                         "Excelente trabalho, _avName_! Aqui está a sua recompensa...",
                         )
QuestsDefaultLeaving = ("Tchau!",
                        "Até logo!",
                        "Até mais, _avName_.",
                        "Te vejo por aí, _avName_!",
                        "Boa sorte!",
                        "Divirta-se em Toontown!",
                        "Vejo você depois!",
                        )
QuestsDefaultReject = ("Olá.",
                       "Posso ajudar?",
                       "Como vai você?",
                       "E aí, pessoal?",
                       "Estou um pouco ocupado agora, _avName_.",
                       "Sim?",
                       "Tudo certo, _avName_!",
                       "Bem-vindo, _avName_!",
                       "Ei, _avName_! Tudo bem?",
                       # Game Hints
                       "Você sabia que pode abrir seu Álbum Toon clicando em F8?",
                       "Você pode usar seu mapa para se teletransportar de volta ao pátio!",
                       "Você pode ficar amigo de outros jogadores clicando neles.",
                       "Você pode descobrir mais sobre um "+ Cog +" clicando nele.",
                       "Junte tesouros nos pátios para encher seu Risômetro.",
                       "Os edifícios " + Cog + " são lugares perigosos! Não entre neles sozinho!",
                       "Quando você perde uma batalha, os "+ Cogs +" tomam todas as suas piadas.",
                       "Para obter mais piadas, jogue no Bondinho!",
                       "Você pode obter mais Pontos de risadas completando as Tarefas Toon.",
                       "Toda Tarefa Toon dá uma recompensa a você.",
                       "Algumas recompensas permitem que você carregue consigo mais Piadas.",
                       "Se você vencer uma batalha, ganhará créditos de Tarefa Toon para cada "+ Cog +" derrotado.",
                       "Se você recuperar um edifício "+ Cog +", entre e verá um agradecimento especial do proprietário!",
                       "Se pressionar a tecla Page Up, poderá ver acima de você!",
                       "Se você pressionar a tecla Tab, poderá ver os arredores sob diversos ângulos!",
                       "Para mostrar aos amigos secretos o que está pensando, coloque '.' antes do pensamento.",
                       "Se um "+ Cog +" estiver atordoado, será mais difícil para ele desviar de objetos cadentes.",
                       "Cada tipo de edifício "+ Cog +" possui um visual diferente.",
                       "Derrotar os "+ Cogs +" nos andares mais altos de um edifício dará a você maiores recompensas de habilidade.",
                       )
QuestsDefaultTierNotDone = ("Olá, _avName_! Você deve concluir sua Tarefa Toon atual antes de começar uma nova.",
                            "E aí? Você precisa concluir suas Tarefas Toon atuais antes de começar uma nova.",
                            "Oi, _avName_! Para que eu possa dar a você uma nova Tarefa Toon, você precisa terminar as que você tem.",
                            )
# The default string gets replaced with the quest getstring
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ("Ouvi falar que _toNpcName_ está procurando por você._where_",
                                 "Passe por lá e visite _toNpcName_ quando tiver um tempinho._where_",
                                 "Visite _toNpcName_ da próxima vez em que estiver passando por aquele caminho._where_",
                                 "Se tiver um tempinho, pare e diga olá para _toNpcName_._where_",
                                 "_toNpcName_ dará a você sua nova Tarefa Toon._where_",
                                 )
QuestsCogQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogQuestHeadline = "PROCURADO"
QuestsCogQuestSCStringS = "Eu preciso derrotar %(cogName)s%(cogLoc)s"
QuestsCogQuestSCStringP = "Eu preciso derrotar alguns %(cogName)s%(cogLoc)s."
QuestsCogQuestDefeat = "Derrotar %s"

QuestsCogNewbieQuestObjective = "Ajude um Toon com %(laffPoints)d risadas, ou menos, a dominar %(objective)s"
QuestsCogNewbieQuestCaption = "Ajude um Toon com %d risadas, ou menos"
QuestsCogNewbieQuestAux = "Derrotar:"
QuestsNewbieQuestHeadline = "APRENDIZ"

QuestsCogTrackQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogTrackQuestHeadline = "PROCURADO"
QuestsCogTrackQuestSCStringS = "Eu preciso derrotar %(cogText)s%(cogLoc)s."
QuestsCogTrackQuestSCStringP = "Eu preciso derrotar alguns %(cogText)s%(cogLoc)s."
QuestsCogTrackQuestDefeat = "Derrotar %s"

QuestsCogLevelQuestProgress = "%(progress)s de %(numCogs)s derrotados"
QuestsCogLevelQuestHeadline = "PROCURADO"
QuestsCogLevelQuestDefeat = "Derrotar %s"
QuestsCogLevelQuestDesc = "um Nível %(level)s+ Cog"
QuestsCogLevelQuestDescC = "%(count)s Nível %(level)s+ Cogs"
QuestsCogLevelQuestDescI = "algum Nível %(level)s+ Cogs"
QuestsCogLevelQuestSCString = "Eu preciso derrotar %(objective)s%(location)s."

QuestsBuildingQuestFloorNumbers = ('','dois+','três+','quatro+','cinco+')
QuestsBuildingQuestBuilding = "Edifício"
QuestsBuildingQuestBuildings = "Edifícios"
QuestsBuildingQuestHeadline = "DERROTAR"
QuestsBuildingQuestProgressString = "%(progress)s de %(num)s derrotados"
QuestsBuildingQuestString = "Derrotar %s"
QuestsBuildingQuestSCString = "Eu preciso derrotar %(objective)s%(location)s."

QuestsBuildingQuestDesc = "um Edifício %(type)s"
QuestsBuildingQuestDescF = "um Edifício %(type)s de %(floors)s andares"
QuestsBuildingQuestDescC = "%(count)s Edifícios %(type)s"
QuestsBuildingQuestDescCF = "%(count)s Edifícios %(type)s de %(floors)s andares"
QuestsBuildingQuestDescI = "alguns Edifícios %(type)s"
QuestsBuildingQuestDescIF = "alguns Edifícios %(type)s de %(floors)s andares"

QuestsDeliverGagQuestProgress = "%(progress)s de %(numGags)s entregues"
QuestsDeliverGagQuestHeadline = "ENTREGAR"
QuestsDeliverGagQuestToSCStringS = "Preciso entregar %(gagName)s."
QuestsDeliverGagQuestToSCStringP = "Preciso entregar algumas %(gagName)s."
QuestsDeliverGagQuestSCString = "Preciso fazer uma entrega."
QuestsDeliverGagQuestString = "Entregar %s"
QuestsDeliverGagQuestStringLong = "Entregar %s a _toNpcName_."

QuestsDeliverItemQuestProgress = ""
QuestsDeliverItemQuestHeadline = "ENTREGAR"
QuestsDeliverItemQuestSCString = "Preciso entregar %(article)s%(itemName)s."
QuestsDeliverItemQuestString = "Entregar %s"
QuestsDeliverItemQuestStringLong = "Entregar %s a _toNpcName_."

QuestsVisitQuestProgress = ""
QuestsVisitQuestHeadline = "VISITAR"
QuestsVisitQuestStringShort = "Visitar"
QuestsVisitQuestStringLong = "Visitar _toNpcName_"
QuestsVisitQuestSeeSCString = "Preciso ver %s."

QuestsRecoverItemQuestProgress = "%(progress)s de %(numItems)s recuperados"
QuestsRecoverItemQuestHeadline = "RECUPERAR"
QuestsRecoverItemQuestSeeHQSCString = "Preciso ver um Oficial do Quartel."
QuestsRecoverItemQuestReturnToHQSCString = "Preciso devolver %s para um Oficial do Quartel."
QuestsRecoverItemQuestReturnToSCString = "Preciso devolver %(item)s para %(npcName)s."
QuestsRecoverItemQuestGoToHQSCString = "Preciso ir a um Quartel dos Toons."
QuestsRecoverItemQuestGoToPlaygroundSCString = "Preciso ir ao Pátio %s."
QuestsRecoverItemQuestGoToStreetSCString = "Preciso ir %(to)s %(street)s em %(hood)s."
QuestsRecoverItemQuestVisitBuildingSCString = "Preciso visitar %s%s."
QuestsRecoverItemQuestWhereIsBuildingSCString = "Onde é %s%s?"
QuestsRecoverItemQuestRecoverFromSCString = "Preciso recuperar %(item)s de %(holder)s%(loc)s."
QuestsRecoverItemQuestString = "Recuperar %(item)s de %(holder)s"

QuestsTrackChoiceQuestHeadline = "ESCOLHER"
QuestsTrackChoiceQuestSCString = "Preciso escolher entre %(trackA)s e %(trackB)s."
QuestsTrackChoiceQuestMaybeSCString = "Talvez eu deva escolher %s."
QuestsTrackChoiceQuestString = "Escolha entre %(trackA)s e %(trackB)s"

QuestsFriendQuestHeadline = "AMIGO"
QuestsFriendQuestSCString = "Preciso fazer um amigo."
QuestsFriendQuestString = "Fazer um amigo"

QuestsFriendNewbieQuestString = "Faça %d amigos %d risadas ou menos"
QuestsFriendNewbieQuestProgress = "%(progress)s de %(numFriends)s feitos"
QuestsFriendNewbieQuestObjective = "Faça amizade com %d novos Toons"

QuestsTrolleyQuestHeadline = "BONDINHO"
QuestsTrolleyQuestSCString = "Preciso pegar o bondinho."
QuestsTrolleyQuestString = "Andar no bondinho"
QuestsTrolleyQuestStringShort = "Pegar o bondinho"

QuestsMinigameNewbieQuestString = "%d Minijogos"
QuestsMinigameNewbieQuestProgress = "%(progress)s de %(numMinigames)s jogados"
QuestsMinigameNewbieQuestObjective = "Divirta-se com %d minijogos com a ajuda de novos Toons"
QuestsMinigameNewbieQuestSCString = "Preciso participar de minijogos com novos Toons."
QuestsMinigameNewbieQuestCaption = "Ajude um novo Toon %d risadas ou menos"
QuestsMinigameNewbieQuestAux = "Jogar:"

QuestsMaxHpReward = "Seu Limite de risadas foi aumentado em %s."
QuestsMaxHpRewardPoster = "Recompensa: %s ponto de Acréscimo de risadas"

QuestsMoneyRewardSingular = "Você ganha 1 balinha."
QuestsMoneyRewardPlural = "Você ganha %s balinhas."
QuestsMoneyRewardPosterSingular = "Recompensa: 1 balinha"
QuestsMoneyRewardPosterPlural = "Recompensa: %s balinhas"

QuestsMaxMoneyRewardSingular = "Agora, você pode carregar 1 balinha."
QuestsMaxMoneyRewardPlural = "Agora, você pode carregar %s balinhas."
QuestsMaxMoneyRewardPosterSingular = "Recompensa: Carregue 1 balinha"
QuestsMaxMoneyRewardPosterPlural = "Recompensa: Carregue %s balinhas"

QuestsMaxGagCarryReward = "Você ganha %(name)s. Agora, você pode carregar %(num)s piadas."
QuestsMaxGagCarryRewardPoster = "Recompensa: %(name)s (%(num)s)"

QuestsMaxQuestCarryReward = "Agora, você pode ter %s Tarefas Toon."
QuestsMaxQuestCarryRewardPoster = "Recompensa: Carregue %s Tarefas Toon"

QuestsTeleportReward = "Agora, você tem acesso por teletransporte a %s."
QuestsTeleportRewardPoster = "Recompensa: Acesso por teletransporte a %s"

QuestsTrackTrainingReward = "Agora, você pode treinar para \"%s\" piadas."
QuestsTrackTrainingRewardPoster = "Recompensa: Treinamento de piadas"

QuestsTrackProgressReward = "Agora, você tem o quadro %(frameNum)s da animação do tipo %(trackName)s."
QuestsTrackProgressRewardPoster = "Recompensa: \"Quadro %(frameNum)s da animação do tipo %(trackName)s\""

QuestsTrackCompleteReward = "Agora, você pode carregar e usar \"%s\" piadas."
QuestsTrackCompleteRewardPoster = "Recompensa: Treinamento final do tipo %s"

QuestsClothingTicketReward = "Você pode trocar de roupa"
QuestsClothingTicketRewardPoster = "Recompensa: Tíquete de roupas"

QuestsCheesyEffectRewardPoster = "Recompensa: %s"

# Quest location dialog text
QuestsStreetLocationThisPlayground = "neste pátio"
QuestsStreetLocationThisStreet = "nesta rua"
QuestsStreetLocationNamedPlayground = "no pátio %s"
QuestsStreetLocationNamedStreet = "na %(toStreetName)s em %(toHoodName)s"
QuestsLocationString = "%(string)s%(location)s"
QuestsLocationBuilding = "O edifício de %s's chama-se"
QuestsLocationBuildingVerb = "o qual é"
QuestsLocationParagraph = "\a%(building)s \"%(buildingName)s\"...\a...%(buildingVerb)s %(street)s."

# MaxGagCarryReward names
QuestsMediumPouch = "Sacola média"
QuestsLargePouch = "Sacola grande"
QuestsSmallBag = "Bolsa pequena"
QuestsMediumBag = "Bolsa média"
QuestsLargeBag = "Bolsa grande"
QuestsSmallBackpack = "Mochila pequena"
QuestsMediumBackpack = "Mochila média"
QuestsLargeBackpack = "Mochila grande"

QuestsItemDict = {
    1 : ["Par de óculos", "Pares de óculos", "um "],
    2 : ["Chave", "Chaves", "uma "],
    3 : ["Quadro-negro", "Quadros-negros", "um "],
    4 : ["Livro", "Livros", "um "],
    5 : ["Chocolate", "Chocolates", "um "],
    6 : ["Pedaço de giz", "Pedaços de giz", "um "],
    7 : ["Receita", "Receitas", "uma "],
    8 : ["Nota", "Notas", "uma "],
    9 : ["Calculadora", "Calculadoras", "uma "],
    10 : ["Pneu de carro de palhaço", "Pneus de carro de palhaço", "um "],
    11 : ["Bomba de ar", "Bombas de ar", "uma "],
    12 : ["Tinta de polvo", "Tintas de polvo", "uma "],
    13 : ["Pacotes", "Pacotes", "um "],
    14 : ["Recibo de peixe dourado", "Recibos de peixe dourado", "um "],
    15 : ["Peixe dourado", "Peixe dourado", "um "],
    16 : ["Óleo", "Óleos", "um pouco de "],
    17 : ["Graxa", "Graxas", "um pouco de "],
    18 : ["Água", "Águas", "uma "],
    19 : ["Relatório de engrenagens", "Relatórios de engrenagens", "um "],

    # This is meant to be delivered to NPCTailors to complete
    # ClothingReward quests
    1000 : ["Tíquete de roupas", "Tíquetes de roupas", "um "],

    # Donald's Dock quest items
    2001 : ["Câmara de ar", "Câmaras de ar", "uma "],
    2002 : ["Receita de monóculo", "Receita de monóculo", "uma "],
    2003 : ["Armação de óculos", "Armações de óculos", "algumas "],
    2004 : ["Monóculo", "Monóculos", "um "],
    2005 : ["Grande peruca branca", "Grandes perucas brancas", "uma "],
    2006 : ["Alqueire de cascalho", "Alqueires de cascalho", "um "],
    2007 : ["Engrenagem Cog", "Engrenagens de Cog", "uma "],
    2008 : ["Carta marinha", "Cartas marinhas", "uma "],
    2009 : ["Braçadeira suja", "Braçadeiras sujas", "uma "],
    2010 : ["Braçadeira limpa", "Braçadeiras limpas", "uma "],
    2011 : ["Mola de relógio", "Molas de relógio", "uma "],
    2012 : ["Contrapeso", "Contrapesos", "um "],

    # Minnie's Melodyland quest items
    4001 : ["Estoque da Tina", "Estoques da Tina", ""],
    4002 : ["Estoque da Cavaca", "Estoques da Cavaca", ""],
    4003 : ["Formulário de estoque", "Formulários de estoque", "um "],
    4004 : ["Estoque da Fifi", "Estoques da Fifi", ""],
    4005 : ["Passagem do Alê Nhador", "Passagens do Alê Nhador", ""],
    4006 : ["Passagem da Tábata", "Passagens da Tábata", ""],
    4007 : ["Passagem do Barry", "Passagens do Barry", ""],
    4008 : ["Castanhola fosca", "Castanholas foscas", ""],
    4009 : ["Tinta de lula azul", "Tintas de lula azul", "obter "],
    4010 : ["Castanhola polida", "Castanholas polidas", "uma "],
    4011 : ["Letra de música do Léo", "Letras de músicas do Léo", ""],

    # Daisy's Gardens quest items
    5001 : ["Gravata de seda", "Gravatas de seda", "uma "],
    5002 : ["Terno listrado", "Ternos listrados", "um "],
    5003 : ["Tesoura", "Tesouras", "uma "],
    5004 : ["Cartão-postal", "Cartões-postais", "um "],
    5005 : ["Caneta", "Canetas", "uma "],
    5006 : ["Tinteiro", "Tinteiros", "um "],
    5007 : ["Bloco de notas", "Blocos de notas", "um "],
    5008 : ["Cofre de escritório", "Cofres de escritório", "um "],
    5009 : ["Saco de ração para pássaros", "Sacos de ração para pássaros", "um "],
    5010 : ["Roda dentada", "Rodas dentadas", "uma "],
    5011 : ["Salada", "Saladas", "uma "],
    5012 : ["Chave para os Jardins da Margarida", "Chaves para os Jardins da Margarida", "uma "],

    # The Brrrgh quests
    3001 : ["Bola de futebol", "Bolas de futebol", "uma "],
    3002 : ["Tobogã", "Tobogãs", "um "],
    3003 : ["Cubo de gelo", "Cubos de gelo", "um "],
    3004 : ["Carta de amor", "Cartas de amor", "uma "],
    3005 : ["Cão-lingüiça", "cães-lingüiça", "um "],
    3006 : ["Anel de noivado", "Anéis de noivado", "um "],
    3007 : ["Bigode de sardinha", "Bigodes de sardinhas", "um pouco de "],
    3008 : ["Poção calmante", "Poções calmantes", "uma "],
    3009 : ["Dente quebrado", "Dentes quebrados", "um "],
    3010 : ["Dente de ouro", "Dentes de ouro", "um "],
    3011 : ["Pão de pinha", "Pães de pinha", "um "],
    3012 : ["Coco em pedaços", "Cocos em pedaços", "um pouco de "],
    3013 : ["Colher simples", "Colheres simples", "uma "],
    3014 : ["Sapo falante", "Sapos falantes", "um "],
    3015 : ["Casquinha de sorvete", "Casquinhas de sorvete", "uma "],
    3016 : ["Pó de peruca", "Pós de perucas", "um pouco de "],
    3017 : ["Patinho de borracha", "Patinhos de borracha", "um "],
    3018 : ["Dados de pelúcia", "Dados de pelúcia", "alguns "],
    3019 : ["Microfone", "Microfones", "um "],
    3020 : ["Teclado elétrico", "Teclados elétricos", "um "],
    3021 : ["Sapatos de plataforma", "Sapatos de plataforma", "alguns "],
    3022 : ["Caviar", "Caviar", "um pouco de "],
    3023 : ["Pó-de-arroz", "Pó-de-arroz", "um pouco de "],
    }
QuestsHQOfficerFillin = 'Oficial do Quartel'
QuestsHQWhereFillin = ""
QuestsHQBuildingNameFillin = 'Quartel dos Toons'
QuestsHQLocationNameFillin = "em qualquer bairro"

QuestsTailorFillin = "Costureiro"
QuestsTailorWhereFillin = ""
QuestsTailorBuildingNameFillin = "Loja de Roupas"
QuestsTailorLocationNameFillin = "em qualquer bairro"
QuestsTailorQuestSCString = "Preciso ir ao Costureiro."

QuestMovieQuestChoiceCancel = "Volte mais tarde se precisar de uma Tarefa Toon! Tchau!"
QuestMovieTrackChoiceCancel = "Volte quando já tiver decidido o que fazer! Tchau!"
QuestMovieQuestChoice = "Escolha uma Tarefa Toon."
QuestMovieTrackChoice = "Já decidiu o que escolher? Escolha um tipo ou volte mais tarde."

# Constants used in Quests.py, globally defined here
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6

TheBrrrghTrackQuestDict = {
    GREETING : "",
    QUEST : "Agora, você está pronto.\aSaia e refresque a cabeça até descobrir que tipo você gostaria de escolher.\aEscolha bem, pois você não poderá mudar.\aQuando tiver certeza, volte aqui.",
    INCOMPLETE_PROGRESS : "Escolha bem.",
    INCOMPLETE_WRONG_NPC : "Escolha bem.",
    COMPLETE : "Ótima escolha!",
    LEAVING : "Boa sorte. Volte aqui quando tiver dominado sua nova habilidade.",
    }

QuestDialog_3225 = {
    QUEST : "Puxa, obrigado por vir, _avName_!\aOs Cogs que estão no bairro assustaram o rapaz que faz as entregas.\aEu não tenho quem entregue esta salada para _toNpcName_!\aVocê poderia fazer isso por mim? Muitíssimo obrigado!_where_"
    }

QuestDialog_2910 = {
    QUEST : "De volta tão rápido assim?\aÓtimo trabalho com aquela mola.\aO último item é um contrapeso.\aPasse lá, veja com _toNpcName_ e traga o que você conseguir._where_"
    }

QuestDialogDict = {
    160 : {GREETING : "",
           QUEST : "Ok, agora acho que você está pronto para um desafio maior.\aDerrote 3 Robôs-chefe.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs-chefe. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    161 : {GREETING : "",
           QUEST : "Ok, agora acho que você está pronto para um desafio maior.\aDerrote 3 Robôs da Lei.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas rua e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs da Lei. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    162 : {GREETING : "",
           QUEST : "Ok, agora acho que você está pronto para um desafio maior.\aDerrote 3 Robôs Mercenários.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs Mercenários. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    163 : {GREETING : "",
           QUEST : "Ok, agora acho que você está pronto para um desafio maior.\aDerrote 3 Robôs Vendedores.",
           INCOMPLETE_PROGRESS : "Os "+ Cogs +" estão soltos pelas ruas e pelos túneis.",
           INCOMPLETE_WRONG_NPC : "Bom trabalho com os Robôs Vendedores. Vá agora para o Quartel dos Toons para receber sua recompensa!",
           COMPLETE : QuestsDefaultComplete,
           LEAVING : QuestsDefaultLeaving,
           },
    164 : {QUEST : "Parece que você precisa de novas piadas.\aVisite o Flippy, talvez ele possa ajudá-lo._where_" },
    165 : {QUEST : "Olá.\aParece que você precisa praticar suas piadas.\aToda vez que você atinge um Cog com uma de suas piadas, sua experiência aumenta.\aQuando tiver experiência suficiente, você será capaz de usar uma piada ainda melhor.\aVá praticar suas piadas derrotando 4 Cogs."},
    166 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVocê pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs-chefe."},
    167 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVocê pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs da Lei."},
    168 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVocê pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs Vendedores."},
    169 : {QUEST : "Bom trabalho com aqueles Cogs.\aSabia que existem quatro tipos diferentes de Cogs?\aEles são os Robôs da Lei, os Robôs Mercenários, os Robôs Vendedores e os Robôs-chefe.\aVocê pode diferenciá-los pela cor e pelas etiquetas com os nomes.\aPara praticar, derrote 4 Robôs Mercenários."},
    170 : {QUEST : "Bom trabalho; agora você sabe a diferença entre os 4 tipos de Cogs.\aAcho que você está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ele pode dar alguns conselhos especiais para você._where_" },
    171 : {QUEST : "Bom trabalho; agora você sabe a diferença entre os 4 tipos de Cogs.\aAcho que você está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ele pode dar alguns conselhos especiais para você._where_" },
    172 : {QUEST : "Bom trabalho; agora você sabe a diferença entre os 4 tipos de Cogs.\aAcho que você está pronto para começar a treinar o seu terceiro tipo de piada.\aFale com _toNpcName_ para escolher o seu próximo tipo de piada - ela pode dar alguns conselhos especiais para você._where_" },

    175 : {GREETING : "",
           QUEST : "Você sabia que possui sua própria casa Toon?\aA vaca Clarabela administra um catálogo telefônico no qual você pode escolher e encomendar móveis para decorar sua casa.\aVocê também pode comprar frases do Chat Rápido, roupas e outras coisas muito legais!\aPedirei à Clarabela para enviar agora a você seu primeiro catálogo.\aVocê receberá um catálogo com novos itens toda semana!\aVá para sua casa e use o seu telefone para ligar para Clarabela.",
           INCOMPLETE_PROGRESS : "Vá para casa e use o seu telefone para ligar para Clarabela.",
           COMPLETE : "Espero que você se divirta fazendo encomendas com Clarabela!\a Acabei de redecorar minha casa. Está Toontástica!\aContinue com as Tarefas Toon para ganhar mais recompensas!",
           LEAVING : QuestsDefaultLeaving,
           },

    400 : {GREETING : "",
           QUEST : "Lançamento e Esguicho são tipos ótimos, mas você vai precisar de mais piadas para lutar com Cogs de níveis mais altos.\aQuando você se juntar com outros Toons para enfrentar os Cogs, pode combinar ataques para conseguir danos maiores ao inimigo.\aTente diferentes combinações de Piadas para ver o que funciona melhor.\aPara o seu próximo tipo, escolha as Sonoras ou Toonar.\aAs Sonoras são especiais, pois quando atingem algum Cog, todos os outros também sofrem danos.\aAs Toonar permitem curar outros Toons durante a batalha.\aQuando estiver pronto para decidir, venha aqui e escolha uma.",
           INCOMPLETE_PROGRESS : "De volta tão rápido? Ok, você está pronto para escolher?",
           INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
           COMPLETE : "Boa decisão. Agora, antes de usar estas piadas, você deve treinar.\aVocê deve completar uma série de Tarefas Toon como treinamento.\aCada tarefa dará a você um único quadro da animação do seu ataque de piadas.\aQuando você coletar todas as 15, poderá obter a tarefa Treinamento final de piadas, que lhe permitirá usar suas novas piadas.\aVocê pode verificar seu progresso no Álbum Toon.",
           LEAVING : QuestsDefaultLeaving,
           },
    1039 : { QUEST : "Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_" },
    1040 : { QUEST : "Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_" },
    1041 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\aÉ, você pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no Álbum Toon.\aÉ claro que você precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se você ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1042 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\aÉ, você pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no Álbum Toon.\aÉ claro que você precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se você ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1043 : { QUEST : "Oi! O que o traz aqui?\aTodo mundo usa o buraco portátil para andar por Toontown.\aÉ, você pode se teletransportar até seus amigos, usando a Lista de amigos, ou até qualquer bairro, usando o mapa no Álbum Toon.\aÉ claro que você precisa consegui-lo!\aOlha, eu posso ativar seu acesso por teletransporte até o Centro de Toontown se você ajudar um amigo meu.\aParece que os Cogs estão dando problema na Travessa dos Tontos. Visite _toNpcName_._where_" },
    1044 : { QUEST : "Puxa, obrigado por passar por aqui. Eu realmente preciso de ajuda.\aComo você pode ver, eu não tenho clientes.\aO meu livro de receitas secreto está perdido e ninguém mais vem ao meu restaurante.\aA última vez que eu o vi foi pouco antes de os Cogs tomarem meu edifício.\aVocê pode me ajudar recuperando quatro de minhas receitas favoritas?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu recuperar minhas receitas?" },
    1045 : { QUEST : "Valeu mesmo!\aLogo terei de volta minha coleção completa e poderei reabrir meu restaurante.\aAh, há uma nota aqui para você - algo sobre acesso por teletransporte?\aDiz: \"obrigado por ajudar meu amigo e, por favor, entregue isto ao Quartel dos Toons\".\aBem, valeu mesmo - tchau!",
             LEAVING : "",
             COMPLETE : "Ah, sim, aqui diz que você foi de grande ajuda para alguns dos caras mais legais da Travessa dos Tontos.\aDiz também que você precisa de acesso por teletransporte para o Centro de Toontown.\aBem, considere concedido.\aAgora, você pode se teletransportar de volta para o pátio, de praticamente qualquer lugar de Toontown.\aBasta abrir o seu mapa e clicar em Centro de Toontown." },
    1046 : { QUEST : "Os Robôs Mercenários têm importunado bastante a Financeira Dinheiro Feliz.\aPasse por lá e veja se há algo que você possa fazer._where_" },
    1047 : { QUEST : "Os Robôs Mercenários têm se infiltrado no banco e roubado nossas calculadoras.\aRecupere 5 calculadoras dos Robôs Mercenários.\aPara evitar que você fique indo para lá e para cá, traga-as todas de uma vez.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda procurando pelas calculadoras?" },
    1048 : { QUEST : "Uau! Valeu mesmo por encontrar nossas calculadoras.\aHumm... Elas parecem danificadas.\aVocê poderia levá-las para a loja de _toNpcName_, \"Máquinas de Cosquinhas\", nesta rua?\aVeja se podem consertá-las.",
             LEAVING : "", },
    1049 : { QUEST : "O que é isto? Calculadoras quebradas?\aRobôs Mercenários?\aBem, vamos dar uma olhada...\aÉ, as engrenagens estão partidas mas eu estou sem essa peça...\aSabe o que poderia dar jeito? Algumas engrenagens de Cog, das grandes, dos Cogs maiores...\aEngrenagens de Cogs de nível 3 devem servir. Precisarei de 2 para cada máquina, 10 no total.\aTraga-as todas de uma vez e eu as consertarei!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Lembre-se, eu preciso de 10 engrenagens para consertar as máquinas." },
    1053 : { QUEST : "Ah sim, isto deve servir.\aTudo consertado agora, grátis.\aLeve-as de volta para a Dinheiro Feliz e diga olá a ela por mim.",
             LEAVING : "",
             COMPLETE : "Calculadoras consertadas?\aBom trabalho. Tenho certeza de que tenho algo por aqui para recompensar você..." },
    1054 : { QUEST : "_toNpcName_ precisa de alguma ajuda com seus carros de palhaço._where_" },
    1055 : { QUEST : "Oláááá! Eu não consigo encontrar os pneus para este carro de palhaço em lugar nenhum!\aVocê acha que pode me ajudar?\aEu acho que o Tito Tonto pode ter jogado os pneus no lago do pátio do Centro de Toontown.\aSe você ficar em um dos cais de lá, poderá tentar pescar os pneus para mim.",
             GREETING : "Iuhuu!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você está tendo problemas para pescar os 4 pneus?" },
    1056 : { QUEST : "Demorôô! Agora, este velho carro de palhaço vai poder voltar às ruas!\aEi, eu pensei que tivesse uma bomba de ar aqui para inflar estes pneus...\aAcho que _toNpcName_ pegou emprestado.\aVocê poderia pedir de volta para mim?_where_",
             LEAVING : "" },
    1057 : { QUEST : "E aí?\aUma bomba de pneus?\aVamos fazer o seguinte: você me ajuda a retirar das ruas alguns desses Cogs de alto nível...\aE, então, darei a você a bomba de pneus.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Isso é o melhor que você pode fazer?" },
    1058 : { QUEST : "Bom trabalho! Eu sabia que você conseguiria.\aAqui está a bomba. Estou certo de que _toNpcName_ ficará feliz em recebê-la de volta.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Dez! Agora está tudo certo!\aPor falar nisso, obrigado por me ajudar.\aAqui, tome isto." },
    1059 : { QUEST : "_toNpcName_ está com poucos suprimentos. Quem sabe você pode ajudá-lo?_where_" },
    1060 : { QUEST : "Valeu mesmo por passar aqui!\aOs Cogs roubam sempre a minha tinta e, por isso, ela está quase no fim.\aVocê poderia pescar um pouco de tinta de polvo para mim no lago?\aPara pescar, basta ficar parado em um cais perto do lago.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você está tendo problemas para pescar?" },
    1061 : { QUEST : "Ótimo, valeu pela tinta!\aSabe de uma coisa, se você eliminasse alguns daqueles Ratos de Escritório...\aAí minha tinta não acabaria tão rápido.\aDerrote 6 Ratos de Escritório no Centro de Toontown para receber sua recompensa.",
             LEAVING : "",
             COMPLETE : "Valeu! Vou recompensar você pela sua ajuda.",
             INCOMPLETE_PROGRESS : "Eu acabei de ver mais alguns Ratos de Escritório." },
    1062 : { QUEST : "Ótimo, valeu pela tinta!\aSabe de uma coisa? Se você eliminasse alguns daqueles Sanguessugas...\aAí minha tinta não acabaria tão rápido.\aDerrote 6 Sanguessugas no Centro de Toontown para receber sua recompensa.",
             LEAVING : "",
             COMPLETE : "Valeu! Vou recompensar você pela sua ajuda.",
             INCOMPLETE_PROGRESS : "Eu acabei de ver mais alguns Sanguessugas." },
    900 : { QUEST : "Fiquei sabendo que _toNpcName_ precisa de ajuda com um pacote._where_" },
    1063 : { QUEST : "Olá! Legal você ter vindo.\aUm Cog roubou um pacote muito importante bem debaixo do meu nariz.\aVeja se você consegue recuperá-lo. Eu acho que ele era de nível 3...\aEntão, derrote Cogs de nível 3 até encontrar meu pacote.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1067 : { QUEST : "É ele mesmo, está tudo certo!\aEi, o endereço está borrado...\aTudo o que eu posso ler é que é para um Dr. - o resto está ilegível.\aTalvez seja para _toNpcName_? Você pode levar para ele?_where_",
             LEAVING : "" },
    1068 : { QUEST : "Eu não estava esperando um pacote. Talvez seja para o Dr. E.U. Fórico.\aMeu assistente ia passar mesmo lá hoje, então pedirei a ele que verifique para você.\aNesse meio tempo, você se importaria de se livrar de alguns dos Cogs que estão na minha rua?\aDerrote 10 Cogs no Centro de Toontown.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Meu assistente ainda não voltou." },
    1069 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô Mercenário roubou o pacote de meu assistente no caminho de volta.\aVocê poderia tentar pegá-lo de volta?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1070 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô Vendedor roubou o pacote de meu assistente no caminho de volta.\aSinto muito, mas você terá que encontrar esse Robô Vendedor para pegá-lo de volta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1071 : { QUEST : "O Dr. Fórico disse que também não estava esperando nenhum pacote.\aInfelizmente um Robô-chefe roubou o pacote de meu assistente no caminho de volta.\aVocê poderia tentar pegá-lo de volta?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o pacote, né?" },
    1072 : { QUEST : "Ótimo, você o pegou de volta!\aTalvez você deva tentar entregá-lo a _toNpcName_, pode ser para ele._where_",
             LEAVING : "" },
    1073 : { QUEST : "Puxa, obrigado por trazer meus pacotes para mim.\aEspere um segundo, eu estava esperando dois. Você poderia verificar com _toNpcName_ e ver se ele está com o outro?",
             INCOMPLETE : "Conseguiu encontrar meu outro pacote?",
             LEAVING : "" },
    1074 : { QUEST : "Ele disse que havia outro pacote? Talvez os Cogs o tenham roubado também.\aDerrote Cogs até encontrar o segundo pacote.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não teve sorte de encontrar o outro pacote, né?" },
    1075 : { QUEST : "No final das contas, acho que não havia um segundo pacote!\aCorra e leve-o para _toNpcName_, com minhas desculpas.",
             COMPLETE : "Ei, meu pacote está aqui!\aJá que você parece ser um Toon tão prestativo, isto vai ser fichinha.",
             LEAVING : "" },
    1076 : { QUEST : "Houve alguns problemas na Peixinhos Dourados Ki-late.\a_toNpcName_ provavelmente podem precisar de você._where_" },
    1077 : { QUEST : "Legal você ter vindo. Os Cogs roubaram todos os meus peixes dourados.\aEu acho que os Cogs querem vendê-los para ganhar dinheiro fácil.\aHá muitos anos, aqueles 5 peixes têm sido minhas únicas companhias nesta pequena loja ...\aSe você pudesse recuperá-los, eu agradeceria muito.\aTenho certeza de que os Cogs estão com meus peixes.\aDerrote Cogs até encontrar meus peixes dourados.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Consiga meus peixes dourados de volta." },
    1078 : { QUEST : "Puxa, você recuperou meus peixes!\aHã? O que é isto - um recibo?\aAi, ai... Acho que eles são Cogs mesmo.\aEu não consigo decifrar este recibo. Você poderia levá-lo para _toNpcName_ e ver se ele consegue lê-lo?_where_",
             INCOMPLETE : "O que _toNpcName_ disse sobre o recibo?",
             LEAVING : "" },
    1079 : { QUEST : "Humm, deixe-me ver este recibo.\a...Ah, sim, diz que 1 peixe dourado foi vendido para um Puxa-saco.\aO recibo não menciona o que aconteceu com os outros 4 peixes.\aTalvez você deva tentar encontrar esse Puxa-saco.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Acho que não há mais nada em que eu possa ajudar.\aPor que você não tenta encontrar aquele peixe dourado?" },
    1092 : { QUEST : "Humm, deixe-me ver este recibo.\a...Ah, sim, diz que 1 peixe dourado foi vendido para um Farsante.\aO recibo não menciona o que aconteceu com os outros 4 peixes.\aTalvez você deva tentar encontrar esse Farsante.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Acho que não há mais nada em que eu possa ajudar.\aPor que você não tenta encontrar aquele peixe dourado?" },
    1080 : { QUEST : "Ah, graças aos céus! Você encontrou Oscar - ele é o meu favorito.\aO que foi, Oscar? Hã-hã... Verdade? ... Estão?\aOscar diz que os outros 4 escaparam para dentro do lago no pátio.\aVocê poderia reuni-los para mim?\aÉ só pescá-los no lago.",
             LEAVING : "",
             COMPLETE : "Nossa, estou tããão feliz! Estou junto com meus companheiros novamente!\aVocê merece uma bela recompensa por isso!",
             INCOMPLETE_PROGRESS : "Você está tendo problemas para pescar esses peixes?" },
    1081 : { QUEST : "_toNpcName_ parece estar numa situação grudenta. Ela, com certeza, apreciaria alguma ajuda._where_" },
    1082 : { QUEST : "Eu derramei supercola e estou presa - presa pra valer!\aSe houver uma maneira de sair, eu gostaria de saber.\aIsso me dá uma idéia; abra os olhos.\aDerrote alguns Robôs Vendedores e traga de volta um pouco de óleo.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Você pode me ajudar a descolar daqui?" },
    1083 : { QUEST : "Bem, o óleo ajudou um pouco, mas eu ainda não consigo me mexer.\aO que mais poderia ajudar? É difícil dizer.\aIsso me dá uma idéia; vale a pena tentar.\aDerrote alguns Robôs da Lei e me traga graxa.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Você pode me ajudar a descolar daqui?" },
    1084 : { QUEST : "Não, isso não ajudou. Isso realmente não é engraçado.\aEu coloquei a graxa bem ali,\aIsso me dá uma idéia, não me deixe esquecer.\aDerrote alguns Robôs Mercenários e traga água para umedecer.",
             LEAVING : "",
             GREETING : "",
             COMPLETE : "Oba! Estou livre da supercola,\aComo recompensa, dou este presente a você.\aVocê pode rir um pouco mais enquanto luta e, então...\aAh, não! Já estou presa aqui novamente!",
             INCOMPLETE_PROGRESS : "Você pode me ajudar a descolar daqui?" },
    1085 : { QUEST : "_toNpcName_ está fazendo uma pesquisa sobre os Cogs.\aVá falar com ele para ver se ele precisa da sua ajuda._where_" },
    1086 : { QUEST : "É verdade, estou fazendo um estudo sobre os Cogs.\aEu quero aprender sobre o comportamento deles.\aCom certeza ajudaria se você pudesse reunir algumas engrenagens de Cogs.\aMas elas têm que ser de Cogs de nível 2, pelo menos, para serem grandes o suficiente para o exame visual.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu encontrar engrenagens suficientes?" },
    1089 : { QUEST : "Certo, vamos dar uma olhada. Estas são amostras excelentes!\aHummm...\aCerto, aqui está meu relatório. Leve isto de volta imediatamente para o Quartel dos Toons.",
             INCOMPLETE : "Você entregou meu relatório no Quartel?",
             COMPLETE : "Bom trabalho _avName_, nós assumiremos a partir daqui.",
             LEAVING : "" },
    1090 : { QUEST : "_toNpcName_ tem informações úteis para você._where_" },
    1091 : { QUEST : "Fiquei sabendo que o Quartel dos Toons está trabalhando em uma espécie de Radar de Cogs.\aEle permite ver onde os Cogs estão, para que seja mais fácil encontrá-los.\aA Página de Cogs em seu Álbum Toon é a chave.\aAo derrotar Cogs suficientes, você pode sintonizar os sinais deles e rastrear onde estão.\aContinue derrotando Cogs para ficar pronto.",
             COMPLETE : "Bom trabalho! Você provavelmente vai poder fazer uso disso...",
             LEAVING : "" },
    401 : {GREETING : "",
           QUEST : "Agora, você tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
           INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
           INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
           COMPLETE : "Uma boa decisão...",
           LEAVING : QuestsDefaultLeaving,
           },
    2201 : { QUEST : "Aqueles cogs traiçoeiros estão envolvidos nisto novamente.\a_toNpcName_ reportou outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_" },
    2202 : { QUEST : "Oi, _avName_. Ainda bem que você está aqui. Um Mão-de-vaca de má aparência acabou de passar por aqui e saiu com uma câmara de ar.\aTemo que ele possa usá-la para seus planos diabólicos.\aVeja se você consegue encontrá-la e trazê-la de volta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha câmara de ar?",
             COMPLETE : "Você encontrou minha câmara de ar! Você é legal MESMO! Olha aqui, tome a sua recompensa...",
             },
    2203 : { QUEST : "Os cogs estão espalhando o caos no banco.\aVá até o Capitão Carlão e veja o que você pode fazer._where_" },
    2204 : { QUEST : "Bem-vindo a bordo, colega.\aDroga! Aqueles cogs patifes quebraram meu monóculo e eu não vivo sem ele.\aSeja um bom marujo e leve esta receita para o Dr. Qüiqüeres para trazer um novo para mim._where_",
             GREETING : "",
             LEAVING : "",
             },
    2205 : { QUEST : "O que é isso?\aPuxa, eu adoraria poder trabalhar nesta receita, mas os cogs têm furtado meus suprimentos.\aSe você pegasse a armação dos óculos de um Puxa-saco eu provavelmente poderia ajudá-lo.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Sinto muito. Sem armações de Puxa-saco, não tem monóculo!",
             },
    2206: { QUEST : "Excelente!\aSó um segundo...\aSua receita está pronta. Leve este monóculo diretamente ao Capitão Carlão._where_",
            GREETING : "",
            LEAVING : "",
            COMPLETE : "Alto!\aVocê vai ganhar sua condecoração, afinal de contas.\aAqui está.",
            },
    2207 : { QUEST : "Há um Cog na loja da Craca Bárbara!\aÉ melhor você ir para lá imediatamente._where_" },
    2208 : { QUEST : "Droga! Você se desencontrou dele, gracinha.\aHavia um Golpe Sujo aqui. Ele levou a minha grande peruca branca.\aEle disse que era para o chefe dele e mencionou algo como \"precedente legal\".\aSe você puder pegá-la de volta, ficarei eternamente grata.",
             LEAVING : "",
             GREETING : "",
             INCOMPLETE_PROGRESS : "Ainda não o encontrou?\aEle é alto e tem uma cabeça pontuda.",
             COMPLETE : "Você a encontrou!?!?\aVocê é uma gracinha!\aSua recompensa é mais do que merecida...",
             },
    2209 : { QUEST : "Moby está se preparando para uma viagem importante.\aVisite-o e veja o que pode fazer para ajudá-lo._where_"},
    2210 : { QUEST : "Sua ajuda será bem-vinda.\aO Quartel dos Toons me pediu para fazer uma viagem e ver se consigo descobrir de onde os cogs estão vindo.\aPrecisarei de algumas coisas para o meu navio, mas não tenho muitas balinhas.\aPasse pela loja da Alice e pegue um pouco de cascalho para mim. Você terá que fazer um favor para ela para poder pegar o cascalho._where_",
             GREETING : "E aí, _avName_",
             LEAVING : "",
             },
    2211 : { QUEST : "Então, o Moby quer cascalho, né?\aEle ainda está me devendo por aquele último alqueire.\aEu lhe darei se você conseguir eliminar cinco Microempresários na minha rua.",
             INCOMPLETE_PROGRESS : "Não, seu bobinho! Eu disse CINCO microempresários...",
             GREETING : "O que posso fazer por você?",
             LEAVING : "",
             },
    2212 : { QUEST : "Trato é trato.\aAqui está o cascalho para aquele fominha do Moby._where_",
             GREETING : "Ora, ora, o que temos aqui...",
             LEAVING : "",
             },
    2213 : { QUEST : "Excelente trabalho. Eu sabia que ela encontraria uma saída.\aAgora, eu preciso pegar uma carta de navegação com o Mário.\aAcho que meu crédito lá também não é tão bom, portanto, você vai ter que negociar com ele._where_",
             GREETING : "",
             LEAVING : "",
             },
    2214 : { QUEST : "Sim, eu tenho a carta de navegação que o Moby quer.\aE se você estiver disposto a trabalhar para consegui-la, eu a darei para você.\aEstou tentando construir um astrolábio para navegar pelas estrelas.\aPreciso de três engrenagens de Cog para construí-la.\aVolte aqui quando encontrá-las.",
             INCOMPLETE_PROGRESS: "Como está indo com aquelas engrenagens de Cog?",
             GREETING : "Bem-vindo!",
             LEAVING : "Boa sorte!",
             },
    2215 : { QUEST : "Oh! Essas engrenagens vão ser úteis mesmo.\aAqui está a carta. Leve para o Moby, com meus cumprimentos._where_",
             GREETING : "",
             LEAVING : "",
             COMPLETE : "Bem, agora sim. Estou pronto para zarpar!\aEu o levaria comigo se você não fosse novato. Leve isto, então.",
             },
    901 : { QUEST : "Se estiver disposto, o Salgado está precisando de ajuda na loja dele..._where_",
            },
    2902 : { QUEST : "Você é o novo recruta?\aBom, bom. Talvez você possa me ajudar.\aEstou construindo um caranguejo pré-fabricado gigante para confundir os cogs.\aEu vou precisar de uma braçadeira. Visite o Mário e me traga uma._where_",
             },
    2903 : { QUEST : "Olá!\aSim, eu ouvi falar no caranguejo gigante que Salgado está construindo.\aA melhor braçadeira que tenho está meio suja.\aSeja gentil e passe pela lavanderia antes de levá-la para ele._where_",
             LEAVING : "Valeu!"
             },
    2904 : { QUEST : "Você deve ser o amigo do Mário.\aAcho que posso limpar isso rapidinho.\aSó um minuto...\aAqui está. Nova em folha!\aDiga olá ao Salgado por mim._where_",
             },
    2905 : { QUEST : "Ah, era exatamente o que eu queria.\aJá que você está aqui, eu também vou precisar de uma mola de relógio de corda bem grande.\aVá até a loja do Gancho e veja se ele tem uma._where_",
             },
    2906 : { QUEST : "Uma mola bem grande?\aSinto muito, mas a maior que tenho ainda é pequena.\aTalvez eu consiga montar uma com as molas do gatilho de revólver de água.\aTraga-me três dessas piadas e eu vou ver o que posso fazer.",
             },
    2907 : { QUEST : "Vamos dar uma olhada...\aArrasou. Simplesmente arrasou.\aAlgumas vezes eu surpreendo até a mim mesmo.\aAqui está: uma mola grande para o Salgado!_where_",
             LEAVING : "Bon Voyage!",
             },
     2911 : { QUEST : "Ficaria feliz em ajudar nisso, _avName_.\aMas temo que as ruas não estejam mais tão seguras.\aPor que você não vai derrotar alguns Robôs Mercenários? Depois a gente conversa.",
             INCOMPLETE_PROGRESS : "Eu ainda acho que você precisa fazer que as ruas fiquem mais seguras.",
             },
    2916 : { QUEST : "Sim, eu tenho um peso para o Salgado.\aNo entanto, acho que seria mais seguro se você derrotasse alguns Robôs Vendedores primeiro.",
             INCOMPLETE_PROGRESS : "Ainda não. Derrote mais alguns Robôs Vendedores.",
             },
    2921 : { QUEST : "Humm, acho que poderia ceder um peso.\aMas eu me sentiria melhor se não houvesse tantos Robôs-chefe por aí.\aDerrote seis deles e volte aqui.",
             INCOMPLETE_PROGRESS : "Acho que ainda não está seguro...",
             },
    2925 : { QUEST : "Tudo pronto?\aBem, acho que agora está suficientemente seguro.\aAqui está o contrapeso para o Salgado._where_"
             },
    2926 : {QUEST : "Bem, isso é tudo.\aDeixe-me ver se funciona.\aHumm, um pequeno problema.\aNão estou conseguindo obter energia, pois aquele edifício Cog está bloqueando meu painel solar.\aVocê poderia dominá-lo para mim?",
            INCOMPLETE_PROGRESS : "Ainda sem energia. E aquele edifício?",
            COMPLETE : "Súper! Você é um destruidor de cogs e tanto! Tome isto aqui como recompensa...",
            },
    3200 : { QUEST : "Acabo de receber uma ligação do _toNpcName_.\aEle está tendo um dia difícil. Talvez você possa ajudá-lo!\aPasse por lá e veja do que ele precisa._where_" },
    3201 : { QUEST : "Puxa, obrigado por vir!\aPreciso de alguém para levar esta nova gravata de seda para _toNpcName_.\aVocê poderia fazer isso para mim?_where_" },
    3203 : { QUEST : "Ah, esta deve ser a gravata que eu pedi! Obrigado!\aEla combina com o terno listrado que acabei de terminar, logo ali.\aEi, o que aconteceu com o terno?\aOh, não! Os Cogs devem ter roubado meu terno novo!\aDerrote Cogs até encontrar meu terno e traga-o de volta para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você já encontrou meu terno? Tenho certeza de que os Cogs o pegaram!",
             COMPLETE : "Legal! Você encontrou meu terno novo!\aViu, eu disse que os Cogs estavam com ele! Aqui está a sua recompensa...",
             },

    3204 : { QUEST : "_toNpcName_ acabou de ligar para informar um roubo.\aPor que você não passa por lá e vê se consegue resolver as coisas?_where_" },
    3205 : { QUEST : "Olá, _avName_! Você veio me ajudar?\aAcabei de expulsar um Sanguessuga de minha loja. Puxa! Foi horrível.\aMas agora não encontro minha tesoura em lugar nenhum! Tenho certeza de que o Sanguessuga a levou.\aEncontre-o e recupere minha tesoura.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você ainda está procurando minha tesoura?",
             COMPLETE : "Minha tesoura! Valeu mesmo, viu? Aqui está a sua recompensa...",
             },

    3206 : { QUEST : "Parece que _toNpcName_ está tendo problemas com alguns Cogs.\aVá ver se você pode ajudá-lo._where_" },
    3207 : { QUEST : "Oi, _avName_! Obrigado por vir!\aUm monte de Duplos Sentidos invadiu minha loja e roubou uma pilha de cartões-postais de meu balcão.\aVá e derrote todos os Duplos Sentidos e recupere meus cartões-postais!",
             INCOMPLETE_PROGRESS : "Não há cartões-postais suficientes! Continue procurando!",
             COMPLETE : "Ah, valeu! Agora eu posso entregar a correspondência na hora certa! Aqui está a sua recompensa...",
             },

    3208 : { QUEST : "Ultimamente temos recebido reclamações dos moradores sobre os Reis da Incerta.\aVeja se consegue derrotar 10 Reis da Incerta para ajudar nossos colegas Toons nos Jardins da Margarida." },
    3209 : { QUEST : "Valeu mesmo por derrotar os Reis da Incerta!\aMas agora os Operadores de Telemarketing ficaram fora de controle.\aDerrote 10 Operadores de Telemarketing nos Jardins da Margarida e volte aqui para pegar sua recompensa." },

    3247 : { QUEST : "Ultimamente, temos recebido reclamações dos moradores sobre os Sanguessugas.\aVeja se consegue derrotar 20 Sanguessugas para ajudar nossos colegas Toons nos Jardins da Margarida." },


    3210 : { QUEST : "Oh, não, a Seivas Florais da Rua das Amendoeiras está sem flores!\aPara ajudar, leve dez de suas flores com esguicho.\aMas veja primeiramente se tem realmente 10 flores com esguicho em seu estoque.",
             LEAVING: "",
             INCOMPLETE_PROGRESS : "Preciso ter 10 flores com esguicho. Você não tem o suficiente!" },
    3211 : { QUEST : "Puxa, valeu mesmo, viu? Estas flores com esguicho vão salvar a pátria.\aMas estou com medo daqueles Cogs lá fora.\aVocê pode me ajudar e derrotar alguns desses Cogs?\aVolte aqui depois de derrotar 20 Cogs nesta rua.",
             INCOMPLETE_PROGRESS : "Ainda há Cogs lá fora para serem derrotados! Continue trabalhando!",
             COMPLETE : "Ah, valeu! Isso ajudou muito. Sua recompensa é...",
             },

    3212 : { QUEST : "_toNpcName_ precisa de ajuda para procurar por algo que ela perdeu.\aVá visitá-la e veja o que pode fazer._where_" },
    3213 : { QUEST : "Oi, _avName_. Você pode me ajudar?\aNão sei onde coloquei minha caneta. Acho que alguns Cogs pegaram-na.\aDerrote Cogs para encontrar minha caneta roubada.",
             INCOMPLETE_PROGRESS : "Você já encontrou minha caneta?" },
    3214 : { QUEST : "Sim, é a minha caneta! Valeu!\aMas, enquanto você estava fora, eu percebi que meu tinteiro também desapareceu.\aDerrote Cogs para encontrar meu tinteiro.",
             INCOMPLETE_PROGRESS : "Ainda estou procurando meu tinteiro!" },
    3215 : { QUEST : "Demais! Agora tenho minha caneta e meu tinteiro de volta!\aMas você nem vai acreditar!\aMeu bloco de notas sumiu! Eles devem tê-lo roubado também!\aDerrote Cogs para encontrar meu bloco de notas roubado e, então, traga-o de volta para ter sua recompensa.",
             INCOMPLETE_PROGRESS : "E meu bloco de notas?" },
    3216 : { QUEST : "É o meu bloco de notas! Maneiro! Sua recompensa é...\aEi! Onde ela está?\aSua recompensa estava bem aqui no cofre de meu escritório. Mas o cofre inteiro sumiu!\aDá para acreditar? Aqueles cogs roubaram sua recompensa!\aDerrote Cogs para recuperar meu cofre.\aQuando você o trouxer de volta, eu lhe darei sua recompensa.",
             INCOMPLETE_PROGRESS : "Continue procurando o cofre! Sua recompensa está lá dentro!",
             COMPLETE : "Finalmente! Seu novo saco de piadas está dentro daquele cofre. Aqui está...",
             },

    3217 : { QUEST : "Temos feito alguns estudos sobre a mecânica dos Robôs Vendedores.\aNós ainda precisamos estudar algumas peças de forma mais detalhada.\aTraga-nos uma roda dentada de algum Dr. Sabe-com-quem-está-falando.\aVocê poderá conseguir uma quando o Cog estiver explodindo." },
    3218 : { QUEST : "Muito bom! Agora precisamos de uma roda dentada de um Amigo-da-Onça.\aEstas são mais difíceis de conseguir, portanto, continue tentando." },
    3219 : { QUEST : "Demais! Agora precisamos de apenas mais uma roda dentada.\aDesta vez, precisamos de uma de um Agitador.\aTalvez você precise procurar esses Cogs nos edifícios dos Robôs Vendedores.\aQuando achar a roda, traga-a aqui para receber sua recompensa." },

    3244 : { QUEST : "Temos feito alguns estudos sobre a mecânica dos Robôs da Lei.\aNós ainda precisamos estudar algumas peças de forma mais detalhada.\aTraga-nos uma roda dentada de algum Perseguidor de Ambulâncias.\aVocê poderá conseguir uma quando o Cog estiver explodindo." },
    3245 : { QUEST : "Muito bom! Agora precisamos de uma roda dentada de um Golpe Sujo.\aEstas são mais difíceis de conseguir, portanto, continue tentando." },
    3246 : { QUEST : "Demais! Agora precisamos de apenas mais uma roda dentada.\aDesta vez, de um Relações Públicas.\aQuando pegá-la, traga-a aqui para conseguir sua recompensa." },

    3220 : { QUEST : "Acabei de saber que _toNpcName_ estava perguntando por você.\aPor que você não passa por lá e vê o que ela quer?_where_" },
    3221 : { QUEST : "Oi, _avName_! Aí está você!\aOuvi dizer que você é especialista em ataques com esguicho.\aPreciso de alguém para dar um bom exemplo a todos os Toons nos Jardins da Margarida.\aUse seus ataques com esguicho para derrotar vários Cogs.\aIncentive seus amigos a usarem o esguicho também.\aQuando tiver derrotado 20 Cogs, volte aqui para pegar sua recompensa!" },

    3222 : { QUEST : "É hora de demonstrar sua Toonmizade.\aSe você recuperar, com sucesso, um número de edifícios de Cogs, ganhará o direito de fazer três buscas.\aPrimeiramente, derrote dois edifícios de Cogs.\aSinta-se à vontade para chamar seus amigos para ajudá-lo."},
    3223 : { QUEST : "Bom trabalho naqueles edifícios!\aAgora, derrote mais dois.\aOs edifícios devem ter, pelo menos, dois andares." },
    3224 : { QUEST : "Fantástico!\aAgora é só derrotar mais dois edifícios.\aEles devem ter, pelo menos, três andares.\aQuando terminar, volte para pegar sua recompensa!",
             COMPLETE : "Você conseguiu, _avName_!\aVocê demonstrou uma elevada Toonmizade.",
             GREETING : "",
             },

    3225 : { QUEST : "_toNpcName_ diz que precisa de ajuda.\aPor que você não vai até lá e vê o que pode fazer para ajudá-la?_where_" },
    3235 : { QUEST : "Ah, esta é a salada que pedi!\aObrigada por trazê-la para mim.\aTodos esses Cogs devem ter amedrontado novamente o entregador de _toNpcName_ .\aPor que você não nos faz um favor e derrota alguns desses Cogs lá fora?\aDerrote 10 Cogs nos Jardins da Margarida e, então, vá até _toNpcName_.",
             INCOMPLETE_PROGRESS : "Você está trabalhando na eliminação de Cogs para mim?\aIsto é maravilhoso! Continue com o bom trabalho!",
             COMPLETE : "Oh, muito obrigada por derrotar aqueles Cogs!\aAgora, acho que poderei manter minha escala normal de entregas.\aSua recompensa é...",
             INCOMPLETE_WRONG_NPC : "Vá contar a _toNpcName_ sobre os Cogs que você derrotou._where_" },

    3236 : { QUEST : "Há muitos Robôs da Lei por aí.\aVocê pode fazer sua parte para ajudar!\aDerrote 3 edifícios de Robôs da Lei." },
    3237 : { QUEST : "Bom trabalho naqueles edifícios de Robôs da Lei!\aMas agora há muitos Robôs Vendedores!\aDerrote 3 edifícios de Robôs Vendedores e volte para buscar sua recompensa." },

    3238 : { QUEST : "Ah não! Um Cog \"Amizade Fácil\" roubou a Chave para os Jardins da Margarida!\aVeja se você consegue recuperá-la.\aLembre-se, o Amizade Fácil só pode ser encontrado dentro dos edifícios de Robôs Vendedores." },
    3239 : { QUEST : "Você achou uma chave, tudo bem, mas esta não é a correta!\aPrecisamos da chave dos Jardins da Margarida.\aContinue de olho! Ela ainda está com algum Cog \"Amizade Fácil\"!" },

    3242 : { QUEST : "Ah não! Um Cog Macaco velho roubou a Chave para os Jardins da Margarida!\aVeja se você consegue recuperá-la.\aLembre-se, os Macacos-velhos só podem ser encontrados dentro dos edifícios de Robôs da Lei." },
    3243 : { QUEST : "Você achou uma chave, tudo bem, mas esta não é a correta!\aPrecisamos da chave dos Jardins da Margarida.\aContinue de olho! Ela ainda está com algum Cog Macaco velho!" },

    3240 : { QUEST : "Acabei de saber que um Macaco velho roubou um saco de ração para pássaros de _toNpcName_ .\aDerrote Macacos velhos até recuperar a ração para pássaros do Florêncio e levá-la de volta para ele.\aOs Macacos velhos só são encontrados dentro de edifícios de Robôs da Lei._where_",
             COMPLETE : "Ah, muito obrigado por encontrar minha ração para pássaros!\aSua recompensa é...",
             INCOMPLETE_WRONG_NPC : "Bom trabalho na recuperação da ração para pássaros!\aAgora, leve-a para _toNpcName_._where_",
             },

    3241 : { QUEST : "Alguns dos edifícios de Cogs estão ficando altos demais e isso já está incomodando.\aVeja se você consegue derrubar alguns dos edifícios mais altos.\aRecupere 5 edifícios de 3 andares, ou mais altos, e volte para pegar sua recompensa.",
             },

    3250 : { QUEST : "A Detetive Linda da Rua dos Carvalhos recebeu informações sobre um Quartel de Robôs Vendedores.\aVá até lá e ajude-a a investigar.",
             },
    3251 : { QUEST : "Há algo estranho acontecendo por aqui.\aHá tantos Robôs Vendedores!\aOuvi dizer que eles organizaram seu próprio quartel no final desta rua.\aVá até lá e veja o que consegue descobrir.\aEncontre Cogs Robôs Vendedores em seu quartel, derrote 5 deles e volte aqui.",
             },
    3252 : { QUEST : "Ok, desembucha.\aO que você disse?\aQuartel de Robôs Vendedores?? Ah não!!! Algo tem que ser feito.\aDevemos avisar a Juíza Gala. Ela saberá o que fazer.\aVá até lá e conte a ela o que descobrimos. É só descer a rua.",
            },
    3253 : { QUEST : "Sim, posso ajudá-lo? Estou muito ocupada.\aHã? Quartel de Cogs?\aHã? Besteira. Isto nunca poderia acontecer.\aVocê deve estar enganado. Absurdo.\aHã? Não discuta comigo.\aOk, então, traga alguma prova.\aSe os Robôs Vendedores realmente estão construindo este Quartel de Cogs, qualquer Cog de lá estará carregando mapas.\aCogs amam trabalhar com papelada, sabe?\aDerrote Robôs Vendedores até encontrar os mapas.\aTraga-os aqui, e eu talvez acredite em você.",
            },
    3254 : { QUEST : "Você de novo, hã? Mapas? Você está com eles?\aDeixe-me vê-los! Humm... Uma fábrica?\aDeve ser lá que eles estão construindo os Robôs Vendedores... E o que é isso?\aSim, exatamente como eu suspeitava. Eu sabia o tempo todo.\aEles estão construindo um Quartel de Robôs Vendedores.\aIsso não é bom. Preciso fazer algumas ligações. Estou muito ocupada. Adeus!\aHã? Ah sim, leve estes mapas de volta para a Detetive Linda.\aEla poderá decifrá-los melhor.",
             COMPLETE : "O que a Juíza Gala disse?\aNós tínhamos razão? Ah, não. Vamos ver estes mapas.\aHumm... Parece que os Robôs Vendedores construíram uma fábrica com maquinário para fazer Cogs.\aParece muito perigoso. Fique de fora até que você tenha mais Pontos de risadas.\aQuando você tiver mais Pontos de risadas, teremos muito mais a aprender sobre o Quartel dos Robôs Vendedores.\aAqui está sua recompensa. Bom trabalho!",
            },


    3255 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se você consegue ajudar._where_" },
    3256 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se você consegue ajudar._where_" },
    3257 : { QUEST : "_toNpcName_ está investigando o "+lSellbotHQ+".\aVeja se você consegue ajudar._where_" },
    3258 : { QUEST : "Há muita confusão sobre o que os Cogs pretendem com seu novo Quartel.\aPreciso que você traga algumas informações diretamente deles.\aSe nós conseguirmos quatro memorandos internos de Robôs Vendedores dentro de seu Quartel, isso ajudará a esclarecer as coisas.\aTraga o primeiro memorando para mim para que possamos nos informar melhor.",
             },
    3259 : { QUEST : "Demais! Vamos ver o que diz o memorando...\a\"A/C Robôs Vendedores:\"\a\"Estarei em meu escritório no topo das Torres Robôs Vendedores promovendo Cogs a níveis mais altos.\"\a\"Quando você tiver méritos suficientes, entre no elevador do saguão para falar comigo\".\a\"O intervalo chegou ao fim. De volta ao trabalho!\"\a\"Assinado, Robô Vendedor VP\"\aAhá.... Flippy vai querer ver isto. Enviarei a ele imediatamente.\aVá buscar o segundo memorando e traga aqui.",
             },
    3260 : { QUEST : "Que bom, você está de volta. Deixe-me ver o que você encontrou....\a\"A/C Robôs Vendedores:\"\a\"As Torres Robôs Vendedores instalaram um novo sistema de segurança para afastar todos os Toons.\"\a\"Os Toons que forem encontrados nas Torres Robôs Vendedores serão detidos para interrogatório\".\a\"Encontrem-se no saguão para um coquetel, no qual discutiremos o assunto.\"\a\"Assinado, Amizade Fácil\"\aMuito interessante... Passarei imediatamente esta informação adiante.\aTraga o terceiro memorando.",
             },
    3261 : { QUEST : "Excelente trabalho _avName_! O que diz o memorando?\a\"A/C Robôs Vendedores:\"\a\"De algum modo, os Toons encontraram um jeito de se infiltrarem nas Torres Robôs Vendedores.\"\a\"Ligarei para vocês esta noite na hora do jantar para fornecer os detalhes.\"\a\"Assinado, Operador de Telemarketing\"\aHumm... Queria saber como os Toons estão conseguindo se infiltrar....\aTraga mais um memorando e acho que assim teremos informações suficientes.",
             COMPLETE : "Eu sabia que você conseguiria! Ok, o memorando diz...\a\"A/C Robôs Vendedores:\"\a\"Ontem, estava almoçando com Dr. Celebridade.\"\a\"Ele disse que o VP tem estado bastante ocupado nestes dias.\"\a\"Ele só receberá os Cogs que merecem promoção.\"\a\"Esqueci de dizer, o Amigo-da-onça jogará golfe comigo no domingo.\"\a\"Assinado, Dr. Sabe-com-quem-está-falando\"\aBem... _avName_, isto foi muito útil.\aAqui está sua recompensa.",
             },

    3262 : { QUEST : "_toNpcName_ tem novas informações sobre a Fábrica do "+lSellbotHQ+".\aVá ver o que ele tem a dizer._where_" },
    3263 : { GREETING : "Olá, parceiro!",
             QUEST : "Eu sou o Treinador Abobrinha, mas você pode me chamar de Treinador A.\aEu sou a favor de treinos com a raquete e alongamento, se é que você me entende.\aOuça, os Robôs Vendedores terminaram uma enorme fábrica para produzir Robôs Vendedores 24 horas por dia.\aReúna um grupo de parceiros Toon e raquetada na fábrica!\aDentro do Quartel do Robô Vendedor, procure pelo túnel que leva até a fábrica e, então, entre no elevador.\aVocê já tem que estar com as piadas e os pontos de risadas completos e ter Toons fortes como guias.\aPara retardar o progresso dos Robôs Vendedores, derrote o Supervisor dentro da fábrica.\aParece um grande exercício, se é que fui bem claro.",
             LEAVING : "Te vejo por aí, parceiro!",
             COMPLETE : "Ei, parceiro, bom trabalho naquela Fábrica!\aParece que você encontrou parte de um terno de Cog.\aDeve ser uma sobra do processo de fabricação de Cogs.\aIsto pode vir a calhar. Continue coletando estas partes quando tiver um tempo livre.\aQuem sabe, quando você coletar um terno de Cog completo, poderá vir a ser útil para alguma coisa....",
             },

    4001 : {GREETING : "",
            QUEST : "Agora, você tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
            INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
            INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
            COMPLETE : "Uma boa decisão...",
            LEAVING : QuestsDefaultLeaving,
            },

    4002 : {GREETING : "",
            QUEST : "Agora você tem que escolher o próximo tipo de piada que deseja aprender.\aDecida e depois volte aqui quando estiver pronto para escolher.",
            INCOMPLETE_PROGRESS : "Pense bem sobre sua decisão antes de escolher.",
            INCOMPLETE_WRONG_NPC : "Pense bem sobre sua decisão antes de escolher.",
            COMPLETE : "Uma boa decisão...",
            LEAVING : QuestsDefaultLeaving,
            },
    4200 : { QUEST : "Aposto que o Tom iria gostar de ter alguma ajuda na pesquisa que ele está fazendo._where_",
             },
    4201 : { GREETING: "Tudo certo?",
             QUEST : "Estou bastante preocupado com a onda de roubos de instrumentos musicais.\aEstou conduzindo uma pesquisa com meus amigos comerciantes.\aTalvez seja possível encontrar um padrão para me ajudar a resolver este caso.\aPeça a Tina o controle de estoque de concertina._where_",
             },
    4202 : { QUEST : "Sim, eu falei com Tom nesta manhã.\aO estoque está bem aqui.\aLeve para ele imediatamente, ok?_where_"
             },
    4203 : { QUEST : "Demais! Um a menos...\aAgora peça o da Cavaca._where_",
             },
    4204 : { QUEST : "Ah! O estoque!\aEsqueci completamente.\aAposto que consigo fazer enquanto você derrota 10 cogs.\aPasse por aqui depois, e eu prometo que estará pronto.",
             INCOMPLETE_PROGRESS : "31, 32... DROGA!\aVocê me fez perder a conta!",
             GREETING : "",
             },
    4205 : { QUEST : "Ah, aí está você.\aObrigada por me dar algum tempo.\aLeve isto para o Tom e diga olá por mim._where_",
             },
    4206 : { QUEST : "Humm, muito interessante.\aAgora estamos chegando a algum lugar.\aOk, o último estoque é o da Fifi._where_",
             },
    4207 : { QUEST : "Estoque?\aComo posso fazer o estoque se não tenho o formulário?\aVá até o Clave e veja se ele tem um para mim._where_",
             INCOMPLETE_PROGRESS : "Algum sinal daquele formulário?",
             },
    4208 : { QUEST : "Claro que eu tenho um formulário de estoque, monsenhor!\aMas eles não são de graça, sabe?.\aFaçamos o seguinte. Eu troco por uma torta de creme inteira.",
             GREETING : "Ei, monsenhor!",
             LEAVING : "Boa sorte...",
             INCOMPLETE_PROGRESS : "Um pedaço não adianta.\aEstou com fome, monsenhor. Eu preciso da torta INTEIRA.",
             },
    4209 : { GREETING : "",
             QUEST : "Humm...\aMuito gostoso!\aAqui está o formulário para Fifi._where_",
             },
    4210 : { GREETING : "",
             QUEST : "Valeu, foi uma grande ajuda.\aVamos ver...Violinos: 2\aTudo pronto! Aqui está!",
             COMPLETE : "Bom trabalho, _avName_.\aTenho certeza de que solucionarei este caso agora.\aPor que você não o soluciona?",
             },

    4211 : { QUEST : "Veja, o Dr. Triturador está ligando de cinco em cinco minutos. Você pode conversar com ele e ver qual o problema?_where_",
             },
    4212 : { QUEST : "Puxa! Estou feliz de ver que o Quartel dos Toons finalmente mandou alguém.\aNão tenho um cliente há dias.\aSão estes malditos Destruidores de Números que estão em todo lugar.\aAcho que eles estão ensinando maus hábitos de higiene oral a nossos moradores.\aDerrote dez deles e vamos ver se o negócio anda.",
             INCOMPLETE_PROGRESS : "Ainda sem clientes. Mas continue assim!",
             },
    4213 : { QUEST : "Sabe, talvez não sejam os Destruidores de Números, no final das contas.\aTalvez sejam apenas os Robôs Mercenários em geral.\aDerrote vinte deles e, com alguma sorte, alguém virá, pelo menos, para um check-up.",
             INCOMPLETE_PROGRESS : "Eu sei que vinte é muito. Mas tenho certeza de que vai valer a pena.",
             },
    4214 : { GREETING : "",
             LEAVING : "",
             QUEST : "Eu não consigo entender!\aAinda não há UM BENDITO freguês.\aTalvez precisemos ir até a fonte.\aTente recuperar um edifício Cog de Robôs Mercenários.\aIsso deve funcionar...",
             INCOMPLETE_PROGRESS : "Oh, por favor! Apenas um mísero prediozinho...",
             COMPLETE : "Ainda não há uma alma sequer aqui.\aMas, pense bem.\aEu não tinha mesmo clientes antes da invasão dos cogs!\aRealmente agradeço toda a sua ajuda.\aIsto deve ajudar você a prosseguir."
             },

    4215 : { QUEST : "A Ana precisa desesperadamente da ajuda de alguém.\aPor que você não passa lá e vê o que pode fazer?_where_",
             },
    4216 : { QUEST : "Obrigada por chegar tão rápido!\aParece que os cogs sumiram com várias passagens dos meus clientes.\aA Cavaca disse que viu um Amigo-da-Onça saindo daqui com as garras cheias de passagens.\aVeja se você consegue recuperar a passagem do Alê Nhador para o Alasca.",
             INCOMPLETE_PROGRESS : "Aqueles Amigos da Onça podem estar em qualquer lugar agora...",
             },
    4217 : { QUEST : "Legal! Você encontrou!\aAgora seja um cavalheiro e entregue ao Alê Nhador para mim, está bem?_where_",
             },
    4218 : { QUEST : "Genial, estupendo, fabuloso!\aAlasca, aqui vou eu!\aNão agüento mais esses cogs infernais.\aOlha, acho que a Ana precisa de você de novo._where_",
             },
    4219 : { QUEST : "Exatamente, você adivinhou!\aPreciso de você para derrotar aquelas pestes dos Amigos da Onça para recuperar a passagem da Tábata para o Festival de Jazz.\aVocê sabe como fazer...",
               INCOMPLETE_PROGRESS : "Há mais lá fora, em algum lugar...",
             },
    4220 : { QUEST : "Gracinha!\aVocê poderia entregar este também?_where_",
             },
    4221 : { GREETING : "",
             LEAVING : "Fica frio...",
             QUEST : "Legal, cara!\aAgora estou na cidade dos gordinhos, _avName_.\aAntes de sair fora, é melhor falar com a Ana Banana de novo..._where_",
             },
    4222 : { QUEST : "Este é o último, prometo!\aAgora procure pela passagem do Barry para o grande concurso de cantores.",
             INCOMPLETE_PROGRESS : "Vamos lá, _avName_.\aO Barry está contando com você.",
             },
    4223 : { QUEST : "Isto deve alegrar o Barry._where_",
             },
    4224 : { GREETING : "",
             LEAVING : "",
             QUEST : "Olá, Olá, OLÁ!\aMagnífico!\aSó conheço eu mesmo e os caras que vão fazer a faxina. \aA Ana disse para você passar lá e pegar a sua recompensa._where_\aTchau, Tchau, TCHAU!",
             COMPLETE : "Obrigado por toda a sua ajuda, _avName_.\aVocê é realmente um tesouro aqui de Toontown.\aFalando em tesouros...",
             },

    902 : { QUEST : "Vá ver o Léo.\aEle precisa de alguém para entregar uma mensagem para ele._where_",
            },
    4903 : { QUEST : "Cara!\aMinhas castanholas estão foscas e tenho um grande show hoje à noite.\aLeve-as para o Carlos e veja se ele pode dar um polimento nelas._where_",
            },
    4904 : { QUEST : "Sim, acho que posso polir esta peça. Mas preciso de alguma tinta azul de lula",
             GREETING : "Olá!",
             LEAVING : "Tchau!",
             INCOMPLETE_PROGRESS : "Você pode achar uma lula perto de algum píer de pesca.",
             },
    4905 : { QUEST : "Claro! Isso mesmo!\aAgora, preciso de um minuto para polir isto. Por que você não trabalha na recuperação de um prédio de um andar enquanto trabalho por aqui?",
             GREETING : "Ola!",
             LEAVING : "Tchau!",
             INCOMPLETE_PROGRESS : "Só mais um minutinho...",
             },
    4906 : { QUEST : "Muito bom!\aAqui estão as castanholas do Léo._onde_",
             },
    4907 : { GREETING : "",
             QUEST : "Maneiro, cara!\aElas estão incríveis!\aAgora preciso que você consiga uma cópia da letra da “Música de Natal” da Heidi._where_",
             },
    4908 : { QUEST: "E aí pessoal!\aHumm, Eu não tenho uma cópia dessa música à mão.\aSe você me der um tempinho, eu posso transcrever de cabeça.\aPor que você não dá uma voltinha e aproveita para recuperar um edifício de dois andares enquanto escrevo?",
             },
    4909 : { QUEST : "Desculpe.\aMinha memória está ficando meio confusa.\aSe você recuperar um edifício de três andares, tenho certeza de que estarei pronta quando voltar...",
             },
    4910 : { QUEST : "Tudo pronto!\aDesculpe a demora.\aLeve isto para o Léo._where_",
             GREETING : "",
             COMPLETE : "Caramba, cara!\aMeu show vai detonar!\aFalando em detonar, você pode detonar alguns cogs com isto..."
             },
    5247 : { QUEST : "Este bairro está ficando perigoso...\aVocê deve estar querendo aprender alguns truques novos.\a_toNpcName_ me ensinou tudo que sei, então, talvez ele possa ajudar você também._where_" },
    5248 : { GREETING : "Ah, sim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você parece estar empenhado na missão.",
             QUEST : "Ah, bem-vindo, novo aprendiz.\aEu sei de tudo que há para saber sobre o jogo de tortas.\aPorém, antes de começarmos o seu treinamento, é necessário uma pequena demonstração.\aSaia e derrote dez dos maiores Cogs." },
    5249 : { GREETING: "Humm.",
             QUEST : "Excelente!\aAgora demonstre sua habilidade como pescador.\aColoquei ontem três dados de pelúcia no lago.\aPesque-os e traga-os para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Parece que você não é tão hábil com a vara e o molinete." },
    5250 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que você sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edifícios mais altos dos Robôs da Lei.",
             INCOMPLETE_PROGRESS : "Os edifícios deram problema para você?", },
    5258 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que você sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edifícios mais altos dos Robôs-chefes.",
             INCOMPLETE_PROGRESS : "Os edifícios deram problema para você?", },
    5259 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que você sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edifícios mais altos dos Robôs Mercenários.",
             INCOMPLETE_PROGRESS : "Os edifícios deram problema para você?", },
    5260 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahá! Estes dados ficarão ótimos pendurados no retrovisor do meu carro de bois!\aAgora, mostre para mim que você sabe distinguir seus inimigos.\aVolte quando tiver recuperado dois dos edifícios mais altos dos Robôs Vendedores.",
             INCOMPLETE_PROGRESS : "Os edifícios deram problema para você?", },
    5200 : { QUEST : "Aqueles cogs traiçoeiros estão envolvidos nisto novamente.\a_toNpcName_ percebeu que tem outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_" },
    5201 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a você por ter vindo.\aUm grupo desses Caça-talentos chegou e roubou minha bola de futebol.\aO líder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVocê pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5261 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a você por ter vindo.\aUm grupo desses Duas Caras chegou e roubou minha bola de futebol.\aO líder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVocê pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5262 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a você por ter vindo.\aUm grupo desses Sacos de Dinheiro chegou e roubou minha bola de futebol.\aO líder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVocê pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5263 : { GREETING: "",
             QUEST : "Oi, _avName_. Acho que eu devo agradecer a você por ter vindo.\aUm grupo desses Relações Públicas chegou e roubou minha bola de futebol.\aO líder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\aVocê pode trazer de volta a minha bola?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Conseguiu achar minha bola de futebol?",
             COMPLETE : "Dez! Encontrei! Olha aqui, tome a sua recompensa...",
             },
    5202 : { QUEST : "O Brrrgh foi invadido por alguns dos mais temíveis Cogs já vistos.\aVocê provavelmente desejará carregar mais piadas consigo.\aOuvi falar que _toNpcName_ tem uma sacola grande que você pode usar para carregar mais piadas._where_" },
    5203 : { GREETING: "Hã? Você está no meu time de trenó?",
             QUEST : "O que é isto? Você quer uma bolsa?\aEu tinha uma aqui em algum lugar... Acho que está no meu tobogã?\aSó que... Eu não vejo o meu tobogã desde a grande corrida!\aTalvez um destes Cogs o tenha pego.",
             LEAVING : "Você viu meu tobogã?",
             INCOMPLETE_PROGRESS : "Quem é você novamente? Desculpe, estou meio confuso depois da batida." },
    5204 : { GREETING : "",
             LEAVING : "",
             QUEST : "Este é o meu tobogã? Não vejo nenhuma sacola aqui.\aAcho que o Cabeção Kika estava na equipe... Será que está com ele?_where_" },
    5205 : { GREETING : "Ai, minha cabeça!",
             LEAVING : "",
             QUEST : "Hã? Tobi? Ah, a bolsa?\aBom, acho que ele estava na nossa equipe de tobogã?\aMinha cabeça dói tanto que não consigo pensar direito.\aVocê consegue para mim alguns cubos de gelo no lago congelado para eu pôr na minha cabeça?",
             INCOMPLETE_PROGRESS : "Aaiii, minha cabeça está me matando! Tem gelo aí?", },
    5206 : { GREETING : "",
             LEAVING : "",
             QUEST : "Ahhh, agora me sinto bem melhor!\aEntão você está procurando a bolsa do Tobi, né?\aAcho que ela foi parar na cabeça do Álvaro Asno depois da batida._where_" },
    5207 : { GREETING : "Iiiiiiiiiip!",
             LEAVING : "",
             QUEST : "O que é bolsa? Quem é Cabeção?\aTenho medo de edifícios! Você detona edifício, eu dou bolsa!",
             INCOMPLETE_PROGRESS : "Mais edifícios! Ainda com medo!",
             COMPLETE : "Ooooh! Mim gosta você!" },
    5208 : { GREETING : "",
             LEAVING : "Iiiiiiiiiiik!",
             QUEST : "Ooooh! Mim gosta você!\aVai pra Clínica do Esqui. Sacola lá." },
    5209 : { GREETING : "Valeu, garoto!",
             LEAVING : "Até mais!",
             QUEST : "Cara, o Álvaro Asno é doido!\aSe você fosse maluco que nem o Álvaro, eu daria a bolsa para você, cara.\aVai ensacar uns Cogs para poder pegar a sua sacola, cara! Essa agora!",
             INCOMPLETE_PROGRESS : "Tem certeza de que você é radical o bastante para isso? Vai ensacar mais Cogs.",
             COMPLETE : "Caramba, você é irado! Aquilo foi um bando de Cogs que você ensacou!\aToma a sua bolsa!" },

    5210 : { QUEST : "_toNpcName_ está gamada em alguém do bairro, mas é segredo.\aSe você ajudá-la, ela pode lhe dar uma boa recompensa._where_" },
    5211 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos com bico veio e a tomou de mim.\aVocê consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5264 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de barbatana veio e a tomou de mim.\aVocê consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5265 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de Amizade Fácil veio e a tomou de mim.\aVocê consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5266 : { GREETING: "Buá!",
             QUEST : "Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\aMas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs Aventureiros Corporativos asquerosos veio e a tomou de mim.\aVocê consegue pegá-la de volta para mim?",
             LEAVING : "Buá!",
             INCOMPLETE_PROGRESS : "Por favor, encontre minha carta." },
    5212 : { QUEST : "Oh, obrigada por encontrar a minha carta!\aPor favor, você poderia entregá-la ao cão mais lindo do bairro? Por favor! Por favor!",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você não entregou a minha carta, não é?",
             },
    5213 : { GREETING : "Enfeitiçado, com certeza.",
             QUEST : "Não posso dar atenção à sua carta, sabe.\aTodos os meus cãezinhos foram levados!\aSe você os trouxer de volta, a gente volta a conversar.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Tadinhos dos meus cãezinhos!" },
    5214 : { GREETING : "",
             LEAVING : "Tchauzinho!",
             QUEST : "Graças a você minhas belezinhas voltaram.\aVamos ver a carta agora...\nMmmm, parece que tenho outra admiradora secreta.\aIsso exigirá uma visita ao meu querido amigo Carlo.\aAposto como você vai adorá-lo._where_" },
    5215 : { GREETING : "He, he...",
             LEAVING : "Volte aqui, sim, sim.",
             INCOMPLETE_PROGRESS : "Ainda há alguns grandalhões na área. Volte aqui para falar conosco quando eles forem embora.",
             QUEST : "Quem mandou você? Não gostamos muito de Snobs, não...\aMas gostamos menos ainda de Cogs...\aExpulse os grandalhões e ajudaremos vocês, ajudaremos." },
    5216 : { QUEST : "Falamos que ajudaríamos você.\aEntão, pegue este anel e leve à garota.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você ainda está com o anel???",
             COMPLETE : "Oh querrrrido!!! Obrigado!!!\aAh, também tenho algo especial para você.",
             },
    5217 : { QUEST : "Parece que _toNpcName_ pode dar uma ajuda._where_" },
    5218 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Tenho certeza de que há mais Amizades Fáceis por aqui em algum lugar.",
             QUEST : "Socorro!!! Socorro!!! Assim não dá!\aEsses Amizades Fáceis estão me deixando maluco!!!" },
    5219 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não são só estes. Só vi um!!!",
             QUEST : "Ah, obrigado, mas agora são os Aventureiros Corporativos!!!\aVocê tem que me ajudar!!!" },
    5220 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não, não, não, havia um aqui agora mesmo!",
             QUEST : "Agora, eu percebo que são aqueles Agiotas!!!\aPensei que você ia me salvar!!!" },
    5221 : { GREETING : "",
             LEAVING : "",
             QUEST : "Sabe de uma coisa, talvez não sejam os Cogs coisa nenhuma!\aVocê pode pedir à Hilária para fazer para mim uma poção calmante? Talvez isto ajude...._where_" },
    5222 : { LEAVING : "",
             QUEST : "Esse Américo é mesmo uma figura!\aVou preparar algo que vai dar jeito nele rapidinho!\aPuxa, parece que estou sem bigodes de sardinha...\aSeja legal comigo e corra lá no lago para pegar alguns para mim.",
             INCOMPLETE_PROGRESS : "Já pegou aqueles bigodes para mim?", },
    5223 : { QUEST : "OK. Obrigada!\aTome, leve agora para o Américo. Isto deve acalmá-lo de uma vez por todas.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vá logo, leve a poção para o Américo.",
             },
    5224 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Vá pegar aqueles Macacos velhos para mim, ok?",
             QUEST : "Puxa vida, graças a Deus você voltou!\aPasse logo para cá esta poção!!!\aGlub, glub, glub...\aQue gosto horrível!\aSabe de uma coisa? Sinto-me bem mais calmo. Agora que eu posso pensar com mais clareza, me toquei que...\aEram os Macacos-velhos que estavam me enlouquecendo todo este tempo!!!",
             COMPLETE : "Nossa! Agora eu posso relaxar!\aTenho certeza de que há alguma coisa aqui que posso dar a você. Aqui, leve isto!" },
    5225 : { QUEST : "Desde o acidente com o pão de nabo, Felipe Nervosinho ficou furioso com _toNpcName_.\aQuem sabe você não consegue ajudar o Pio a acertar os ponteiros entre eles?_where_" },
    5226 : { QUEST : "Isso mesmo, você deve ter ouvido falar que o Felipe Nervosinho está furioso comigo...\aEu estava só tentando ser legal oferecendo o pão de nabo.\aQuem sabe você não consegue alegrá-lo.\aO Felipe detesta aqueles Cogs Robôs Mercenários, principalmente os edifícios deles.\aSe você recuperar alguns edifícios de Robôs Mercenários, talvez ajude.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Quem sabe alguns edifícios a mais?", },
    5227 : { QUEST : "Demais! Vá dizer ao Felipe o que você fez._where_" },
    5228 : { QUEST : "Puxa, ele fez isso mesmo?\aEsse Pio acha que pode se safar fácil, né?\aSó quebrou meu dente, só isso que ele fez, com aquele pão de nabo dele!\aSe você levar o meu dente para o Dr. Ban Guela para mim, quem sabe ele consegue dar jeito.",
             GREETING : "Mmmmrrf.",
             LEAVING : "Resmungo, resmungo.",
             INCOMPLETE_PROGRESS : "Você de novo? Pensei que você estava indo levar meu dente para consertar.",
             },
    5229 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "É, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVocê não quer dar cabo de alguns daqueles Cogs Robôs Mercenários das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5267 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "É, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVocê não quer dar cabo de alguns daqueles Cogs Robôs Vendedores das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5268 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "É, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVocê não quer dar cabo de alguns daqueles Cogs Robôs da Lei das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5269 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda estou ajeitando o dente. Vai demorar um pouco.",
             QUEST : "É, este dente parece estar ruim mesmo, mas tudo bem.\aEu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\aVocê não quer dar cabo de alguns daqueles Cogs Robôs-chefe das ruas enquanto espera?\aEles estão assustando os meus clientes." },
    5230 : { GREETING: "",
             QUEST : "Ainda bem que você voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Barão Ladrão entrou aqui e o levou, infelizmente.\aSerá que você não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você já achou aquele dente?" },
    5270 : { GREETING: "",
             QUEST : "Ainda bem que você voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Rei da Cocada Preta entrou aqui e o levou, infelizmente.\aSerá que você não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você já achou aquele dente?" },
    5271 : { GREETING: "",
             QUEST : "Ainda bem que você voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que o Dr. Celebridade entrou aqui e o levou, infelizmente.\aSerá que você não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você já achou aquele dente?" },
    5272 : { GREETING: "",
             QUEST : "Ainda bem que você voltou!\aDesisti de consertar aquele dente velho e, em vez de consertá-lo, fiz um novo dente de ouro para o Felipe.\aSó que um Figurão entrou aqui e o levou, infelizmente.\aSerá que você não consegue pegá-lo? Vamos, apresse-se!",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Você já achou aquele dente?" },
    5231 : { QUEST : "Legal, é este dente mesmo!\aPor que você não corre para levá-lo para o Felipe?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Aposto como o Felipe vai adorar ver o dente novo dele.",
             },
    5232 : { QUEST : "Puxa, obrigado.\aMmmrrrfffffff\aE aí, que tal, hein?\aOk, tá legal, pode dizer ao Pio que eu o perdôo.",
             LEAVING : "",
             GREETING : "", },
    5233 : { QUEST : "Legal, muito bom saber disso.\aAchei mesmo que meu velho amigo Felipe não podia ficar com raiva de mim.\aPara agradecer e ser gentil, preparei para ele este pão de pinha.\aSerá que você podia correr lá e entregar a ele para mim?",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Melhor se apressar. O pão de pinha só é bom quando está quente.",
             COMPLETE : "Puxa, o que é isto? Para mim?\aNham, nham...\aOhhhhhh! Meu dente! Aquele Pio Arrepio!\aTá legal, não foi sua culpa. Tome aqui, leve isto por todo o trabalho que demos a você.",
             },
    903 : { QUEST : "Você deve se aprontar para ver _toNpcName_, o Mago do Lago Congelado, para o seu teste final._where_", },
    5234 : { GREETING: "",
             QUEST : "Ahá! Você voltou.\aAntes de você começar, precisamos comer.\aTraga para a gente alguns pedaços de coco para o nosso caldo.\aO coco em pedaços só pode ser conseguido nos Cogs Rei da Cocada Preta.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda precisamos de coco em pedaços." },
    5278 : { GREETING: "",
             QUEST : "Ahá! Você voltou.\aAntes de você começar, precisamos comer.\aTraga para a gente caviar para o nosso caldo.\aO caviar só pode ser conseguido nos Cogs Dr. Celebridade.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Ainda precisamos de caviar." },
    5235 : { GREETING: "",
             QUEST : "Homens simples comem com colheres simples.\aOs Cogs levaram minha colher simples, por isso, eu simplesmente não posso comer.\aPegue minha colher de volta. Acho que foi um Barão Ladrão.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Eu simplesmente preciso da minha colher." },
    5279 : { GREETING: "",
             QUEST : "Homens simples comem com colheres simples.\aOs Cogs levaram minha colher simples, por isso, eu não posso comer.\aPegue minha colher de volta. Acho que foi um Figurão.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Eu simplesmente preciso da minha colher." },
    5236 : { GREETING: "",
             QUEST : "Muito obrigado.\aSlurp, slurp...\aAhhh, agora, você precisa pegar um sapo falante. Tente pescá-lo no lago.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cadê o sapo falante?" },

    5237 : {  GREETING : "",
              LEAVING : "",
              INCOMPLETE_PROGRESS : "Você não conseguiu a sobremesa ainda.",
              QUEST : "Ah, isto é, com certeza, um sapo falante. Passe para cá.\aO que você me diz, sapo?\aUh huh.\aUh huh...\aO sapo falou. Precisamos da sobremesa.\aTraga para a gente algumas casquinhas de sorvete da _toNpcName_.\aPor alguma razão, o sapo gosta de sorvete sabor feijão vermelho._where_", },
    5238 : { GREETING: "",
             QUEST : "Então, o mago mandou você aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feijão vermelho.\aVocê nem imagina, mas um bando de Cogs entrou aqui e as levou.\aEles disseram que iam levá-las para o Dr. Celebridade, ou alguma baboseira parecida.\aCertamente, apreciaria se você pudesse recuperá-las para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Já achou todas as minhas casquinhas de sorvete?" },
    5280 : { GREETING: "",
             QUEST : "Então, o mago mandou você aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feijão vermelho.\aVocê nem imagina, mas um bando de Cogs entrou aqui e as levou.\aEles disseram que iam levá-las para O Rei da Cocada Preta, ou alguma baboseira parecida.\aCertamente, apreciaria se você pudesse recuperá-las para mim.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Já achou todas as minhas casquinhas de sorvete?" },
    5239 : { QUEST : "Obrigado por trazer de volta as minhas casquinhas de sorvete!\aTome uma para o Pequeno Grande Ancião.",
             GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "É melhor você levar este sorvete para o Pequeno Grande Ancião antes que ele derreta.", },
    5240 : { GREETING: "",
             QUEST : "Muito bem. Aqui está, sapo...\aSlurp, slurp...\aOk, agora estamos quase prontos.\aSe você pudesse apenas trazer um pozinho para secar as minhas mãos...\aAcho que das perucas daqueles Cogs Figurões às vezes sai pó.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Achou algum pó?" },
    5281 : { GREETING: "",
             QUEST : "Muito bem. Aqui está, sapo...\aSlurp, slurp...\aOk, agora estamos quase prontos.\aSe você pudesse apenas trazer um pozinho para secar as minhas mãos...\aAcho que aqueles Cogs Drs. Celebridades às vezes têm pó para o nariz.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Achou algum pó?" },
    5241 : { QUEST : "Ok.\aComo já disse antes, para lançar uma torta pra valer, não basta jogá-la com a mão...\a...É preciso jogar com a alma.\aNão sei exatamente o que isto significa, portanto, sentarei e contemplarei você em seu trabalho de recuperar edifícios.\aVolte quando tiver concluído a sua tarefa.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Sua tarefa ainda não está concluída.", },
    5242 : { GREETING: "",
             QUEST : "Embora eu ainda não saiba sobre o que estou falando, você realmente merece.\aDou a você, então, uma tarefa final...\aO sapo falante precisa de uma namorada.\aAche uma sapa falante. O sapo falou.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cadê a sapa falante?",
             COMPLETE : "Puxa! Estou cansado com todo esse esforço. Preciso descansar agora.\aAgora, pegue a sua recompensa e saia." },

    5243 : { QUEST : "Soares Suado está começando a feder no início da rua.\aFala com ele para tomar um banho ou algo do gênero?_where_" },
    5244 : { GREETING: "",
             QUEST : "É, acho que suei demais aqui.\aMmmm, se eu pudesse consertar aquele vazamento no encanamento do meu chuveiro...\aAcho que a engrenagem de um daqueles Cogs pequenos bastaria para o conserto.\aVá achar uma engrenagem de um Microempresário para a gente tentar consertar.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Onde está aquela engrenagem que você ia conseguir?" },
    5245 : { GREETING: "",
             QUEST : "É, parece que funcionou.\aMas eu fico solitário quando tomo banho...\aSerá que você poderia pescar um patinho de borracha para me fazer companhia?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não acha o patinho de borracha?" },
    5246 : { QUEST : "O patinho é ótimo, mas...\aTodos aqueles edifícios aqui em volta me deixam com os nervos em frangalhos.\aEu me sentiria bem melhor se houvesse menos edifícios por aqui.",
             LEAVING : "",
             COMPLETE : "Ok, agora eu vou tomar banho. Ah, aqui está uma coisinha para você.",
             INCOMPLETE_PROGRESS : "Ainda estou preocupado com os edifícios.", },
    5251 : { QUEST : "Vítor Vestíbulo devia estar fazendo um show nesta noite.\aOuvi falar que ele estava tendo problemas com o equipamento._where_" },
    5252 : { GREETING: "",
             QUEST : "É isso aí! Seria bom mesmo aceitar a sua ajuda.\aAqueles Cogs entraram aqui e levaram todas as engrenagens do meu equipamento enquanto eu estava descarregando a caminhonete.\aVocê pode me dar uma mãozinha e conseguir de volta o meu microfone?",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Cara, eu não consigo cantar sem o microfone." },
    5253 : { GREETING: "",
             QUEST : "Legal, você conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Aventureiros Corporativos o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5273 : { GREETING: "",
             QUEST : "Legal, você conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Amizades Fáceis o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5274 : { GREETING: "",
             QUEST : "Legal, você conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Agiotas o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5275 : { GREETING: "",
             QUEST : "Legal, você conseguiu meu microfone de volta.\aValeu, mas...\aEu preciso mesmo do meu teclado para poder fazer um som.\aAcho que um daqueles Macacos velhos o levaram.",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Não conseguiu pegar o meu teclado?" },
    5254 : { GREETING: "",
             QUEST : "Tudo em cima! Agora estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Dr. Celebridade, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5282 : { GREETING: "",
             QUEST : "Tudo em cima! Agora, estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Rei da Cocada Preta, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5283 : { GREETING: "",
             QUEST : "Tudo em cima! Agora estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Barão Ladrão, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },
    5284 : { GREETING: "",
             QUEST : "Tudo em cima! Agora, estou na parada.\aSe ao menos eles não tivessem levado meus sapatos de plataforma...\aAqueles sapatos provavelmente acabaram com algum Figurão, creio eu.",
             LEAVING : "",
             COMPLETE : "Tudo bem!! Estou pronto agora.\aOlá Brrrgh!!!\aHã? Onde está todo mundo?\aOk, pegue isto e reúna alguns fãs, está bem?",
             INCOMPLETE_PROGRESS : "Não posso me apresentar sem sapatos, né?" },

    5255 : { QUEST : "Parece que você pode usar mais pontos de risadas.\aTalvez _toNpcName_ entre em um acordo com você.\aNão deixe de firmar o acordo por escrito..._where_" },
    5256 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Trato é trato.",
             QUEST : "Então, você está atrás de pontos de risadas, né?\aSe eu tenho uma proposta para você!?\aÉ só tomar conta de alguns Cogs Robôs-chefe para mim...\aAí eu dou uma injeção de ânimo nos seus pontos." },
    5276 : { GREETING : "",
             LEAVING : "",
             INCOMPLETE_PROGRESS : "Trato é trato.",
             QUEST : "Então, você está atrás de pontos de risadas, né?\aSe eu tenho uma proposta para você!?\aÉ só tomar conta de alguns Cogs Robôs da Lei para mim...\aAí eu dou uma injeção de ânimo nos seus pontos." },
    5257 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Ok, mas tenho certeza de que falei para você reunir alguns Cogs Robôs da Lei.\aBom, se você está falando, tudo bem, mas, então, fica me devendo uma.",
             INCOMPLETE_PROGRESS : "Acho que você não terminou ainda.",
             QUEST : "Você está dizendo que acabou? Derrotou todos os Cogs?\aVocê deve ter entendido errado, nosso trato era para os Cogs Robôs Vendedores.\aTenho certeza de que disse para você derrotar alguns Cogs Robôs Vendedores para mim." },
    5277 : { GREETING : "",
             LEAVING : "",
             COMPLETE : "Ok, mas tenho certeza de que falei para você reunir alguns Cogs Robôs da Lei.\aBom, se você está falando, tudo bem, mas, então, fica me devendo uma.",
             INCOMPLETE_PROGRESS : "Acho que você não terminou ainda.",
             QUEST : "Você está dizendo que acabou? Derrotou todos os Cogs?\aVocê deve ter entendido errado, nosso trato era para os Cogs Robôs Mercenários.\aTenho certeza de que disse para você derrotar alguns Cogs Robôs Mercenários para mim." },
}

# ChatGarbler.py
ChatGarblerDog = ["au", "arf", "grrrr"]
ChatGarblerCat = ["miau", "miu"]
ChatGarblerMouse = ["quick", "quiiii", "quiiiiquiiii"]
ChatGarblerHorse = ["rííírrrr", "brrr"]
ChatGarblerRabbit = ["ick", "iipr", "iipi", "iicki"]
ChatGarblerFowl= ["quá", "quack", "quáááck"]
ChatGarblerDefault = ["blá"]

# AvatarDNA.py
Bossbot = "Robô-chefe"
Lawbot = "Robô da Lei"
Cashbot = "Robô Mercenário"
Sellbot = "Robô Vendedor"
BossbotS = "um Robô-chefe"
LawbotS = "um Robô da Lei"
CashbotS = "um Robô Mercenário"
SellbotS = "um Robô Vendedor"
BossbotP = "Robôs-chefe"
LawbotP = "Robôs da Lei"
CashbotP = "Robôs Mercenários"
SellbotP = "Robôs Vendedores"

# AvatarDetailPanel.py
AvatarDetailPanelOK = 'OK'
AvatarDetailPanelCancel = 'Cancelar'
AvatarDetailPanelClose = 'Fechar'
AvatarDetailPanelLookup = "Procurando detalhes de %s."
AvatarDetailPanelFailedLookup = "Não foi possível obter detalhes de %s."
AvatarDetailPanelOnline = "Região: %(district)s\nLocal: %(location)s"
AvatarDetailPanelOffline = "Região: off-line\nLocal: off-line"

# AvatarPanel.py
AvatarPanelFriends = "Amigos"
AvatarPanelWhisper = "Cochichar"
AvatarPanelSecrets = "Secretos"
AvatarPanelGoTo = "Ir para"
AvatarPanelIgnore = "Ignorar"
AvatarPanelCogLevel = "Nível: %s"
AvatarPanelCogDetailClose = 'Fechar'

# DistributedAvatar.py
WhisperNoLongerFriend = "%s saiu da sua lista de amigos."
WhisperNowSpecialFriend = "%s agora é seu amigo secreto!"
WhisperComingToVisit = "%s está vindo visitar você."
WhisperFailedVisit = "%s tentou visitar você."
WhisperTargetLeftVisit = "%s foi para algum outro lugar. Tente novamente!"
WhisperGiveupVisit = "%s não conseguiu encontrá-lo porque você está se movendo!"
WhisperIgnored = "%s está ignorando você!"
TeleportGreeting = "Oi, %s."

DialogSpecial = "ooo"
DialogExclamation = "!"
DialogQuestion = "?"

# Cutoff string lengths to determine how much barking to play
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20

# LocalAvatar.py
FriendsListLabel = "Amigos"

# DistributedAvatar.py
WhisperFriendComingOnline = "%s está entrando on-line!"
WhisperFriendLoggedOut = "%s fez logout."

# TeleportPanel.py
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Tentando ir para %s."
TeleportPanelNotAvailable = "%s está ocupado(a) agora; tente novamente mais tarde."
TeleportPanelIgnored = "%s está ignorando você."
TeleportPanelNotOnline = "%s não está on-line neste momento."
TeleportPanelWentAway = "%s saiu."
TeleportPanelUnknownHood = "Você não sabe ir para %s!"
TeleportPanelUnavailableHood = "%s não está disponível agora; tente novamente mais tarde."
TeleportPanelDenySelf = "Você não pode ir lá por conta própria!"
TeleportPanelOtherShard = "%(avName)s está na região %(shardName)s, e você está na região %(myShardName)s. Deseja ir para %(shardName)s?"

# DistributedBattleBldg.py
BattleBldgBossTaunt = "Sou o chefe."

# HealJokes.py
ToonHealJokes = [
    ["O que faz TIQUE-TIQUE-TIQUE-AU?",
     "Um cãonômetro!"],
    ["Por que o louco toma banho com o chuveiro desligado?",
     "Porque ele comprou xampú para cabelos secos!"],
    ["Por que é difícil para o fantasma contar mentiras?",
     "Porque seus pensamentos são transparentes."],
    ["Do que a bailarina é chamada quando machuca o pé e se recusa a dançar?",
     "Pé-nóstica!"],
    ["O que a vaca foi fazer no espaço?",
     "Foi se encontrar com o vácuo!"],
    ["Por que o gato mia para a Lua e a Lua não mia para o gato?",
     "Porque astro-no-mia!"],
    ["Por que as tartarugas não ficam bêbadas?",
     "Porque elas só têm um casco!"],
    ["Por que o elefante usa tênis vermelhos?",
     "Porque os branquinhos sujam muito."],
    ["Por que a galinha atravessa a rua?",
     "Para chegar ao outro lado!"],
    ["Qual é a maior injustiça do Natal?",
     "O peru morre e a missa é do galo."],
    ["Qual é o cúmulo dos trabalhos manuais?",
     "Tricotar com a linha do trem."],
    ["O que é um vulcão?",
     "Uma montanha com soluço."],
    ["O que é um pontinho vermelho, um azul e um rosa em cima de uma árvore?",
     "Um morangotango com urublue num pinkenick."],
    ["Por que o elefante não consegue tirar carteira de motorista?",
     "Porque ele só dá trombada."],
    ["O que um tijolo disse para o outro?",
     "Existe um 'ciumento' entre nós."],
    ["O que a porta disse para a chave?",
     "Vamos dar uma voltinha."],
    ["O que o elétron fala quando atende ao telefone?",
     "Próton!"],
    ["Quem é o rei da horta?",
     "Rei Polho."],
    ["Por que as pilhas são melhores que os políticos?",
     "Porque elas têm, pelo menos, um lado positivo."],
    ["O que Benjamin Franklin disse quando inventou a eletricidade?",
     "Nada. Ele estava em estado de choque."],
    ["Por que o cachorro balança o rabo?",
     "Porque o rabo não tem força para balançar o cachorro."],
    ["Qual é o cúmulo da força?",
     "Dobrar a esquina."],
    ["O que não é de comer, mas dá água na boca?",
     "O copo."],
    ["Quem é a mãe do mingau?",
     "Mãe Zena."],
    ["O que o Batman disse para o Robin na hora em que entraram no carro?",
     "BAT a porta!"],
    ["O que é um pontinho amarelo tomando sol?",
     "É um fandango querendo virar baconzito."],
    ["O que é um pontinho rosa no armário?",
     "É um cupink."],
    ["Quem é o tio da construção?",
     "Tio Jolo."],
    ["O que dá um cruzamento de um dálmata com um canário?",
     "Uma onça pintada da Amazônia."],
    ["O que é uma porção de letras voando?",
     "Um bando de borboletras."],
    ["O que é que viaja o mundo inteiro, mas fica o tempo todo em um canto só?",
     "O selo."],
    ["O que é um pontinho verde em cima de um amarelo no canto da parede?",
     "Uma ervilha de castigo ajoelhada no milho."],
    ["Por que o namoro da goiabada com o queijo não deu certo?",
     "Porque o queijo era fresco."],
    ["O que é um pontinho azul no guarda-roupas?",
     "É uma bluesa."],
    ["O que é um pontinho verde no fundo da piscina?",
     "É uma ervilha... Segurando a respiração!"],
    ["O que é um pontinho vermelho e azul voando de um lado para o outro?",
     "Uma mosca fantasiada de Super-homem."],
    ["Qual é o animal que tem mais de três olhos e menos de quatro?",
     "O pi-olho, ou seja, 3,14."],
    ["O que a aranha faz quando vai para a aula de dança?",
     "Sapa-teia."],
    ["Por que o pato tem ciúmes do cavalo?",
     "Porque ele tem quatro patas."],
    ["Quando você tem certeza de que um ovo não tem um pintinho dentro?",
     "Quando o ovo é de pata."],
    ["Por que ninguém apareceu no enterro do elefante?",
     "Porque ninguém queria carregar o caixão."],
    ["O que é que sempre aumenta, mas nunca diminui?",
     "A idade."],
    ["O que é que tem muitos pés, mas não fica de pé?",
     "A centopéia."],
    ["Em que espécie de mato se senta o elefante quando chove?",
     "Mato molhado."],
    ["Quem é que bate em você, mas você não revida?",
     "O vento."],
    ["O que é o cúmulo do contra-senso?",
     "Na casa de saúde, só haver doentes."],
    ["Quando um jogador de futebol é um literato?",
     "Quando ele faz um gol de letra."],
    ["Onde é que a sereia Ariel vê filmes?",
     "No cinemaré."],
    ["O que é que atravessa a porta, mas nunca entra nem sai?",
     "A fechadura."],
    ["Por que os rios são considerados preguiçosos?",
     "Porque não saem dos seus leitos."],
    ["Qual é a diferença entre a galinha e o tecido?",
     "A galinha bota e o tecido desbota."],
    ["Era uma vez uma orquestra que não tocava nada. Qual o nome do filme?",
     "Os Intocáveis."],
    ["Quando é que um gaúcho é chamado de mineiro?",
     "Quando trabalha em uma mina."],
    ["O que deveríamos colocar embaixo da forca para que o condenado não morra?",
     "Cedilha!"],
    ["O que é que todos nós temos, mas quando precisamos vamos ao mercado comprar?",
     "Canela!"],
    ["O que você faz quando está nadando em um oceano e um crocodilo ataca?",
     "Você acorda."],
    ["Quem é que nasce no rio, vive no rio e morre no rio, mas só se molha se quiser?",
     "O carioca."],
    ["O que é que está no fim de tudo?",
     "A letra O."],
    ["Qual é o único monstro que é bonzinho?",
     "Good-zila."],
    ["O que é a única coisa que o vencedor da maratona perde?",
     "O fôlego."],
    ["O que acontece se você alimentar uma vaca com flores?",
     "Ela dará leite de rosas."],
    ["O que é que tem seis olhos, mas não pode ver?",
     "Três ratinhos cegos."],
    ["Afinal, o que é que sempre encontramos no final do túnel?",
     "A letra L."],
    ["Qual a palavra que tem duas letras e três sílabas?",
     "Arara!"],
    ["Por que os elefantes são encontrados na África?",
     "Porque eles são muito grandes para se esconderem."],
    ["Onde estavam todos os moradores da cidade durante o último apagão?",
     "No escuro."],
    ["Quando é que o cliente fica preso no banco?",
     "Quando fecha a conta-corrente."],
    ["Quem é que vai a todos os casamentos sem ser convidado?",
     "O padre."],
    ["Por que os dinossauros têm pescoços longos?",
     "Porque eles têm chulé."],
    ["Qual é a mulher que sempre aparece antes do nascer do sol?",
     "Aurora."],
    ["Por que os elefantes nunca esquecem?",
     "Porque ninguém nunca fala nada para eles."],
    ["Qual é o país que o criminoso não gosta de visitar?",
     "O Cana-dá."],
    ["Por que o leão é considerado o rei das selvas?",
     "Porque ele é macho; se fosse fêmea, seria rainha."],
    ["O que é um 'fuio'?",
     "É um 'buiaco na paiede'."],
    ["Sou enrolado, tenho a cabeça rachada e vivo apertado?",
     "Parafuso."],
    ["Por que o cachorro rói o osso?",
     "Porque ele não consegue engolir o osso inteiro."],
    ["Como é que você impede um elefante de passar pelo buraco de uma agulha?",
     "Dando um nó no rabo dele."],
    ["Em que lugar do mundo, o sono é mais profundo?",
     "No cemitério."],
    ["O que é que é menor que a boca de uma formiga?",
     "O que ela come."],
    ["Um é pouco, dois é bom, três é demais. O que são quatro e cinco?",
     "Nove."],
    ["Qual é a corrente que, por mais forte que seja, não consegue segurar o navio?",
     "A corrente marinha."],
    ["O que é que tem boca e um só dente e chama a atenção de muita gente?",
     "O sino."],
    ["Qual deve ser o comprimento máximo de uma perna?",
     "O suficiente para alcançar o chão."],
    ["O que é uma molécula?",
     "É uma 'Meninula Sapécula'."],
    ["Como se pode escrever a maior palavra do mundo?",
     "Com a caneta."],
    ["Que refeição é colocada sobre a água e não afunda?",
     "A bóia."],
    ["Qual o melhor castigo para um time de futebol que joga sujo?",
     "Levar um banho de gols."],
    ["Por que os elefantes usam tênis de corrida?",
     "Para fazer cooper, é claro."],
    ["Por que os elefantes são grandes e cinza?",
     "Porque, se eles fossem pequenos e amarelos, seriam canários."],
    ["O que é que tem na árvore, no futebol, no chapéu e na casa?",
     "Copa."],
    ["O que é que deixa um cachorro desconfiado?",
     "Uma pulga atrás da orelha."],
    ["Por que o "+ Donald +" espalhou açúcar no travesseiro?",
     "Porque ele queria ter doces sonhos."],
    ["Por que o "+ Goofy +" levou o pente dele ao dentista?",
     "Porque ele perdeu todos os dentes."],
    ["Por que o "+ Goofy +" usa a camisa no banho?",
     "Porque a etiqueta diz para lavar e usar."],
    ["Qual o país está na granja e a capital está no pomar?",
     "Peru, capital Lima."],
    ["Qual é o prato preferido da maioria das pessoas?",
     "O prato cheio."],
    ["Como você chama uma pessoa que leva outra para almoçar?",
     "Canibal."],
    ["O que é um ponto amarelo no canto da sala?",
     "É milho Santiago."],
    ["O que é um ponto preto dentro do tubo de ensaio?",
     "Uma blacktéria."],
    ["Por que o "+ Pluto +" dorme com uma casca de banana?",
     "Para pular da cama cedo."],
    ["Por que o rato usa tênis marrom?",
     "Porque o branco está lavando."],
    ["O que é que a dentadura tem em comum com as estrelas?",
     "Ela sai à noite."],
    ["O que é um pontinho preto no meio da estrada?",
     "É um calhamblack."],
    ["Por que o arqueólogo foi à falência?",
     "Porque sua carreira estava uma ruína."],
    ["Como é que você ficaria se atravessasse o Atlântico no Titanic?",
     "Ensopado."],
    ["O que é um pontinho amarelo no alto de um prédio?",
     "Um milho suicida."],
    ["Por que é que o milho suicida quer se suicidar?",
     "Porque o lugar onde ele mora é um bagaço."],
    ["O que é um pontinho vermelho lá embaixo do prédio onde está o milho suicida?",
     "Um milho bombeiro para salvar o milho suicida..."],
    ["Qual a cor mais barulhenta?",
     "A corneta."],
    ["O que é que a banana suicida falou?",
     "Macacos me mordam!!!"],
    ["Qual o tipo de alimento de que o político mais gosta?",
     "As massas."],
    ["O que a chaminé grande falou para a chaminé pequena?",
     "Você é muito jovem para fumar."],
    ["O que é um pontinho vermelho no pântano?",
     "É um jacared."],
    ["O que é um pontinho azul no gramado?",
     "Uma formiguinha de calça jeans."],
    ["O que é um ponto brilhante no gramado?",
     "Uma formiguinha de aparelho nos dentes."],
    ["O que é um pontinho marrom na pré-história?",
     "Um browntossauro."],
    ["Como se chama um dinossauro que nunca se atrasa?",
     "Prontossauro."],
    ["O que é um pontinho vermelho num pedacinho de neve?",
     "Uma miniatura da bandeira do Japão."],
    ["O que é um pontinho dourado no gramado?",
     "É uma formiguinha brincando de Jaspion."],
    ["Qual e a comida que liga e desliga ?",
     "O StrogON-OFF."],
    ["Por que o livro de matemática ficou triste?",
     "Porque ele tinha muitos problemas."],
    ["O que o tomate foi fazer no banco?",
     "Foi tirar extrato"],
    ["Como se faz para transformar um giz numa cobra?",
     "É só colocar o giz num copo de água. Aí o 'gizbóia'"],
    ["Qual é o cúmulo da rapidez?",
     "Fechar a gaveta, trancar e jogar a chave dentro."],
    ["Qual é o cúmulo do egoísmo?",
     "Não vou contar, só eu que sei."],
    ["Qual é o cúmulo da revolta?",
     "Morar sozinho, fugir de casa e deixar um bilhete dizendo que não volta mais."],
    ["Qual é o cúmulo do exagero?",
     "Passar manteiga no Pão de Açúcar."],
    ["Qual é o cúmulo do arrependimento do carrasco?",
     "Pois é, sempre que enforco alguém me dá um nó na garganta..."],
    ["Qual é o cúmulo da visão?",
     "Derrubar dez faixas-pretas com um golpe de vista."],
    ["Qual é o cúmulo da sorte?",
     "Ser atropelado por uma ambulância."],
    ["Qual é o cúmulo da maldade?",
     "Colocar tachinhas na cadeira elétrica."],
    ["Qual é o cúmulo da burrice?",
     "Ser reprovado no exame de fezes."],
    ["Qual é o cúmulo da economia?",
     "Usar o papel higiênico dos dois lados."],
    ["Qual é o cúmulo do esquecimento?",
     "Ih! Esqueci!"],
    ["Qual é o cúmulo da sede?",
     "Tomar um ônibus."],
    ["O que que faz ABC...Slurp...DEF...Slurp?",
     "Alguém tomando sopa de letrinhas."],
    ["O que é que é verde e fica saltando sem parar em cima do sofá?",
     "Uma ervilha que saiu do castigo."],
    ["O que é que o tomate foi fazer no banco?",
     "Tirar extrato."],
    ["Por que o médico que trabalha à noite se veste de verde?",
     "Porque ele está de plantão."],
    ["O que é que é branco com pontinhos pretos e vermelhos?",
     "Um dálmata com catapora."],
    ["O que a galinha foi fazer na igreja?",
     "Assistir à missa do galo."],
    ["O que é o que é? Cai em pé e corre deitado?",
     "Não é a chuva não! É uma minhoca de pára-quedas."],
    ["Por que é que não é bom guardar o quibe no freezer?",
     "Porque lá dentro ele esfirra."],
    ["O que o advogado do frango foi fazer na delegacia?",
     "Foi soltar a franga"],
    ["Por que o galo canta de olhos fechados?",
     "Porque ele já sabe a música de cor."],
    ["Um peixe foi jogado de cima de um prédio de vinte andares. Que peixe era esse?",
     "Um atum, porque quando ele caiu fez: Aaaaaaaaaaaa Tum!"],
    ["Como se faz omelete de chocolate?",
     "Com ovos de Páscoa."],
    ["Para que servem óculos verdes?",
     "Para verde perto."],
    ["Para que servem óculos vermelhos?",
     "Para 'vermelhor'."],
    ["O que é verde por fora e amarela por dentro?",
     "Uma banana disfarçada de pepino."],
    ["Qual é a parte do carro que se originou no Antigo Egito?",
     "Os faraóis."],
    ["Como é que a bruxa sai na chuva?",
     "De rodo."],
    ["Por que o cachorro entrou na igreja?",
     "Porque ele é um cão pastor."],
    ["Quem é o pai do volante?",
     "O painel."],
    ["Como chamamos uma mulher que visitou uma plantação de uva?",
     "Viúva."],
    ["O que o amendoim falou para o elefante?",
     "Nada, o amendoim não fala."],
    ["O que os elefantes falam quando se esbarram?",
     "Mundo pequeno esse, né?"],
    ["O que o caixa falou para a registradora?",
     "Estou contando com você."],
    ["Por que o caminhão de frigorífico não sobe a ladeira?",
     "Porque 'elingüiça'."],
    ["Qual é a comida que liga e desliga?",
     "É o strogON-OFF."],
    ["O que a vaca foi fazer na Argentina?",
     "Foi ver o Boi nos Ares."],
    ["Qual é o peixe mais salgado que existe?",
     "O sal-mão."],
    ["O que é um cão indeciso?",
     "É um 'cão-fuso'."],
    ["Sabe por que o italiano não come churrasco?",
     "Porque o macarrão não cabe no espeto."],
    ["Qual é o cúmulo da rapidez?",
     "Ir ao enterro de um parente e ainda encontrá-lo vivo."],
    ["Qual é o cúmulo do azar?",
     "Ser atropelado por um carro funerário."],
    ["Por que o jacaré tomou o cartão de crédito do jacarezinho?",
     "Porque o jacarezinho gastou muito e mandou o jacarepaguá."],
    ["Qual é o cúmulo da burrice?",
     "Olhar pelo buraco da fechadura numa porta de vidro."],
    ["Qual é o cúmulo da confiança?",
     "Jogar par-ou-ímpar pelo telefone?"],
    ["Qual é o cúmulo da paciência?",
     "Esvaziar uma piscina com conta-gotas."],
    ["Qual é o cúmulo da traição?",
     "Suicidar-se com uma punhalada nas costas."],
    ["O que uma nuvem disse pra outra?",
     "'Nu-vem' não."],
    ["Qual é o cúmulo da moleza?",
     "Correr sozinho e chegar em segundo."],
    ["Por que o jacaré tirou o jacarezinho da escola?",
     "Porque ele 'reptil'."],
    ["Qual é o fim da picada?",
     "Quando o mosquito vai embora."],
    ["O que o pára-quedas disse para o pára-quedista?",
     "Tô contigo e não abro."],
    ["Qual é a cor mais barulhenta?",
     "A corneta."],
    ["O que é um pontinho amarelo no céu?",
     "Um yellowcóptero."],
    ]
# MovieHeal.py
MovieHealLaughterMisses = ("hmm","hehe","ah","Rá rá")
MovieHealLaughterHits1= ("Ah ah ah","Ri, ri, ri","Ré, ré","Ah, ah")
MovieHealLaughterHits2= ("AH HAH HAH!","HO HO HO!","RÁ RÁ RÁ!")

# MovieSOS.py
MovieSOSCallHelp = "%s SOCORRO!"
MovieSOSWhisperHelp = "%s precisa de ajuda na batalha!"
MovieSOSObserverHelp = "SOCORRO!"

# MovieSuitAttacks.py
MovieSuitCancelled = "CANCELADO\nCANCELADO\nCANCELADO"

# RewardPanel.py
RewardPanelToonTasks = "Tarefas Toon"
RewardPanelItems = "Itens recuperados"
RewardPanelMissedItems = "Itens não-recuperados"
RewardPanelQuestLabel = "Buscar %s"
RewardPanelCongratsStrings = ["É isso aí!", "Parabéns!", "Uau!",
                              "Legal!", "Caraca!", "Toon-tástico!"]
RewardPanelNewGag = "Nova piada %(gagName)s para %(avName)s!"

# Cheesy effect descriptions: (short desc, sentence desc)
CheesyEffectDescriptions = [
    ("Toon normal", "você ficará normal"),
    ("Cabeção", "você ficará com uma cabeça grande"),
    ("Cabecinha", "você ficará com uma cabeça pequena"),
    ("Pernonas", "você ficará com pernas grandes"),
    ("Perninhas", "você ficará com pernas pequenas"),
    ("Toonzão", "você ficará um pouco maior"),
    ("Toonzinho", "você ficará um pouco menor"),
    ("Quadro reto", "você ficará em duas dimensões"),
    ("Perfil reto", "você ficará em duas dimensões"),
    ("Transparente", "você ficará transparente"),
    ("Sem cor", "você ficará sem cor"),
    ("Toon invisível", "você ficará invisível"),
    ]
CheesyEffectIndefinite = "Até que escolha outro efeito, %(effectName)s%(whileIn)s."
CheesyEffectMinutes = "Nos próximos %(time)s minutos, %(effectName)s%(whileIn)s."
CheesyEffectHours = "Nas próximas %(time)s horas, %(effectName)s%(whileIn)s."
CheesyEffectDays = "Nos próximos %(time)s dias, %(effectName)s%(whileIn)s."
CheesyEffectWhileYouAreIn = " enquanto estiver %s"
CheesyEffectExceptIn = ", exceto em %s"


# SuitBattleGlobals.py
SuitFlunky = "Puxa-saco"
SuitPencilPusher = "Rato de Escritório"
SuitYesman = "Vaquinha de Presépio"
SuitMicromanager = "Micro\4empresário"
SuitDownsizer = "Facão"
SuitHeadHunter = "Caça-\4talentos"
SuitCorporateRaider = "Aventureiro Corporativo"
SuitTheBigCheese = "O Rei da Cocada Preta"
SuitColdCaller = "Rei da Incerta"
SuitTelemarketer = "Operador de Tele\4marketing"
SuitNameDropper = "Dr. Sabe-com-\4quem-está-\4falando"
SuitGladHander = "Amigo-da-Onça"
SuitMoverShaker = "Agitador"
SuitTwoFace = "Duas Caras"
SuitTheMingler = "Amizade Fácil"
SuitMrHollywood = "Dr. Celebridade"
SuitShortChange = "Farsante"
SuitPennyPincher = "Mão-de-vaca"
SuitTightwad = "Pão-duro"
SuitBeanCounter = "Conta-\4moedinha"
SuitNumberCruncher = "Destruidor de Números"
SuitMoneyBags = "Sacos de Dinheiro"
SuitLoanShark = "Agiota"
SuitRobberBaron = "Barão Ladrão"
SuitBottomFeeder = "Comensal"
SuitBloodsucker = "Sanguessuga"
SuitDoubleTalker = "Duplo Sentido"
SuitAmbulanceChaser = "Perseguidor de Ambulâncias"
SuitBackStabber = "Golpe Sujo"
SuitSpinDoctor = "Relações Públicas"
SuitLegalEagle = "Macaco velho"
SuitBigWig = "Figurão"

# Singular versions (indefinite article)
SuitFlunkyS = "um Puxa-saco"
SuitPencilPusherS = "um Rato de Escritório"
SuitYesmanS = "uma Vaquinha de Presépio"
SuitMicromanagerS = "um Micro\4empresário"
SuitDownsizerS = "um Facão"
SuitHeadHunterS = "um Caça-talentos"
SuitCorporateRaiderS = "um Aventureiro Corporativo"
SuitTheBigCheeseS = "um Rei da Cocada Preta"
SuitColdCallerS = "um Rei da Incerta"
SuitTelemarketerS = "um Operador de Telemarketing"
SuitNameDropperS = "um Dr. Sabe-com-\4quem-está-\4falando"
SuitGladHanderS = "um Amigo-da-Onça"
SuitMoverShakerS = "um Agitador"
SuitTwoFaceS = "um Duas Caras"
SuitTheMinglerS = "um Amizade Fácil"
SuitMrHollywoodS = "um Dr. Celebridade"
SuitShortChangeS = "um Farsante"
SuitPennyPincherS = "um Mão-de-vaca"
SuitTightwadS = "um Pão-duro"
SuitBeanCounterS = "um Conta-\4moedinha"
SuitNumberCruncherS = "um Destruidor de Números"
SuitMoneyBagsS = "um Sacos de Dinheiro"
SuitLoanSharkS = "um Agiota"
SuitRobberBaronS = "um Barão Ladrão"
SuitBottomFeederS = "um Comensal"
SuitBloodsuckerS = "um Sanguessuga"
SuitDoubleTalkerS = "um Duplo Sentido"
SuitAmbulanceChaserS = "um Perseguidor de Ambulâncias"
SuitBackStabberS = "um Golpe Sujo"
SuitSpinDoctorS = "um Relações Públicas"
SuitLegalEagleS = "um Macaco velho"
SuitBigWigS = "um Figurão"

# Plural versions
SuitFlunkyP = "Puxa-sacos"
SuitPencilPusherP = "Ratos de Escritório"
SuitYesmanP = "Vaquinhas de Presépio"
SuitMicromanagerP = "Micro\4empresários"
SuitDownsizerP = "Facões"
SuitHeadHunterP = "Caça-\4talentos"
SuitCorporateRaiderP = "Aventureiros Corporativos"
SuitTheBigCheeseP = "Os Reis da Cocada Preta"
SuitColdCallerP = "Reis da Incerta"
SuitTelemarketerP = "Operadores de Tele\4marketing"
SuitNameDropperP = "Drs. Sabe-com-\4quem-está-\4falando"
SuitGladHanderP = "Amigos-da-Onça"
SuitMoverShakerP = "Agitadores"
SuitTwoFaceP = "Duas Caras"
SuitTheMinglerP = "Amizades Fáceis"
SuitMrHollywoodP = "Drs. Celebridade"
SuitShortChangeP = "Farsantes"
SuitPennyPincherP = "Mãos-de-vaca"
SuitTightwadP = "Pães-duros"
SuitBeanCounterP = "Conta-\4moedinhas"
SuitNumberCruncherP = "Destruidores de Números"
SuitMoneyBagsP = "Sacos de Dinheiro"
SuitLoanSharkP = "Agiotas"
SuitRobberBaronP = "Barões Ladrões"
SuitBottomFeederP = "Comensais"
SuitBloodsuckerP = "Sanguessugas"
SuitDoubleTalkerP = "Duplos Sentidos"
SuitAmbulanceChaserP = "Perseguidores de Ambulâncias"
SuitBackStabberP = "Golpes Sujos"
SuitSpinDoctorP = "Relações Públicas"
SuitLegalEagleP = "Macacos velhos"
SuitBigWigP = "Figurões"

SuitFaceOffDefaultTaunts = ['Buuuuu!']

# SuitDialog.py
SuitFaceoffTaunts = {
    'b':  ["Você tem uma doação para mim?",
           "Você vai detestar perder a parada.",
           "Você não vai ter salvação.",
           "Sou \"A Positivo\", portanto, vou ganhar.",
           "\"O\"não seja tão \"Negativo\".",
           "É uma surpresa você ter me achado; não tenho parada.",
           "Vou precisar fazer uma rápida contagem em você.",
           "Em breve, você vai precisar comer biscoito e tomar um suco.",
           "Quando eu terminar, você vai precisar dar uma descansada.",
           "Só vai doer um pouquinho.",
           "Vou deixar você tonto.",
           "Na hora certa, só estou um pouquinho abaixo.",
           ],
    'm':  ["Você não sabe com quem está se metendo.",
           "Nunca se meteu com alguém da minha turma?",
           "Isso é bom, quando um não quer dois não se misturam.",
           "Vamos fazer amizade.",
           "Parece um bom lugar para confraternizar.",
           "Não é confortável?",
           "Vocês estão se unindo com a derrota.",
           "Vou me juntar a você no negócio.",
           "Tem certeza de que está pronto para a união?",
           ],
    'ms': ["Prepare-se para uma sacudida.",
           "Melhor você sair do caminho.",
           "Olha a frente.",
           "Acho que é minha vez.",
           "Isso deve agitar você.",
           "Prepare-se para ser movido.",
           "Estou pronto para dar o meu passo.",
           "Cuidado Toon, você está em terreno instável.",
           "Este deve ser um momento de movimento.",
           "Sinto um impulso de derrotar você.",
           "Você ainda está tremendo?",
           ],
    'hh': ["Estou na sua frente nesta caçada.",
           "Você está caçando encrenca da grande.",
           "A sua cabeça está na mira do caçador de cabeças.",
           "Que bom, estava atrás de você.",
           "Vou perseguir você por isto.",
           "Fique de olho!",
           "Parece que você está perdido nesta caçada.",
           "Está indo pela mesma trilha que eu?",
           "Um troféu perfeito para a minha coleção.",
           "Você vai ter uma dor de cabeça...",
           "Não perca o rumo comigo.",
           ],
    'tbc': ["Cuidado, vou adoçar você.",
            "Pode me chamar de Coquinho.",
            "Tem certeza? Às vezes ajo como um Cãocadão.",
            "Finalmente, estava achando que você ia me deixar aqui à mercê das formigas.",
            "Vou queimar o seu coco.",
            "Não acha que eu sou um docinho de coco?",
            "Você vai virar cocada comigo.",
            "As pessoas me acham durão.",
            "Cuidado, eu sei a sua data de validade.",
            "Cuidado, sou uma fera neste jogo.",
            "Bater você vai ser mole.",
            ],
    'cr': ["ATAQUE!",
           "Você não é adequado para a minha corporação.",
           "Prepare-se para ser atacado.",
           "Parece que você está preparado para assumir o comando da aventura.",
           "Esta roupa não é apropriada para ambientes corporativos.",
           "Você parece estar bem vulnerável.",
           "É hora de botar os bens em seu nome.",
           "Estou em uma cruzada a favor da eliminação dos Toons.",
           "Você fica sem defesa contra as minhas idéias.",
           "Relaxa, você vai ver que vai ser melhor assim.",
           ],
    'mh': ["Está preparado para a minha tomada?",
           "Luz, câmera, ação!",
           "Vai começar a rodar.",
           "Hoje o papel do Toon derrotado será feito por - VOCÊ!",
           "Esta cena vai ser cortada.",
           "Já sei qual vai ser a minha motivação para esta cena.",
           "Está preparado para a sua cena final?",
           "Estou pronto para passar os seus créditos no final.",
           "Eu disse para você não me chamar.",
           "O show tem que continuar.",
           "Não tem negócio igual a este!",
           "Espero que você não se esqueça das suas falas.",
           ],
    'nc': ["Parece que o seu número está em alta.",
           "Prefere ser destruído com ou sem cobertura crocante?",
           "Agora, você está destruído.",
           "Já está na hora de dizimar todos estes números?",
           "Vamos fazer uma matemática.",
           "Onde você gostaria de fazer uma subtração hoje?",
           "Você me deu uma coisa para calcular!",
           "Não vai ser fácil.",
           "Vai em frente, pegue um número qualquer.",
           "Vou destruir você com os meus cálculos.",
           ],
    'ls': ["É hora de recolher o seu empréstimo.",
           "Você tem estado na pior.",
           "O empréstimo agora tem que ser pago.",
           "Hora de liquidar a dívida.",
           "Bom, você queria um adiantamento e conseguiu.",
           "Você terá que pagar por isso.",
           "É hora de devolver o que pegou.",
           "Pode me dar uma mãozinha?",
           "Ainda bem que você está aqui, isto está uma loucura.",
           "Podemos fazer um lanchinho?",
           "Deixe-me dar um tasco.",
           ],
    'mb': ["Está na hora de trazer os sacos.",
           "Posso ensacar isso.",
           "Papel ou plástico?",
           "Você tem o tíquete da bagagem?",
           "Lembre-se de que o dinheiro não vai fazer você feliz.",
           "Cuidado, tenho muita bagagem.",
           "Você está prestes a ficar no vermelho.",
           "O dinheiro vai fazer o seu mundo girar.",
           "Sou muito rico para o seu bico.",
           "Você nunca poderá ter tanto dinheiro!",
           ],
    'rb': ["Você foi roubado.",
           "Vou roubar esta vitória de você.",
           "Sou um chato de galochas!",
           "Espero que você ainda possa sorrir para o barão.",
           "Você terá que denunciar este roubo.",
           "Mãos ao alto.",
           "Sou um adversário nobre.",
           "Vou levar tudo o que você tem.",
           "Você pode chamar isto de roubo no bairro.",
           "Você já devia saber que não se fala com estranhos.",
           ],
    'bs': ["Nunca vire as costas para mim.",
           "Você não vai voltar mesmo.",
           "Retire o que disse, ou então...!",
           "Sou bom em cortar custos.",
           "Tenho as costas quentes.",
           "Agora, não dá mais para voltar atrás.",
           "Sou o melhor e posso provar.",
           "Ôôô, parado aí, Toon.",
           "Deixe-me dar cobertura a você.",
           "Você vai ter uma dor de cabeça infernal.",
           "Tenho um golpe perfeito.",
           ],
    'bw': ["Quero sair bem na foto.",
           "Você me arrepia os cabelos.",
           "Posso deixar assim para sempre, se quiser.",
           "Parece que você vai ficar com a cara boa.",
           "Você não consegue encarar a verdade.",
           "Acho que é sua vez de mudar de cor.",
           "Estou tão feliz que você chegou na hora de mudar o visual.",
           "Você está encrencado.",
           "Vou deixar você doidão.",
           "Sou um baita de um Toonzinho.",
           ],
    'le': ["Cuidado, sou legal mas nem tanto.",
           "Eu pulo de galho em galho, mas alguns quebram.",
           "Vou fazer a lei chegar até você.",
           "Você já devia saber que tenho instintos criminosos.",
           "Vou fazer você ter pesadelos jurídicos.",
           "Você não vai ganhar esta batalha.",
           "Isto é tão divertido que deveria ser proibido por lei.",
           "Legalmente falando, você é muito pequeno para lutar comigo.",
           "Não há limites para os meus botes.",
           "Chamo isso de prisão de cidadão.",
           ],
    'sd': ["Você nunca saberá quando vou parar.",
           "Deixe-me levar você para uma volta.",
           "Vida social é comigo mesmo.",
           "Vou colocar você em um agito.",
           "Você parece precisar de animação.",
           "A festa está rolando, mas Toons não entram.",
           "Você não vai gostar do meu pitaco nisto.",
           "Você vai ficar fora de controle.",
           "Você se importa de dar umas voltinhas comigo?",
           "Tenho minha própria teoria sobre o assunto.",
           ],
    'f': ["Vou falar sobre você com o chefe!",
          "Posso ser apenas um puxa-saco, mas sou demais.",
          "Estou usando você para subir os vários degraus dentro da empresa.",
          "Você não vai gostar do jeito como eu trabalho.",
          "O chefe está contando comigo para deter você.",
          "Você vai ficar bonito no meu currículo.",
          "Você terá que passar por cima de mim primeiro.",
          "Vamos ver como você classifica meu desempenho funcional.",
          "Eu me sobressaio na eliminação de Toons.",
          "Você jamais conhecerá o meu chefe.",
          "Vou mandar você de volta para o Pátio.",
          ],
    'p':  ["Eu vou apagar você!",
           "Ei, você não pode ficar mandando em mim.",
           "Sou o número 2!",
           "Vou cortar você.",
           "Vou ter que me fazer mais claro.",
           "Deixe-me ir direto ao ponto.",
           "Rápido, eu fico irritado com facilidade.",
           "Odeio quando as coisas ficam bobas.",
           "Então, você quer arriscar a própria sorte?",
           "Você me passou o lápis?",
           "Cuidado, posso deixar uma marca.",
           ],
    'ym': ["Concordo com tudo.",
           "Não sei o que significa não.",
           "Quer me conhecer? Eu digo sim sempre.",
           "Você precisa de uma força positiva.",
           "Vou deixar uma impressão positiva.",
           "Ainda não me enganei.",
           "Sim, estou pronto para você.",
           "Acha mesmo que quer fazer isto?",
           "Você certamente terminará com saldo positivo nessa.",
           "Confirmando a hora da sua reunião.",
           "Não aceito não como resposta.",
           ],
    'mm': ["Vou entrar neste negócio.",
           "Às vezes, os piores venenos vêm em pequenos frascos.",
           "Nenhum trabalho é insignificante para mim.",
           "Quero o trabalho feito direito, por isso eu mesmo o faço.",
           "Você precisa de alguém para gerenciar os seus bens.",
           "Que bom, um projeto.",
           "Bem, você conseguiu me achar.",
           "Acho que você precisa de alguma organização.",
           "Vou cuidar de você em dois tempos.",
           "Estou observando tudo que você faz.",
           "Tem certeza de que deseja fazer isto?",
           "Vamos fazer da minha maneira.",
           "Vou estar na sua cola.",
           "Posso ser bem intimidador.",
           ],
    'ds': ["Você está caindo no meu golpe!",
           "Você vai encolher com meu ataque.",
           "Espere retornos minúsculos.",
           "Você vai deixar de existir.",
           "Não me peça nenhuma dispensa.",
           "Vou precisar fazer alguns cortes.",
           "As coisas parecem estar despedaçadas para você.",
           "Por que você parece tão machucado?",
           ],
    'cc': ["Surpreso de saber de mim?",
           "Você ligou?",
           "Está pronto para aceitar as minhas tarifas?",
           "Este aqui sempre recolhe alguma coisa.",
           "Eu opero bem as linhas.",
           "Espere um segundo, estou aqui.",
           "Estava esperando a minha ligação?",
           "Estava torcendo para você atender a minha ligação.",
           "Vou deixar uma sensação tocante.",
           "Sempre faço ligações diretas.",
           "Cara, tem boi na linha.",
           "Esta ligação terá um custo para você.",
           "Você tem um pepino nesta linha.",
           ],
    'tm': ["Meu plano é tornar isto inconveniente para você.",
           "Posso incluir você em um seguro?",
           "Você não deveria ter me atendido.",
           "Você não vai conseguir se livrar de mim agora.",
           "Tá chateado? Que bom.",
           "Estava pensando em atropelar você.",
           "Vou inverter as cobranças desta ligação.",
           "Tenho alguns itens bem caros para você hoje.",
           "Se deu mal, eu faço ligações locais.",
           "Estou preparado para fechar este negócio rapidinho.",
           "Vou usar um monte de recursos seus.",
           ],
    'nd': ["Na minha opinião, seu nome está na lama.",
           "Espero que não se importe se eu jogar o seu nome na boca das matildes.",
           "A gente já não se conhece?",
           "Depressa, vou almoçar com o Dr. Celebridade.",
           "Eu falei que conheço o Amizade Fácil?",
           "Você nunca vai me esquecer.",
           "Conheço todas as pessoas certas para detonar você.",
           "Acho que vou passar aí.",
           "Estou a fim de detonar alguns Toons.",
           "Eu te disse, detonei.",
           ],
    'gh': ["Diz aí, Toon.",
           "O bicho vai pegar.",
           "Vou gostar disso.",
           "Você vai acabar vendo as minhas garras.",
           "Vamos assinar embaixo.",
           "Vamos direto ao que interessa.",
           "Não cutuca a onça com vara curta, ou você vai acabar mal.",
           "Você vai acabar gostando da minha pinta.",
           "Olha que eu viro uma onça.",
           "Você não vai escapar das minhas garras.",
           "Você quer que eu safe a onça?",
           "Se ficar o bicho come, se correr o bicho pega.",
           "As marcas das minhas unhas afiadas estão na parede.",
           ],
    'sc': ["Vamos logo acabar com esta farsa.",
           "Você está prestes a ficar no vermelho.",
           "Você está prestes a pagar taxas abusivas.",
           "O projeto vai ser de fachada.",
           "Esta fraude vai ser moleza.",
           "Logo, logo você vai cair na minha arapuca.",
           "Vamos embromar um pouquinho.",
           "Veio cedo para ver o meu truque, né?",
           "Tenho pavio curto com Toons.",
           "Logo vou armar minha armadilha para você.",
           "Você está prestes a cair na minha lábia.",
           ],
    'pp': ["Meu aperto de mão é forte.",
           "Minha mão é de ferro.",
           "Você não quer que a vaca vá pro brejo, ou quer?",
           "Seu sorriso vai ficar pálido como leite.",
           "Tenho um lugar para você, mas não pense que sou mão-aberta.",
           "Deixe e pagar na mesma moeda.",
           "Dou tchau com a mão fechada.",
           "Vou provar que você não está sonhando.",
           "Cabeças vão rolar, e eu vou ganhar.",
           "Dou uma moedinha pelas suas piadas.",
           ],
    'tw': ["Vamos ter que dar duro.",
           "É o Pão-duro.",
           "Vou ter que cortar a sua verba.",
           "É a melhor oferta que você pode fazer?",
           "Vamos logo. Tempo é dinheiro.",
           "Você vai descobrir como dou duro.",
           "Você está na corda bamba.",
           "Prepare-se para a dureza.",
           "Você não conhece o pão que o diabo amassou.",
           "Vou ter que apertar o cinto.",
           "Vou fazer um rombo no seu orçamento.",
           ],
    'bc': ["Adoro subtrair Toons.",
           "Pode contar comigo para fazer você pagar.",
           "O negócio é contar as moedinhas.",
           "Contar é comigo mesmo.",
           "Sou um contador de balinhas.",
           "Sua planilha de gastos está excedendo o limite.",
           "É hora de fazer uma auditoria.",
           "Vamos entrar no meu escritório.",
           "Onde você estava? Eu contava com você.",
           "Estou esperando por você há um milhão de horas.",
           "Você não vale um níquel.",
           ],
    'bf': ["Parece que você chegou na hora do lanche.",
           "Estou pronto para o banquete.",
           "Sou um comedor de Toons.",
           "Êba, hora do almoço.",
           "Na hora certa! Preciso de um lanchinho.",
           "Gostaria de alguma opinião sobre o meu desempenho.",
           "Vamos falar sobre o que interessa.",
           "Você vai descobrir que tenho um talento imensurável.",
           "Bom, preciso de um pequeno estímulo.",
           "Adoraria se você almoçasse comigo.",
           ],
    'tf': ["Está na hora de nosso duelo!",
           "Melhor encarar a derrota.",
           "Prepare-se para enfrentar o seu pior pesadelo!",
           "Encare os fatos: eu sou melhor que você.",
           "Duas cabeças pensam melhor que uma.",
           "Se um não quer, dois não brigam. Quer brigar?",
           "Você está duplamente encrencado.",
           "Qual face você quer que o derrote?",
           "Eu sou demais para você.",
           "Você não sabe com quem está se metendo.",
           "Você está preparado para encarar sua derrota?",
           ],
    'dt': ["Você terá trabalho em dobro comigo.",
           "Veja se você consegue enfrentar meu golpe duplo.",
           "Trabalho para um ARMÁRIO 4x4 muito mau.",
           "Está na hora de um golpe duplo.",
           "Meu plano é ter duas FONTES.",
           "Você não vai gostar do meu jogo duplo.",
           "Talvez queira pensar duas vezes nisso.",
           "Prepare-se para uma LIGAÇÃO dupla.",
           "Talvez queira aplicar uma dose dupla contra mim.",
           "Duplas, alguém??",
           ],
    'ac': ["Eu vou botar você prá correr desta cidade!",
           "Está ouvindo uma sirene?",
           "Vou gostar disso.",
           "Adoro a emoção da perseguição.",
           "Vou dar um passa-fora.",
           "Você tem seguro?",
           "Espero que tenha trazido uma maca.",
           "Duvido que você possa comigo.",
           "É só ralação a partir daqui.",
           "Em breve você vai precisar de uma ambulância.",
           "Não é piada.",
           "Vou passar a parada para você.",
           ]
    }
