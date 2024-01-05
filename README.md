# Usando ARIMA em Python para Prever Receita da Olist

## 📃 [Medium Article](https://medium.com/@caiocasagrande/using-arima-in-python-to-forecast-olist-revenue-3e19fbe6e424)
### 📊 [Análise Exploratória de Dados da Olist com Plotly](https://github.com/caiocasagrande/olist_eda)

## Os benefícios da Ciência de Dados para empresas

A ciência de dados capacita as empresas com modelos estatísticos e algoritmos, fornecendo-lhes insights valiosos que orientam as decisões estratégicas. Para a **Olist**, gigante brasileira do comércio eletrônico, prever receitas é fundamental para o planejamento financeiro, mitigar riscos, otimizar recursos e realizar investimentos, causando um enorme impacto positivo no patrimônio da empresa no futuro.

## Sobre o problema de negócios

A Olist encontrou um desafio na gestão das suas receitas devido a flutuações imprevistas nas vendas. Eles esperavam vender muito mais nesta época do ano e fatores externos tornaram difícil para a empresa antecipar sua situação financeira.

- Os dados obtidos para este projeto são públicos e estão disponíveis em [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

## Objetivos
- Para resolver este problema, o gestor de dados sugeriu a utilização da metodologia de Séries Temporais univariada ARIMA (Autoregressive Integrated Moving Average) para prever a receita das duas semanas seguintes
- O objetivo principal é fornecer ao Olist modelos de previsão robustos, capazes de prever receitas para os próximos 14 dias
- Ao obter insights sobre vendas futuras, a Olist pode fazer ajustes financeiros estratégicos de forma proativa para otimizar suas operações

## 📝 Solução do problema
- Explorando a série temporal por diferentes maneiras, com apresentações visuais e estatísticas
- Decomposição da série em tendência, sazonalidade e resíduo
- Verificação de estacionaridade através dos testes Augmented Dickey-Fuller (ADF) e Kwiatkowski–Phillips–Schmidt–Shin (KPSS)
- Verificação através da Função de Autocorrelação (ACF) e Função Parcial de Autocorrelação (PACF)
- Aplicação dos modelos, realização de previsões, avaliação por métricas e sua visualização gráfica: Auto ARIMA, ARIMA, SARIMA
- Resultados finais dos modelos dispostos em tabela
- Próximos passos

## A série temporal 
Uma série temporal é o resultado de observações feitas sequencialmente ao longo do tempo. Sua característica mais importante é que as observações adjacentes são dependentes umas das outras e, portanto, os fatores que influenciaram a série no passado e atuam no presente continuarão a influenciá-la no futuro.

![olist_revenue_1](https://github.com/caiocasagrande/arima_revenue/blob/main/images/olist_revenue_1.png)

O primeiro passo é analisar todos os dados. A figura acima é um gráfico linear da receita diária da Olist de fevereiro de 2017 a meados de agosto de 2018. Para a previsão, o conjunto de dados será dividido em treinamento e teste, onde os dados até julho serão utilizados para prever a receita para os dias em Agosto.

## Modelo Auto ARIMA
A função `pmdarima.arima.auto_arima` foi projetada para selecionar o modelo ARIMA ideal. Ele será usado para encontrar os valores de *p*, *q* e ordens sazonais, dado o contexto dos testes anteriores, como gráficos ADF, KPSS, ACF e PACF.

![olist_revenue_7](https://github.com/caiocasagrande/arima_revenue/blob/main/images/olist_revenue_7.png)

Para avaliar os resultados, usaremos o erro médio absoluto (MAE), o erro quadrático médio (RMSE) e o erro percentual médio absoluto (MAPE)
- MAE: é a diferença média absoluta entre os valores previstos e os valores reais. Em outras palavras, as previsões do modelo estão erradas em aproximadamente $4.783,97, em média
- RMSE: é uma medida da magnitude média dos erros, dando mais peso aos erros maiores. Neste caso $6.284,02
- MAPE: mede a diferença percentual entre os valores previstos e os reais. Portanto, as previsões do modelo apresentam um erro de aproximadamente 17,11%

A soma dos valores reais para os próximos quatorze dias é de $536.219,46, enquanto o modelo indicava $519.067,91, uma diferença de $17.151,54 e um erro relativo de apenas 3,2%.

## Modelo ARIMA
O modelo ARIMA utilizado é importado da biblioteca `statsmodel`.

![olist_revenue_8](https://github.com/caiocasagrande/arima_revenue/blob/main/images/olist_revenue_8.png) 

A função ARIMA mostra que prever o mesmo valor para os próximos 14 dias, *não acompanhando as oscilações de acordo com os dados originais*, ainda pode reproduzir bons resultados olhando o quadro geral.

## Modelo SARIMA
O modelo SARIMA utilizado é importado da biblioteca `statsmodel`.
![olist_revenue_9](https://github.com/caiocasagrande/arima_revenue/blob/main/images/olist_revenue_9.png)

Ao contrário do ARIMA, o modelo SARIMA foi capaz de capturar os movimentos dos dados da série temporal devido ao seu componente sazonal. 

# Resultados financeiros

<div align="center">

| Modelo       | MAE         | RMSE        | MAPE   | Soma Real    | Soma Prevista   | Diferença    | Erro Relativo    |
|--------------|-------------|-------------|--------|--------------|------------------|--------------|-------------------|
| Auto ARIMA   | $4,783.97   | $6,284.02   | 17.11% | $536,219.46  | $519,067.91      | $17,151.55   | 3.20%             |
| ARIMA        | $5,853.48   | $7,641.89   | 15.11% | $536,219.46  | $520,940.50      | $15,278.96   | 2.85%             |
| SARIMA       | $4,978.98   | $6,378.03   | 17.44% | $536,219.46  | $525,548.79      | $10,670.67   | 1.99%             |

</div>

- Em geral, os modelos produziram bons resultados com pequenos erros relativos para os próximos quatorze dias de receita
- Os modelos Auto ARIMA e SARIMA se destacam por serem capazes de capturar os movimentos de oscilação dos dados no futuro
- Se a empresa tivesse utilizado a média para previsão como *baseline* ($322.182,84) seria um Erro Relativo de quase 40%, confirmando os ótimos resultados dos modelos testados

### 🎯 Agora, munida de modelos de previsão com baixos erros, a Olist pode prever receitas a fim de melhorar sua organização financeira, otimizar os recursos necessários e planejar investimentos para o futuro.

## Próximos Passos
- Estudar o impacto da Black Friday nos dados. Deve ser removido? Deve ser suavizado?
- Aplicar o teste Ljung-Box nos resíduos para verificar sua autocorrelação
- Testar outros modelos como o XGBoost para comparar os resultados
- Usar validação cruzada para melhorar o modelo
- Incorporar outras variáveis e usar modelos multivariados de séries temporais como VAR e VEC para previsão





