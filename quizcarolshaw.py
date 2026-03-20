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
    st.session_state.mostrar_resposta = False  # NOVO: flag para mostrar resposta após segunda tentativa

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
    opcao = st.radio("Escolha:", ["Iniciar jogo", "Ver regras"])

    if opcao == "Informações":
        if st.button("Mostrar Informações"):
            st.session_state.pagina = "Informações"
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

# -------- REGRAS --------
elif st.session_state.pagina == "regras":
    st.title("📜 Regras")
    st.write("- Você terá 2 chances por pergunta")
    st.write("- Acertar de primeira vale mais pontos")
    st.write("- Segunda tentativa vale menos pontos")
    if st.button("Voltar"):
        st.session_state.pagina = "menu"
        st.rerun()

# -------- QUIZ --------
elif st.session_state.pagina == "quiz":
    perguntas = st.session_state.perguntas
    i = st.session_state.pergunta_atual

    st.write(f"👤 Jogador: {st.session_state.nome}")

    if i < len(perguntas):
        pergunta, opcoes, correta = perguntas[i]
        st.subheader(f"Pergunta {i+1}")

        if st.session_state.mostrar_resposta:
            # Mostrar resposta correta após segunda tentativa errada
            st.error(f"A resposta correta era: {correta}) {opcoes[ord(correta)-97]}")
            if st.button("Próxima pergunta"):
                st.session_state.mostrar_resposta = False
                st.session_state.pergunta_atual += 1
                st.rerun()
        else:
            # Mostrar tentativa atual
            if st.session_state.tentativa == 1:
                st.info(f"🎯 Tentativa 1 de 2 — vale {st.session_state.valor_principal} pontos")
            else:
                st.warning(f"⚠️ Tentativa 2 de 2 — agora vale apenas {st.session_state.valor_segunda} pontos")

            st.write(pergunta)

            resposta = st.radio(
                "Escolha:",
                ["a","b","c","d"],
                format_func=lambda x: f"{x}) {opcoes[ord(x)-97]}",
                key=f"resposta_{i}_{st.session_state.tentativa}"
            )

            if st.button("Responder"):
                if resposta == correta:
                    if st.session_state.tentativa == 1:
                        st.success(f"✔ Acertou de primeira! (+{st.session_state.valor_principal} pontos)")
                        st.session_state.pontuacao += st.session_state.valor_principal
                    else:
                        st.success(f"✔ Acertou na segunda tentativa! (+{st.session_state.valor_segunda} pontos)")
                        st.session_state.pontuacao += st.session_state.valor_segunda

                    st.session_state.tentativa = 1
                    st.session_state.pergunta_atual += 1
                    st.rerun()
                else:
                    if st.session_state.tentativa == 1:
                        st.session_state.tentativa = 2
                        st.error(f"❌ Errou! Segunda tentativa liberada — agora vale apenas {st.session_state.valor_segunda} pontos.")
                    else:
                        st.session_state.erros += 1
                        st.session_state.tentativa = 1
                        st.session_state.mostrar_resposta = True  # Flag para mostrar resposta antes de avançar

    else:
        st.session_state.pagina = "resultado"
        st.rerun()

# -------- RESULTADO --------
elif st.session_state.pagina == "resultado":
    st.title("🏁 Resultado Final")
    st.write(f"👤 Jogador: {st.session_state.nome}")
    st.write(f"Pontuação: {st.session_state.pontuacao} / {st.session_state.total}")
    st.write(f"Erros: {st.session_state.erros}")

    percentual = st.session_state.pontuacao / st.session_state.total
    if percentual >= 0.7:
        st.success("🔥 Excelente! Mestre em Carol Shaw!")
    elif percentual >= 0.4:
        st.info("👍 Bom! Você conhece bastante!")
    else:
        st.warning("📚 Continue estudando sobre Carol Shaw!")

    if st.button("Reiniciar"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
