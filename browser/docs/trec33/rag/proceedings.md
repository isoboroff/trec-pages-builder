# Proceedings - Retrieval-Augmented Generation 2024

#### Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks

_Lukas Gienapp,  Maik Fröbe,  Jan Heinrich Merker,  Harrisen Scells,  Eric Oliver Schmidt,  Matti Wiegmann,  Martin Potthast,  Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf)
- :material-file-search: **Runs:** [webis-01](./runs.md#webis-01) | [webis-02](./runs.md#webis-02) | [webis-03](./runs.md#webis-03) | [webis-04](./runs.md#webis-04) | [webis-05](./runs.md#webis-05) | [webis-ag-run0-taskrag](./runs.md#webis-ag-run0-taskrag) | [webis-ag-run1-taskrag](./runs.md#webis-ag-run1-taskrag) | [webis-ag-run3-reuserag](./runs.md#webis-ag-run3-reuserag) | [webis-ag-run2-reuserag](./runs.md#webis-ag-run2-reuserag) | [webis-manual](./runs.md#webis-manual) | [webis-rag-run0-taskrag](./runs.md#webis-rag-run0-taskrag) | [webis-rag-run1-taskrag](./runs.md#webis-rag-run1-taskrag) | [webis-rag-run3-taskrag](./runs.md#webis-rag-run3-taskrag) | [webis-rag-run4-reuserag](./runs.md#webis-rag-run4-reuserag) | [webis-rag-run5-reuserag](./runs.md#webis-rag-run5-reuserag)

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

#### The University of Stavanger (IAI) at the TREC 2024 Retrieval-Augmented Generation Track

_Weronika Lajewska,  Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [uis-iai](./participants.md#uis-iai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/uis-iai.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/uis-iai.rag.pdf)
- :material-file-search: **Runs:** [ginger_top_5](./runs.md#ginger_top_5) | [baseline_top_5](./runs.md#baseline_top_5) | [ginger-fluency_top_5](./runs.md#ginger-fluency_top_5) | [ginger-fluency_top_10](./runs.md#ginger-fluency_top_10) | [ginger-fluency_top_20](./runs.md#ginger-fluency_top_20)

??? abstract "Abstract"
	
	This paper describes the participation of the IAI group at the University of Stavanger in the TREC 2024 Retrieval-Augmented Generation track. We employ a modular pipeline for Grounded Information Nugget-based GEneration of Conversational Information-Seeking Responses (GINGER) to ensure factual correctness and source attribution. The multistage process includes detecting, clustering, and ranking information nuggets, summarizing top clusters, and generating follow-up questions based on uncovered subspaces of relevant information. In our runs, we experiment with different length of the responses and different number of input passages. Preliminary results indicate that ours was one of the top performing systems in the augmented generation task.
	

??? quote "Bibtex"
	```
	@inproceedings{uis-iai-trec2024-papers-proc-1,
		title = {The University of Stavanger (IAI) at the TREC 2024 Retrieval-Augmented Generation Track},
		author = {Weronika Lajewska and Krisztian Balog},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Laboratory for Analytic Sciences in TREC 2024 Retrieval Augmented Generation Track

_Yue Wang,  John M. Conroy,  Neil Molino,  Julia Yang,  Mike Green_

- :fontawesome-solid-user-group: **Participant:** [ncsu-las](./participants.md#ncsu-las)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/ncsu-las.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/ncsu-las.rag.pdf)
- :material-file-search: **Runs:** [LAS_ENN_T5_RERANKED_MXBAI](./runs.md#las_enn_t5_reranked_mxbai) | [LAS-splade-mxbai-rrf](./runs.md#las-splade-mxbai-rrf) | [LAS-splade-mxbai](./runs.md#las-splade-mxbai) | [LAS_enn_t5](./runs.md#las_enn_t5) | [LAS_ann_t5_qdrant](./runs.md#las_ann_t5_qdrant) | [LAS-splade-mxbai-rrf-mmr8](./runs.md#las-splade-mxbai-rrf-mmr8) | [LAS-splade-mxbai-mmr8-RAG](./runs.md#las-splade-mxbai-mmr8-rag) | [LAS-T5-mxbai-mmr8-RAG](./runs.md#las-t5-mxbai-mmr8-rag) | [LAS-splade-mxbai-rrf-mmr8-doc](./runs.md#las-splade-mxbai-rrf-mmr8-doc) | [LAS_splad_mxbai-rrf-occams_50_RAG](./runs.md#las_splad_mxbai-rrf-occams_50_rag)

??? abstract "Abstract"
	
	We report on our approach to the NIST TREC 2024 retrieval-augmented generation (RAG) track. The goal of this track was to build and evaluate systems that can answer complex questions by 1) retrieving excerpts of webpages from a large text collection (hundreds of millions of excerpts taken from tens of millions of webpages); 2) summarizing relevant information within retrieved excerpts into an answer containing up to 400 words; 3) attributing each sentence in the generated summary to one or more retrieved excerpts. We participated in the retrieval (R) task and retrieval augmented generation (RAG) task.
	

??? quote "Bibtex"
	```
	@inproceedings{ncsu-las-trec2024-papers-proc-1,
		title = {Laboratory for Analytic Sciences in TREC 2024 Retrieval Augmented Generation Track},
		author = {Yue Wang and John M. Conroy and Neil Molino and Julia Yang and Mike Green},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Monster Ranking

_Charles L. A. Clarke,  Siqing Huo,  Negar Arabzadeh_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/WaterlooClarke.lateral.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/WaterlooClarke.lateral.rag.pdf)
- :material-file-search: **Runs:** [monster](./runs.md#monster) | [uwc1](./runs.md#uwc1) | [uwc2](./runs.md#uwc2) | [uwc0](./runs.md#uwc0) | [uwcCQAR](./runs.md#uwccqar) | [uwcCQA](./runs.md#uwccqa) | [uwcCQR](./runs.md#uwccqr) | [uwcCQ](./runs.md#uwccq) | [uwcBA](./runs.md#uwcba) | [uwcBQ](./runs.md#uwcbq) | [UWCrag](./runs.md#uwcrag) | [UWCrag_stepbystep](./runs.md#uwcrag_stepbystep) | [UWCgarag](./runs.md#uwcgarag)

??? quote "Bibtex"
	```
	@inproceedings{WaterlooClarke-trec2024-papers-proc-1,
		title = {Monster Ranking},
		author = {Charles L. A. Clarke and Siqing Huo and Negar Arabzadeh},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### CIR at TREC 2024 RAG: Task 2 - Augmented Generation with Diversified Segments and Knowledge Adaption

_Jüri Keller,  Björn Engelmann,  Fabian Haak,  Philipp Schaer,  Hermann Kroll,  Christin Katharina Kreutz_

- :fontawesome-solid-user-group: **Participant:** [CIR](./participants.md#cir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/CIR.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/CIR.rag.pdf)
- :material-file-search: **Runs:** [cir_gpt-4o-mini_Jaccard_50_0.5_100_301_p0](./runs.md#cir_gpt-4o-mini_jaccard_50_05_100_301_p0) | [cir_gpt-4o-mini_Jaccard_50_1.0_100_301_p0](./runs.md#cir_gpt-4o-mini_jaccard_50_10_100_301_p0) | [cir_gpt-4o-mini_Cosine_50_0.5_100_301_p1](./runs.md#cir_gpt-4o-mini_cosine_50_05_100_301_p1) | [cir_gpt-4o-mini_Cosine_50_0.25_100_301_p1](./runs.md#cir_gpt-4o-mini_cosine_50_025_100_301_p1) | [cir_gpt-4o-mini_Cosine_50_0.75_100_301_p1](./runs.md#cir_gpt-4o-mini_cosine_50_075_100_301_p1) | [cir_gpt-4o-mini_Cosine_50_1.0_100_301_p1](./runs.md#cir_gpt-4o-mini_cosine_50_10_100_301_p1) | [cir_gpt-4o-mini_Cosine_20_0.5_100_301_p1](./runs.md#cir_gpt-4o-mini_cosine_20_05_100_301_p1) | [cir_gpt-4o-mini_Cosine_50_0.5_100_301_p2](./runs.md#cir_gpt-4o-mini_cosine_50_05_100_301_p2) | [cir_gpt-4o-mini_Cosine_50_0.5_100_301_p3](./runs.md#cir_gpt-4o-mini_cosine_50_05_100_301_p3) | [cir_gpt-4o-mini_no_reranking_50_0.5_100_301_p1](./runs.md#cir_gpt-4o-mini_no_reranking_50_05_100_301_p1)

??? abstract "Abstract"
	
	This paper describes the CIR team’s participation in the TREC 2024 RAG track for task 2, augmented generation. With our approach, we intended to explore the effects of diversification of the segments that are considered in the generation as well as variations in the depths of users’ knowledge on a query topic. We describe a two-step approach that first reranks input segments such that they are as similar as possible to a query while also being as dissimilar as possible from higher ranked relevant segments. In the second step, these reranked segments are relayed to an LLM, which uses them to generate an answer to the query while referencing the segments that have contributed to specific parts of the answer. The LLM considers the varying background knowledge of potential users through our prompts.
	

??? quote "Bibtex"
	```
	@inproceedings{CIR-trec2024-papers-proc-1,
		title = {CIR at TREC 2024 RAG: Task 2 - Augmented Generation with Diversified Segments and Knowledge Adaption},
		author = {Jüri Keller and Björn Engelmann and Fabian Haak and Philipp Schaer and Hermann Kroll and Christin Katharina Kreutz},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### TREMA-UNH at TREC: RAG Systems and RUBRIC-style Evaluation

_Naghmeh Farzi,  Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/TREMA-UNH.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/TREMA-UNH.rag.pdf)
- :material-file-search: **Runs:** [Ranked_Iterative_Fact_Extraction_and_Refinement](./runs.md#ranked_iterative_fact_extraction_and_refinement) | [Enhanced_Iterative_Fact_Refinement_and_Prioritization](./runs.md#enhanced_iterative_fact_refinement_and_prioritization) | [Ranked_Iterative_Fact_Extraction_and_Refinement_RIFER_-_bm25](./runs.md#ranked_iterative_fact_extraction_and_refinement_rifer_-_bm25)

??? abstract "Abstract"
	
	The TREMA-UNH team participated in the TREC Retrieval-Augmented Generation track (RAG). In Part 1 we describe the RAG systems submitted to the Augmented Generation Task (AG) and the Retrieval-Augmented Generation Task (RAG), the latter using a BM25 retrieval model. In Part 2 we describe an alternative LLM-based evaluation method for this track using the RUBRIC Autograder Workbench approach, which won the SIGIR’24 best paper award.
	

??? quote "Bibtex"
	```
	@inproceedings{TREMA-UNH-trec2024-papers-proc-1,
		title = {TREMA-UNH at TREC: RAG Systems and RUBRIC-style Evaluation},
		author = {Naghmeh Farzi and Laura Dietz},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

