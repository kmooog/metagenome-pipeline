import pandas as pd

df1 = pd.read_csv("/home/kumay/metagenome_data/clusterd_genes/eggnog-mapper/chunks/emapper_output.emapper.annotations",delimiter = "\t", names=["genes","seed_eggNOGortholog","seed_ortholog_evalue","seed_ortholog_score","Predicted_taxonomi_group","Predicted_protein_name","Gene_Ontology_terms" , "EC_number", "KEGG_ko", "KEGG_Pathway","KEGG_Module", "KEGG_Reaction", "KEGG_rclass","BRITE","KEGG_TC", "CAZy" , "BiGG_Reaction", "tax_scope:_eggNOG_taxonomic_level_used_for_annotation", "eggNOG_OGs" , "bestOG", "COG_Functional_Category","eggNOG_free_text_description"])
df2 = pd.read_csv("/home/kumay/metagenome_data/mapping/merged_profile.csv")

dfmerge = pd.merge(df1, df2, how='outer')
dfmerge.groupby('COG_Functional_Category').sum().to_csv('COGprofile.csv')
dfmerge.groupby('seed_eggNOGortholog').sum().to_csv('eggNOGprofile.csv')
