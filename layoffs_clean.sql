-- SELECT * FROM world_layoffs.layoffs;

-- create table layoffs_staging
-- like layoffs;

-- select*
-- from layoffs_staging;

-- insert layoffs_staging
-- select*
-- from layoffs;

select *
from layoffs;

select * 
from layoffs_staging;

select *,
row_number() over(
partition by company, industry, total_laid_off,percentage_laid_off, `date`) as row_num
from layoffs_staging;

with duplicate_cte as
(
select *,
row_number() over(
partition by company,location, industry, total_laid_off,percentage_laid_off, `date`,stage,country, funds_raised_millions) as row_num
from layoffs_staging
)

delete
from duplicate_cte
where row_num>1;

select *
from layoffs_staging
where company="Casper";



CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

select *
from layoffs_staging2;

insert into layoffs_staging2
select *,
row_number() over(
partition by company,location, industry, total_laid_off,percentage_laid_off, `date`,stage,country, funds_raised_millions) as row_num
from layoffs_staging;

delete
from layoffs_staging2
where row_num>1;

select *
from layoffs_staging2
where row_num>1;

select company, trim(company)
from layoffs_staging2;

update layoffs_staging2
set company=trim(company);

select distinct industry
from layoffs_staging2
order by 1;

select *
from layoffs_staging2
where industry like "Crypto%";

update layoffs_staging2
set industry = "Crypto"
where industry like "Crypto%";

select *
from layoffs_staging2
where country like "United States%"
order by 1;

update layoffs_staging2
set country="United States"
where country like "United States%";

-- or

update layoffs_staging2
set country=trim(trailing "." from country)
where country like "United States%";

select `date`,
str_to_date(`date`, "%m/%d/%Y")
from layoffs_staging2;

update layoffs_staging2
set `date` =str_to_date(`date`, "%m/%d/%Y");

select *
from layoffs_staging2
where industry is null
or industry="";

alter table layoffs_staging2
modify column `date` date;

select *
from layoffs_staging2
where company  like "Bally%";

update layoffs_staging2 
set industry= null
where industry="";

select t1.industry, t2.industry
from layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company=t2.company
where (t1.industry is null or t1.industry="")
and t2.industry is not null;




update layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company=t2.company
set t1.industry=t2.industry 
where (t1.industry is null)
and (t2.industry is not null);

select distinct industry
from layoffs_staging2;

select *
from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null;
    
select *
from layoffs_staging2;

alter table layoffs_staging2
drop column row_num;

-- Exploratory Data Analysis 

select *
from layoffs_staging2;

select *
from layoffs_staging2
where stage ="Unknown";

select max(total_laid_off), max(percentage_laid_off)
from layoffs_staging2;

select *
from layoffs_staging2
where percentage_laid_off=1
order by funds_raised_millions desc;

select company, sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc;

select min(`date`),max(`date`)
from layoffs_staging2;

with Rolling_total as
(
select  substring(`date`,1,7) as month, sum(total_laid_off) as total_off
from layoffs_staging2
where substring(`date`,1,7) is not null
group by 1
order by 1
)
select `month`, total_off, sum(total_off) over(order by `month`) as rolling_total
from Rolling_total;

select company,year(`date`),sum(total_laid_off)
from layoffs_staging2
group by company,year(`date`)
order by 3 desc;

with company_year (Company, Years, total_laid_off) as
(
select company,year(`date`),sum(total_laid_off)
from layoffs_staging2
group by company,year(`date`)
) ,company_year_rank as
(
select *, (dense_rank() over(partition by Years order by total_laid_off desc)) as Ranking
from company_year
where Years is not null
)
select * 
from company_year_rank
where Ranking <=5




