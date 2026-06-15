
## 1. Resumo Executivo
Este relatório analisa os dados de feedback de clientes coletados recentemente para identificar os principais gargalos de qualidade nos modelos de veículos da marca. O objetivo é isolar as falhas mais críticas que impactam diretamente a percepção de valor e a nota de satisfação dos clientes, direcionando ações corretivas imediatas para a equipe de Engenharia.

## 2. Metodologia e Dados Analisados
Foram processados registros de chamados (tickets) contendo a região do cliente, modelo do veículo, categoria do problema, nota de satisfação (escala de 1 a 5) e a descrição textual do relato. Os dados passaram por uma etapa de limpeza para tratamento de quebras de linha órfãs e isolamento de strings textuais com vírgulas internas.

## 3. Diagnóstico Crítico
### Crise 1: Instabilidade no Sistema de Entretenimento
* **Volume:** Concentra cerca de 45% das reclamações.
* **Impacto:** Média de satisfação de **1,4 estrelas**.
* **Modelo Afetado:** O problema é massivamente concentrado no **X-SUV**. Os clientes relatam telas apagando sozinhas , loops infinitos de reinicialização , falhas graves de conexão Bluetooth e travamento do GPS nativo.

> **Nota:** Os clientes relatam telas apagando sozinhas e loops infinitos.

### Crise 2: Falhas Mecânicas no Desempenho do Motor
* **Volume:** É o segundo maior gargalo em volumetria de chamados., cerca de 35% das reclamações.
* **Impacto:** Média de satisfação de **1,8 estrelas**.
* **Modelo Afetado:** O problema manifesta-se de forma crítica no **X-Sedan**. Os relatos incluem perda de força em subidas íngremes , solavancos/trancos ao trocar de marcha em alta velocidade , engasgos em acelerações rápidas e barulhos metálicos ao ligar o veículo pela manhã.

> **Nota:** O modelo X-SUV também pontua nesta categoria com relatos isolados de luz de injeção acesa precocemente.

## 4. Visualização dos Dados

![[Pasted image 20260608141824.png]]

![[Pasted image 20260608142349.png|501]]

**--- Média de Satisfação por Categoria de Problema ---**
Categoria_Problema
Sistema de Entretenimento-------------1.375000
Desempenho do Motor-----------------1.857143
Design do Interior-----------------------3.500000
Segurança-------------------------------4.666667
## 5. Recomendações Imediatas
Com base na severidade dos relatos e no impacto direto nas notas, recomendamos as seguintes ações prioritárias:
1. **Força-Tarefa de Software para o X-SUV:**
   - **Ação:** Congelar novas atualizações estéticas e focar 100% da equipe de engenharia de software no desenvolvimento de um patch de correção para a central multimídia.
   - **Foco:** Corrigir o gerenciamento de memória que causa o _loop_ de reinicialização e revisar o driver do chip Bluetooth para estabilizar a conexão.

1. **Auditoria de Componentes de Transmissão e Injeção para o X-Sedan:**
   - **Ação:** Abrir uma investigação interna com os fornecedores de componentes do motor e da transmissão do lote do X-Sedan.
   - **Foco:** Mapear o módulo de controle da transmissão (TCU) para eliminar os solavancos em alta velocidade e investigar a lubrificação/ajuste das válvulas frias para sanar o barulho metálico matinal.

1. **Monitoramento Proativo de Segurança:**
   - Embora as categorias "Segurança" tenham recebido notas excelentes (médias 4 e 5) para sensores de ponto cego e freios ABS, recomenda-se manter o monitoramento preventivo, pois falhas nessa categoria geram alto risco jurídico.

## Próximos passos para Análise de Dados
- Aprofundar a análise de sentimento das descrições dos clientes utilizando NLP
- Cruzar os dados de feedback com a tabela de vendas para entender a proporção real de carros afetados por Região

