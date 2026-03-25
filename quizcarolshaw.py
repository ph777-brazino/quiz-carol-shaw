import streamlit as st

st.set_page_config(page_title="Quiz Carol Shaw")

# -------- ESTADO --------
if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"
    st.session_state.nome = ""
    st.session_state.pergunta_atual = 0
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    st.session_state.tentativa = 1
    st.session_state.perguntas = []
    st.session_state.valor_principal = 0
    st.session_state.valor_segunda = 0
    st.session_state.total = 0
    st.session_state.mostrar_resposta = False

# -------- PERGUNTAS --------
perguntas_facil = [
    ("Quem foi Carol Shaw?", ["Atriz","Programadora de jogos","Cantora","Jogadora profissional"], "b"),
    ("Carol Shaw trabalhou com o que?", ["Filmes","Videogames","Música","Moda"], "b"),
    ("Carol Shaw é conhecida por ser:", ["Primeira mulher programadora de jogos","Jogadora profissional","Streamer","Cientista"], "a"),
    ("Ela trabalhou em qual área?", ["Medicina","Engenharia de software","Direito","Administração"], "b"),
    ("Carol Shaw nasceu em qual país?", ["Brasil","Estados Unidos","Japão","Canadá"], "b"),
    ("Em que década começou a programar?", ["1970","1980","1990","1960"], "a"),
    ("Qual profissão sua mãe tinha?", ["Professora","Enfermeira","Cientista","Advogada"], "a"),
    ("Carol Shaw se destacou como?", ["Designer de moda","Engenheira de software e programadora de jogos","Pintora","Atriz"], "b"),
    ("Ela é pioneira em qual indústria?", ["Cinema","Jogos eletrônicos","Música","Teatro"], "b"),
    ("Carol Shaw ainda é lembrada como?", ["Inventora de consoles","Primeira mulher programadora de jogos famosa","Jogadora profissional","Pesquisadora de IA"], "b"),
]

perguntas_media = [
    ("Em qual empresa Carol Shaw trabalhou?", ["Nintendo","Atari","Sony","Sega"], "b"),
    ("Qual jogo famoso ela ajudou a criar?", ["River Raid","Mario Bros","Sonic","Pac-Man"], "a"),
    ("Carol Shaw programava para qual console?", ["PlayStation","Atari 2600","Xbox","NES"], "b"),
    ("Ela começou sua carreira em qual empresa?", ["Apple","Atari","Microsoft","Nintendo"], "b"),
    ("Carol Shaw também trabalhou na:", ["Activision","Ubisoft","EA","Capcom"], "a"),
    ("Qual gênero de jogos ela mais programou?", ["Shooter","Corrida","RPG","Quebra-cabeça"], "a"),
    ("River Raid foi criado originalmente para qual plataforma?", ["Atari 2600","NES","Game Boy","Sega Master System"], "a"),
    ("Ela contribuiu para jogos principalmente nos anos:", ["70","80","90","2000"], "b"),
    ("Carol Shaw estudou engenharia ou ciência da computação?", ["Engenharia","Ciência da Computação","Biologia","Matemática"], "b"),
    ("Ela ajudou a abrir portas para:", ["Homens na indústria","Mulheres na programação de jogos","Artistas digitais","Jogadores profissionais"], "b"),
]

perguntas_dificil = [
    ("Qual o gênero do jogo River Raid?", ["Corrida","Tiro (shooter)","RPG","Plataforma"], "b"),
    ("River Raid foi lançado em qual década?", ["1970","1980","1990","1960"], "b"),
    ("Carol Shaw se formou em qual área?", ["Ciência da Computação","Medicina","Arquitetura","Engenharia Civil"], "a"),
    ("Ela é considerada pioneira em:", ["Jogos mobile","Programação de jogos","Design gráfico","Jogos educativos"], "b"),
    ("Após sair da indústria, Carol Shaw:", ["Virou atriz","Se aposentou cedo","Virou cantora","Engenheira de IA"], "b"),
    ("River Raid foi um dos primeiros jogos a ter:", ["Multiplayer online","Rolagem vertical","Gráficos 3D","Som estéreo"], "b"),
    ("Ela trabalhou com gráficos em qual tipo de sistema?", ["Consoles domésticos","PCs modernos","Arcade","Mainframe"], "a"),
    ("Carol Shaw ajudou a definir padrões para:", ["Música em jogos","Programação de jogos","Marketing de consoles","Computação gráfica"], "b"),
    ("Ela contribuiu para jogos de qual desenvolvedora?", ["Atari","Sega","Nintendo","Sony"], "a"),
    ("River Raid foi famoso por:", ["Jogabilidade inovadora","Multiplayer online","Realismo gráfico","Efeitos sonoros"], "a"),
]

# -------- MENU --------
if st.session_state.pagina == "menu":
    st.title("🎮 Quiz Carol Shaw")
    opcao = st.radio("Escolha:", ["Iniciar jogo", "Informações do Quiz", "Informações sobre Carol Shaw"])

    if opcao == "Informações do Quiz":
        if st.button("Mostrar informações"):
            st.session_state.pagina = "informações"
            st.rerun()

    elif opcao == "Informações sobre Carol Shaw":
        if st.button("Ver informações"):
            st.session_state.pagina = "homenageada"
            st.rerun()

    else:
        st.session_state.nome = st.text_input("Digite seu nome:")
        dificuldade = st.radio("Dificuldade:", ["Fácil", "Média", "Difícil"])

        if st.button("Começar") and st.session_state.nome.strip() != "":
            if dificuldade == "Fácil":
                st.session_state.perguntas = perguntas_facil
                st.session_state.valor_principal = 10
                st.session_state.valor_segunda = 5
                st.session_state.total = 100
            elif dificuldade == "Média":
                st.session_state.perguntas = perguntas_media
                st.session_state.valor_principal = 20
                st.session_state.valor_segunda = 10
                st.session_state.total = 200
            else:
                st.session_state.perguntas = perguntas_dificil
                st.session_state.valor_principal = 30
                st.session_state.valor_segunda = 15
                st.session_state.total = 300

            st.session_state.pagina = "quiz"
            st.rerun()

# -------- INFORMAÇÕES DO QUIZ --------
elif st.session_state.pagina == "informações":
    st.title("📜 Informações do Quiz")
    st.write("- Você terá 2 chances por pergunta")
    st.write("- Acertar de primeira vale mais pontos")
    st.write("- Segunda tentativa vale menos pontos")
    if st.button("Voltar"):
        st.session_state.pagina = "menu"
        st.rerun()

# -------- INFORMAÇÕES SOBRE CAROL SHAW --------
elif st.session_state.pagina == "homenageada":
    st.title("👩‍💻 Informações sobre Carol Shaw")

    st.write("""
Carol Shaw nasceu em 1955 e, desde jovem, demonstrava interesse por tecnologia, algo incomum para mulheres na época. Mesmo enfrentando desafios por estar em um ambiente dominado por homens, decidiu seguir nessa área.

Iniciou sua carreira na Atari, onde já mostrava seu talento na criação de jogos. Mais tarde, na Activision, ganhou destaque ao desenvolver o jogo River Raid, que fez grande sucesso e marcou a história dos videogames.

Além de suas contribuições técnicas, Carol Shaw se tornou uma pioneira, mesmo se aposentando cedo, ela abriu caminhos para a participação feminina na tecnologia e inspirando diversas pessoas com sua trajetória.
""")

    if st.button("Voltar"):
        st.session_state.pagina = "menu"
        st.rerun()
