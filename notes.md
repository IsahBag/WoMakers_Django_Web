## Anotações

*"Framework é como uma caixa de ferramentas"*

**Padrão MVT:**
Orientado por Model View Template.

**Model:** 
Representa a camada de dados responsável por definir a estrutura do banco de dados;
Envolve o salvamento, armazenamento, recuperação e busca de informações.

**View:**
Representa a camada responsável pela lógica do processamento e exibição das informações.

**Template:**
Define como os dados vão ser renderizados e apresentados para os usuários.

**MVC (Model, View, Controller) ->** 
Controller é responsável por receber e responder as solicitações dos usuários e interagir em tempo real com a model.

**Framework Django:**
* montar páginas (Templates)
* interagir com diversos bancos de dados (ORM)
* validar input dos usuários (Forms)
* controlar acesso (Authorization)
* gerenciar a aplicação (Admin)

**Servidor Redis:**
Um servidor de banco de dados que consegue salvar as informações em um servidor específico de uma forma otimizada,armazenando na memória RAM

Sempre que criar um novo aplicativo, deve avisar para o projeto da sua criação:
-> settings
-> installed_apps
-> 'nome_app'

1. Criando Views (base)
 * inclui todas as funções que irão indicar as funcionalidades do sistema
 * todas as telas do sistema representam uma view 

2. Criar URLs das views (projeto)  

3. Criando os tamplates das páginas (base):

 * criar uma pasta 'templates'
 * criar os arquivos html de cada página
 * códigos CSS e JavaScript devem ser colocados numa pasta criada com o nome 'static'

4. Criando forms (base):
 * criar um arquivo forms.py 

5. Armazenando em banco de dados:
 * criar as classes em models (base)
 * SEMPRE que houver alteração no banco de dados, rodar os comandos já descritos

6. Configurando admin (base):
 * criar classes para que o banco de dados apareça na página admin

7. Criando novo aplicativo para cadastrar os cursos:
 * criar novo app usando manage.py
 * adicionar o aplicativo criardo em settings
 * criar a classe em models (cursos)
 * realizar a migração para o banco de dados
 * configurar Admin 
 * criar a view e a página em HTML
 * definir uma url -> nesse caso foi criado um arquivo urls.py dentro do aplicativo curso