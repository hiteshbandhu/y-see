## this project uses the following flow for now :

### Scraping 

- scrape the `y-combinator startup directory` page for open-source, ai and web3/crypto companies in the last four bactches. link : `https://www.ycombinator.com/companies`
- visit each company page on y-combinator, scrape their page and also the links, like emails and github, official sites etc
- using their official sites, scrape their career pages constantly every 7 days : `- [] TODO : USE GHActions`
- store all this data in a `csv` file, that can be used to have chat with 

### ChatAPI/Langchain

- using langchain, make an RAG pipeline to take a user query and retrive relevant information from the csv file
- send it to the gemini api to get a result and show it with the all the links and sources
- make an api with the schema of question and get the answer

### Technologies Used : 

1. fastapi - for api
2. langchain - to make rag pipeline
3. gemini_api - the main llm to be used
4. github-actions [todo] : add a script to use scrape function every 7 days for career pages and also, update the database
5. neon-db and pinecone : for the main and vector database respectively
