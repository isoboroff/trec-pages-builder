# Proceedings - CrisisFACTs 2023

#### CrisisFACTS 2023 - Overview Paper

_Cody Buntain,  Amanda Lee Hughes,  Richard McCreadie,  Benjamin D. Horne,  Muhammad Imran,  Hemant Purohit_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_crisis.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_crisis.pdf)
??? abstract "Abstract"
	
	This paper describes the second and final edition of CrisisFACTS, run for TREC 2023. In this edition, we transitioned from a two-phases of manual assessment (fact identification followed by fact matching) to a single-phase approach where facts are manually identified from analysis of the output of the pooled systems and that output is matched to facts as a single step. We also introduced fact quality ratings, allowing us to distinguish between Useful, Poor, Redundant and Lagged (out-of-date) facts. We experimented with replacing the manual matching of participant outputs to facts with automatic matching techniques (both exact and semantic matching). And we added 7 new crisis events. For evaluation, we compared results from standard similarity-based summarization techniques to manual assessments and, while we show some similarity in rankings across methods, we point to paths for improving similarity-based summarization, as these methods are likely to be increasingly needed in the face of generative models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainHMHIP23.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuntainHMHIP23,
		author = {Cody Buntain and Amanda Lee Hughes and Richard McCreadie and Benjamin D. Horne and Muhammad Imran and Hemant Purohit},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CrisisFACTS 2023 - Overview Paper},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_crisis.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuntainHMHIP23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Large Language Models in Summarizing Social Media for Emergency Management

_Jayr Pereira,  Rodrigo Nogueira,  Roberto A. Lotufo_

