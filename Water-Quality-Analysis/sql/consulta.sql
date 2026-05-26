create database agua;
use agua;

select * from waterquality;

select station_location,
-- informamos os "novos campos"
substring_index(station_location,',',-1) as latitude,
substring_index(station_location,',',-1) as longitude
from waterquality;

-- quando temos uma data para separar, não precisa ser o substring
select Date,
year(Date) as Ano,
month(Date) as Mês,

CASE month(date)
when 1 then 'Jan'
when 2 then 'Fev'
when 3 then 'Mar'
when 4 then 'Abr'
when 5 then 'Mai'
when 6 then 'Jun'
when 7 then 'Jul'
when 8 then 'Ago'
when 9 then 'Set'
when 10 then 'Out'
when 11 then 'Nov'
when 12 then 'Dez'
END as 'Mês (txt)',
day(Date) as Dia
from waterquality;

-- criando nossa "tabela" para o power binlog
-- inicialmente consultamos a tabela e deixamos no modo ideal
-- caso de uso: USUARIO SEM PRIVILEGIO DE CRIAR TABELAS E VIEWS

-- passo 1: consulta padrão
select * from waterquality;
-- pensando que nao temos privilegio para criar uma view

-- PROBLEMA: quando fazemos consulta personalizada devemos informar todos os campos necessarios

select station_id as "id da estação",
substring_index(station_location,',',1) as latitude,
substring_index(station_location,',',-1) as longitude,
date,
elt(month(date), 'jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez') as "mês",
pH, Dissolved_Oxygen, Turbidity, Nitrogen, Phosphorus,rainfall,land_use,pollution_event,fish_population
from waterquality;