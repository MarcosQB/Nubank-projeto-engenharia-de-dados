# Nubank
> ###### Autor: Marcos Alexandre
> ###### Data: Julho 29, 2023
### Descrição
Este projeto tem como objetivo automatizar a coleta, análise e visualização dos dados da conta Nubank por meio de uma arquitetura de engenharia de dados provisionada na nuvem AWS (Amazon Web Services). A solução oferece uma visão detalhada das transações, despesas, receitas, saldo da conta e limites de crédito, permitindo um gerenciamento financeiro mais eficiente e consciente.

#### Fluxo do projeto:

1. **Coleta de Dados da Conta do Nubank:** 
Através de uma integração com a API do Nubank, os dados financeiros, incluindo transações, saldo da conta, limites de crédito e movimentações, são coletados de forma automatizada e segura.

2. **Armazenamento na Nuvem AWS:** 
Os dados coletados são armazenados no serviço de armazenamento S3 da AWS, garantindo a segurança, escalabilidade e disponibilidade necessárias para o projeto.    

3. **Pré-processamento e Limpeza de Dados:** Utilizando o PySpark, o projeto realiza transformações nos dados coletados, garantindo que eles estejam formatados corretamente para a análise.

4. **Análise e Classificação de Transações:**
 O projeto categoriza as transações de acordo com seus tipos, como compras, parcelamentos e receitas. Isso permite uma análise detalhada do uso do cartão de crédito ao longo do mês.

5. **Geração de Tabelas e Relatórios:** 
Os dados processados são organizados em tabelas e salvas no formato Parquet. Essas tabelas podem ser utilizadas para gerar relatórios detalhados sobre as despesas, receitas, saldo e limites de crédito.

6. **Integração com o Google Sheets e Data Studio:** 
Os dados são enviados para o Google Sheets e o Data Studio para uma visualização interativa e personalizada dos insights obtidos. Isso permite um acompanhamento mais dinâmico e uma melhor compreensão da gestão financeira.

7. **Notificações por E-mail:**
 O projeto envia notificações via e-mail para informar o início e conclusão do processamento dos dados, me mantendo informado sobre o status do fluxo de processamento.

#### Benefícios do Projeto:

- **Automatização Financeira:**
 A automatização da coleta e análise de dados me permite ter uma visão completa e atualizada das minhas finanças, eliminando a necessidade de acompanhamento manual e trabalhoso.

- **Melhoria na Gestão Financeira:** 
Com os insights detalhados obtidos a partir da análise dos dados, posso tomar decisões financeiras mais conscientes, otimizando meus gastos e aumentando o controle sobre minhas finanças.

- **Comparação de Períodos:** 
O armazenamento dos dados em formato Parquet possibilita a comparação entre diferentes períodos de tempo, permitindo identificar tendências e mudanças no comportamento financeiro ao longo do tempo.
#### Dependências
```shell
urllib3==1.26.6
cryptography==38.0.2
s3fs
boto3
google-api-python-client
google-auth-httplib2
google-auth-oauthlib
pynubank
```
### Serviços utilizados

| Icon| Serviços | Descrição |
|------|----------|-----------|
|<img src="./docs/Icons/Athena.png" alt="Athena" width="50" height="50">| Athena (AWS)|Serviço de análise interativo e sem servidor que oferece suporte a formatos de tabela e arquivo abertos. Permite aos usuários realizar consultas SQL em grandes conjuntos de dados armazenados no Amazon S3, sem a necessidade   de gerenciar infraestrutura de banco de dados.|
|<img src="./docs/Icons/ElasticMapReduce.png" alt="EMR" width="50" height="50"> | ElasticMapReduce (AWS)|Serviço de big data que permite processar e analisar grandes volumes de dados usando estruturas de processamento distribuído, como Apache Hadoop e Apache Spark.|
|<img src="./docs/Icons/Glue Crawler.png" alt="Crawler" width="50" height="50"> |Glue Crawlers (AWS)|Serviço de descoberta de dados que automatiza o processo de extrair metadados de várias fontes de dados, como bancos de dados, Data Lakes e tabelas no Amazon S3. Ele facilita o rastreamento e a organização dos dados para análise e consulta.|
|<img src="./docs/Icons/Glue Data Catalog.png" alt="DataCatalog" width="50" height="50"> |Glue Data Catalog (AWS)|Serviço que armazena informações estruturais e de esquema para os dados processados pelo AWS Glue. Ele permite que os dados sejam compartilhados entre diferentes serviços, facilitando a integração e o acesso aos dados.|
|<img src="./docs/Icons/SNS.png" alt="SNS" width="50" height="50"> |SNS (AWS)|Serviço de mensagens que permite enviar notificações e alertas para diversos endpoints, como e-mail, SMS, HTTP, Lambda e outros. É uma forma eficiente de manter usuários e sistemas informados sobre eventos e mudanças em tempo real.|
|<img src="./docs/Icons/Command Line Interface.png" alt="CLI" width="50" height="50"> |Command Line Interface (AWS)|A AWS Command Line Interface (CLI) é uma ferramenta que permite interagir com os serviços da AWS a partir da linha de comando.|
|<img src="./docs/Icons/StepFunctions.png" alt="Step Functions (AWS)" width="50" height="50">|StepFunctions (AWS)|Serviço que permite criar e orquestrar facilmente fluxos de trabalho baseados em nuvem usando visualizações visuais. Ele coordena as etapas do aplicativo e facilita a integração de serviços diferentes, criando fluxos de trabalho eficientes.|
|<img src="./docs/Icons/Lambda.png" alt="Lambda" width="50" height="50">|Lambda (AWS)|Serviço de computação sem servidor que permite executar código sem precisar provisionar ou gerenciar servidores. Ele é acionado por eventos, como alterações em dados do Amazon S3 ou mensagens do Amazon SNS, oferecendo escalabilidade automática e pagamento apenas pelas execuções do código.|
|<img src="./docs/Icons/Secrets Manager.png" alt="SecretsManager" width="50" height="50">|Secrets Manager (AWS)|Serviço para gerenciar o armazenamento seguro de informações confidenciais, como senhas, tokens de acesso e chaves de API. Ele permite proteger e controlar o acesso a esses segredos, além de facilitar sua rotação automática para garantir a segurança contínua.|
|<img src="./docs/Icons/S3.png" alt="S3" width="50" height="50">|S3 (AWS)|Serviço de armazenamento de objetos altamente escalável e durável. Ele permite armazenar e recuperar qualquer quantidade de dados a qualquer momento, oferecendo alta disponibilidade e segurança avançada para os dados armazenados.|
|<img src="./docs/Icons/Google Sheets.png" alt="Sheets" width="50" height="50">|Google Sheets (Google)|Planilha online oferecida pelo Google, permite criar, editar e compartilhar planilhas com outras pessoas em tempo real, facilitando a colaboração e organização de dados.|
|<img src="./docs/Icons/DataStudio.png" alt="DataStudio" width="50" height="50">|DataStudio (Google)|Ferramenta de visualização de dados que permite criar relatórios interativos e painéis informativos usando várias fontes de dados.Facilita a criação de gráficos e dashboards personalizados para análise e tomada de decisões.|

### Arquitetura dos dados
<img src="./Infra/Arquitetura_Dados.gif" alt="Aqt" width="1200" height="600">

![](./Infra/Arquitetura_Dados.gif)

### Dashboard Construido
![](./Dashboard/Layout.jpg)


