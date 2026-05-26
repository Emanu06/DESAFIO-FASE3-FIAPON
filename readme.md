# Sistema Inteligente para Colônia Espacial

## Visão geral

Este projeto implementa um sistema de monitoramento e decisão para a gestão de energia em uma colônia espacial. O código analisa dados de energia, consumo e clima, gera alertas e faz previsões de energia eólica.

## Estrutura do projeto

- `PYTHON/main.py` - ponto de entrada principal que exibe o status da colônia, calcula energia e consumo, toma decisões e gera um relatório.
- `PYTHON/data.py` - contém a base de dados da colônia.
- `PYTHON/decision.py` - lógica de decisão sobre consumo vs geração.
- `PYTHON/regression.py` - previsão de geração e energia eólica.
- `PYTHON/energy_analysis.py` - análise de energia e reserva.
- `PYTHON/utils.py` - funções utilitárias para cálculo, exibição e relatório.
- `requirements.txt` - dependências do projeto.

## Requisitos

- Python 3.8 ou superior

## Como executar

1. Abra um terminal na pasta do projeto:

```powershell
cd "c:\Users\emanu\OneDrive\Documents\FIAP-FACUL\FASE 3\DESAFIO-FASE3-FIAPON"
```

2. (Opcional) instale dependências:

```powershell
python -m pip install -r requirements.txt
```

3. Execute o script principal:

```powershell
python PYTHON/main.py
```

## O que o sistema faz

- Exibe o status atual da colônia
- Calcula energia total disponível
- Calcula consumo total
- Toma decisões de alerta conforme a diferença entre geração e consumo
- Previsão de energia eólica com regressão
- Análise de reserva de energia
- Gera relatório resumido

## Exemplo de saída

```text
Status da colônia:
... (detalhes do ambiente e energia)

Decisão: ...
Previsão de energia eólica: ...
Análise: ...
```

## Preparar para o GitHub

- Todos os arquivos do projeto foram adicionados ao repositório local.
- Um `.gitignore` foi incluído para ignorar arquivos temporários do Python e do sistema.

## Observação

Se quiser fazer commit e enviar para o GitHub, use:

```powershell
git add .
git commit -m "Adicionar projeto de colônia espacial"
git push origin main
```
