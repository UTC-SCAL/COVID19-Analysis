library(htmltab)
library(data.table)
library(RPostgreSQL)

##This dataset is the count of COVID-19 cases per county in Tennessee, updated each day at 2PM
library(rvest)
url <- "https://www.tn.gov/health/cedep/ncov.html"
webpage <- read_html(url)
# tbls <- html_nodes(webpage, "table")

tbls_ls <- webpage %>%
  html_nodes("table") %>%
  html_table(fill = TRUE)

for(i in tbls_ls){
  columns = colnames(i)
  if(columns == c("County","Positive","Negative","Deaths"))
  {
    countytable = i
    countytable[is.na(countytable)] = 0
  }
  
}
remove(url, webpage, tbls_ls)

#This dataset is the projection of hospital resources necessary for the COVID-19 epidemic in the Tennessee area. 
projection <- fread("curl https://ihmecovid19storage.blob.core.windows.net/latest/ihme-covid19.zip | tar -xf- --to-stdout *Hospitalization_all_locs.csv")
projection = projection[which(projection$location_name == 'Tennessee'),]

#Covid 19 Positive numbers from John Hopkins
usadat_confirmed_time = read.csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
tndata = usadat_confirmed_time[which(usadat_confirmed_time$Province_State == 'Tennessee'),]
hamdata = tndata[which(tndata$Admin2 == 'Hamilton'),]

print(countytable[1])
print(hamdata[1])