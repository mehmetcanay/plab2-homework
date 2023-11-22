# Week5 homework

- [Week5 homework](#week5-homework)
  - [WikiPathways](#wikipathways)
    - [Features](#features)
    - [Objectives](#objectives)
    - [Structure of Datasets and their Relationships](#structure-of-datasets-and-their-relationships)
    - [Unique Identifiers](#unique-identifiers)
  - [Material and Methods](#material-and-methods)
    - [Libraries and Software](#libraries-and-software)
    - [Data](#data)

**author:** Mehmet Can Ay

## WikiPathways
[Wikipathways](https://www.wikipathways.org) is a platform where individuals in the scientific community collaborate to curate, create, and distribute information about biological pathways. It is a community-based effort enabling researchers, scientists, and enthusiasts to collectively organize and exchange knowledge on biological pathways in an easily accessible format. <br>

### Features

1. [Search tool](https://www.wikipathways.org/search.html): A query based database search tool, the query can be formed by using one or multiple of the following terms: pathway titles, descriptions, genes, metabolites, organisms, ontology annotations, WPIDs, and/or last-edited dates.
2. [Browse tool](https://www.wikipathways.org/#browse): The database can be browsed by selecting organisms, communities, and/or annotations. Filtering of pathway search can also be further filtered based on the browse method used.
3. [Contribution](https://www.wikipathways.org/help.html#create): Scientific community can contribute and/or curate WikiPathways database by monitoring the changes, coding new features, etc.
4. [Analyze and Publish](https://www.wikipathways.org/#analyze): With [PathVisio biological pathway editor](https://pathvisio.org) WikiPathways enable researchers to analyze their data. Noenetheless, the publishing of the pathway in WikiPathways database is allowed broadening the limits of the database.

### Objectives

1. Allowing scientists, researchers, and enthusiasts to jointly contribute to crafting and refining information on biological pathways.
2. Providing an open-access platform for sharing comprehensive knowledge about biological pathways, ensuring accessibility to a wide audience globally.
3. Fostering a community-driven environment where members work together to ensure accuracy, relevance, and completeness of pathway information.
4. Serving as an educational resource for students and researchers to understand complex biological interactions while aiding in the interpretation of experimental data.
5. Incorporating the latest findings and advancements in biological sciences, integrating with various databases to ensure pathways are up-to-date.
6. Offering tools for pathway analysis and visualization, aiding in the interpretation of biological data and facilitating a better understanding of molecular interactions.

### Structure of Datasets and their Relationships

Entry [10q11.21q11.23 copy number variation syndrome (WP5352)](https://www.wikipathways.org/pathways/WP5352.html) is used as an example. The participant terms in the graph are listed in Participants table. The table has 4 columns called Label, Type, Compact Identifier, and Comments. Label column contains the name of the participant whereas Type column specifies the type of the participant (such as Metabolite, GeneProduct, etc.). Compact Identifier column contains identifiers pointing out to other databases such as [Chemical Entities of Biological Interest (ChEBI)](https://www.ebi.ac.uk/chebi/), or [Ensembl](https://www.ensembl.org/index.html). An organism specific table containing all participants can be downloaded from the [Downloads](https://data.wikipathways.org/current/gpml/) section.

### Unique Identifiers

The database contains unique identifiers for each graph, links to other databases.

## Material and Methods

### Libraries and Software
pandas, numpy, lxml

### Data
1. [*Homo sapiens* SQL Database](./data/homo_sapiens.db)
2. [WikiPathways SQL Database](./data/pathways.db)
3. [*Homo sapiens* Sampled Data](./data/homo_sapiens.csv)
4. [WikiPathways Table](./data/pathways.csv)