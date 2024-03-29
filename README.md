# italian-cinemas-sciviz
Project created for the "Visualizzazione Scientifica" course in 2022-2023.

# Presentation of my results
- various _jupyter notebook_ and _.py_ files (if you want to see the code)
- [powerpoint presentation (pdf)](presentazione_davide_carniselli.pdf)
- [Power BI Report (pdf)](cinema_italiani_BI.pdf)

# How I extracted the [data](#credit)
- Most of the data that i found, was in **pdf** format, the "good" thing was that the data itself was in a tabular format, so i used a tool, [tabula](https://tabula.technology/), written in java to extract the data in **csv** format. 
- I couldn't find a way to automate the process, although there is also a [python version](https://pypi.org/project/tabula-py/) of tabula, but, in this case was less effective than the original tool.
- Also, sometimes, the tool wasn't able to get all the data, or it got partial data or it merged multiple column in ones, so i had to restore the data manually. I also used an extension on vscode called [edit csv](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv), in order to facilitate this task. This is also his [github](https://github.com/janisdd/vscode-edit-csv).
- Other data was in **excel** format, but also in this case i couldn't find a way to automate the process, because the files structure was the same only for some years, and the *spreadsheet* names were different too. This time the data was fewer and the copy/paste was also easier.
- In order to create the *italian actors network graph*, i used the [TMDB API](https://developers.themoviedb.org/3/getting-started/introduction) through [tmdbsimple](https://github.com/celiao/tmdbsimple), a python wrapper for this api, and saved the data in **json** format.

# .env for TMDB api key
In order to re-run my code about the *actors network* you have to:
- get a **TMDB api key** by following the [official documentation](https://developers.themoviedb.org/3/getting-started/introduction)
  - create a **TMDB account** [here](https://www.themoviedb.org/signup)
  - then go [here](https://www.themoviedb.org/settings/api) and follow the steps
- rename the file **.env_sample** in **.env**
- open the **.env** file
- replace the placeholder with your *api key*

# Credit
- to [Cinetel/Anica](https://www.cinetel.it/pages/studi_e_ricerche.php), where you can find most of the data that i reworked
- to [SIAE](https://www.siae.it/it/cosa-facciamo/dati-dello-spettacolo/), where you can find other data that i reworked
- to [Istat](https://www.istat.it/it/archivio/222527), where you can find the shapefiles of Italy
- to [TMDB API](https://developers.themoviedb.org/3/getting-started/introduction), for the movies/actors data
