# Previsão de Diabetes

Este projeto foi desenvolvido como desafio final do Bootcamp Desenvolvedor Python, do IGTI.

O objetivo do projeto foi o desenvolvimento de um projeto completo de machine learning: desde o pré-processamento, normalização dos dados, treinamento, teste, persistência do modelo e “deploy” da solução final.

## Base de Dados
A base de dados utilizada no desenvolvimento (**diabetes.csv**) provém do famoso Dataset do Kaggle Pima Indians Diabetes Database (**https://www.kaggle.com/uciml/pima-indians-diabetes-database**) que trata da ocorrência de diabetes em mulheres.

Por motivos didáticos o Dataset foi fornecido sem cabeçalho, abaixo está o dicionário de dados:

0. Número de vezes em que ficou grávida.
1. Concentração de glicose.
2. Pressão diastólica (mm Hg).
3. Espessura da dobra cutânea do tríceps (mm).
4. Insulina (mu U/ml).
5. Índice de massa corporal (peso em kg/(altura em m)^2).
6. Histórico familiar de diabetes.
7. Idade (anos).
8. Classificação (0 não diabético | 1 diabético ).

## Construção do Modelo
As etapas de pré-processamento dos dados e a construção, treinamento, teste e persistência do modelo foram feitas em um jupyter notebook (**construção_modelo.ipynb**). Foram testados 3 modelos: *KNN (K nearest neighbor)*, *Decision Tree* e *MLP (Multilayer Perceptron)*. 

Como o objetivo era o desenvolvimento do projeto como um todo, não foi criado um baseline para comparação com o desempenho dos modelos (etapa altamente necessária em um projeto real) nem mesmo foi realizado *tuning* do modelo (outra etapa muito importante em um projeto real), sendo utilizado o modelo da forma padrão como foi criado.

O modelo com melhor nível de acuracidade foi persistido para o arquivo **mlp_model.sav** e a normalização dos dados foi persistida para o arquivo **normalização.sav** (para que os dados novos que chegasem via formulário fossem corretamente normalizados e não alterassem o comportamento do modelo). 

## Aplicação web
Para colocar o modelo "em produção" foi utilizado o micro-framework Flask, o arquivo **app.py** faz toda a integração através das rotas.
Foram criadas 2 páginas HTML, uma para que o usuário coloque os dados para uma nova predição (**formulario.html**) e uma segunda onde é mostrado o resultado da predição (**resultado.html**). Ambas as páginas estão na pasta *templates*.

## Limitações
O projeto buscou desenvolver uma solução simples e unicamente com fins educacionais, não sendo, portanto, uma proposta real de solucação do problema.
Como pontos de melhoría podem ser apontados: 
1. Necessidade de uma base de dados maior, o que traria maior confiabilidade ao modelo.
2. Necessidade de uma baseline, de forma a avaliar a efetividade da solucação proposta em relação a uma solução simples e rápida.
3. Necessidade de tuning do modelo, a fim de melhorar os resultados.
