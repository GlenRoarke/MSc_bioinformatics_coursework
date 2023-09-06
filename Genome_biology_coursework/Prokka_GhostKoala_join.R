library("vroom")
library("tidyverse")
library("ggplot2")

#sets wd to location of rmd file R studio only not console
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

#load in data from prokka and ghostKoala annotations
prokka_data <- vroom("../GBG_exam/archaea_prokka/PROKKA_04032023.tsv")

ghost_koala <- vroom("../GBG_exam/GhostKoala_archaea/user.out.top")

ghost_annot <- vroom("../GBG_exam/GhostKoala_archaea/user_ko_definition.txt")

#tidy up the names
col_names <- paste0("gtax_Column_", 1:ncol(ghost_koala))
colnames(ghost_koala) <- col_names


col_names <- paste0("gann_Column_", 1:ncol(ghost_annot))
colnames(ghost_annot) <- col_names



#View data
head(prokka_data)
head(ghost_koala)
head(ghost_annot)

#rename useful columns.
ghost_koala <- ghost_koala %>% 
  rename(locus_tag = gtax_Column_1) %>% 
  rename(genus = gtax_Column_5)


ghost_annot <- ghost_annot %>%
  rename(locus_tag = gann_Column_1) %>% 
  rename(KEGG_annotation = gann_Column_3)



# clean up - locus 
ghost_koala <- ghost_koala %>% 
  mutate(locus_tag = str_replace(locus_tag, "user:", ""))


# join the two datasets via locus tag.
joined_df <- inner_join(prokka_data, ghost_koala, by = "locus_tag") %>% 
             inner_join(ghost_annot, by = "locus_tag") %>% 
  select(locus_tag, ftype, genus, gene, EC_number, COG, product , KEGG_annotation, gtax_Column_3, gtax_Column_4)


joined_df

#write output to csv
vroom_write(joined_df, "joined_data.tsv", delim = "\t")