- :fontawesome-solid-user-group: **Participant:** [NM](./participants.md#nm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/NM.F.pdf](https://trec.nist.gov/pubs/trec32/papers/NM.F.pdf)
- :material-file-search: **Runs:** [nm-gpt35](./runs.md#nm-gpt35) | [nm-gpt4](./runs.md#nm-gpt4) | [nm-gpt35-bm25](./runs.md#nm-gpt35-bm25)

??? abstract "Abstract"
	
	The exponential increase of information during crisis events necessitates efficient and real-time summarizationtechniques to aid emergency response and coordination. To this end, this study leverages the power of largelanguage models (LLMs) to summarize social media content in the context of crisis management. We introduce anovel method that combines advanced search algorithms with state-of-the-art LLMs to generate concise, relevantsummaries based on user queries. Specifically, we utilize the BM25 algorithm and the monoT5 reranker to filterthe most pertinent documents, which are then summarized using OpenAI’s GPT-3.5-turbo and GPT-4 models.Our submission to the TREC CrisisFACTS Track 2023 demonstrates that integrating the monoT5 reranker withGPT-3.5-turbo significantly reduces redundancy and enhances the comprehensiveness of summaries. This progressindicates a substantial advancement over our previous year’s efforts, reflecting the rapid evolution in the fieldof natural language processing. The capacity of the latest models to process larger contextual inputs withoutextensive data underpins their utility in streamlining the summarization process, which is vital for effective crisiscommunication.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PereiraNL23.bib) "
	```
	@inproceedings{DBLP:conf/trec/PereiraNL23,
		author = {Jayr Pereira and Rodrigo Nogueira and Roberto A. Lotufo},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Large Language Models in Summarizing Social Media for Emergency Management},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/NM.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PereiraNL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Summarizing Social Media & News Streams for Crisis-related Events  by Integrated Content-Graph Analysis: TREC-2023 CrisisFACTS Track

_Hossein Salemi,  Yasas Senarath,  Tarin Sultana Sharika,  Anuridhi Gupta,  Hemant Purohit_

- :fontawesome-solid-user-group: **Participant:** [Human_Info_Lab](./participants.md#human_info_lab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Human_Info_Lab.F.pdf](https://trec.nist.gov/pubs/trec32/papers/Human_Info_Lab.F.pdf)
- :material-file-search: **Runs:** [Human_Info_Lab-FM-B](./runs.md#human_info_lab-fm-b) | [Human_Info_Lab-FM-A](./runs.md#human_info_lab-fm-a)

??? abstract "Abstract"
	
	Extracting informative content from different sources of data like social media and news web-sites and summarizing it is critical for disaster response agencies during crises. This paper describesour proposed system to extract and rank facts from online data sources for summarizing crisis-related events in the TREC 2023 CrisisFACTS track. First, our system leverages establishedmethods such as REBEL or ClausIE to extract relevant facts from the input data stream. Then,since the summary should reflect the information needed by the response agencies, our systemfilters the extracted facts using an extended set of indicative terms used by those agencies. Wethen employ an integrated content-graph analysis to capture the similarity of facts to each other,facts to queries, and facts to indicative terms to score the importance of extracted facts. We eval-uate and compare the performance of our proposed system by utilizing two extractive methods toextract facts from the multi-stream data and score them for summarizing the crisis-related events.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SalemiSSGP23.bib) "
	```
	@inproceedings{DBLP:conf/trec/SalemiSSGP23,
		author = {Hossein Salemi and Yasas Senarath and Tarin Sultana Sharika and Anuridhi Gupta and Hemant Purohit},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Summarizing Social Media {\&} News Streams for Crisis-related Events by Integrated Content-Graph Analysis: {TREC-2023} CrisisFACTS Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Human\_Info\_Lab.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SalemiSSGP23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-Query Focused Disaster Summarization via Instruction-Based Prompting

_Philipp Seeberger,  Korbinian Riedhammer_

- :fontawesome-solid-user-group: **Participant:** [OHM](./participants.md#ohm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/OHM.F.pdf](https://trec.nist.gov/pubs/trec32/papers/OHM.F.pdf)
- :material-file-search: **Runs:** [ilp_mmr](./runs.md#ilp_mmr) | [llama_13b_chat](./runs.md#llama_13b_chat)

??? abstract "Abstract"
	
	Automatic summarization of mass-emergencyevents plays a critical role in disaster man-agement. The second edition of CrisisFACTSaims to advance disaster summarization basedon multi-stream fact-finding with a focus onweb sources such as Twitter, Reddit, Facebook,and Webnews. Here, participants are askedto develop systems that can extract key factsfrom several disaster-related events, which ul-timately serve as a summary. This paper de-scribes our method to tackle this challeng-ing task. We follow previous work and pro-pose to use a combination of retrieval, rerank-ing, and an embarrassingly simple instruction-following summarization. The two-stage re-trieval pipeline relies on BM25 and MonoT5,while the summarizer module is based on theopen-source Large Language Model (LLM)LLaMA-13b. For summarization, we explore aQuestion Answering (QA)-motivated prompt-ing approach and find the evidence useful forextracting query-relevant facts. The automaticmetrics and human evaluation show strong re-sults but also highlight the gap between open-source and proprietary systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeebergerR23.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeebergerR23,
		author = {Philipp Seeberger and Korbinian Riedhammer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multi-Query Focused Disaster Summarization via Instruction-Based Prompting},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/OHM.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SeebergerR23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Extractive Summarization, Abstractive Summarization, and Hybrid  Summarization for CrisisFACTS at TREC 2023

_Violet Burbank,  John M. Conroy,  Sean Lynch,  Neil P. Molino,  Julia S. Yang_

- :fontawesome-solid-user-group: **Participant:** [IDACCS](./participants.md#idaccs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IDACCS.F.pdf](https://trec.nist.gov/pubs/trec32/papers/IDACCS.F.pdf)
- :material-file-search: **Runs:** [IDACCS_occams_extract](./runs.md#idaccs_occams_extract) | [IDACCS_occamsHybridGPT3.5](./runs.md#idaccs_occamshybridgpt35) | [IDACCS_GPT3.5](./runs.md#idaccs_gpt35)

??? abstract "Abstract"
	
	The CrisisFACTS task seeks to find relevant, non-redundant informa-tion for an ongoing natural disaster. The task this year allowed bothextractive and abstractive summaries. This notebook describes our threesubmissions: an extractive approach using the occams summarizer andtwo abstractive approaches using GPT-3.5. Of the two abstractive sub-missions, one used GPT-3.5 on a high-scoring subset of the data, whilethe second was a hybrid, a paraphrase of an occams extractive summary.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurbankCLMY23.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurbankCLMY23,
		author = {Violet Burbank and John M. Conroy and Sean Lynch and Neil P. Molino and Julia S. Yang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Fast Extractive Summarization, Abstractive Summarization, and Hybrid Summarization for CrisisFACTS at {TREC} 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/IDACCS.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurbankCLMY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### nut-kslab at TREC 2023 CrisisFACTS track

_Phichamon Theamtun,  Takashi Yukawa_

- :fontawesome-solid-user-group: **Participant:** [nut-kslab](./participants.md#nut-kslab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/nut-kslab.F.pdf](https://trec.nist.gov/pubs/trec32/papers/nut-kslab.F.pdf)
- :material-file-search: **Runs:** [nut-kslab01](./runs.md#nut-kslab01)

??? abstract "Abstract"
	
	This notebook is the summary of our approach for the TREC CrisisFACTS 2023.  Our approach will be presented in Section 2, and our run and results will be discussed in Section 3. With run discussion and problem we faced led to our future work in Sections 4 and 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TheamtunY23.bib) "
	```
	@inproceedings{DBLP:conf/trec/TheamtunY23,
		author = {Phichamon Theamtun and Takashi Yukawa},
		editor = {Ian Soboroff and Angela Ellis},
		title = {nut-kslab at {TREC} 2023 CrisisFACTS track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/nut-kslab.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TheamtunY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Facts Summarization at the TREC 2023: IIT(BHU) in CrisisFACTs  Track

_Amit Yadav,  Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IRLAB_IIT_BHU](./participants.md#irlab_iit_bhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IRLAB_IIT_BHU.F.pdf](https://trec.nist.gov/pubs/trec32/papers/IRLAB_IIT_BHU.F.pdf)
- :material-file-search: **Runs:** [IRLabIITBHU_BM25_1](./runs.md#irlabiitbhu_bm25_1) | [IRLabIITBHU_DFReeKLIM_1](./runs.md#irlabiitbhu_dfreeklim_1) | [IRLabIITBHU_DFReeKLIM_2](./runs.md#irlabiitbhu_dfreeklim_2)

??? abstract "Abstract"
	
	The CrisisFACTS Track tackles the challenges of gathering crucial facts from diversedisaster-related events through multi-stream fact-finding. This paper presents our innovativemethod for summarizing crisis events in the TREC 2023 CrisisFACTS track. Our approachinvolves a two-step summarization process utilizing retrieval and ranking techniques. Initially,a sparse retrieval framework treats content from various online streams as a document corpus.It uses term matching to retrieve relevant contents, termed “facts”, based on specific event dayqueries. Subsequently, pre-trained models assess the semantic similarity between query-factand fact-fact pairs. These similarities are used to score and rank the facts, forming the basisfor extracting daily event summaries. Relevant data are first retrieved using the IR techniquefrom pyTerrier and then re-ranked. Top-k (k=32) posts are finally used to create summaries.Our model is not able to create good summaries for the event on a specific day. But Weare confident that this approach holds potential for yielding promising results with “BM25 +DFReeKLIM” model, especially for labels with limited resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YadavP23.bib) "
	```
	@inproceedings{DBLP:conf/trec/YadavP23,
		author = {Amit Yadav and Sukomal Pal},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Facts Summarization at the {TREC} 2023: {IIT(BHU)} in CrisisFACTs Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/IRLAB\_IIT\_BHU.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YadavP23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Crisis Events

_Jack Cheverton,  Sharon G. Small,  Ting Liu_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/SienaCLTeam.F.pdf](https://trec.nist.gov/pubs/trec32/papers/SienaCLTeam.F.pdf)
- :material-file-search: **Runs:** [Siena.Baseline1](./runs.md#sienabaseline1) | [Siena.FactTrigrams1](./runs.md#sienafacttrigrams1) | [Siena.WikiTrigrams1](./runs.md#sienawikitrigrams1) | [Siena.WikiTrigrams2](./runs.md#sienawikitrigrams2)

??? abstract "Abstract"
	
	This paper discusses our work and participation in the Text RetrievalConference (TREC) CrisisFacts Track (CFT) of 2023. Social mediasystems can be a valuable source of information for emergencyresponders during a crisis event if harnessed properly. The task ofextracting relevant information as a crisis event is unfolding is a uniqueinformation retrieval task, such that it is attempting to detect postsrelative to a specific event that is ongoing and evolving in real time. TheCFT is in its second year of fostering research in this area. The CFT teamhas supplied multi-stream datasets from several disasters, coveringTwitter, Reddit, Facebook, and online news sources (from the NELANews Collection1). We will report on our query expansion work that weimplement to participate in the CFT.1. IntroductionThe Incident Streams Track (Buntain et al., 2020), first run in 2018, is a program in theText Retrieval Conference (TREC) (Voorhees 2007). TREC is a program co-sponsored bythe National Institute of Standards and Technology (NIST) and the U.S. Department ofDefense and it focuses on supporting research in information retrieval and extraction, andto increase availability of appropriate evaluation techniques. The CFT (McCreadie &Buntain 2022) evolved from the Incident Streams Track and was run for its secondconsecutive year in 2023.Public Information Officers are tasked with monitoring social media streams inorder to identify any requests for help. There are currently no satisfactory tools to aid themin this process and it becomes mostly manual. Given that it is quite obvious thatinformation may not be provided to incident commanders in a timely fashion.The CFT is in its second year of fostering research in this area. The CFT team hassupplied multi-stream datasets from several disasters, covering Twitter, Reddit, Facebook,and online news sources (from the NELA News Collection). We had a team of twoundergraduate researchers work for 6 weeks to generate explore ideas that we believedcould potentially boost performance for this type of task. This paper discusses our workand participation in the TREC CrisisFacts Track of 2023.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChevertonSL23.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChevertonSL23,
		author = {Jack Cheverton and Sharon G. Small and Ting Liu},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Query Expansion for Crisis Events},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/SienaCLTeam.F.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChevertonSL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

