# Proceedings - Lateral Reading 2024

#### Overview of the TREC 2024 Lateral Reading Track

_Dake Zhang (University of Waterloo), Mark D. Smucker (University of Waterloo), Charles L. A. Clarke (University of Waterloo)_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_lateral.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_lateral.pdf)
??? abstract "Abstract"
	
	The current web landscape, characterized by abundant information and widespread misinformation, highlights the pressing need for people to evaluate the trustworthiness of online content effectively. However, this remains a daunting challenge for many internet users. The TREC 2024 Lateral Reading Track seeks to address this issue by supporting the use of lateral reading, a proven strategy used by professional fact-checkers, to help users evaluate news articles more effectively and efficiently. In its first year, the track had two tasks: (1) generating questions that readers should consider when assessing the trustworthiness of the given news articles, and (2) retrieving documents to help answer these questions. This paper presents an overview of the track, including its objectives, methodologies, resources, and evaluation results. Our evaluation of the submitted runs shows the significant challenges these tasks pose to existing approaches, including state-of-the-art large language models. Further details on this track can be found on its website: https://trec-dragun.github.io/.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-5,
		author = {Dake Zhang (University of Waterloo), Mark D. Smucker (University of Waterloo), Charles L. A. Clarke (University of Waterloo)},
		title = {Overview of the TREC 2024 Lateral Reading Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {coordinators},
		trec_runs = {},
		trec_tracks = {lateral},
		url = {https://trec.nist.gov/pubs/trec33/papers/Overview_lateral.pdf}
	}
	```

#### Monster Ranking

_Charles L. A. Clarke (University of Waterloo), Siqing Huo (University of Waterloo), Negar Arabzadeh (University of Waterloo)_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/WaterlooClarke.lateral.rag.pdf](https://trec.nist.gov/pubs/trec33/papers/WaterlooClarke.lateral.rag.pdf)
- :material-file-search: **Runs:** [uwclarke_auto](./runs.md#uwclarke_auto) | [uwclarke_auto_summarized](./runs.md#uwclarke_auto_summarized) | [UWClarke_rerank](./runs.md#uwclarke_rerank)

??? abstract "Abstract"
	
	Participating as the UWClarke group, we focused on the RAG track; we also submitted runs for the Lateral Reading Track. For the retrieval task (R) of the RAG Track, we attempted what we have come to call “monster ranking”. Largely ignoring cost and computational resources, monster ranking attempts to determine the best possible ranked list for a query by whatever means possible, including explicit LLM-based relevance judgments, both pointwise and pairwise. While a monster ranker could never be deployed in a production environment, its output may be valuable for evaluating cheaper and faster rankers. For the full retrieval augmented generation (RAG) task we explored two general approaches, depending on if generation happens first or second: 1) Generate an Answer and support with Retrieved Evidence (GARE). 2) Retrieve And Generate with Evidence (RAGE).
	

??? quote "Bibtex"
	```
	@inproceedings{WaterlooClarke-trec2024-papers-proc-1,
		author = {Charles L. A. Clarke (University of Waterloo), Siqing Huo (University of Waterloo), Negar Arabzadeh (University of Waterloo)},
		title = {Monster Ranking},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {WaterlooClarke},
		trec_runs = {uwclarke_auto, uwclarke_auto_summarized, UWCrag, UWCrag_stepbystep, UWCgarag, monster, uwc1, uwc2, uwc0, uwcCQAR, uwcCQA, uwcCQR, uwcCQ, uwcBA, uwcBQ, UWClarke_rerank},
		trec_tracks = {lateral.rag},
		url = {https://trec.nist.gov/pubs/trec33/papers/WaterlooClarke.lateral.rag.pdf}
	}
	```

