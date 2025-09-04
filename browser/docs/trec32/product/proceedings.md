# Proceedings - Product Search 2023

#### OVERVIEW OF THE TREC 2023 PRODUCT PRODUCT SEARCH TRACK

_Daniel Campos,  Surya Kallumadi,  Corby Rosset,  Cheng Xiang Zhai,  Alessandro Magnani_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/trackorg.P.pdf](https://trec.nist.gov/pubs/trec32/papers/trackorg.P.pdf)
??? abstract "Abstract"
	
	This is the first year of the TREC Product search track. The focus this year was the creation ofa reusable collection and evaluation of the impact of the use of metadata and multi-modal data onretrieval accuracy. This year we leverage the new product search corpus, which includes contextualmetadata. Our analysis shows that in the product search domain, traditional retrieval systems arehighly effective and commonly outperform general-purpose pretrained embedding models. Ouranalysis also evaluates the impact of using simplified and metadata-enhanced collections, finding noclear trend in the impact of the expanded collection. We also see some surprising outcomes; despitetheir widespread adoption and competitive performance on other tasks, we find single-stage denseretrieval runs can commonly be noncompetitive or generate low-quality results both in the zero-shotand fine-tuned domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CamposKRZM23.bib) "
	```
	@inproceedings{DBLP:conf/trec/CamposKRZM23,
		author = {Daniel Campos and Surya Kallumadi and Corby Rosset and Cheng Xiang Zhai and Alessandro Magnani},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{OVERVIEW} {OF} {THE} {TREC} 2023 {PRODUCT} {PRODUCT} {SEARCH} {TRACK}},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/trackorg.P.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CamposKRZM23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JBNU at TREC 2023 Product Search Track

_Gi-taek An,  Woo-Seok Choi,  Jun-Yong Park,  Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [jbnu](./participants.md#jbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/jbnu.P.pdf](https://trec.nist.gov/pubs/trec32/papers/jbnu.P.pdf)
- :material-file-search: **Runs:** [JBNU-1](./runs.md#jbnu-1) | [JBNU-2](./runs.md#jbnu-2) | [JBNU-A](./runs.md#jbnu-a) | [JBNU-B](./runs.md#jbnu-b) | [JBNU-C](./runs.md#jbnu-c)

??? abstract "Abstract"
	
	This paper describes the participation of the JBNU team for TREC 2023 Product Search Track. Ourprimary focus revolves around tackling the issue of performance degradation in queries. We categorizequeries into specific and abstract types, leveraging the power of the DeBERTa deep learning model forreranking. This enhancement involves the incorporation of nine specialized tokens, such as brand, material,category, and others, and is specifically applied to queries of the specific type.1. IntroductionThe TREC 2023 Product Search Track [1] centers on information retrieval within the domain of productsearch, aiming to assist users in locating the products they desire by aligning with their objectives andintentions. Our team, JBNU, has participated in the Product Ranking Task and Product Retrieval Task.In the context of product search, we have observed the frequent occurrence of common errors in queries.Traditional typo correction methods often led to incorrect corrections for words that are not commonlyfound in dictionaries, such as product names, brand names, and author names in product search queries. Totackle this challenge, we have created a specialized dictionary designed to refine and correct product searchqueries.For all tasks, the queries undergo the following preprocessing steps:- Translation of multilingual queries to English utilizing Googletrans [4].- Typo correction in queries using a dedicated product search dictionary for Pyspellchecker [5].- Replacement of product codes (ASIN) in queries with the corresponding product titles.Furthermore, we observed a common occurrence of product attributes within queries. We pinpointedattributes from the product information that held notable relevance to the queries and integrated nine specialtokens within our deep learning methodology to ensure the attribute information substantially influencesthe learning and inference processes.We categorize queries into specific and abstract types, and our reranking process with a deep learningmodel is specifically targeted at the specific query types. These specific query types are characterized bythe inclusion of one of nine special tokens, such as brand name, color, material, and more.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnCPL23.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnCPL23,
		author = {Gi{-}taek An and Woo{-}Seok Choi and Jun{-}Yong Park and Kyung{-}Soon Lee},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{JBNU} at {TREC} 2023 Product Search Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/jbnu.P.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnCPL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2023 - h2oloo in the Product Search Challenge

_Jheng-Hong Yang,  Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.P.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.P.pdf)
- :material-file-search: **Runs:** [r_gpt3d5_turbo](./runs.md#r_gpt3d5_turbo) | [f_splade_clip_bm25](./runs.md#f_splade_clip_bm25) | [f_splade_bm25](./runs.md#f_splade_bm25) | [f_gpt_rerank](./runs.md#f_gpt_rerank)

??? abstract "Abstract"
	
	This paper presents the submitted runs for the TREC 2023 Product Search track,offering insights into our multi-stage retrieval systems designed for both end-to-end retrieval and reranking tasks. In our approach, we employed a sparsefirst-stage ranker that leveraged textual information, complemented by a densefirst-stage ranker tailored for processing visual data. Additionally, we evaluatethe effectiveness of utilizing a large-language model within the context of productsearch, shedding light on its capabilities and contributions to improving retrievalperformance. Our findings contribute to the ongoing discourse on enhancingproduct search techniques, showcasing the potential of combining various retrievalstrategies and advanced language models for enhanced search accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangL23.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangL23,
		author = {Jheng{-}Hong Yang and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2023 - h2oloo in the Product Search Challenge},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/h2oloo.P.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CFDA & CLIP Labs at TREC'23 Product Search Track

_Jia-Huei Ju,  Chung-Kang Lo,  Yao-Cheng Lu,  Kuan-Lin Lai,  Cheng-Wei Huang,  Wei-Hsin Chiu,  Ming-Feng Tsai,  Chuan-Ju Wang_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CFDA_CLIP.P.pdf](https://trec.nist.gov/pubs/trec32/papers/CFDA_CLIP.P.pdf)
- :material-file-search: **Runs:** [cfdaclip_ER_A](./runs.md#cfdaclip_er_a) | [cfdaclip_ER_B](./runs.md#cfdaclip_er_b) | [cfdaclip_MR_A](./runs.md#cfdaclip_mr_a) | [cfdaclip_MR_B](./runs.md#cfdaclip_mr_b)

??? abstract "Abstract"
	
	In this notebook, we present our pipeline approach for the prod-uct search track. We utilize both product textual data and imagesto enhance retrieval diversity. Our experiments also demonstratethe good generalization capability of a few off-the-shelf retrievalmodels. Additionally, we adopt retrieval fusion and consider it anefficient method to integrate text and images for product search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuLLLHCTW23.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuLLLHCTW23,
		author = {Jia{-}Huei Ju and Chung{-}Kang Lo and Yao{-}Cheng Lu and Kuan{-}Lin Lai and Cheng{-}Wei Huang and Wei{-}Hsin Chiu and Ming{-}Feng Tsai and Chuan{-}Ju Wang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CFDA} {\&} {CLIP} Labs at TREC'23 Product Search Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CFDA\_CLIP.P.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JuLLLHCTW23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

