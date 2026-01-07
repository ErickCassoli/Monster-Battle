# Monster-Battle

##Aviso:
Esse projeto foi desenvolvido como um trabalho academico para estudo de Design Pattern, modularidade e escalabilidade

## Descrição
**Monster-Battle** é um jogo de batalha entre monstros baseado em turnos, jogado diretamente no console. Nele, os jogadores podem escolher e personalizar seus personagens para participar de intensas batalhas PvP (Jogador vs Jogador) ou PvE (Jogador vs Computador). O objetivo é derrotar o adversário utilizando ataques básicos, habilidades especiais e estratégias defensivas.

---

## Funcionalidades
- **Modos de Jogo**:
  - PvP: Dois jogadores criam personagens e batalham entre si.
  - PvE: Um jogador enfrenta ondas de monstros controlados por IA.
- **Criação de Personagens**:
  - Personagens personalizados com diferentes classes e raças.
- **Sistema de Combate por Turnos**:
  - Escolha entre atacar, defender ou utilizar habilidades especiais.
- **Habilidades Especiais**:
  - Cada classe e raça tem habilidades únicas que podem mudar o curso da batalha.
- **Pontuação e Progresso**:
  - Pontuações são salvas e podem ser visualizadas no menu principal.

---

## Requisitos
- **Linguagem**: Python 3.10 ou superior
- **Dependências**:
  - Nenhuma biblioteca adicional é necessária. O jogo utiliza somente bibliotecas padrão do Python.

---

## Como Executar
1. Clone o repositório:
   ```bash
   git clone <URL-DO-REPOSITORIO>
   cd Monster-Battle
   ```
2. Cria ambiente virtual:
   ```bash
   python -m venv ./venv
   ```
3. Ativar ambiente virtual:
   ```bash
   ./venv/Scripts/activate
   ```
4. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o jogo:
   ```bash
   python main.py
   ```

---

## Como Executar (testes)
1. Clone o repositório:
   ```bash
   git clone <URL-DO-REPOSITORIO>
   cd Monster-Battle
   ```
2. Cria ambiente virtual:
   ```bash
   python -m venv ./venv
   ```
3. Ativar ambiente virtual:
   ```bash
   ./venv/Scripts/activate
   ```
4. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o jogo:
   ```bash
   pytest tests/[Test-name]
   ```

---

## Como Jogar
1. Ao iniciar o jogo, escolha uma das opções do menu principal:
   - `1`: Jogar no modo PvP.
   - `2`: Jogar no modo PvE.
   - `3`: Carregar e visualizar pontuações salvas.
   - `4`: Sair do jogo.

2. **Criação de Personagem**:
   - No início de uma batalha, você será guiado para criar seu personagem.
   - Escolha uma classe e uma raça, que definirão as habilidades disponíveis.

3. **Durante a Batalha**:
   - Escolha entre as seguintes ações:
     - **1**: Ataque básico.
     - **2**: Habilidade da raça.
     - **3**: Habilidade especial da classe.
     - **4**: Ultimate (habilidade mais poderosa).

4. O jogo continua em turnos até que um lado seja derrotado.

---

## Estrutura do Projeto
- `main.py`: Ponto de entrada do jogo.
- `game/`:
  - `game_manager.py`: Lógica principal do jogo.
  - `monster_factory.py`: Gerador de monstros utilizando o padrão Factory.
  - `save_manager.py`: Gerencia o salvamento e carregamento de pontuações.
  - `character/`: Lógica de personagens, incluindo classes e raças.
  - `monsters/`: Lógica de monstros e seus tipos.
  - `utils/`: Utilitários para menus e manipulação de personagens.

---

## Padrões de projetos
- `Factory`: Em monster_factory.py, para criar instâncias flexíveis de monstros.
- `Facade/Controller`: Em game_manager.py, para organizar o fluxo e as interações do jogo.
- `Singleton-like Utility`: Em save_manager.py, para manipular o estado persistente do jogo.
- `Herança e Polimorfismo`: Implementados em baseMonster.py e subclasses específicas como Dragon.
- `Template Method`: No método special_ability de BaseMonster, fornecendo um comportamento que é sobrescrito nas subclasses.

---

## Extensibilidade
O projeto foi estruturado de forma modular para facilitar a adição de:
- Novos tipos de monstros.
- Classes ou raças adicionais.
- Habilidades e modos de jogo.

---

## Contribuição
Siga estas diretrizes para contribuir:
1. Crie um fork do repositório.
2. Faça suas alterações em uma branch separada.
3. Abra um Pull Request com uma descrição clara das mudanças.

---

## Autores
Este projeto foi desenvolvido para o aprendizado de padrões de design e sistemas de combate baseados em turnos. Sinta-se à vontade para utilizá-lo e expandi-lo.
feito por:

- Erick Cassoli
- Gabriel Ramos
- Sergio Ricardo

---

## Video de apresentação:
- [Youtube](https://www.youtube.com/watch?v=YbVNY4z5RvA)
