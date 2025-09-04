# Proceedings - Tip-of-the-Tongue 2024

#### Overview of the TREC 2024 Tip-of-the-Tongue track

_Jaime Arguello (University of North Carolina, USA), Samarth Bhargav (University of Amsterdam, Netherlands), Fernando Diaz (Carnegie Mellon University, USA), To Eun Kim (Carnegie Mellon University, USA), Yifan He (Carnegie Mellon University, USA), Evangelos Kanoulas (University of Amsterdam, Netherlands), Bhaskar Mitra (Microsoft Research, Canada)_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_tot.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_tot.pdf)
??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves re-finding an item for which the searcher does not reliably recall an identifier. ToT information requests (or queries) are verbose and tend to include several complex phenomena, making them especially difficult for existing information retrieval systems.  The TREC 2024 ToT track focused on a single ad-hoc retrieval task.  Participants were provided with training and development data in the movie domain.  Conversely, systems were tested on data that combined three domains: movies, celebrities, and landmarks.  This year, 6 groups (including the track coordinators) submitted 18 runs.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-3,
		author = {Jaime Arguello (University of North Carolina, USA), Samarth Bhargav (University of Amsterdam, Netherlands), Fernando Diaz (Carnegie Mellon University, USA), To Eun Kim (Carnegie Mellon University, USA), Yifan He (Carnegie Mellon University, USA), Evangelos Kanoulas (University of Amsterdam, Netherlands), Bhaskar Mitra (Microsoft Research, Canada)},
		title = {Overview of the TREC 2024 Tip-of-the-Tongue track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {coordinators},
		trec_runs = {},
		trec_tracks = {tot},
		url = {https://trec.nist.gov/pubs/trec33/papers/Overview_tot.pdf}
	}
	```

#### IISERK@ToT_2024:  Query Reformulation and Layered Retrieval for  Tip-of-Tongue Items

_Subinay Adhikary (IISER-K),, Shuvam Banerji Seal (IISER-K),, Soumyadeep Sar (IISER-K),, Dwaipayan Roy (IISER-K)_

- :fontawesome-solid-user-group: **Participant:** [IISER-K](./participants.md#iiser-k)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/IISER-K.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/IISER-K.tot.pdf)
- :material-file-search: **Runs:** [ThinkIR_BM25](./runs.md#thinkir_bm25) | [ThinIR_BM25_layer_2](./runs.md#thinir_bm25_layer_2) | [ThinkIR_semantic](./runs.md#thinkir_semantic) | [ThinkIR_4_layer_2_w_small](./runs.md#thinkir_4_layer_2_w_small)

??? abstract "Abstract"
	
	In this study, we explore various approaches for known-item retrieval, referred to as ``Tip-of-the-Tongue" (ToT). The TREC 2024 ToT track involves retrieving previously encountered items, such as movie names or landmarks when the searcher struggles to recall their exact identifiers. In this paper, we (ThinkIR) focus on four different approaches to retrieve the correct item for each query, including BM25 with optimized parameters and leveraging Large Language Models (LLMs) to reformulate the queries. Subsequently, we utilize these reformulated queries during retrieval using the BM25 model for each method. The four-step query reformulation technique, combined with two-layer retrieval, has enhanced retrieval performance in terms of NDCG and Recall. Eventually,  two-layer retrieval achieves the best performance among all the runs, with a Recall@1000 of 0.8067.
	

??? quote "Bibtex"
	```
	@inproceedings{IISER-K-trec2024-papers-proc-1,
		author = {Subinay Adhikary (IISER-K),, Shuvam Banerji Seal (IISER-K),, Soumyadeep Sar (IISER-K),, Dwaipayan Roy (IISER-K)},
		title = {IISERK@ToT_2024:  Query Reformulation and Layered Retrieval for  Tip-of-Tongue Items},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {IISER-K},
		trec_runs = {ThinkIR_BM25, ThinIR_BM25_layer_2, ThinkIR_semantic, ThinkIR_4_layer_2_w_small},
		trec_tracks = {tot},
		url = {https://trec.nist.gov/pubs/trec33/papers/IISER-K.tot.pdf}
	}
	```

#### Yale NLP at TREC 2024: Tip-of-the-Tongue Track

_Rohan Phanse (Yale University), Gabrielle Kaili-May Liu (Yale University), Arman Cohan (Yale University)_

- :fontawesome-solid-user-group: **Participant:** [yalenlp](./participants.md#yalenlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/yalenlp.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/yalenlp.tot.pdf)
- :material-file-search: **Runs:** [dpr-lst-rerank](./runs.md#dpr-lst-rerank) | [dpr-pnt-lst-rerank](./runs.md#dpr-pnt-lst-rerank) | [dpr-router-lst-rerank](./runs.md#dpr-router-lst-rerank)

??? abstract "Abstract"
	
	This paper describes our submissions to the TREC 2024 Tip-of-the-Tongue (ToT) track. We use a two-stage pipeline consisting of DPR-based retrieval followed by reranking with GPT-4o mini to answer ToT queries across three domains: movies, celebrities, and landmarks. Two of our runs performed retrieval using a "general" DPR model trained to handle queries from all domains. For our third run, we developed an approach to route queries to multiple "expert" DPR models each trained on a single domain. To build training sets for our DPR models, we collected existing ToT queries and generated over 100k synthetic queries using few-shot prompting with LLMs. After retrieval, results were reranked either listwise or using a combined pointwise and listwise approach. Our results demonstrate the efficacy of our three submitted approaches, which achieved NDCG@1000 scores ranging from 0.51 to 0.60.
	

??? quote "Bibtex"
	```
	@inproceedings{yalenlp-trec2024-papers-proc-1,
		author = {Rohan Phanse (Yale University), Gabrielle Kaili-May Liu (Yale University), Arman Cohan (Yale University)},
		title = {Yale NLP at TREC 2024: Tip-of-the-Tongue Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {yalenlp},
		trec_runs = {dpr-lst-rerank, dpr-pnt-lst-rerank, dpr-router-lst-rerank},
		trec_tracks = {tot},
		url = {https://trec.nist.gov/pubs/trec33/papers/yalenlp.tot.pdf}
	}
	```

#### Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks

_Maik Fröbe (Friedrich-Schiller-Universität), Lukas Gienapp (Leipzig University     ScaDS.AI), Harrisen Scells (Universität Kassel), Eric Oliver Schmidt (Martin-Luther-Universität Halle), Matti Wiegmann (Bauhaus-Universität Weimar), Martin Potthast, Universität Kassel (Universität Kassel     hessian.AI     ScaDS.AI), Matthias Hagen (Friedrich-Schiller-Universität Jena)_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf)
- :material-file-search: **Runs:** [webis-base](./runs.md#webis-base) | [webis-tot-01](./runs.md#webis-tot-01) | [webis-tot-02](./runs.md#webis-tot-02) | [webis-tot-04](./runs.md#webis-tot-04) | [webis-tot-03](./runs.md#webis-tot-03)

??? abstract "Abstract"
	
	In this paper, we describe the Webis Group's participation in the 2024~edition of TREC. We participated in the Biomedical Generative Retrieval track, the Retrieval-Augmented Generation track, and the Tip-of-the-Tongue track. For the biomedical track, we applied different paradigms of retrieval-augmented generation with open- and closed-source LLMs. For the Retrieval-Augmented Generation track, we aimed to contrast manual response submissions with fully-automated responses. For the Tip-of-the-Tongue track, we employed query relaxation as in our last year's submission (i.e., leaving out terms that likely reduce the retrieval effectiveness) that we combine with a new cross-encoder that we trained on an enriched version of the TOMT-KIS dataset.
	

??? quote "Bibtex"
	```
	@inproceedings{webis-trec2024-papers-proc-1,
		author = {Maik Fröbe (Friedrich-Schiller-Universität), Lukas Gienapp (Leipzig University & ScaDS.AI), Harrisen Scells (Universität Kassel), Eric Oliver Schmidt (Martin-Luther-Universität Halle), Matti Wiegmann (Bauhaus-Universität Weimar), Martin Potthast, Universität Kassel (Universität Kassel & hessian.AI & ScaDS.AI), Matthias Hagen (Friedrich-Schiller-Universität Jena)},
		title = {Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {webis},
		trec_runs = {webis-01, webis-02, webis-03, webis-04, webis-05, webis-ag-run0-taskrag, webis-ag-run1-taskrag, webis-manual, webis-rag-run0-taskrag, webis-rag-run1-taskrag, webis-rag-run3-taskrag, webis-ag-run3-reuserag, webis-rag-run4-reuserag, webis-rag-run5-reuserag, webis-ag-run2-reuserag, webis-1, webis-2, webis-3, webis-gpt-1, webis-gpt-4, webis-gpt-6, webis-5, webis-base, webis-tot-01, webis-tot-02, webis-tot-04, webis-tot-03},
		trec_tracks = {biogen.rag.tot},
		url = {https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf}
	}
	```

