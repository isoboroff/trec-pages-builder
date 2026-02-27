# Proceedings - Tip-of-the-Tongue 2024

#### OVERVIEW OF THE TREC 2024 TIP-OF-THE-TONGUE TRACK

_Jaime Arguello,  Samarth Bhargav,  Fernando Diaz,  To Eun Kim,  Yifan He,  Evangelos Kanoulas,  Bhaskar Mitra_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_tot.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_tot.pdf)
??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves re-finding an item for which the searcher does not reliably recall an identifier. ToT information requests (or queries) are verbose and tend to include several complex phenomena, making them especially difficult for existing information retrieval systems. The TREC 2024 ToT track focused on a single ad-hoc retrieval task. Participants were provided with training and development data in the movie domain. Conversely, systems were tested on data that combined three domains: movies, celebrities, and landmarks. This year, 6 groups (including the track coordinators) submitted 18 runs.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-3,
		title = {OVERVIEW OF THE TREC 2024 TIP-OF-THE-TONGUE TRACK},
		author = {Jaime Arguello and Samarth Bhargav and Fernando Diaz and To Eun Kim and Yifan He and Evangelos Kanoulas and Bhaskar Mitra},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Yale NLP at TREC 2024: Tip-of-the-Tongue Track

_Rohan Phanse,  Gabrielle Kaili-May Liu,  Arman Cohan_

- :fontawesome-solid-user-group: **Participant:** [yalenlp](./participants.md#yalenlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/yalenlp.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/yalenlp.tot.pdf)
- :material-file-search: **Runs:** [dpr-lst-rerank](./runs.md#dpr-lst-rerank) | [dpr-pnt-lst-rerank](./runs.md#dpr-pnt-lst-rerank) | [dpr-router-lst-rerank](./runs.md#dpr-router-lst-rerank)

??? abstract "Abstract"
	
	After preparing training sets for each domain, we trained a single “general” DPR model to handle queries from all domains and used it in our first two runs. In addition, we developed an approach to route queries to multiple single-domain “expert” DPR models for our third run. We used GPT-4o mini to rerank the results retrieved by our DPR models. We developed an initial pointwise reranking stage that we used along with Borges et al.’s [3] list-wise round-robin approach in our first run. We only performed listwise reranking in our other two runs to measure the specific contribution of our proposed pointwise reranking stage to overall performance.
	

??? quote "Bibtex"
	```
	@inproceedings{yalenlp-trec2024-papers-proc-1,
		title = {Yale NLP at TREC 2024: Tip-of-the-Tongue Track},
		author = {Rohan Phanse and Gabrielle Kaili-May Liu and Arman Cohan},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks

_Lukas Gienapp,  Maik Fröbe,  Jan Heinrich Merker,  Harrisen Scells,  Eric Oliver Schmidt,  Matti Wiegmann,  Martin Potthast,  Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf)
- :material-file-search: **Runs:** [webis-base](./runs.md#webis-base) | [webis-tot-01](./runs.md#webis-tot-01) | [webis-tot-02](./runs.md#webis-tot-02) | [webis-tot-04](./runs.md#webis-tot-04) | [webis-tot-03](./runs.md#webis-tot-03)

??? abstract "Abstract"
	
	In this paper, we describe the Webis Group’s participation in the 2024 edition of TREC. We participated in the Biomedical Generative Retrieval track, the Retrieval-Augmented Generation track, and the Tip-of-the-Tongue track. For the biomedical track, we applied different paradigms of retrieval-augmented generation with open- and closed-source LLMs. For the Retrieval-Augmented Generation track, we aimed to contrast manual response submissions with fully-automated responses. For the Tip-of-the-Tongue track, we employed query relaxation as in our last year’s submission (i.e., leaving out terms that likely reduce the retrieval effectiveness) that we combine with a new cross-encoder that we trained on an enriched version of the TOMT-KIS dataset.
	

??? quote "Bibtex"
	```
	@inproceedings{webis-trec2024-papers-proc-1,
		title = {Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks},
		author = {Lukas Gienapp and Maik Fröbe and Jan Heinrich Merker and Harrisen Scells and Eric Oliver Schmidt and Matti Wiegmann and Martin Potthast and Matthias Hagen},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### IISERK@ToT_2024: Query Reformulation and Layered Retrieval for Tip-of-Tongue Items

_Subinay Adhikary,  Shuvam Banerji Seal,  Soumyadeep Sar,  Dwaipayan Roy_

- :fontawesome-solid-user-group: **Participant:** [IISER-K](./participants.md#iiser-k)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/IISER-K.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/IISER-K.tot.pdf)
- :material-file-search: **Runs:** [ThinkIR_BM25](./runs.md#thinkir_bm25) | [ThinIR_BM25_layer_2](./runs.md#thinir_bm25_layer_2) | [ThinkIR_semantic](./runs.md#thinkir_semantic) | [ThinkIR_4_layer_2_w_small](./runs.md#thinkir_4_layer_2_w_small)

??? abstract "Abstract"
	
	In this study, we explore various approaches for known-item retrieval, referred to as “Tip-of-the-Tongue” (ToT). The TREC 2024 ToT track involves retrieving previously encountered items, such as movie names or landmarks when the searcher struggles to recall their exact identifiers. In this paper, we (ThinkIR) focus on four different approaches to retrieve the correct item for each query, including BM25 with optimized parameters and leveraging Large Language Models (LLMs) to reformulate the queries. Subsequently, we utilize these reformulated queries during retrieval using the BM25 model for each method. The four-step query reformulation technique, combined with two-layer retrieval, has enhanced retrieval performance in terms of NDCG and Recall. Eventually, two-layer retrieval achieves the best performance among all the runs, with a Recall@1000 of 0.8067.
	

??? quote "Bibtex"
	```
	@inproceedings{IISER-K-trec2024-papers-proc-1,
		title = {IISERK@ToT\_2024: Query Reformulation and Layered Retrieval for Tip-of-Tongue Items},
		author = {Subinay Adhikary and Shuvam Banerji Seal and Soumyadeep Sar and Dwaipayan Roy},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

