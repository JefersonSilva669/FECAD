import sys, re

extra_q = '''
fcKB['Matemática'].push(
    { q: 'O que é um número primo?', a: 'Número maior que 1 que tem apenas dois divisores: 1 e ele mesmo.' },
    { q: 'O que é uma progressão aritmética (PA)?', a: 'Sequência numérica em que cada termo é o anterior somado a uma constante.' },
    { q: 'Qual a fórmula da soma dos termos de uma PA?', a: 'Sn = (a1 + an) * n / 2' },
    { q: 'O que é uma progressão geométrica (PG)?', a: 'Sequência onde cada termo é o anterior multiplicado por constante.' },
    { q: 'O que é um polinômio?', a: 'Expressão algébrica formada pela soma de monômios.' },
    { q: 'Como calcular a área de um círculo?', a: 'A = π * r²' },
    { q: 'O que é um ângulo obtuso?', a: 'Ângulo cuja medida é maior que 90° e menor que 180°.' },
    { q: 'O que é a mediana na estatística?', a: 'Valor que divide conjunto de dados ordenados exatamente ao meio.' }
);
fcKB['Física'].push(
    { q: 'O que é aceleração da gravidade?', a: 'Na Terra é aprox 9,8 m/s².' },
    { q: 'Princípio de Arquimedes?', a: 'Empuxo: num fluido sofre força para cima igual ao peso do fluido deslocado.' },
    { q: 'Primeira lei da termodinâmica?', a: 'Energia não pode ser criada nem destruída.' },
    { q: 'Efeito Doppler?', a: 'Alteração da frequência percebida com movimento relativo da fonte.' },
    { q: 'Velocidade da luz?', a: 'Aproximadamente 300.000 km/s.' },
    { q: 'Circuito em série?', a: 'A corrente é a mesma em todos os componentes.' },
    { q: 'Campo magnético?', a: 'Região onde cargas ou ímãs sofrem força magnética.' },
    { q: 'Trabalho de força constante?', a: 'Trabalho = Força * deslocamento * cos(ângulo).' },
    { q: 'Segunda Lei de Newton?', a: 'F = m * a (Força = massa * aceleração).' }
);
fcKB['Química'].push(
    { q: 'Isótopo?', a: 'Átomos do mesmo elemento com diferentes massas (nêutrons diferentes).' },
    { q: 'Mistura homogênea?', a: 'Apresenta uma única fase visual.' },
    { q: 'Número de Avogadro?', a: '6,022 × 10²³ partículas num mol.' },
    { q: 'Tabela periódica?', a: 'Elementos em ordem crescente de número atômico.' },
    { q: 'Gás mais abundante na atmosfera?', a: 'Nitrogênio (N2), cerca de 78%.' },
    { q: 'Oxidação?', a: 'Quando um átomo perde elétrons.' },
    { q: 'Hidrocarbonetos?', a: 'Compostos de carbono e hidrogênio.' },
    { q: 'Ponto de ebulição?', a: 'Temperatura da passagem líquido para gasoso onde pressões se igualam.' },
    { q: 'Ácido de Arrhenius?', a: 'Libera H+ em solução.' },
    { q: 'O que é uma ligação metálica?', a: 'Nuvem de elétrons livres entre cátions.' }
);
fcKB['Biologia'].push(
    { q: 'Bases nitrogenadas do DNA?', a: 'A, T, C, G.' },
    { q: 'Meiose?', a: 'Divisão que reduz à metade o número de cromossomos (gametas).' },
    { q: 'Função da mitocôndria?', a: 'Respiração celular (ATP).' },
    { q: 'Autótrofos?', a: 'Produzem próprio alimento.' },
    { q: 'Função dos ribossomos?', a: 'Síntese de proteínas.' },
    { q: 'Sistema nervoso central?', a: 'Encéfalo e medula espinhal.' },
    { q: 'Anticorpos?', a: 'Proteínas neutralizadoras de antígenos.' },
    { q: 'Simbiose?', a: 'Relação estreita de longo prazo entre duas espécies.' },
    { q: 'Clorofila?', a: 'Pigmento verde para fotossíntese.' }
);
fcKB['Gramática da Língua Portuguesa'].push(
    { q: 'Verbo transitivo direto?', a: 'Exige complemento sem preposição obrigatória.' },
    { q: 'Conjunção adversativa?', a: 'Exprime oposição (ex: mas, porém).' },
    { q: 'Pronome relativo?', a: 'Retoma termo anterior (ex: que, onde).' },
    { q: 'Onde vs aonde', a: 'Onde: lugar fixo. Aonde: indica movimento.' },
    { q: 'Pleonasmo?', a: 'Repetição de ideia (subir pra cima).' },
    { q: 'Adjetivo?', a: 'Caracteriza substantivo.' },
    { q: 'Parônimas?', a: 'Parecidas na grafia/pronúncia, significados diferentes.' },
    { q: 'Predicativo do sujeito?', a: 'Característica do sujeito ligada por verbo de ligação.' },
    { q: 'Sintaxe?', a: 'Estuda disposição e relações na frase.' },
    { q: 'O que é oxítona?', a: 'Palavra com a última sílaba tônica.' }
);
fcKB['Literatura Lusófona'].push(
    { q: 'Machado de Assis?', a: 'Fundador ABL, autor de Dom Casmurro.' },
    { q: 'Romantismo no BR?', a: 'Indianismo, nacionalismo, idealização.' },
    { q: 'Semana Arte 1922?', a: 'Início do Modernismo no Brasil.' },
    { q: 'Vidas Secas?', a: 'Graciliano Ramos, regionalismo 1930.' },
    { q: 'Os Lusíadas (Camoes)?', a: 'Exalta as conquistas navais portuguesas.' },
    { q: 'Parnasianismo?', a: 'Arte pela arte, Olavo Bilac.' },
    { q: 'Naturalismo?', a: 'Análise do homem biológico e social (O Cortiço).' },
    { q: 'Clarice Lispector?', a: 'Modernista, fluxo de consciência.' },
    { q: 'Quinhentismo?', a: 'Primeiros textos pós descobrimento (catequese e cartas).' },
    { q: 'Arcadismo?', a: 'Séc XVIII, vida bucólica e fugere urbem.' }
);
fcKB['Leitura e produção de textos'].push(
    { q: 'Dissertação argumentativa?', a: 'Defende ponto de vista com argumentos.' },
    { q: 'Denotação x Conotação?', a: 'Literal vs Figurado.' },
    { q: 'Intertextualidade?', a: 'Diálogo/referência entre textos.' },
    { q: 'Conectivo?', a: 'Palavras que dão coesão (logo, porque).' },
    { q: 'Figuras de linguagem?', a: 'Recursos para mais expressividade.' },
    { q: 'Ambiguidade?', a: 'Dois ou mais sentidos.' },
    { q: 'Tópico frasal?', a: 'Ideia central que abre parágrafos.' },
    { q: 'Texto expositivo?', a: 'Objetivo de transmitir info pura.' },
    { q: 'Polissemia?', a: 'Palavra ter múltiplos sentidos.' },
    { q: 'Gêneros textuais?', a: 'Formatos sociais do texto (e-mail, receita).' }
);
fcKB['Geografia'].push(
    { q: 'Cartografia?', a: 'Estudo/criação de mapas.' },
    { q: 'Coordenadas Geográficas?', a: 'Latitudes e Longitudes.' },
    { q: 'Assoreamento?', a: 'Acúmulo de areia no rio.' },
    { q: 'Bioma?', a: 'Conjunto de ecossistemas.' },
    { q: 'Meridiano de Greenwich?', a: 'Longitude 0°.' },
    { q: 'Clima x Tempo?', a: 'Clima = padrão. Tempo = momento.' },
    { q: 'Aquífero Guarani?', a: 'Bacia de água doce subterrânea América Sul.' },
    { q: 'Gentrificação?', a: 'Revalorização cara de ambiente urbano.' },
    { q: 'Hidrografia BR?', a: 'Rios extensos, poucos lagos.' },
    { q: 'Latitude?', a: 'Distância à linha do equador.' }
);
fcKB['Artes'].push(
    { q: 'Renascimento?', a: 'Valorização clássica (Séc XV).' },
    { q: 'Mona Lisa?', a: 'Pintura de Da Vinci.' },
    { q: 'Cubismo?', a: 'Formas geométricas, Picasso.' },
    { q: 'Música erudita?', a: 'Clássica, sinfonias.' },
    { q: 'Van Gogh?', a: 'Pós-impressionista (A Noite Estrelada).' },
    { q: 'Pop Art?', a: 'Cultura massa (Warhol).' },
    { q: 'Surrealismo?', a: 'Mundo onírico, Dalí.' },
    { q: 'Cinema?', a: 'Sétima arte.' },
    { q: 'Cores primárias pigmento (CMY)?', a: 'Ciano, Magenta, Amarelo.' },
    { q: 'Aleijadinho?', a: 'Escultor Barroco.' },
    { q: 'Fotografia?', a: 'Imagens geradas por exposição à luz.' }
);
fcKB['Educação Física'].push(
    { q: 'Atividade aeróbica?', a: 'Usa oxigênio em exercício longo.' },
    { q: 'Massa magra?', a: 'Peso subtraído gordura.' },
    { q: 'Sedentarismo?', a: 'Falta de exercício.' },
    { q: 'VO2 Max?', a: 'Captação max de Oxigênio.' },
    { q: 'Jogos Olímpicos?', a: 'A cada 4 anos, origem Grécia.' },
    { q: 'Alongamento?', a: 'Traz flexibilidade, previne lesões.' },
    { q: 'Carboidratos?', a: 'Fonte de energia.' },
    { q: 'Hipertrofia musculação?', a: 'Aumento tamanho músculo.' },
    { q: 'Esportes Invasão?', a: 'Futebol, basquete, handebol.' },
    { q: 'Coordenação motora fina?', a: 'Movimentos pequenos como escrever.' },
    { q: 'Hidratação média dia?', a: '2 a 3 litros.' }
);
fcKB['Direito e Ética'].push(
    { q: 'Estado Democrático Direito?', a: 'Governo do povo, submisso à lei.' },
    { q: 'Maria da Penha?', a: 'Punição à violência doméstica.' },
    { q: 'Direitos civis?', a: 'Liberdade, igualdade, defesa.' },
    { q: 'Plágio?', a: 'Apropriar ideias de outrem ilegalmente.' },
    { q: 'Bioética?', a: 'Ética na medicina e biologia.' },
    { q: 'Presunção inocência?', a: 'Inocente até prova/julgamento finalizado.' },
    { q: 'Três Poderes BR?', a: 'Exec, Legis, Judic.' },
    { q: 'Compliance?', a: 'Estar conforme nas normas corporativas.' },
    { q: 'Código Defesa Consumidor?', a: 'CDC, rege relações consumo BR.' },
    { q: 'Ética vs Moral?', a: 'Ética é estudo da moral (regras).' },
    { q: 'Cyberbullying?', a: 'Violência por tela.' }
);
fcKB['Lógica de Programação'].push(
    { q: 'Algoritmo?', a: 'Passo a passo finito de resolução de problema.' },
    { q: 'Erro Sintaxe?', a: 'Quando regras de codificação são desrespeitadas.' },
    { q: 'Depurar/Debug?', a: 'Achar bugs/erros.' },
    { q: 'Matriz/Array?', a: 'Cadeia de dados indexáveis.' },
    { q: 'String?', a: 'Texto na prog.' },
    { q: 'Switch?', a: 'Estrutura seletiva para muitos casos.' },
    { q: 'Loop infinito?', a: 'Problema quando laço não encontra condição de saída.' },
    { q: 'Comentários da Lang?', a: 'Explicam o código.' },
    { q: 'Constante?', a: 'Dado imutável.' },
    { q: 'Inteiro (int)?', a: 'Número sem vírgula.' }
);
fcKB['Linguagem de Programação'].push(
    { q: 'Prog Orientada Obj (POO)?', a: 'Classes e objetos.' },
    { q: 'Instanciar classe?', a: 'Cria objeto na memória.' },
    { q: 'Herança?', a: 'Filha recebe atributos mãe.' },
    { q: 'int vs float vs double?', a: 'Int: sem decimal. Float/double: Decimais.' },
    { q: 'Ponto-E-Virgula?', a: 'Fim de instrução.' },
    { q: 'Compilar?', a: 'Converter fonte p/ máquina.' },
    { q: 'Encapsulamento?', a: 'Esconder detalhes via private/public.' },
    { q: 'using / import?', a: 'Trazer funções externas.' },
    { q: 'return em void?', a: 'Para funções que devolvem dado de volta.' },
    { q: 'Framework?', a: 'Bases prontas de código facilitadoras.' }
);
fcKB['Manutenção e Suporte de Computadores'].push(
    { q: 'Ver memória Win?', a: 'Ctrl+Shift+Esc Gerenciador.' },
    { q: 'Pasta térmica?', a: 'Dissipar calor no cooler.' },
    { q: 'Overclock?', a: 'Superação max Hz original.' },
    { q: 'Cabo SATA?', a: 'Liga dados do HD/SSD placa mãe.' },
    { q: 'Pilha CR2032 placa?', a: 'Grava Bios e relógio CMOS.' },
    { q: 'Formatar?', a: 'Refazer OS e apagar disco limpo.' },
    { q: 'Vídeo onboard?', a: 'Chip dentro CPU, partilha RAM.' },
    { q: 'SSD M.2 NVME?', a: 'SSD direto na p-mãe super veloz.' },
    { q: 'COMANDO PING?', a: 'Confere rede e lentidão ao IP destino.' },
    { q: 'Fonte (PSU)?', a: 'Alimentação.' },
    { q: 'Drivers?', a: 'Softwares que ensinam placa a ler equipamento USB e Placa vídeo.' }
);
fcKB['Robótica'].push(
    { q: 'Servomotor?', a: 'Motor de giro com posições graus exatas.' },
    { q: 'Sensor Ultrassônico?', a: 'Identidade por eco batend no som de Morcego.' },
    { q: 'Potenciômetro?', a: 'Botão girante variador Resistência.' },
    { q: 'Protoboard?', a: 'Placa furos pro projeto elétr.' },
    { q: 'PWM em pino?', a: 'Faz digital modular parecendo analógico (brilho led suave).' },
    { q: 'Motor DC?', a: 'Motor escovado de rotação constante.' },
    { q: 'I2C/Wire.h?', a: 'Biblioteca do SDA SLC painel Led display.' },
    { q: 'GND?', a: 'Terra, referência V=0.' },
    { q: 'IDE?', a: 'Local para programar (C/C++).' },
    { q: 'VCC?', a: 'Alimentação da voltagem positiva (5v etc).' }
);
fcKB['Sistemas Operacionais'].push(
    { q: 'O que o OS faz?', a: 'Base do software pra controlar máquina.' },
    { q: 'Kernel?', a: 'O núcleo primário que lida com o hardware.' },
    { q: 'Linux mascote?', a: 'Tux.' },
    { q: 'Agendamentos Cron Linux?', a: 'Cron via crontab p/ processos diários rodar s/ dono.' },
    { q: 'BSOD Windows?', a: 'A gloriosa tela azul.' },
    { q: '/etc/?', a: 'Pasta confs UNIX.' },
    { q: 'Desfragmentação?', a: 'Junta as peças do HD que ficaram quebradas espalhadas.' },
    { q: 'CMD no Windows?', a: 'Shell DOS.' },
    { q: 'Ifconfig / ipconfig?', a: 'Endereço IPs local.' }
);
fcKB['Tecnologias Interativas'].push(
    { q: 'Docs links?', a: 'Livre acesso, compartilhar.' },
    { q: 'Excel SOMA?', a: 'Soma(A1:A5).' },
    { q: 'Slide mestre PPT?', a: 'Layout modelo invisível do topo base para replicar em tudo auto.' },
    { q: 'PROCV no EXCEL?', a: 'O mágico procurador Vertical.' },
    { q: 'PPT to MPe4?', a: 'Expostar Criar Vídeos do Slide com as aulas faladas.' },
    { q: 'Word crash check?', a: 'Auto-recuperação arquivos docs.' },
    { q: 'Atalho Moeda?', a: 'Ctrl shift $ no pc excel.' },
    { q: 'Gerador Gráfico?', a: 'Seleciona + INSERIR -> Guia Graf.' },
    { q: 'Justificar atalho Word?', a: 'Ctrl J.' }
);
fcKB['Steam Maker'].push(
    { q: 'Eletrônica e maker?', a: 'Dar vida aos papelões recicls.' },
    { q: 'Gambiarras diy válidas?', a: 'Sim, fita crepe, tesoura, criatividade.' },
    { q: 'Corte a Laser Acrílico?', a: 'Fácil, veloz, vetor.' },
    { q: 'FDM Printer 3D?', a: 'Péla Extrusor quente fio plástico camada 1a1.' },
    { q: 'STEAM sigla?', a: 'Science Tech Eng Art Math.' },
    { q: 'Scratch?', a: 'Gato Laranja dev Crianças do MIT, block based.' },
    { q: 'Aula maker exige DEV C#?', a: 'Não, baterias solares de LED tb valem.' },
    { q: 'Tinkercad usa local?', a: 'WEB APP para arduinos e 3D simples.' },
    { q: 'ABS filament 3D?', a: 'Cheiroso ruim mas robusto calor sol forte mecânico.' },
    { q: 'Lego Spike?', a: 'Motor e Hub via Lego de encaixes fáceis Maker.' },
    { q: 'STEAM A e M = ?', a: 'Artes e Matemática.' },
    { q: 'Rasperry PI Maker?', a: 'MiniLinux placa verde poderosa para AI cam makers.' }
);
'''

with open('c:/Users/26012465/Desktop/FECAD - FLASH CARDS/FECAD_Copia/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

anchor = """            ]
        };

        // ===== AI FLASHCARD SYSTEM ====="""

injection = """            ]
        };

        // Script Extra para complementar todas as materias em 15 cards+
        (() => {
"""
for line in extra_q.strip().split('\n'):
    injection += '            ' + line + '\n'
injection += """        })();

        // ===== AI FLASHCARD SYSTEM ====="""

new_text = text.replace(anchor, injection)
with open('c:/Users/26012465/Desktop/FECAD - FLASH CARDS/FECAD_Copia/index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Success')
