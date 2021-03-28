## Previsão de Diabetes

Visando testar meus conhecimentos e habilidades em Data Science, resolvi treinar um modelo de Machine Learning para prever a ocorrência de diabetes em mulheres, utilizando o famoso Dataset do Kaggle **Pima Indians Diabetes Database**.

Este projeto passou por todas as etapas de desenvolvimento de uma solução de Machine Learning, indo desde a exploração dos dados, validação e teste, até o deploy da solução final. 

O app está em produção e pode ser testado no link: https://previsaodiabetes.herokuapp.com/

## Base de Dados
A base de dados utilizada no desenvolvimento (**diabetes.csv**) provém do famoso Dataset do Kaggle Pima Indians Diabetes Database (**https://www.kaggle.com/uciml/pima-indians-diabetes-database**) que trata da ocorrência de diabetes em mulheres.

Originalmente o Dataset foi fornecido sem cabeçalho, abaixo está o dicionário de dados:

0. Número de vezes em que ficou grávida.
1. Concentração de glicose.
2. Pressão diastólica (mm Hg).
3. Espessura da dobra cutânea do tríceps (mm).
4. Insulina (mu U/ml).
5. Índice de massa corporal (peso em kg/(altura em m)^2).
6. Histórico familiar de diabetes.
7. Idade (anos).
8. Classificação (0 não diabético | 1 diabético ).

## Treinamento do Modelo
As etapas de pré-processamento e análise dos dados e a construção, treinamento, validação, teste e persistência do modelo podem ser conferidas no jupyter notebook (**construção_modelo.ipynb**). 

Devido ao desbalanceamento da classe alvo, utilizei o modelo *Decision Tree* para tentar amenizar o problema. Escolhi F1 como métrica de avaliação, uma vez que essa métrica avalia Precision e Recall de forma unificada. O modelo foi tunado com GridsearchCV e foi possível chegar ao score F1 de 0.687, contra uma baseline de 0.523.

O modelo com os melhores parâmetros foi persistido para o arquivo **model.sav** e a normalização dos dados foi persistida para o arquivo **scaler.sav** (para que os dados novos, que chegam via formulário, possam ser corretamente normalizados e não alterem o comportamento do modelo). 

## Aplicação web
Para fazer o deploy do modelo foi utilizado o micro-framework Flask, o arquivo **app.py** faz toda a orquestração através das rotas. Foram criadas 2 páginas HTML, uma para que o usuário coloque os dados para uma nova predição (**formulario.html**) e uma segunda onde é mostrado o resultado da predição (**resultado.html**). Ambas as páginas estão na pasta *templates*.

O deploy da solução final foi feito na cloud do Heroku.

## Limitações
O projeto buscou desenvolver uma solução simples e unicamente com fins educacionais, não sendo, portanto, uma proposta real de solucação do problema.
Como pontos de melhoría podem ser apontados: 
1. Necessidade de melhor entendimento das features, através da conversa com profissionais da área da saúde, e novas formas de tratamento dos dados.
2. Novas abordagens para o problema da classe alvo desbalanceada: outros modelos, boosting, oversampling, undersampling, etc.
3. Melhorar os templates html para que o app fiquei mais fácil de utilizar e mais bonito.
4. Constribuições e críticas construtivas são bem vindas: https://www.linkedin.com/in/josewalterlima/
