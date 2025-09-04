# Proceedings 2023

## Clinical Trials

#### UNIMIB at TREC 2023 Clinical Trials Track

_Georgios Peikos_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UNIMIB_IKR3.C.pdf](https://trec.nist.gov/pubs/trec32/papers/UNIMIB_IKR3.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [UNIMIB_IKR3](./trials/participants.md#unimib_ikr3)
- :material-file-search: **Runs:** [BM25RM3_single_run](./trials/runs.md#bm25rm3_single_run) | [BM25_two_stage](./trials/runs.md#bm25_two_stage) | [BM25RM3_gpt35_run](./trials/runs.md#bm25rm3_gpt35_run) | [BM25RM3_gpt35_strict_run](./trials/runs.md#bm25rm3_gpt35_strict_run)
??? abstract "Abstract"
	
	This notebook summarizes our participation as the UNIMIB team in the TREC 2023 Clinical Trials Track. Our research evaluates the efficacy of Large Language Models (LLMs) in assessing patient eligibility for clinical trials. For this purpose, we integrated GPT-3.5 as the final stage in our retrieval pipeline. The results indicate that GPT-3.5 may enhance the performance of retrieval tasks in this context. Nonetheless, comparable results may be attained with less complex retrieval systems that utilize BM25.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Peikos23.bib)"
	```
	@inproceedings{DBLP:conf/trec/Peikos23,
		author = {Georgios Peikos},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNIMIB} at {TREC} 2023 Clinical Trials Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/UNIMIB\_IKR3.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Peikos23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DoSSIER at TREC 2023 Clinical Trials Track

_Wojciech Kusa,  Patrick Styll,  Maximilian Seeliger,  Óscar E. Mendoza,  Allan Hanbury_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/DoSSIER.C.pdf](https://trec.nist.gov/pubs/trec32/papers/DoSSIER.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [DoSSIER](./trials/participants.md#dossier)
- :material-file-search: **Runs:** [DoSSIER_2](./trials/runs.md#dossier_2) | [DoSSIER_1](./trials/runs.md#dossier_1) | [DoSSIER_3](./trials/runs.md#dossier_3) | [DoSSIER_4](./trials/runs.md#dossier_4) | [DoSSIER_5](./trials/runs.md#dossier_5)
??? abstract "Abstract"
	
	This paper describes the experimental setup and results of the DoSSIER team’s participation in the Clinical Trials Track at TREC 2023. The primary objective of this track was to identify clinical trials for which patients meet the eligibility criteria. Our approach uses pipeline-based models, including large language models (LLMs) for query expansion and entity extraction techniques to augment both queries and documents. In our pipelines, we tested two different first-stage retrieval models, followed by a neural re-ranking framework that leverages topical relevance and eligibility criteria. We add to the pipeline a GPT-3.5-based question-answering post-processing step. Our findings demonstrate that the neural re-ranking and subsequent LLM post-processing notably enhanced performance. Future research will focus on a comprehensive assess- ment of the impact of query and document representation strategies on retrieval efficacy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KusaSSMH23.bib)"
	```
	@inproceedings{DBLP:conf/trec/KusaSSMH23,
		author = {Wojciech Kusa and Patrick Styll and Maximilian Seeliger and {\'{O}}scar E. Mendoza and Allan Hanbury},
		editor = {Ian Soboroff and Angela Ellis},
		title = {DoSSIER at {TREC} 2023 Clinical Trials Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/DoSSIER.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KusaSSMH23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MALNIS and EMA3 @ TREC 2023 Clinical Trials Track

_Mozhgan Saeidi,  Aman Jaiswal,  Abhishek Dhankar,  Alan Katz,  Evangelos E. Milios_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/EMA3.C.pdf](https://trec.nist.gov/pubs/trec32/papers/EMA3.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [EMA3](./trials/participants.md#ema3)
- :material-file-search: **Runs:** [stage1ema](./trials/runs.md#stage1ema) | [brsema3](./trials/runs.md#brsema3) | [nrema3](./trials/runs.md#nrema3) | [wrsema3](./trials/runs.md#wrsema3)
??? abstract "Abstract"
	
	This paper describes the submissions of the EMA31 team from the MALNIS2 lab to the TREC 2023 Clinical Trials Track. In our ap- proach to the TREC clinical trial matching problem, we use a two-stage process for effec- tively ranking and re-ranking clinical trials per- taining to a specific disorder. First, we identify candidate trials by matching normalized medi- cal terms and non-negated inclusion/exclusion criteria to the disorder. Then, we rank the can- didates using weighted relevance scores based on cosine similarity between contextual embed- dings of the disorder and trial criteria. We use three different weighting schemes to compute a matching score. The unique aspect of our approach lies in the innovative use of these cri- teria to filter clinical trials and in the weighted relevance scoring, which reflects the varying importance of inclusion and exclusion crite- ria. Once we have computed the weighted rel- evance score for each candidate clinical trial, we rank the clinical trials by their score. Our submission performs better in terms of Preci- sion@10 and NDCG-cut-10 than the median scores of the TREC 2023 Clinical trials track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SaeidiJDKM23.bib)"
	```
	@inproceedings{DBLP:conf/trec/SaeidiJDKM23,
		author = {Mozhgan Saeidi and Aman Jaiswal and Abhishek Dhankar and Alan Katz and Evangelos E. Milios},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{MALNIS} and {EMA3} @ {TREC} 2023 Clinical Trials Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/EMA3.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SaeidiJDKM23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team IELAB at TREC Clinical Trial Track 2023: Enhancing Clinical  Trial Retrieval with Neural Rankers and Large Language Models

_Shengyao Zhuang,  Bevan Koopman,  Guido Zuccon_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CSIRO-UQ-ielab.C.pdf](https://trec.nist.gov/pubs/trec32/papers/CSIRO-UQ-ielab.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [CSIRO-UQ-ielab](./trials/participants.md#csiro-uq-ielab)
- :material-file-search: **Runs:** [GPT4](./trials/runs.md#gpt4) | [CE_weighted](./trials/runs.md#ce_weighted) | [Hybrid](./trials/runs.md#hybrid) | [DR](./trials/runs.md#dr) | [SPLADEv2](./trials/runs.md#spladev2)
??? abstract "Abstract"
	
	We describe team ielab from CSIRO and The University of Queensland’s approach to the 2023 TREC Clinical Trials Track. Our approach was to use neural rankers but to utilise Large Language Models to overcome the issue of lack of training data for such rankers. Specifically, we employ ChatGPT to generate relevant patient descriptions for randomly selected clinical trials from the corpus. This synthetic dataset, combined with human-annotated training data from previous years, is used to train both dense and sparse retrievers based on PubmedBERT. Additionally, a cross-encoder re-ranker is integrated into the system. To further enhance the effectiveness of our approach, we prompting GPT-4 as a TREC annotator to provide judgments on our run files. These judgments are subsequently employed to re-rank the results. This architecture tightly integrates strong PubmedBERT-based rankers with the aid of SOTA Large Language Models, demonstrating a new approach to clinical trial retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuangKZ23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ZhuangKZ23,
		author = {Shengyao Zhuang and Bevan Koopman and Guido Zuccon},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Team {IELAB} at {TREC} Clinical Trial Track 2023: Enhancing Clinical Trial Retrieval with Neural Rankers and Large Language Models},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CSIRO-UQ-ielab.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuangKZ23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Matching of Patient Questionnaires to Clinical Trials with Large Language  Models

_Maciej Rybinski,  Sarvnaz Karimi_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CSIROmed.C.pdf](https://trec.nist.gov/pubs/trec32/papers/CSIROmed.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./trials/participants.md#csiromed)
- :material-file-search: **Runs:** [qe_prr_ft_rf](./trials/runs.md#qe_prr_ft_rf) | [qe_prr_zs](./trials/runs.md#qe_prr_zs) | [qe_err](./trials/runs.md#qe_err) | [qe](./trials/runs.md#qe) | [bm25_bsln](./trials/runs.md#bm25_bsln)
??? abstract "Abstract"
	
	To assist with finding eligible participants for clinical trials,the TREC 2023 Clinical Trials track sets a task where patientdata, in the form of patient questionnaires, can be used tomatch eligible patients to a relevant clinical trial. We exploreseveral query expansion and reranking methods using largelanguage models. Our best method uses query expansionwith GPT 3.5-turbo and reranking with a fine-tuned versionof the same model.CCS CONCEPTS• Information systems → Retrieval models and ranking;Language models; Decision support systems; • Applied comput-ing → Health informatics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiK23.bib)"
	```
	@inproceedings{DBLP:conf/trec/RybinskiK23,
		author = {Maciej Rybinski and Sarvnaz Karimi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Matching of Patient Questionnaires to Clinical Trials with Large Language Models},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CSIROmed.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiK23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leveraging OpenAI's Ada Embedding Model for Zero-Shot Classification  at TREC 2023 Clinical Trials

_Luke Richmond,  Priya Deshpande_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/MU_CS.C.pdf](https://trec.nist.gov/pubs/trec32/papers/MU_CS.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [MU_CS](./trials/participants.md#mu_cs)
- :material-file-search: **Runs:** [run1](./trials/runs.md#run1)
??? abstract "Abstract"
	
	This paper briefly discusses our submission to the TREC 2023 Clinical Records Track.  The track challenged participants to match patient details with medical research trials based on whether the patients were believed to be a good fit. Our method utilized OpenAI’s Ada model, a market solution for finding similarity based on given strings. By using a prebuilt solution, we sought to produce a solution that gave results better than random guessing with both low design cost and low overall monetary cost.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RichmondD23.bib)"
	```
	@inproceedings{DBLP:conf/trec/RichmondD23,
		author = {Luke Richmond and Priya Deshpande},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Leveraging OpenAI's Ada Embedding Model for Zero-Shot Classification at {TREC} 2023 Clinical Trials},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/MU\_CS.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RichmondD23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TMU at TREC Clinical Trials Track 2023

_Aritra Kumar Lahiri,  Emrul Hasan,  Qinmin Vivian Hu,  Cherie Ding_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/V-TorontoMU.C.pdf](https://trec.nist.gov/pubs/trec32/papers/V-TorontoMU.C.pdf)
- :fontawesome-solid-user-group: **Participant:** [V-TorontoMU](./trials/participants.md#v-torontomu)
- :material-file-search: **Runs:** [v1tmurun](./trials/runs.md#v1tmurun) | [v4tmurun](./trials/runs.md#v4tmurun) | [v2tmurun](./trials/runs.md#v2tmurun) | [v3tmurun](./trials/runs.md#v3tmurun)
??? abstract "Abstract"
	
	This paper describes Toronto Metropolitan University’s participation in the TREC Clinical Trials Track for 2023. As part of the tasks, we utilize ad- vanced natural language processing techniques and neural language models in our experiments to retrieve the most relevant clinical trials. We illustrate the overall methodology, experimental settings, and results of our implementation for the run submission as part of (Team - V-Ryerson).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LahiriHHD23.bib)"
	```
	@inproceedings{DBLP:conf/trec/LahiriHHD23,
		author = {Aritra Kumar Lahiri and Emrul Hasan and Qinmin Vivian Hu and Cherie Ding},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TMU} at {TREC} Clinical Trials Track 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/V-TorontoMU.C.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LahiriHHD23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## CrisisFACTs

#### CrisisFACTS 2023 - Overview Paper

_Cody Buntain,  Amanda Lee Hughes,  Richard McCreadie,  Benjamin D. Horne,  Muhammad Imran,  Hemant Purohit_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_crisis.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_crisis.pdf)
??? abstract "Abstract"
	
	This paper describes the second and final edition of CrisisFACTS, run for TREC 2023. In this edition, we transitioned from a two-phases of manual assessment (fact identification followed by fact matching) to a single-phase approach where facts are manually identified from analysis of the output of the pooled systems and that output is matched to facts as a single step. We also introduced fact quality ratings, allowing us to distinguish between Useful, Poor, Redundant and Lagged (out-of-date) facts. We experimented with replacing the manual matching of participant outputs to facts with automatic matching techniques (both exact and semantic matching). And we added 7 new crisis events. For evaluation, we compared results from standard similarity-based summarization techniques to manual assessments and, while we show some similarity in rankings across methods, we point to paths for improving similarity-based summarization, as these methods are likely to be increasingly needed in the face of generative models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainHMHIP23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/NM.F.pdf](https://trec.nist.gov/pubs/trec32/papers/NM.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [NM](./crisis/participants.md#nm)
- :material-file-search: **Runs:** [nm-gpt35](./crisis/runs.md#nm-gpt35) | [nm-gpt4](./crisis/runs.md#nm-gpt4) | [nm-gpt35-bm25](./crisis/runs.md#nm-gpt35-bm25)
??? abstract "Abstract"
	
	The exponential increase of information during crisis events necessitates efficient and real-time summarizationtechniques to aid emergency response and coordination. To this end, this study leverages the power of largelanguage models (LLMs) to summarize social media content in the context of crisis management. We introduce anovel method that combines advanced search algorithms with state-of-the-art LLMs to generate concise, relevantsummaries based on user queries. Specifically, we utilize the BM25 algorithm and the monoT5 reranker to filterthe most pertinent documents, which are then summarized using OpenAI’s GPT-3.5-turbo and GPT-4 models.Our submission to the TREC CrisisFACTS Track 2023 demonstrates that integrating the monoT5 reranker withGPT-3.5-turbo significantly reduces redundancy and enhances the comprehensiveness of summaries. This progressindicates a substantial advancement over our previous year’s efforts, reflecting the rapid evolution in the fieldof natural language processing. The capacity of the latest models to process larger contextual inputs withoutextensive data underpins their utility in streamlining the summarization process, which is vital for effective crisiscommunication.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PereiraNL23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Human_Info_Lab.F.pdf](https://trec.nist.gov/pubs/trec32/papers/Human_Info_Lab.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [Human_Info_Lab](./crisis/participants.md#human_info_lab)
- :material-file-search: **Runs:** [Human_Info_Lab-FM-B](./crisis/runs.md#human_info_lab-fm-b) | [Human_Info_Lab-FM-A](./crisis/runs.md#human_info_lab-fm-a)
??? abstract "Abstract"
	
	Extracting informative content from different sources of data like social media and news web-sites and summarizing it is critical for disaster response agencies during crises. This paper describesour proposed system to extract and rank facts from online data sources for summarizing crisis-related events in the TREC 2023 CrisisFACTS track. First, our system leverages establishedmethods such as REBEL or ClausIE to extract relevant facts from the input data stream. Then,since the summary should reflect the information needed by the response agencies, our systemfilters the extracted facts using an extended set of indicative terms used by those agencies. Wethen employ an integrated content-graph analysis to capture the similarity of facts to each other,facts to queries, and facts to indicative terms to score the importance of extracted facts. We eval-uate and compare the performance of our proposed system by utilizing two extractive methods toextract facts from the multi-stream data and score them for summarizing the crisis-related events.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SalemiSSGP23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/OHM.F.pdf](https://trec.nist.gov/pubs/trec32/papers/OHM.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [OHM](./crisis/participants.md#ohm)
- :material-file-search: **Runs:** [ilp_mmr](./crisis/runs.md#ilp_mmr) | [llama_13b_chat](./crisis/runs.md#llama_13b_chat)
??? abstract "Abstract"
	
	Automatic summarization of mass-emergencyevents plays a critical role in disaster man-agement. The second edition of CrisisFACTSaims to advance disaster summarization basedon multi-stream fact-finding with a focus onweb sources such as Twitter, Reddit, Facebook,and Webnews. Here, participants are askedto develop systems that can extract key factsfrom several disaster-related events, which ul-timately serve as a summary. This paper de-scribes our method to tackle this challeng-ing task. We follow previous work and pro-pose to use a combination of retrieval, rerank-ing, and an embarrassingly simple instruction-following summarization. The two-stage re-trieval pipeline relies on BM25 and MonoT5,while the summarizer module is based on theopen-source Large Language Model (LLM)LLaMA-13b. For summarization, we explore aQuestion Answering (QA)-motivated prompt-ing approach and find the evidence useful forextracting query-relevant facts. The automaticmetrics and human evaluation show strong re-sults but also highlight the gap between open-source and proprietary systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeebergerR23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IDACCS.F.pdf](https://trec.nist.gov/pubs/trec32/papers/IDACCS.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [IDACCS](./crisis/participants.md#idaccs)
- :material-file-search: **Runs:** [IDACCS_occams_extract](./crisis/runs.md#idaccs_occams_extract) | [IDACCS_occamsHybridGPT3.5](./crisis/runs.md#idaccs_occamshybridgpt35) | [IDACCS_GPT3.5](./crisis/runs.md#idaccs_gpt35)
??? abstract "Abstract"
	
	The CrisisFACTS task seeks to find relevant, non-redundant informa-tion for an ongoing natural disaster. The task this year allowed bothextractive and abstractive summaries. This notebook describes our threesubmissions: an extractive approach using the occams summarizer andtwo abstractive approaches using GPT-3.5. Of the two abstractive sub-missions, one used GPT-3.5 on a high-scoring subset of the data, whilethe second was a hybrid, a paraphrase of an occams extractive summary.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurbankCLMY23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/nut-kslab.F.pdf](https://trec.nist.gov/pubs/trec32/papers/nut-kslab.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [nut-kslab](./crisis/participants.md#nut-kslab)
- :material-file-search: **Runs:** [nut-kslab01](./crisis/runs.md#nut-kslab01)
??? abstract "Abstract"
	
	This notebook is the summary of our approach for the TREC CrisisFACTS 2023.  Our approach will be presented in Section 2, and our run and results will be discussed in Section 3. With run discussion and problem we faced led to our future work in Sections 4 and 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TheamtunY23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IRLAB_IIT_BHU.F.pdf](https://trec.nist.gov/pubs/trec32/papers/IRLAB_IIT_BHU.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [IRLAB_IIT_BHU](./crisis/participants.md#irlab_iit_bhu)
- :material-file-search: **Runs:** [IRLabIITBHU_BM25_1](./crisis/runs.md#irlabiitbhu_bm25_1) | [IRLabIITBHU_DFReeKLIM_1](./crisis/runs.md#irlabiitbhu_dfreeklim_1) | [IRLabIITBHU_DFReeKLIM_2](./crisis/runs.md#irlabiitbhu_dfreeklim_2)
??? abstract "Abstract"
	
	The CrisisFACTS Track tackles the challenges of gathering crucial facts from diversedisaster-related events through multi-stream fact-finding. This paper presents our innovativemethod for summarizing crisis events in the TREC 2023 CrisisFACTS track. Our approachinvolves a two-step summarization process utilizing retrieval and ranking techniques. Initially,a sparse retrieval framework treats content from various online streams as a document corpus.It uses term matching to retrieve relevant contents, termed “facts”, based on specific event dayqueries. Subsequently, pre-trained models assess the semantic similarity between query-factand fact-fact pairs. These similarities are used to score and rank the facts, forming the basisfor extracting daily event summaries. Relevant data are first retrieved using the IR techniquefrom pyTerrier and then re-ranked. Top-k (k=32) posts are finally used to create summaries.Our model is not able to create good summaries for the event on a specific day. But Weare confident that this approach holds potential for yielding promising results with “BM25 +DFReeKLIM” model, especially for labels with limited resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YadavP23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/SienaCLTeam.F.pdf](https://trec.nist.gov/pubs/trec32/papers/SienaCLTeam.F.pdf)
- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./crisis/participants.md#sienaclteam)
- :material-file-search: **Runs:** [Siena.Baseline1](./crisis/runs.md#sienabaseline1) | [Siena.FactTrigrams1](./crisis/runs.md#sienafacttrigrams1) | [Siena.WikiTrigrams1](./crisis/runs.md#sienawikitrigrams1) | [Siena.WikiTrigrams2](./crisis/runs.md#sienawikitrigrams2)
??? abstract "Abstract"
	
	This paper discusses our work and participation in the Text RetrievalConference (TREC) CrisisFacts Track (CFT) of 2023. Social mediasystems can be a valuable source of information for emergencyresponders during a crisis event if harnessed properly. The task ofextracting relevant information as a crisis event is unfolding is a uniqueinformation retrieval task, such that it is attempting to detect postsrelative to a specific event that is ongoing and evolving in real time. TheCFT is in its second year of fostering research in this area. The CFT teamhas supplied multi-stream datasets from several disasters, coveringTwitter, Reddit, Facebook, and online news sources (from the NELANews Collection1). We will report on our query expansion work that weimplement to participate in the CFT.1. IntroductionThe Incident Streams Track (Buntain et al., 2020), first run in 2018, is a program in theText Retrieval Conference (TREC) (Voorhees 2007). TREC is a program co-sponsored bythe National Institute of Standards and Technology (NIST) and the U.S. Department ofDefense and it focuses on supporting research in information retrieval and extraction, andto increase availability of appropriate evaluation techniques. The CFT (McCreadie &Buntain 2022) evolved from the Incident Streams Track and was run for its secondconsecutive year in 2023.Public Information Officers are tasked with monitoring social media streams inorder to identify any requests for help. There are currently no satisfactory tools to aid themin this process and it becomes mostly manual. Given that it is quite obvious thatinformation may not be provided to incident commanders in a timely fashion.The CFT is in its second year of fostering research in this area. The CFT team hassupplied multi-stream datasets from several disasters, covering Twitter, Reddit, Facebook,and online news sources (from the NELA News Collection). We had a team of twoundergraduate researchers work for 6 weeks to generate explore ideas that we believedcould potentially boost performance for this type of task. This paper discusses our workand participation in the TREC CrisisFacts Track of 2023.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChevertonSL23.bib)"
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

## Deep Learning

#### Overview of the TREC 2023 Deep Learning Track

_Nick Craswell,  Bhaskar Mitra,  Emine Yilmaz,  Hossein A. Rahmani,  Daniel Campos,  Jimmy Lin,  Ellen M. Voorhees,  Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_deep.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_deep.pdf)
??? abstract "Abstract"
	
	This is the fifth year of the TREC Deep Learning track. As in previous years, we leverage the MSMARCO datasets that made hundreds of thousands of human-annotated training labels availablefor both passage and document ranking tasks. We mostly repeated last year’s design, to get anothermatching test set, based on the larger, cleaner, less-biased v2 passage and document set, with passageranking as primary and document ranking as a secondary task (using labels inferred from passage).As we did last year, we sample from MS MARCO queries that were completely held out, unusedin corpus construction, unlike the test queries in the first three years. This approach yields a moredifficult test with more headroom for improvement. Alongside the usual MS MARCO (human)queries from MS MARCO, this year we generated synthetic queries using a fine-tuned T5 modeland using a GPT-4 prompt.The new headline result this year is that runs using Large Language Model (LLM) prompting insome way outperformed runs that use the “nnlm” approach, which was the best approach in theprevious four years. Since this is the last year of the track, future iterations of prompt-based rankingcan happen in other tracks. Human relevance assessments were applied to all query types, notjust human MS MARCO queries. Evaluation using synthetic queries gave similar results to humanqueries, with system ordering agreement of τ = 0.8487. However, human effort was needed toselect a subset of the synthetic queries that were usable. We did not see clear evidence of bias,where runs using GPT-4 were favored when evaluated using synthetic GPT-4 queries, or where runsusing T5 were favored when evaluated on synthetic T5 queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellMYRCLVS23.bib)"
	```
	@inproceedings{DBLP:conf/trec/CraswellMYRCLVS23,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Hossein A. Rahmani and Daniel Campos and Jimmy Lin and Ellen M. Voorhees and Ian Soboroff},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2023 Deep Learning Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_deep.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellMYRCLVS23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naverloo @ TREC Deep Learning and Neuclir 2023: As Easy as Zero,  One, Two, Three - Cascading Dual Encoders, Mono, Duo, and Listo for  Ad-Hoc Retrieval

_Carlos Lassance,  Ronak Pradeep,  Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf)
- :fontawesome-solid-user-group: **Participant:** [h2oloo](./deep/participants.md#h2oloo)
- :material-file-search: **Runs:** [agg-cocondenser](./deep/runs.md#agg-cocondenser) | [slim-pp-0shot-uw](./deep/runs.md#slim-pp-0shot-uw) | [naverloo_bm25_RR](./deep/runs.md#naverloo_bm25_rr) | [naverloo-frgpt4](./deep/runs.md#naverloo-frgpt4) | [naverloo-rgpt4](./deep/runs.md#naverloo-rgpt4) | [splade_pp_ensemble_distil](./deep/runs.md#splade_pp_ensemble_distil) | [splade_pp_self_distil](./deep/runs.md#splade_pp_self_distil) | [bm25_splades](./deep/runs.md#bm25_splades) | [naverloo_fs](./deep/runs.md#naverloo_fs) | [naverloo_fs_RR](./deep/runs.md#naverloo_fs_rr) | [naverloo_fs_RR_duo](./deep/runs.md#naverloo_fs_rr_duo) | [naverloo_bm25_splades_RR](./deep/runs.md#naverloo_bm25_splades_rr) | [D_bm25_splades](./deep/runs.md#d_bm25_splades) | [D_naverloo-frgpt4](./deep/runs.md#d_naverloo-frgpt4) | [D_naverloo_bm25_RR](./deep/runs.md#d_naverloo_bm25_rr) | [D_naverloo_bm_splade_RR](./deep/runs.md#d_naverloo_bm_splade_rr)
??? abstract "Abstract"
	
	In this notebook, we outline the architecture and evaluation of our TREC 2023submissions, which employ a sophisticated cascading multi-stage ranking frame-work comprising four distinct steps. Through experimentation across multipleconfigurations, we validate the efficacy of each stage within this hierarchy. Ourfindings demonstrate the high effectiveness of our pipeline, consistently outper-forming median benchmarks and approaching the maximal aggregate scores. No-tably, reproducibility is a key outcome of our methodology. Nevertheless, thereproducibility of the final component, termed “listo”, is contingent upon interac-tions with the proprietary and inherently non-deterministic GPT4, raising salientquestions about its consistency and reliability in a research context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassancePL23.bib)"
	```
	@inproceedings{DBLP:conf/trec/LassancePL23,
		author = {Carlos Lassance and Ronak Pradeep and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Naverloo @ {TREC} Deep Learning and Neuclir 2023: As Easy as Zero, One, Two, Three - Cascading Dual Encoders, Mono, Duo, and Listo for Ad-Hoc Retrieval},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LassancePL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at TREC 2023: Deep Learning Track and Tip-of-the-Tongue  Track

_Dake Zhang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf](https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf)
- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./deep/participants.md#uwaterloomds)
- :material-file-search: **Runs:** [WatS-LLM-Rerank](./deep/runs.md#wats-llm-rerank) | [WatS-Augmented-BM25](./deep/runs.md#wats-augmented-bm25)
??? abstract "Abstract"
	
	Our submissions to the TREC 2023 Deep LearningTrack and the Tip-of-the-Tongue Track utilized thepower of language models. For the Deep Learningtrack, we prompted a Large Language Model (LLM)to generate more queries for BM25 retrieval, whichdid not yield better performance than the BM25 base-line. We also tried to prompt the model to per-form passage assessments similar to human asses-sors, which effectively improved the ranking of thebaseline. For the Tip-of-the-Tongue track, we useda general-purpose text embedding model to performdense retrieval, achieving better performance thanthe dense retrieval baseline with a high recall. Whenwe instructed an LLM to assess whether a Wikipediapage matches a user’s description, the model did notseem to produce accurate assessments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zhang23.bib)"
	```
	@inproceedings{DBLP:conf/trec/Zhang23,
		author = {Dake Zhang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UWaterlooMDS at {TREC} 2023: Deep Learning Track and Tip-of-the-Tongue Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zhang23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Tsukuba Team at the TREC 2023 Deep Learning Track

_Kaiyu Yang,  Lingzhen Zheng,  Haitao Yu,  Sumio Fujita,  Hideo Joho_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.D.pdf](https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.D.pdf)
- :fontawesome-solid-user-group: **Participant:** [uot-yj](./deep/participants.md#uot-yj)
- :material-file-search: **Runs:** [uot-yj_rankgpt35](./deep/runs.md#uot-yj_rankgpt35) | [uot-yj_rankgpt4](./deep/runs.md#uot-yj_rankgpt4) | [uot-yj_LLMs-blender](./deep/runs.md#uot-yj_llms-blender)
??? abstract "Abstract"
	
	This paper describes the approaches used in three automatic submission runs for the TREC 2023 deep learning track specifically for the passage re-ranking task. We tested three different approaches using GPT-3.5-turbo, GPT-4, and a combination of multiple LLMs to explore effective methods for this task and demonstrated a variable performance of these methods, where none did better than the average results from the other participants in the track. These findings indicate a potential area for further exploration into how current LLMs re-rank search results, highlighting the need for careful prompt creation and model selection in information retrieval. Our work is an initial attempt to understand what LLMs can achieve and where they could be improved, offering some direction for future research in this area.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZYFJ23.bib)"
	```
	@inproceedings{DBLP:conf/trec/YangZYFJ23,
		author = {Kaiyu Yang and Lingzhen Zheng and Haitao Yu and Sumio Fujita and Hideo Joho},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Tsukuba Team at the {TREC} 2023 Deep Learning Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.D.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangZYFJ23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Topic Landscape for Question-Answering Models in Hyperbolic  Embedding Space

_Sumanta Kashyapi,  Laura Dietz_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/TREMA-UNH.D.pdf](https://trec.nist.gov/pubs/trec32/papers/TREMA-UNH.D.pdf)
- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./deep/participants.md#trema-unh)
??? abstract "Abstract"
	
	This notebook describes the submission from the TREMA-UNHteam to the TREC 2023 deep learning track. Conventional DPRsystems use dense vector representations from large language mod-els such as BERT to measure how similar queries are to candidatepassages. For effective open-domain question-answering, it’s cru-cial for the embedding model to grasp both high-level topics andtheir detailed subtopics. While recent DPR systems implicitly learntopic similarities, explicitly integrating topic taxonomies wouldbe beneficial. Vital article category scheme from Wikipedia is uti-lized to establish an overarching topic framework, and a hyperbolicembedding space is used to gain insights into topic hierarchies.When integrated into a DPR system, the entire topic landscape isconsidered while responding to a query. The resulting DPR systemis utilized to produce runs for the reranking task of TREC 2023deep learning track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiD23.bib)"
	```
	@inproceedings{DBLP:conf/trec/KashyapiD23,
		author = {Sumanta Kashyapi and Laura Dietz},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Exploring Topic Landscape for Question-Answering Models in Hyperbolic Embedding Space},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/TREMA-UNH.D.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiD23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIP at TREC Deep Learning Track 2023

_Xiaoyang Chen,  Ben He,  Le Sun,  Yingfei Sun_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CIP.D.pdf](https://trec.nist.gov/pubs/trec32/papers/CIP.D.pdf)
- :fontawesome-solid-user-group: **Participant:** [CIP](./deep/participants.md#cip)
- :material-file-search: **Runs:** [cip_run_7](./deep/runs.md#cip_run_7) | [cip_run_1](./deep/runs.md#cip_run_1) | [cip_run_2](./deep/runs.md#cip_run_2) | [cip_run_3](./deep/runs.md#cip_run_3) | [cip_run_4](./deep/runs.md#cip_run_4) | [cip_run_5](./deep/runs.md#cip_run_5) | [cip_run_6](./deep/runs.md#cip_run_6)
??? abstract "Abstract"
	
	This study presents the strategies and experimental results employed by the CIP team in the Passage Ranking task of the 2023 TREC Deep Learning Track. In the full-ranking task, we incorporated sparse retrieval methods such as Unicoil [4] and DocT5Query [6], cross- attention mechanism (MonoT5 [8]), and the recent advancements in large language models (LLM) to achieve improved sorting effectiveness. Ad- ditionally, we utilized a multi-round iterative optimization strategy for deep ranking of selected candidate documents. The experimental data suggests that by harnessing the power of existing resources, our approach has yielded favorable results in this task, without necessitating any ad- ditional training.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenHSS23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ChenHSS23,
		author = {Xiaoyang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CIP} at {TREC} Deep Learning Track 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CIP.D.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenHSS23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Generative Relevance Feedback and Convergence of Adaptive Re-Ranking:  University of Glasgow Terrier Team at TREC DL 2023

_Andrew Parry,  Thomas Jänich,  Sean MacAvaney,  Iadh Ounis_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uogTr.D.pdf](https://trec.nist.gov/pubs/trec32/papers/uogTr.D.pdf)
- :fontawesome-solid-user-group: **Participant:** [uogTr](./deep/participants.md#uogtr)
- :material-file-search: **Runs:** [uogtr_dph](./deep/runs.md#uogtr_dph) | [uogtr_dph_bo1](./deep/runs.md#uogtr_dph_bo1) | [uogtr_be](./deep/runs.md#uogtr_be) | [uogtr_se](./deep/runs.md#uogtr_se) | [uogtr_s](./deep/runs.md#uogtr_s) | [uogtr_se_gb](./deep/runs.md#uogtr_se_gb) | [uogtr_be_gb](./deep/runs.md#uogtr_be_gb) | [uogtr_qr_be_gb](./deep/runs.md#uogtr_qr_be_gb) | [uogtr_b_grf_e](./deep/runs.md#uogtr_b_grf_e) | [uogtr_qr_be](./deep/runs.md#uogtr_qr_be) | [uogtr_b_grf_e_gb](./deep/runs.md#uogtr_b_grf_e_gb)
??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2023 DeepLearning Track. We submitted runs that apply generative relevancefeedback from a large language model in both a zero-shot andpseudo-relevance feedback setting over two sparse retrieval ap-proaches, namely BM25 and SPLADE. We couple this first stagewith adaptive re-ranking over a BM25 corpus graph scored using amonoELECTRA cross-encoder. We investigate the efficacy of thesegenerative approaches for different query types in first-stage re-trieval. In re-ranking, we investigate operating points of adaptivere-ranking with different first stages to find the point in graphtraversal where the first stage no longer has an effect on the perfor-mance of the overall retrieval pipeline. We find some performancegains from the application of generative query reformulation. How-ever, our strongest run in terms of P@10 and nDCG@10 appliedboth adaptive re-ranking and generative pseudo-relevance feed-back, namely uogtr_b_grf_e_gb.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParryJMO23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ParryJMO23,
		author = {Andrew Parry and Thomas J{\"{a}}nich and Sean MacAvaney and Iadh Ounis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Generative Relevance Feedback and Convergence of Adaptive Re-Ranking: University of Glasgow Terrier Team at {TREC} {DL} 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/uogTr.D.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParryJMO23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Interactive Knowledge Assistance

#### TREC iKAT 2023: The Interactive Knowledge Assistance Track Overview

_Mohammad Aliannejadi,  Zahra Abbasiantaeb,  Shubham Chatterjee,  Jeffery Dalton,  Leif Azzopardi_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_ikat.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_ikat.pdf)
??? abstract "Abstract"
	
	Conversational Information Seeking has evolved rapidly in thelast few years with the development of Large Language Modelsproviding the basis for interpreting and responding in a natural-istic manner to user requests. iKAT emphasizes the creation andresearch of conversational search agents that adapt responses basedon the user’s prior interactions and present context. This meansthat the same question might yield varied answers, contingent onthe user’s profile and preferences. The challenge lies in enablingConversational Search Agents (CSA) to incorporate personalizedcontext to effectively guide users through the relevant informationto them. iKAT’s first year attracted seven teams and a total of 24runs. Most of the runs leveraged Large Language Models (LLMs)in their pipelines, with a few focusing on a generate-then-retrieveapproach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiACDA23.bib)"
	```
	@inproceedings{DBLP:conf/trec/AliannejadiACDA23,
		author = {Mohammad Aliannejadi and Zahra Abbasiantaeb and Shubham Chatterjee and Jeffery Dalton and Leif Azzopardi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} iKAT 2023: The Interactive Knowledge Assistance Track Overview},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_ikat.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AliannejadiACDA23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LLM-based Retrieval and Generation Pipelines for TREC Interactive  Knowledge Assistance Track (iKAT) 2023

_Zahra Abbasiantaeb,  Chuan Meng,  David Rau,  Antonis Krasakis,  Hossein A. Rahmani,  Mohammad Aliannejadi_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IRLab-Amsterdam.K.pdf](https://trec.nist.gov/pubs/trec32/papers/IRLab-Amsterdam.K.pdf)
- :fontawesome-solid-user-group: **Participant:** [IRLab-Amsterdam](./ikat/participants.md#irlab-amsterdam)
- :material-file-search: **Runs:** [run-4-GPT-4](./ikat/runs.md#run-4-gpt-4) | [run-2-llama-fine-tuned](./ikat/runs.md#run-2-llama-fine-tuned) | [run-1-llama-zero-shot](./ikat/runs.md#run-1-llama-zero-shot) | [run-3-llama-fine-tuned-manual](./ikat/runs.md#run-3-llama-fine-tuned-manual)
??? abstract "Abstract"
	
	The interactive Knowledge Assistant Track (iKAT) aims to developpersonalized conversational assistants. In this task, the persona ofthe user is provided to the system before the conversation. iKATconsists of three main tasks including, Personal Textual KnowledgeBase (PTKB) statement ranking, passage ranking, and responsegeneration. We proposed two different pipelines to approach thetask, namely, retrieve-then-generate and generate-then-retrieve. Wesubmitted three runs based on the retrieve-then-generate pipelineusing the Llama model and one run based on the generate-then-retrieve pipeline. The automatic run based on generate-then-retrievepipeline outperformed the other automatic runs in the passageranking task. This run achieved comparable results to the manualrun based on the retrieve-then-generate pipeline. For the PTKB state-ment ranking task, we proposed two approaches including rankingPTKB statements using (MiniLM12) model and using the GPT-4model as a zero-shot learner for classifying the PTKB statements asrelevant or non-relevant. The ranking approach using (MiniLM12)model achieved better performance than the classification modelapproach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbasiantaebMRKRA23.bib)"
	```
	@inproceedings{DBLP:conf/trec/AbbasiantaebMRKRA23,
		author = {Zahra Abbasiantaeb and Chuan Meng and David Rau and Antonis Krasakis and Hossein A. Rahmani and Mohammad Aliannejadi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {LLM-based Retrieval and Generation Pipelines for {TREC} Interactive Knowledge Assistance Track (iKAT) 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/IRLab-Amsterdam.K.pdf},
		timestamp = {Tue, 26 Nov 2024 17:05:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbbasiantaebMRKRA23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval Combined with Large Language Model: Summarization  Perspective

_Shivani Choudhary,  Niladri Chatterjee,  Subir Kumar Saha_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IITD.K.pdf](https://trec.nist.gov/pubs/trec32/papers/IITD.K.pdf)
- :fontawesome-solid-user-group: **Participant:** [IITD](./ikat/participants.md#iitd)
- :material-file-search: **Runs:** [run_automatic_dense_mini_LM_reranker](./ikat/runs.md#run_automatic_dense_mini_lm_reranker) | [run_automatic_llm_damo](./ikat/runs.md#run_automatic_llm_damo) | [run_automatic_dense_monot5](./ikat/runs.md#run_automatic_dense_monot5) | [run_automatic_dense_damo_canard_16000_recall](./ikat/runs.md#run_automatic_dense_damo_canard_16000_recall)
??? abstract "Abstract"
	
	Conventional information retrieval procedurestypically entail multiple stages, encompassinginformation retrieval and subsequent responsegeneration. The quality of the response derivedfrom the retrieved content significantly influ-ences the overall efficacy of the retrieval pro-cess. With the advent of large language models,it is possible to utilize larger contexts to gener-ate more cogent summaries for users. To ensurethe production of contextually grounded andpertinent responses, particularly in conversa-tional models, a good retrieval mechanism actsas a keystone. This study aims to develop a con-versational engine adept at extracting relevantdocuments and generating pertinent responsesby summarizing key passages, leveraging vari-ous types of language models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoudharyCS23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ChoudharyCS23,
		author = {Shivani Choudhary and Niladri Chatterjee and Subir Kumar Saha},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Information Retrieval Combined with Large Language Model: Summarization Perspective},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/IITD.K.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoudharyCS23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Tsukuba Team at the TREC 2023 Interactive Knowledge  Assistance Track

_Lingzhen Zheng,  Kaiyu Yang,  Haitao Yu,  Sumio Fujita,  Hideo Joho_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.K.pdf](https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.K.pdf)
- :fontawesome-solid-user-group: **Participant:** [uot-yj](./ikat/participants.md#uot-yj)
- :material-file-search: **Runs:** [uot-yj_run](./ikat/runs.md#uot-yj_run) | [uot-yj_run_llmnoptkb](./ikat/runs.md#uot-yj_run_llmnoptkb) | [uot-yj_run_rankgpt35](./ikat/runs.md#uot-yj_run_rankgpt35) | [uot-yj_run_monot5](./ikat/runs.md#uot-yj_run_monot5)
??? abstract "Abstract"
	
	In this paper, we present our approach employed in the four automatic submission runs for the TREC 2023 Interactive Knowledge Assistance Track. This track comprises three subtasks: passage ranking, response genera- tion, and Personal Text Knowledge Base (PTKB) statement ranking. Our comprehensive multi-stage pipeline for this task encompasses query rewriting, PTKB statement ranking, passage retrieval and re-ranking, and response generation. In particular, we employed fine-tuned pre-trained T5-CANARD for query rewriting, a combination of BERT, RankGPT, and MonoT5 for PTKB statement ranking, and Large Language Models (LLMs), RankGPT, and MonoT5 separately for passage re-ranking in four submission runs. For response generation, we adopted "mrm8488/t5-base-finetuned-summarize-news" from HuggingFace, which is a Text-to-Text Transfer Transformer (T5) based model that specially fine-tuned for summarization tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengYYFJ23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ZhengYYFJ23,
		author = {Lingzhen Zheng and Kaiyu Yang and Haitao Yu and Sumio Fujita and Hideo Joho},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Tsukuba Team at the {TREC} 2023 Interactive Knowledge Assistance Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.K.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhengYYFJ23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sequencing Matters: A Generate-Retrieve-Generate Model for Building  Conversational Agents

_Quinn Patwardhan,  Grace Hui Yang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/InfoSense.K.pdf](https://trec.nist.gov/pubs/trec32/papers/InfoSense.K.pdf)
- :fontawesome-solid-user-group: **Participant:** [InfoSense](./ikat/participants.md#infosense)
- :material-file-search: **Runs:** [georgetown_infosense_ikat_run_1](./ikat/runs.md#georgetown_infosense_ikat_run_1) | [georgetown_infosense_ikat_run_2](./ikat/runs.md#georgetown_infosense_ikat_run_2) | [georgetown_infosense_ikat_run_3](./ikat/runs.md#georgetown_infosense_ikat_run_3)
??? abstract "Abstract"
	
	The Text Retrieval Conference (TREC)’s Interactive KnowledgeAssistance (iKAT) Track has the goal of combining conversationaland personalizable elements with existing information retrieval(IR) technologies to facilitate information-seeking. To accomplishthis, an iKAT system is given two pieces of information from theuser: 1) a Personal Textual Knowledge Base (PTKB), which is apersistent set of a handful of factual statements about the user (like"I am lactose intolerant" or "I am afraid of roller coasters") thatlasts throughout a conversation, and 2) the user utterance, whichis usually written from an information-seeking standpoint. In anautomatic run, the system must find both the PTKBs relevant toeach utterance and provide relevant responses to both the currentutterance and the conversation history. Answers must be generatedbased on passages retrieved from the ClueWeb 22B Corpus.This paper contains what the Georgetown InfoSense group hasdone in regard to solving the challenges presented by TREC iKAT2023. Our submitted runs outperform the median runs by a sig-nificant margin, exhibiting superior performance in nDCG acrossvarious cut numbers and in overall success rate. Our approach uses aGenerate-Retrieve-Generate method, which we’ve found to greatlyoutpace Retrieve-Then-Generate approaches for the purposes ofiKAT. Our solution involves the use of Large Language Models(LLMs) for initial answers, answer grounding by BM25, passagequality filtering by logistic regression, and answer generation byLLMs again. We leverage several purpose-built Language Models,including BERT, Chat-based, and text-to-transfer-based models, fortext understanding, classification, generation, and summarization.The official results of the TREC evaluation contradict our initialself-evaluation, which may suggest that a decrease in the relianceon our retrieval and classification methods is better. Nonetheless,our findings suggest that the sequence of involving these differentcomponents matters, where we see an essentiality of using LLMsbefore using search engines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PatwardhanY23.bib)"
	```
	@inproceedings{DBLP:conf/trec/PatwardhanY23,
		author = {Quinn Patwardhan and Grace Hui Yang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Sequencing Matters: {A} Generate-Retrieve-Generate Model for Building Conversational Agents},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/InfoSense.K.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PatwardhanY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RALI@TREC iKAT 2023: Generative Query Reformulation for Conversational  Information Seeking

_Fengran Mo,  Bole Yi,  Jian-Yun Nie_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/RALI.K.pdf](https://trec.nist.gov/pubs/trec32/papers/RALI.K.pdf)
- :fontawesome-solid-user-group: **Participant:** [RALI](./ikat/participants.md#rali)
- :material-file-search: **Runs:** [ConvGQR](./ikat/runs.md#convgqr) | [LLMConvGQR](./ikat/runs.md#llmconvgqr)
??? abstract "Abstract"
	
	The Recherche Appliquée en Linguistique Informatique (RALI)team has participated in the 2023 TREC Interactive KnowledgeAssistance Track (iKAT). This paper introduces our approaches andreports our results on the passage ranking task. The most challeng-ing in conversational information seeking is to reveal the user’sreal search intent. To tackle these challenges, we employ a com-bination of query rewriting and query expansion techniques torephrase conversational queries using generative language modelsin both supervised and zero-shot manner. Furthermore, to establisha connection between query reformulation and the retrieval pro-cess, we implement a knowledge infusion mechanism to enhanceboth procedures during training. The outcome of our efforts yieldsimpressive results, with an nDCG@5 score of 16.24% and an MRRof 32.75% in our best-performing experiments. Besides, we alsoexplore the impact of personal information on the search resultsbased on GPT-4, showing that not all query turns are associatedwith personalized information needs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoYN23.bib)"
	```
	@inproceedings{DBLP:conf/trec/MoYN23,
		author = {Fengran Mo and Bole Yi and Jian{-}Yun Nie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {RALI@TREC iKAT 2023: Generative Query Reformulation for Conversational Information Seeking},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/RALI.K.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoYN23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## NeuCLIR

#### Overview of the TREC 2023 NeuCLIR Track

_Dawn J. Lawrie,  Sean MacAvaney,  James Mayfield,  Paul McNamee,  Douglas W. Oard,  Luca Soldaini,  Eugene Yang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_neuclir.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_neuclir.pdf)
??? abstract "Abstract"
	
	The principal goal of the TREC Neural Cross-Language Informa-tion Retrieval (NeuCLIR) track is to study the impact of neuralapproaches to cross-language information retrieval. The track hascreated four collections, large collections of Chinese, Persian, andRussian newswire and a smaller collection of Chinese scientificabstracts. The principal tasks are ranked retrieval of news in one ofthe three languages, using English topics. Results for a multilingualtask, also with English topics but with documents from all threenewswire collections, are also reported. New in this second yearof the track is a pilot technical documents CLIR task for rankedretrieval of Chinese technical documents using English topics. Atotal of 220 runs across all tasks were submitted by six participatingteams and, as baselines, by track coordinators. Task descriptionsand results are presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LawrieMMMOSY23.bib)"
	```
	@inproceedings{DBLP:conf/trec/LawrieMMMOSY23,
		author = {Dawn J. Lawrie and Sean MacAvaney and James Mayfield and Paul McNamee and Douglas W. Oard and Luca Soldaini and Eugene Yang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2023 NeuCLIR Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_neuclir.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LawrieMMMOSY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naverloo @ TREC Deep Learning and Neuclir 2023: As Easy as Zero,  One, Two, Three - Cascading Dual Encoders, Mono, Duo, and Listo for  Ad-Hoc Retrieval

_Carlos Lassance,  Ronak Pradeep,  Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf)
- :fontawesome-solid-user-group: **Participant:** [h2oloo](./neuclir/participants.md#h2oloo)
- :material-file-search: **Runs:** [fas-h2oloo-A1PND_SpladeMiraclMonoqt](./neuclir/runs.md#fas-h2oloo-a1pnd_splademiraclmonoqt) | [fas-h2oloo-A1PNL_spladeqt](./neuclir/runs.md#fas-h2oloo-a1pnl_spladeqt) | [fas-h2oloo-A1PND_mContrieverqt](./neuclir/runs.md#fas-h2oloo-a1pnd_mcontrieverqt) | [fas-h2oloo-A1PNS_bm25qt](./neuclir/runs.md#fas-h2oloo-a1pns_bm25qt) | [fas-h2oloo-AETD_RetroMAEReprodt](./neuclir/runs.md#fas-h2oloo-aetd_retromaereprodt) | [fas-h2oloo-AETD_SpladeMiraclENdt](./neuclir/runs.md#fas-h2oloo-aetd_splademiraclendt) | [fas-h2oloo-AETL_spladedt](./neuclir/runs.md#fas-h2oloo-aetl_spladedt) | [fas-h2oloo-AETS_bm25dt](./neuclir/runs.md#fas-h2oloo-aets_bm25dt) | [fas-h2oloo-A1NETSP_BM25s](./neuclir/runs.md#fas-h2oloo-a1netsp_bm25s) | [fas-h2oloo-A1NETHP_BM25sSplades](./neuclir/runs.md#fas-h2oloo-a1nethp_bm25ssplades) | [fas-h2oloo-A1NETHP_EverythingRun](./neuclir/runs.md#fas-h2oloo-a1nethp_everythingrun) | [fas-h2oloo-A_rgpt4](./neuclir/runs.md#fas-h2oloo-a_rgpt4) | [fas-h2oloo-A_frgpt4](./neuclir/runs.md#fas-h2oloo-a_frgpt4) | [fas-h2oloo-A_RERANKBM25s](./neuclir/runs.md#fas-h2oloo-a_rerankbm25s) | [fas-h2oloo-A_RERANKBM25sSplades](./neuclir/runs.md#fas-h2oloo-a_rerankbm25ssplades) | [fas-h2oloo-A_RERANKEverythingRun](./neuclir/runs.md#fas-h2oloo-a_rerankeverythingrun) | [rus-h2oloo-A_frgpt4](./neuclir/runs.md#rus-h2oloo-a_frgpt4) | [rus-h2oloo-A_rgpt4](./neuclir/runs.md#rus-h2oloo-a_rgpt4) | [rus-h2oloo-A_RERANKEverythingRun](./neuclir/runs.md#rus-h2oloo-a_rerankeverythingrun) | [rus-h2oloo-A_RERANKBM25sSplades](./neuclir/runs.md#rus-h2oloo-a_rerankbm25ssplades) | [rus-h2oloo-A_RERANKBM25s](./neuclir/runs.md#rus-h2oloo-a_rerankbm25s) | [rus-h2oloo-A1NETHR_EverythingRun](./neuclir/runs.md#rus-h2oloo-a1nethr_everythingrun) | [rus-h2oloo-A1NETHR_BM25sSplades](./neuclir/runs.md#rus-h2oloo-a1nethr_bm25ssplades) | [rus-h2oloo-A1NETSR_BM25s](./neuclir/runs.md#rus-h2oloo-a1netsr_bm25s) | [zho-h2oloo-A1NETSC_BM25s](./neuclir/runs.md#zho-h2oloo-a1netsc_bm25s) | [zho-h2oloo-A1NETHC_BM25sSplades](./neuclir/runs.md#zho-h2oloo-a1nethc_bm25ssplades) | [zho-h2oloo-A1NETHC_EverythingRun](./neuclir/runs.md#zho-h2oloo-a1nethc_everythingrun) | [zho-h2oloo-A_RERANKBM25s](./neuclir/runs.md#zho-h2oloo-a_rerankbm25s) | [zho-h2oloo-A_RERANKBM25sSplades](./neuclir/runs.md#zho-h2oloo-a_rerankbm25ssplades) | [zho-h2oloo-A_RERANKEverythingRun](./neuclir/runs.md#zho-h2oloo-a_rerankeverythingrun) | [zho-h2oloo-A_rgpt4](./neuclir/runs.md#zho-h2oloo-a_rgpt4) | [zho-h2oloo-A_frgpt4](./neuclir/runs.md#zho-h2oloo-a_frgpt4) | [mlir-h2oloo-A_frgpt4](./neuclir/runs.md#mlir-h2oloo-a_frgpt4) | [mlir-h2oloo-A_rgpt4](./neuclir/runs.md#mlir-h2oloo-a_rgpt4) | [mlir-h2oloo-A_RERANKEverythingRun](./neuclir/runs.md#mlir-h2oloo-a_rerankeverythingrun) | [mlir-h2oloo-A_RERANKBM25sSplades](./neuclir/runs.md#mlir-h2oloo-a_rerankbm25ssplades) | [mlir-h2oloo-A_RERANKBM25s](./neuclir/runs.md#mlir-h2oloo-a_rerankbm25s) | [mlir-h2oloo-A_EverythingRun](./neuclir/runs.md#mlir-h2oloo-a_everythingrun) | [mlir-h2oloo-A_BM25sSplades](./neuclir/runs.md#mlir-h2oloo-a_bm25ssplades) | [mlir-h2oloo-A_BM25s](./neuclir/runs.md#mlir-h2oloo-a_bm25s) | [rus-h2oloo-A1RND_mContrieverqt](./neuclir/runs.md#rus-h2oloo-a1rnd_mcontrieverqt) | [rus-h2oloo-A1RND_SpladeMiraclMonoqt](./neuclir/runs.md#rus-h2oloo-a1rnd_splademiraclmonoqt) | [rus-h2oloo-A1RNL_spladeqt](./neuclir/runs.md#rus-h2oloo-a1rnl_spladeqt) | [rus-h2oloo-A1RNS_bm25qt](./neuclir/runs.md#rus-h2oloo-a1rns_bm25qt) | [rus-h2oloo-AETD_RetroMAEReprodt](./neuclir/runs.md#rus-h2oloo-aetd_retromaereprodt) | [rus-h2oloo-AETD_SpladeMiraclENdt](./neuclir/runs.md#rus-h2oloo-aetd_splademiraclendt) | [rus-h2oloo-AETL_spladedt](./neuclir/runs.md#rus-h2oloo-aetl_spladedt) | [rus-h2oloo-AETS_bm25dt](./neuclir/runs.md#rus-h2oloo-aets_bm25dt) | [zho-h2oloo-AETS_bm25dt](./neuclir/runs.md#zho-h2oloo-aets_bm25dt) | [zho-h2oloo-AETL_spladedt](./neuclir/runs.md#zho-h2oloo-aetl_spladedt) | [zho-h2oloo-AETD_SpladeMiraclENdt](./neuclir/runs.md#zho-h2oloo-aetd_splademiraclendt) | [zho-h2oloo-AETD_RetroMAEReprodt](./neuclir/runs.md#zho-h2oloo-aetd_retromaereprodt) | [zho-h2oloo-A1CNS_bm25qt](./neuclir/runs.md#zho-h2oloo-a1cns_bm25qt) | [zho-h2oloo-A1CNL_spladeqt](./neuclir/runs.md#zho-h2oloo-a1cnl_spladeqt) | [zho-h2oloo-A1CND_SpladeMiraclMonoqt](./neuclir/runs.md#zho-h2oloo-a1cnd_splademiraclmonoqt) | [zho-h2oloo-A1CND_mContrieverqt](./neuclir/runs.md#zho-h2oloo-a1cnd_mcontrieverqt) | [tech-h2oloo-AETS_bm25dt](./neuclir/runs.md#tech-h2oloo-aets_bm25dt) | [tech-h2oloo-A1CNS_bm25qt](./neuclir/runs.md#tech-h2oloo-a1cns_bm25qt) | [tech-h2oloo-A1CND_mContrieverqt](./neuclir/runs.md#tech-h2oloo-a1cnd_mcontrieverqt) | [tech-h2oloo-A1CNL_SpladeMiraclMonoqt](./neuclir/runs.md#tech-h2oloo-a1cnl_splademiraclmonoqt) | [tech-h2oloo-A1CNL_SpladeNeuclirqt](./neuclir/runs.md#tech-h2oloo-a1cnl_spladeneuclirqt) | [tech-h2oloo-AETD_RetroMAEReprodt](./neuclir/runs.md#tech-h2oloo-aetd_retromaereprodt) | [tech-h2oloo-AETL_SpladeMiraclENdt](./neuclir/runs.md#tech-h2oloo-aetl_splademiraclendt) | [tech-h2oloo-AETL_SpladePPSDdt](./neuclir/runs.md#tech-h2oloo-aetl_spladeppsddt) | [tech-h2oloo-A1NETSC_BM25s](./neuclir/runs.md#tech-h2oloo-a1netsc_bm25s) | [tech-h2oloo-A1NETHC_BM25sSplades](./neuclir/runs.md#tech-h2oloo-a1nethc_bm25ssplades) | [tech-h2oloo-A1NETHC_EverythingRun](./neuclir/runs.md#tech-h2oloo-a1nethc_everythingrun) | [tech-h2oloo-A_BM25s_RR](./neuclir/runs.md#tech-h2oloo-a_bm25s_rr) | [tech-h2oloo-A_BM25s_fRR](./neuclir/runs.md#tech-h2oloo-a_bm25s_frr) | [tech-h2oloo-A_BM25sSplades_fRR](./neuclir/runs.md#tech-h2oloo-a_bm25ssplades_frr) | [tech-h2oloo-A_BM25sSplades_RR](./neuclir/runs.md#tech-h2oloo-a_bm25ssplades_rr) | [tech-h2oloo-A_EverythingRun_RR](./neuclir/runs.md#tech-h2oloo-a_everythingrun_rr) | [tech-h2oloo-A_EverythingRun_fRR](./neuclir/runs.md#tech-h2oloo-a_everythingrun_frr)
??? abstract "Abstract"
	
	In this notebook, we outline the architecture and evaluation of our TREC 2023submissions, which employ a sophisticated cascading multi-stage ranking frame-work comprising four distinct steps. Through experimentation across multipleconfigurations, we validate the efficacy of each stage within this hierarchy. Ourfindings demonstrate the high effectiveness of our pipeline, consistently outper-forming median benchmarks and approaching the maximal aggregate scores. No-tably, reproducibility is a key outcome of our methodology. Nevertheless, thereproducibility of the final component, termed “listo”, is contingent upon interac-tions with the proprietary and inherently non-deterministic GPT4, raising salientquestions about its consistency and reliability in a research context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassancePL23.bib)"
	```
	@inproceedings{DBLP:conf/trec/LassancePL23,
		author = {Carlos Lassance and Ronak Pradeep and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Naverloo @ {TREC} Deep Learning and Neuclir 2023: As Easy as Zero, One, Two, Three - Cascading Dual Encoders, Mono, Duo, and Listo for Ad-Hoc Retrieval},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LassancePL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISI's SEARCHER II System for TREC's 2023 NeuCLIR Track

_Scott Miller,  Shantanu Agarwal,  Joel Barry_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/ISI_SEARCHER.N.pdf](https://trec.nist.gov/pubs/trec32/papers/ISI_SEARCHER.N.pdf)
- :fontawesome-solid-user-group: **Participant:** [ISI_SEARCHER](./neuclir/participants.md#isi_searcher)
- :material-file-search: **Runs:** [zho-ISI_SEARCHER-ANE_run1](./neuclir/runs.md#zho-isi_searcher-ane_run1) | [tech-ISI_SEARCHER-ANE_run_tech_base](./neuclir/runs.md#tech-isi_searcher-ane_run_tech_base) | [tech-ISI_SEARCHER-ANE_run_tech_rr](./neuclir/runs.md#tech-isi_searcher-ane_run_tech_rr) | [tech-ISI_SEARCHER-ANE_run_tech_rr_combine](./neuclir/runs.md#tech-isi_searcher-ane_run_tech_rr_combine) | [tech-ISI_SEARCHER-ANE_run_tech_rr_combine_td](./neuclir/runs.md#tech-isi_searcher-ane_run_tech_rr_combine_td)
??? abstract "Abstract"
	
	This overviews the University of Massachusetts’s efforts in cross-lingual retrieval run submissions for the TREC 2023 NeuCLIR Track. In this cross-lingual information retrieval (CLIR) task, the search queries are written in English, and three target collections are in Chinese, Persian, and Russian. We focus on building strong ensembles of initial ranking models, including dense and sparse retrievers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MillerAB23.bib)"
	```
	@inproceedings{DBLP:conf/trec/MillerAB23,
		author = {Scott Miller and Shantanu Agarwal and Joel Barry},
		editor = {Ian Soboroff and Angela Ellis},
		title = {ISI's {SEARCHER} {II} System for TREC's 2023 NeuCLIR Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/ISI\_SEARCHER.N.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MillerAB23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2023 NeuCLIR Track

_Zhiqi Huang,  Puxuan Yu,  James Allan_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CIIR.N.pdf](https://trec.nist.gov/pubs/trec32/papers/CIIR.N.pdf)
- :fontawesome-solid-user-group: **Participant:** [CIIR](./neuclir/participants.md#ciir)
- :material-file-search: **Runs:** [fas-CIIR-LATE-SPLADE](./neuclir/runs.md#fas-ciir-late-splade) | [zho-CIIR-LATE-SPLADE](./neuclir/runs.md#zho-ciir-late-splade) | [rus-CIIR-LATE-SPLADE](./neuclir/runs.md#rus-ciir-late-splade) | [mlir-CIIR-LATE-SPLADE](./neuclir/runs.md#mlir-ciir-late-splade) | [fas-CIIR-ATEH-TransFuisonTrec23](./neuclir/runs.md#fas-ciir-ateh-transfuisontrec23) | [rus-CIIR-ATEH-TransFuisonTrec23](./neuclir/runs.md#rus-ciir-ateh-transfuisontrec23) | [zho-CIIR-ATEH-TransFuisonTrec23](./neuclir/runs.md#zho-ciir-ateh-transfuisontrec23) | [mlir-CIIR-ATEH-TransFuisonTrec23](./neuclir/runs.md#mlir-ciir-ateh-transfuisontrec23) | [fas-CIIR-ANEH-NativeFuisonTrec23](./neuclir/runs.md#fas-ciir-aneh-nativefuisontrec23) | [zho-CIIR-ANEH-NativeFuisonTrec23](./neuclir/runs.md#zho-ciir-aneh-nativefuisontrec23) | [fas-CIIR-ATEH-HybridFuisonTrec23](./neuclir/runs.md#fas-ciir-ateh-hybridfuisontrec23) | [zho-CIIR-ATEH-HybridFuisonTrec23](./neuclir/runs.md#zho-ciir-ateh-hybridfuisontrec23) | [rus-CIIR-ANEH-NativeFuisonTrec23](./neuclir/runs.md#rus-ciir-aneh-nativefuisontrec23) | [mlir-CIIR-ANEH-NativeFuisonTrec23](./neuclir/runs.md#mlir-ciir-aneh-nativefuisontrec23) | [rus-CIIR-ATEH-HybridFuisonTrec23](./neuclir/runs.md#rus-ciir-ateh-hybridfuisontrec23) | [mlir-CIIR-ATEH-HybridFuisonTrec23](./neuclir/runs.md#mlir-ciir-ateh-hybridfuisontrec23) | [tech-CIIR-ANEH-NativeFuisonTrec23](./neuclir/runs.md#tech-ciir-aneh-nativefuisontrec23) | [tech-CIIR-ATEH-TransFuisonTrec23](./neuclir/runs.md#tech-ciir-ateh-transfuisontrec23) | [tech-CIIR-ATEH-HybridFuisonTrec23](./neuclir/runs.md#tech-ciir-ateh-hybridfuisontrec23)
??? abstract "Abstract"
	
	This overviews the University of Massachusetts’s efforts in cross-lingual retrieval run submissions for the TREC 2023 NeuCLIR Track. In this cross-lingual information retrieval (CLIR) task, the search queries are written in English, and three target collections are in Chinese, Persian, and Russian. We focus on building strong ensembles of initial ranking models, including dense and sparse retrievers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangYA23.bib)"
	```
	@inproceedings{DBLP:conf/trec/HuangYA23,
		author = {Zhiqi Huang and Puxuan Yu and James Allan},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UMass at {TREC} 2023 NeuCLIR Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CIIR.N.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuangYA23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2023 NeuCLIR Track

_Eugene Yang,  Dawn J. Lawrie,  James Mayfield_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/hltcoe.N.pdf](https://trec.nist.gov/pubs/trec32/papers/hltcoe.N.pdf)
- :fontawesome-solid-user-group: **Participant:** [hltcoe](./neuclir/participants.md#hltcoe)
- :material-file-search: **Runs:** [fas-hltcoe-SEMN-PSQ-td](./neuclir/runs.md#fas-hltcoe-semn-psq-td) | [rus-hltcoe-SEMN-PSQ-td](./neuclir/runs.md#rus-hltcoe-semn-psq-td) | [zho-hltcoe-SEMN-PSQ-td](./neuclir/runs.md#zho-hltcoe-semn-psq-td) | [mlir-hltcoe-SEMN-PSQraw-td](./neuclir/runs.md#mlir-hltcoe-semn-psqraw-td) | [mlir-hltcoe-SEMN-PSQraw-t](./neuclir/runs.md#mlir-hltcoe-semn-psqraw-t) | [fas-hltcoe-SEMN-PSQ-t](./neuclir/runs.md#fas-hltcoe-semn-psq-t) | [rus-hltcoe-SEMN-PSQ-t](./neuclir/runs.md#rus-hltcoe-semn-psq-t) | [zho-hltcoe-SEMN-PSQ-t](./neuclir/runs.md#zho-hltcoe-semn-psq-t) | [fas-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./neuclir/runs.md#fas-hltcoe-demn-plaidkd-monomt5tt-td) | [rus-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./neuclir/runs.md#rus-hltcoe-demn-plaidkd-monomt5tt-td) | [zho-hltcoe-DCMN-PLAID192mono-td](./neuclir/runs.md#zho-hltcoe-dcmn-plaid192mono-td) | [fas-hltcoe-HEMN-PLAIDkd-mT5gt-td](./neuclir/runs.md#fas-hltcoe-hemn-plaidkd-mt5gt-td) | [rus-hltcoe-HEMN-PLAIDkd-mT5gt-td](./neuclir/runs.md#rus-hltcoe-hemn-plaidkd-mt5gt-td) | [zho-hltcoe-HEMN-PLAIDkd-mT5gt-dt](./neuclir/runs.md#zho-hltcoe-hemn-plaidkd-mt5gt-dt) | [fas-hltcoe-DPMN-PLAID192mono-td](./neuclir/runs.md#fas-hltcoe-dpmn-plaid192mono-td) | [rus-hltcoe-DRMN-PLAID192mono-td](./neuclir/runs.md#rus-hltcoe-drmn-plaid192mono-td) | [fas-hltcoe-HEMN2-mT5gt-td](./neuclir/runs.md#fas-hltcoe-hemn2-mt5gt-td) | [rus-hltcoe-HEMN2-mT5gt-td](./neuclir/runs.md#rus-hltcoe-hemn2-mt5gt-td) | [zho-hltcoe-HEMN2-mT5gt-dt](./neuclir/runs.md#zho-hltcoe-hemn2-mt5gt-dt) | [fas-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./neuclir/runs.md#fas-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [rus-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./neuclir/runs.md#rus-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [zho-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./neuclir/runs.md#zho-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [fas-hltcoe-MTED-plaid_v2_eng_1](./neuclir/runs.md#fas-hltcoe-mted-plaid_v2_eng_1) | [rus-hltcoe-MTED-plaid_v2_eng_1](./neuclir/runs.md#rus-hltcoe-mted-plaid_v2_eng_1) | [zho-hltcoe-MTED-plaid_v2_eng_1](./neuclir/runs.md#zho-hltcoe-mted-plaid_v2_eng_1) | [fas-hltcoe-MNED-colbertX](./neuclir/runs.md#fas-hltcoe-mned-colbertx) | [rus-hltcoe-MNED-colbertX](./neuclir/runs.md#rus-hltcoe-mned-colbertx) | [zho-hltcoe-MNED-colbertX](./neuclir/runs.md#zho-hltcoe-mned-colbertx) | [mlir-hltcoe-MNED-plaid_v1_mtt_1bit](./neuclir/runs.md#mlir-hltcoe-mned-plaid_v1_mtt_1bit) | [mlir-hltcoe-MTED-plaid_v2_eng_1](./neuclir/runs.md#mlir-hltcoe-mted-plaid_v2_eng_1) | [mlir-hltcoe-MNED-colbertX](./neuclir/runs.md#mlir-hltcoe-mned-colbertx) | [fas-hltcoe-MTES-patapscoBM25RM3td](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25rm3td) | [fas-hltcoe-MTES-patapscoBM25RM3title](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25rm3title) | [rus-hltcoe-MTES-patapscoBM25RM3td](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25rm3td) | [zho-hltcoe-MTES-patapscoBM25RM3td](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25rm3td) | [rus-hltcoe-MTES-patapscoBM25RM3title](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25rm3title) | [zho-hltcoe-MTES-patapscoBM25RM3title](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25rm3title) | [fas-hltcoe-MTES-patapscoBM25RM3desc](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25rm3desc) | [rus-hltcoe-MTES-patapscoBM25RM3desc](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25rm3desc) | [zho-hltcoe-MTES-patapscoBM25RM3desc](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25rm3desc) | [fas-hltcoe-MNES-patapscoBM25RM3td](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25rm3td) | [rus-hltcoe-MNES-patapscoBM25RM3td](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25rm3td) | [zho-hltcoe-MNES-patapscoBM25RM3td](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25rm3td) | [fas-hltcoe-MNES-patapscoBM25RM3title](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25rm3title) | [rus-hltcoe-MNES-patapscoBM25RM3title](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25rm3title) | [zho-hltcoe-MNES-patapscoBM25RM3title](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25rm3title) | [fas-hltcoe-MNES-patapscoBM25RM3desc](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25rm3desc) | [rus-hltcoe-MNES-patapscoBM25RM3desc](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25rm3desc) | [zho-hltcoe-MNES-patapscoBM25RM3desc](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25rm3desc) | [fas-hltcoe-MNPS-patapscoBM25RM3td](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25rm3td) | [rus-hltcoe-MNRS-patapscoBM25RM3td](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25rm3td) | [fas-hltcoe-MNPS-patapscoBM25RM3title](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25rm3title) | [rus-hltcoe-MNRS-patapscoBM25RM3title](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25rm3title) | [fas-hltcoe-MNPS-patapscoBM25RM3desc](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25rm3desc) | [rus-hltcoe-MNRS-patapscoBM25RM3desc](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25rm3desc) | [fas-hltcoe-MTES-patapscoBM25noRM3td](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25norm3td) | [rus-hltcoe-MTES-patapscoBM25noRM3td](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25norm3td) | [zho-hltcoe-MTES-patapscoBM25noRM3td](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25norm3td) | [fas-hltcoe-MTES-patapscoBM25noRM3title](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25norm3title) | [rus-hltcoe-MTES-patapscoBM25noRM3title](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25norm3title) | [zho-hltcoe-MTES-patapscoBM25noRM3title](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25norm3title) | [fas-hltcoe-MTES-patapscoBM25noRM3desc](./neuclir/runs.md#fas-hltcoe-mtes-patapscobm25norm3desc) | [rus-hltcoe-MTES-patapscoBM25noRM3desc](./neuclir/runs.md#rus-hltcoe-mtes-patapscobm25norm3desc) | [zho-hltcoe-MTES-patapscoBM25noRM3desc](./neuclir/runs.md#zho-hltcoe-mtes-patapscobm25norm3desc) | [fas-hltcoe-MNES-patapscoBM25noRM3td](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25norm3td) | [rus-hltcoe-MNES-patapscoBM25noRM3td](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25norm3td) | [zho-hltcoe-MNES-patapscoBM25noRM3td](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25norm3td) | [fas-hltcoe-MNES-patapscoBM25noRM3title](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25norm3title) | [rus-hltcoe-MNES-patapscoBM25noRM3title](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25norm3title) | [zho-hltcoe-MNES-patapscoBM25noRM3title](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25norm3title) | [fas-hltcoe-MNES-patapscoBM25noRM3desc](./neuclir/runs.md#fas-hltcoe-mnes-patapscobm25norm3desc) | [rus-hltcoe-MNES-patapscoBM25noRM3desc](./neuclir/runs.md#rus-hltcoe-mnes-patapscobm25norm3desc) | [zho-hltcoe-MNES-patapscoBM25noRM3desc](./neuclir/runs.md#zho-hltcoe-mnes-patapscobm25norm3desc) | [fas-hltcoe-MNPS-patapscoBM25noRM3td](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25norm3td) | [rus-hltcoe-MNRS-patapscoBM25noRM3td](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25norm3td) | [fas-hltcoe-MNPS-patapscoBM25noRM3title](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25norm3title) | [rus-hltcoe-MNRS-patapscoBM25noRM3title](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25norm3title) | [fas-hltcoe-MNPS-patapscoBM25noRM3desc](./neuclir/runs.md#fas-hltcoe-mnps-patapscobm25norm3desc) | [rus-hltcoe-MNRS-patapscoBM25noRM3desc](./neuclir/runs.md#rus-hltcoe-mnrs-patapscobm25norm3desc) | [mlir-hltcoe-MTES-patapscoBM25RM3td](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25rm3td) | [mlir-hltcoe-MTES-patapscoBM25RM3title](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25rm3title) | [mlir-hltcoe-MTES-patapscoBM25RM3desc](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25rm3desc) | [mlir-hltcoe-MTES-patapscoBM25noRM3td](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25norm3td) | [mlir-hltcoe-MTES-patapscoBM25noRM3title](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25norm3title) | [mlir-hltcoe-MTES-patapscoBM25noRM3desc](./neuclir/runs.md#mlir-hltcoe-mtes-patapscobm25norm3desc) | [zho-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./neuclir/runs.md#zho-hltcoe-demn-plaidkd-monomt5tt-td) | [mlir-hltcoe-MNED-plaid_v1_mtt_1bit_date](./neuclir/runs.md#mlir-hltcoe-mned-plaid_v1_mtt_1bit_date) | [zho-hltcoe-MNCS-patapscoBM25RM3td](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25rm3td) | [zho-hltcoe-MNCS-patapscoBM25RM3title](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25rm3title) | [zho-hltcoe-MNCS-patapscoBM25RM3desc](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25rm3desc) | [zho-hltcoe-MNCS-patapscoBM25noRM3td](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25norm3td) | [zho-hltcoe-MNCS-patapscoBM25noRM3title](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25norm3title) | [zho-hltcoe-MNCS-patapscoBM25noRM3desc](./neuclir/runs.md#zho-hltcoe-mncs-patapscobm25norm3desc) | [tech-hltcoe-MNES-psq_t_f32](./neuclir/runs.md#tech-hltcoe-mnes-psq_t_f32) | [tech-hltcoe-MNES-psq_td_f32](./neuclir/runs.md#tech-hltcoe-mnes-psq_td_f32) | [tech-hltcoe-MTES-patapsco_bm25_d_rm3](./neuclir/runs.md#tech-hltcoe-mtes-patapsco_bm25_d_rm3) | [tech-hltcoe-MTES-patapsco_bm25_td_rm3](./neuclir/runs.md#tech-hltcoe-mtes-patapsco_bm25_td_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_d_rm3](./neuclir/runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_d_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_td_rm3](./neuclir/runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_td_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_t_rm3](./neuclir/runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_t_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_d_rm3](./neuclir/runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_d_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_t_rm3](./neuclir/runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_t_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_td_rm3](./neuclir/runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_td_rm3) | [tech-hltcoe-MNEL-blade-t](./neuclir/runs.md#tech-hltcoe-mnel-blade-t) | [tech-hltcoe-MNEL-blade-d](./neuclir/runs.md#tech-hltcoe-mnel-blade-d) | [tech-hltcoe-MNEL-blade-td](./neuclir/runs.md#tech-hltcoe-mnel-blade-td) | [tech-hltcoe-2MNEH-rerank_mt5gt_td](./neuclir/runs.md#tech-hltcoe-2mneh-rerank_mt5gt_td) | [tech-hltcoe-2MNCH-rerank_mt5ht_td](./neuclir/runs.md#tech-hltcoe-2mnch-rerank_mt5ht_td) | [tech-hltcoe-MNCD-plaid_monozh_mt5ht_td](./neuclir/runs.md#tech-hltcoe-mncd-plaid_monozh_mt5ht_td) | [tech-hltcoe-MNED-plaid_tt_mt5gt_td](./neuclir/runs.md#tech-hltcoe-mned-plaid_tt_mt5gt_td) | [tech-hltcoe-MNED-plaid_tt_td](./neuclir/runs.md#tech-hltcoe-mned-plaid_tt_td) | [tech-hltcoe-MNED-plaid_distilled_td](./neuclir/runs.md#tech-hltcoe-mned-plaid_distilled_td) | [tech-hltcoe-MTED-plaid_V2model_td](./neuclir/runs.md#tech-hltcoe-mted-plaid_v2model_td) | [tech-hltcoe-MNCD-plaid_mono_td](./neuclir/runs.md#tech-hltcoe-mncd-plaid_mono_td) | [tech-hltcoe-MNED-plaid_jhpolo_td](./neuclir/runs.md#tech-hltcoe-mned-plaid_jhpolo_td) | [tech-hltcoe-MNED-colbert_x_td](./neuclir/runs.md#tech-hltcoe-mned-colbert_x_td) | [tech-hltcoe-MTES-patapsco_bm25_t_rm3](./neuclir/runs.md#tech-hltcoe-mtes-patapsco_bm25_t_rm3)
??? abstract "Abstract"
	
	The HLTCOE team applied PLAID, an mT5 reranker, and docu-ment translation to the TREC 2023 NeuCLIR track. For PLAID weincluded a variety of models and training techniques – the Englishmodel released with ColBERT v2, translate-train (TT), TranslateDistill (TD) and multilingual translate-train (MTT). TT trains aColBERT model with English queries and passages automaticallytranslated into the document language from the MS-MARCO v1collection. This results in three cross-language models for the track,one per language. MTT creates a single model for all three doc-ument languages by combining the translations of MS-MARCOpassages in all three languages into mixed-language batches. Thusthe model learns about matching queries to passages simultane-ously in all languages. Distillation uses scores from the mT5 modelover non-English translated document pairs to learn how to scorequery-document pairs. The team submitted runs to all NeuCLIRtasks: the CLIR and MLIR news task as well as the technical docu-ments task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLM23.bib)"
	```
	@inproceedings{DBLP:conf/trec/YangLM23,
		author = {Eugene Yang and Dawn J. Lawrie and James Mayfield},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{HLTCOE} at {TREC} 2023 NeuCLIR Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/hltcoe.N.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLM23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BLADE: The University of Maryland at the TREC 2023 NeuCLIR Track

_Suraj Nair,  Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/umd_hcil.N.pdf](https://trec.nist.gov/pubs/trec32/papers/umd_hcil.N.pdf)
- :fontawesome-solid-user-group: **Participant:** [umd_hcil](./neuclir/participants.md#umd_hcil)
- :material-file-search: **Runs:** [fas-umd_hcil-AELN_blade](./neuclir/runs.md#fas-umd_hcil-aeln_blade) | [zho-umd_hcil-AELN_blade](./neuclir/runs.md#zho-umd_hcil-aeln_blade) | [rus-umd_hcil-AELN_blade](./neuclir/runs.md#rus-umd_hcil-aeln_blade)
??? abstract "Abstract"
	
	The University of Maryland submitted three runs to the Ad Hoc CLIR Task of the TREC 2023NeuCLIR track. This paper describes three systems that cross the language barrier using a learnedsparse retrieval model using bilingual embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NairO23.bib)"
	```
	@inproceedings{DBLP:conf/trec/NairO23,
		author = {Suraj Nair and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{BLADE:} The University of Maryland at the {TREC} 2023 NeuCLIR Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/umd\_hcil.N.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NairO23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## AToMiC

#### TREC2023 AToMiC Overview

_Jheng-Hong Yang,  Carlos Lassance,  Rafael Sampaio de Rezende,  Krishna Srinivasan,  Miriam Redi,  Stéphane Clinchant,  Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_atomic.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_atomic.pdf)
??? abstract "Abstract"
	
	This paper presents an exploration of evaluating image–text re-trieval tasks designed for multimedia content creation, with a par-ticular focus on the dynamic interplay among various modalities,including text and images. The study highlights the pivotal roleof visual-textual multimodality, where elements such as photos,graphics, and diagrams are not merely ornamental but significantlyaugment, complement, or even reshape the meaning conveyed bytextual content. This integration of multiple modalities is central tocrafting immersive and captivating multimedia experiences. In thecontext of detailing the TREC initiative’s evaluation process for theyear, the paper introduces the AToMiC test collection, which servesas the foundational framework for evaluation. The authors delveinto the distinctive task design, elucidating the specific challengesand objectives that characterize this year’s evaluation. The paperfurther outlines the evaluation protocols, encompassing method-ologies such as pooling dependencies and the criteria employed forrelevance judgments. This overview offers valuable insights intothe intricate process of evaluating multimedia retrieval systems,underscoring the evolving complexity and interdisciplinary natureof this field.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLRSRCL23.bib)"
	```
	@inproceedings{DBLP:conf/trec/YangLRSRCL23,
		author = {Jheng{-}Hong Yang and Carlos Lassance and Rafael Sampaio de Rezende and Krishna Srinivasan and Miriam Redi and St{\'{e}}phane Clinchant and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC2023} AToMiC Overview},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_atomic.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLRSRCL23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multimodal Learned Sparse Retrieval for Image Suggestion Task

_Thong Nguyen,  Mariya Hendriksen,  Andrew Yates_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf](https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf)
- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./atomic/participants.md#uamsterdam)
- :material-file-search: **Runs:** [UvA-IRLab-mlp-mlm-images](./atomic/runs.md#uva-irlab-mlp-mlm-images) | [UvA-IRLab-mlp-mlm-caption](./atomic/runs.md#uva-irlab-mlp-mlm-caption) | [UvA-IRLab-mlp-mlm-cap1](./atomic/runs.md#uva-irlab-mlp-mlm-cap1) | [UvA-IRLab-mlp-mlm-img_cap](./atomic/runs.md#uva-irlab-mlp-mlm-img_cap)
??? abstract "Abstract"
	
	Learned Sparse Retrieval (LSR) is a group of neural methods de-signed to encode queries and documents into sparse lexical vectors.These vectors can be efficiently indexed and retrieved using aninverted index. While LSR has shown promise in text retrieval,its potential in multi-modal retrieval remains largely unexplored.Motivated by this, in this work we explore the application of LSRin the multi-modal domain, i.e., we focus on Multi-Modal LearnedSparse Retrieval (MLSR). We conduct experiments using severalMLSR model configurations and evaluate the performance on theimage suggestion task. We find that solving the task solely basedon the image content is challenging. Enriching the image contentwith its caption improves the model’s performance significantly,implying the importance of image captions to provide fine-grainedconcepts and context information of images. Our approach presentsa practical and effective solution for training LSR retrieval modelsin multi-modal settings.ACM Reference Format:Nguyen, Hendriksen, Yates. 2023. Multimodal Learned Sparse Retrieval forImage Suggestion Task. In Proceedings of (TREC 2023). ACM, New York, NY,USA, 5 pages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenHY23.bib)"
	```
	@inproceedings{DBLP:conf/trec/NguyenHY23,
		author = {Thong Nguyen and Mariya Hendriksen and Andrew Yates},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multimodal Learned Sparse Retrieval for Image Suggestion Task},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/UAmsterdam.A.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenHY23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Product Search

#### OVERVIEW OF THE TREC 2023 PRODUCT PRODUCT SEARCH TRACK

_Daniel Campos,  Surya Kallumadi,  Corby Rosset,  Cheng Xiang Zhai,  Alessandro Magnani_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/trackorg.P.pdf](https://trec.nist.gov/pubs/trec32/papers/trackorg.P.pdf)
??? abstract "Abstract"
	
	This is the first year of the TREC Product search track. The focus this year was the creation ofa reusable collection and evaluation of the impact of the use of metadata and multi-modal data onretrieval accuracy. This year we leverage the new product search corpus, which includes contextualmetadata. Our analysis shows that in the product search domain, traditional retrieval systems arehighly effective and commonly outperform general-purpose pretrained embedding models. Ouranalysis also evaluates the impact of using simplified and metadata-enhanced collections, finding noclear trend in the impact of the expanded collection. We also see some surprising outcomes; despitetheir widespread adoption and competitive performance on other tasks, we find single-stage denseretrieval runs can commonly be noncompetitive or generate low-quality results both in the zero-shotand fine-tuned domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CamposKRZM23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/jbnu.P.pdf](https://trec.nist.gov/pubs/trec32/papers/jbnu.P.pdf)
- :fontawesome-solid-user-group: **Participant:** [jbnu](./product/participants.md#jbnu)
- :material-file-search: **Runs:** [JBNU-1](./product/runs.md#jbnu-1) | [JBNU-2](./product/runs.md#jbnu-2) | [JBNU-A](./product/runs.md#jbnu-a) | [JBNU-B](./product/runs.md#jbnu-b) | [JBNU-C](./product/runs.md#jbnu-c)
??? abstract "Abstract"
	
	This paper describes the participation of the JBNU team for TREC 2023 Product Search Track. Ourprimary focus revolves around tackling the issue of performance degradation in queries. We categorizequeries into specific and abstract types, leveraging the power of the DeBERTa deep learning model forreranking. This enhancement involves the incorporation of nine specialized tokens, such as brand, material,category, and others, and is specifically applied to queries of the specific type.1. IntroductionThe TREC 2023 Product Search Track [1] centers on information retrieval within the domain of productsearch, aiming to assist users in locating the products they desire by aligning with their objectives andintentions. Our team, JBNU, has participated in the Product Ranking Task and Product Retrieval Task.In the context of product search, we have observed the frequent occurrence of common errors in queries.Traditional typo correction methods often led to incorrect corrections for words that are not commonlyfound in dictionaries, such as product names, brand names, and author names in product search queries. Totackle this challenge, we have created a specialized dictionary designed to refine and correct product searchqueries.For all tasks, the queries undergo the following preprocessing steps:- Translation of multilingual queries to English utilizing Googletrans [4].- Typo correction in queries using a dedicated product search dictionary for Pyspellchecker [5].- Replacement of product codes (ASIN) in queries with the corresponding product titles.Furthermore, we observed a common occurrence of product attributes within queries. We pinpointedattributes from the product information that held notable relevance to the queries and integrated nine specialtokens within our deep learning methodology to ensure the attribute information substantially influencesthe learning and inference processes.We categorize queries into specific and abstract types, and our reranking process with a deep learningmodel is specifically targeted at the specific query types. These specific query types are characterized bythe inclusion of one of nine special tokens, such as brand name, color, material, and more.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnCPL23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.P.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.P.pdf)
- :fontawesome-solid-user-group: **Participant:** [h2oloo](./product/participants.md#h2oloo)
- :material-file-search: **Runs:** [r_gpt3d5_turbo](./product/runs.md#r_gpt3d5_turbo) | [f_splade_clip_bm25](./product/runs.md#f_splade_clip_bm25) | [f_splade_bm25](./product/runs.md#f_splade_bm25) | [f_gpt_rerank](./product/runs.md#f_gpt_rerank)
??? abstract "Abstract"
	
	This paper presents the submitted runs for the TREC 2023 Product Search track,offering insights into our multi-stage retrieval systems designed for both end-to-end retrieval and reranking tasks. In our approach, we employed a sparsefirst-stage ranker that leveraged textual information, complemented by a densefirst-stage ranker tailored for processing visual data. Additionally, we evaluatethe effectiveness of utilizing a large-language model within the context of productsearch, shedding light on its capabilities and contributions to improving retrievalperformance. Our findings contribute to the ongoing discourse on enhancingproduct search techniques, showcasing the potential of combining various retrievalstrategies and advanced language models for enhanced search accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangL23.bib)"
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

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CFDA_CLIP.P.pdf](https://trec.nist.gov/pubs/trec32/papers/CFDA_CLIP.P.pdf)
- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./product/participants.md#cfda_clip)
- :material-file-search: **Runs:** [cfdaclip_ER_A](./product/runs.md#cfdaclip_er_a) | [cfdaclip_ER_B](./product/runs.md#cfdaclip_er_b) | [cfdaclip_MR_A](./product/runs.md#cfdaclip_mr_a) | [cfdaclip_MR_B](./product/runs.md#cfdaclip_mr_b)
??? abstract "Abstract"
	
	In this notebook, we present our pipeline approach for the prod-uct search track. We utilize both product textual data and imagesto enhance retrieval diversity. Our experiments also demonstratethe good generalization capability of a few off-the-shelf retrievalmodels. Additionally, we adopt retrieval fusion and consider it anefficient method to integrate text and images for product search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuLLLHCTW23.bib)"
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

## Tip-of-the-Tongue

#### Overview of the TREC 2023 Tip-of-the-Tongue Track

_Jaime Arguello,  Samarth Bhargav,  Fernando Diaz,  Evangelos Kanoulas,  Bhaskar Mitra_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_tot.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_tot.pdf)
??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves supporting searchers interested in refindinga previously encountered item for which they are unable to reliably recall an identifier. ToT requeststend to be verbose and include several complex phenomena, making them especially difficult for ex-isting information retrieval systems. The TREC 2023 ToT track focused on a single ad-hoc retrievaltask in the movie domain. Requests were sampled from an existing ToT dataset and the documentcorpus consisted of a subset of Wikipedia pages associated with the “audiovisual works” category.This year 11 groups submitted a total of 33 runs. Consistent with earlier findings, there is a negativecorrelation between query length and retrieval performance. We found that successful teams wereable to leverage large external datasets to substantially improve performance. While a closed largelanguage model managed to beat 26 participant runs, it did so with much lower recall.Track website: https://trec-tot.github.io
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArguelloBDKM23.bib)"
	```
	@inproceedings{DBLP:conf/trec/ArguelloBDKM23,
		author = {Jaime Arguello and Samarth Bhargav and Fernando Diaz and Evangelos Kanoulas and Bhaskar Mitra},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2023 Tip-of-the-Tongue Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Overview\_tot.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArguelloBDKM23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team CMU-LTI at TREC 2023 Tip-of-the-Tongue Track

_Luís Borges,  Jamie Callan,  Bruno Martins_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf](https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [CMU-LTI](./tot/participants.md#cmu-lti)
- :material-file-search: **Runs:** [dpr-100-rerank](./tot/runs.md#dpr-100-rerank) | [dpr-1000-rerank-robin](./tot/runs.md#dpr-1000-rerank-robin) | [dpr-abstract-100-rerank](./tot/runs.md#dpr-abstract-100-rerank) | [dpr-abstract-1000-robin](./tot/runs.md#dpr-abstract-1000-robin)
??? abstract "Abstract"
	
	This paper describes our submissions to the 2023 TREC Tip- of-the-Tongue (ToT) track. We opted for the common retrieval method- ology of a Recall oriented first-stage retrieval, followed by the use of a more accurate re-ranker model. For first-stage retrieval, we considered a DPR retriever either aggregating the passages from the documents, or matching different parts of the queries against the abstract sections of the Wikipedia articles that describe the movies. Re-ranking was dele- gated to a Large Language Model (LLM) in a zero-shot setting, taking as input the movie titles from the first stage of retrieval. Results attest to the effectiveness of the proposed approach with the best run achieving an NDCG@1000 of 0.55.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorgesCM23.bib)"
	```
	@inproceedings{DBLP:conf/trec/BorgesCM23,
		author = {Lu{\'{\i}}s Borges and Jamie Callan and Bruno Martins},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Team {CMU-LTI} at {TREC} 2023 Tip-of-the-Tongue Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BorgesCM23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2023: Tip-of-the-Tongue track

_Maik Fröbe,  Christine Brychcy,  Elisa Kluge,  Eric Oliver Schmidt,  Matthias Hagen_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Webis.T.pdf](https://trec.nist.gov/pubs/trec32/papers/Webis.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [Webis](./tot/participants.md#webis)
- :material-file-search: **Runs:** [webis-t5-01](./tot/runs.md#webis-t5-01) | [webis-t5-f](./tot/runs.md#webis-t5-f) | [webis-fus-01](./tot/runs.md#webis-fus-01) | [webis-bm25r-1](./tot/runs.md#webis-bm25r-1) | [webis-t53b-01](./tot/runs.md#webis-t53b-01)
??? abstract "Abstract"
	
	In this paper, we describe the Webis Group’s participation in theTREC 2023 Tip-of-the-Tongue track. Our runs focus on improvingthe retrieval effectiveness via query relaxation (i.e., leaving outterms that likely reduce the retrieval effectiveness). We combineBERT- or ChatGPT-based query relaxation with BM25- or monoT5-based retrieval and also experiment with reciprocal rank fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrobeBKSH23.bib)"
	```
	@inproceedings{DBLP:conf/trec/FrobeBKSH23,
		author = {Maik Fr{\"{o}}be and Christine Brychcy and Elisa Kluge and Eric Oliver Schmidt and Matthias Hagen},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2023: Tip-of-the-Tongue track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/Webis.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FrobeBKSH23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RSLTOT at the TREC 2023 ToT Track

_Reo Yoshikoshi,  Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/RSLTOT.T.pdf](https://trec.nist.gov/pubs/trec32/papers/RSLTOT.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [RSLTOT](./tot/participants.md#rsltot)
- :material-file-search: **Runs:** [RSLTOTY](./tot/runs.md#rsltoty)
??? abstract "Abstract"
	
	In this study, we focused on the situation that a user can recall only the movie’s synopsis, character features, etc., but not the movie’s title. In our experiment, we introduced systems based on TF– IDF and BERT. The results showed that our TF–IDF vectorizer is better than our BERT model if they are used individually. In addition, as each system showed different tendencies in the results, we tried a hybrid model combining these two systems. The results showed that combining these models outperformed the two component models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YoshikoshiS23.bib)"
	```
	@inproceedings{DBLP:conf/trec/YoshikoshiS23,
		author = {Reo Yoshikoshi and Tetsuya Sakai},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{RSLTOT} at the {TREC} 2023 ToT Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/RSLTOT.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YoshikoshiS23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-ToT: Endicott and UNC Notebook Paper

_Henry Feild,  Jaime Arguello_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/endicott-unc.T.pdf](https://trec.nist.gov/pubs/trec32/papers/endicott-unc.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [endicott-unc](./tot/participants.md#endicott-unc)
- :material-file-search: **Runs:** [endicott_unc_baseline](./tot/runs.md#endicott_unc_baseline) | [endicott_unc_boost_oracle](./tot/runs.md#endicott_unc_boost_oracle) | [endicott_unc_boost_pred](./tot/runs.md#endicott_unc_boost_pred) | [endicott_unc_boost_conf](./tot/runs.md#endicott_unc_boost_conf)
??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves retrievinga previously encountered item for which the searcher is unableto reliably recall an identifier. The TREC 2023 ToT track focusedon an ad-hoc retrieval task in the movie identification domain.The Endicott and UNC team submitted four runs to the track. Ourbaseline run used BM25, while our three experimental runs used a“boosted” version of BM25 that weighed query-terms differently. AllToT queries used in the track had sentence-level annotations basedon the topics and language phenomena found in the sentence. Ourthree experimental runs weighed query-terms depending on thesentence-level categories associated with the sentence from whicheach query-term originated. One experimental run weighed query-terms using gold-standard sentence-level categories. The other twoused predicted categories. Across all metrics considered, our threeexperimental runs outperformed our baseline run by a statisticallysignificant margin. Differences between experimental runs werenot statistically significant across metrics. Our results suggest thatsentence-level categories were predicted with sufficient accuracyto inform the re-weighing of query-terms to improve retrievalperformance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FeildA23.bib)"
	```
	@inproceedings{DBLP:conf/trec/FeildA23,
		author = {Henry Feild and Jaime Arguello},
		editor = {Ian Soboroff and Angela Ellis},
		title = {TREC-ToT: Endicott and {UNC} Notebook Paper},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/endicott-unc.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FeildA23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UFMG at the TREC 2023 Tip of the Tongue Track

_Rita Borges de Lima,  Rodrygo L. T. Santos_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/ufmg.T.pdf](https://trec.nist.gov/pubs/trec32/papers/ufmg.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [ufmg](./tot/participants.md#ufmg)
- :material-file-search: **Runs:** [ufmgDBmBQD](./tot/runs.md#ufmgdbmbqd) | [ufmgDBmBdTQD](./tot/runs.md#ufmgdbmbdtqd) | [ufmgG4mBQD](./tot/runs.md#ufmgg4mbqd) | [ufmgG4dTQD](./tot/runs.md#ufmgg4dtqd) | [ufmgDBmBQ](./tot/runs.md#ufmgdbmbq)
??? abstract "Abstract"
	
	In the TREC 2023 Tip of the Tongue (ToT)track, we address the challenge of movieretrieval from queries laden with impre-cise or incorrect natural language. In par-ticular, the Movie Identification Task aimsto produce a well-ranked list of movies,identified by Wikipedia page IDs, in re-sponse to a set of queries in Tip of theTongue (TOT) format. In our participa-tion, we experiment with reranking tech-niques, leveraging both sparse and denseretrieval approaches to refine the returnedresults. Additionally, we incorporate termfiltering heuristics for both queries anddocuments, enhancing the overall effec-tiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimaS23.bib)"
	```
	@inproceedings{DBLP:conf/trec/LimaS23,
		author = {Rita Borges de Lima and Rodrygo L. T. Santos},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UFMG} at the {TREC} 2023 Tip of the Tongue Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/ufmg.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LimaS23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SNU LDILAB @ TREC Tip of the tongue 2023

_Jongho Kim,  Soona Hong,  Seung-won Hwang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/snuldilab.T.pdf](https://trec.nist.gov/pubs/trec32/papers/snuldilab.T.pdf)
- :fontawesome-solid-user-group: **Participant:** [snuldilab](./tot/participants.md#snuldilab)
- :material-file-search: **Runs:** [pre_aug_vat](./tot/runs.md#pre_aug_vat) | [pre_aug_vat_max4_origin](./tot/runs.md#pre_aug_vat_max4_origin) | [pre_aug_vat_max4](./tot/runs.md#pre_aug_vat_max4)
??? abstract "Abstract"
	
	This paper describes our participation in theTREC 2023 Tip-of-the-Tongue (ToT) Track.Our first contribution involves formulating theproblem as a retrieval, of finding a relevantdocument with a much shorter query. Inspiredby a self-supervised learning approach, we ex-tract ToT query surrogates from the corpus andpair them with the document. These pairs areused for self-supervised training and then en-riching document representations to handle in-sufficiency. Second, we augment ToT querieswith cropping and adversarial perturbation. Ourresults in the ToT benchmark show that ourmodel outperforms state-of-the-art methods in-cluding GPT-4 and performs competitively inthe TREC-ToT competition.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimHH23.bib)"
	```
	@inproceedings{DBLP:conf/trec/KimHH23,
		author = {Jongho Kim and Soona Hong and Seung{-}won Hwang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{SNU} {LDILAB} @ {TREC} Tip of the tongue 2023},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/snuldilab.T.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimHH23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at TREC 2023: Deep Learning Track and Tip-of-the-Tongue  Track

_Dake Zhang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf](https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf)
- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./tot/participants.md#uwaterloomds)
- :material-file-search: **Runs:** [WatS-DR](./tot/runs.md#wats-dr) | [WatS-TDR](./tot/runs.md#wats-tdr) | [WatS-TDR-RR](./tot/runs.md#wats-tdr-rr)
??? abstract "Abstract"
	
	Our submissions to the TREC 2023 Deep LearningTrack and the Tip-of-the-Tongue Track utilized thepower of language models. For the Deep Learningtrack, we prompted a Large Language Model (LLM)to generate more queries for BM25 retrieval, whichdid not yield better performance than the BM25 base-line. We also tried to prompt the model to per-form passage assessments similar to human asses-sors, which effectively improved the ranking of thebaseline. For the Tip-of-the-Tongue track, we useda general-purpose text embedding model to performdense retrieval, achieving better performance thanthe dense retrieval baseline with a high recall. Whenwe instructed an LLM to assess whether a Wikipediapage matches a user’s description, the model did notseem to produce accurate assessments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zhang23.bib)"
	```
	@inproceedings{DBLP:conf/trec/Zhang23,
		author = {Dake Zhang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UWaterlooMDS at {TREC} 2023: Deep Learning Track and Tip-of-the-Tongue Track},
		booktitle = {The Thirty-Second Text REtrieval Conference Proceedings {(TREC} 2023), Gaithersburg, MD, USA, November 14-17, 2023},
		series = {{NIST} Special Publication},
		volume = {1328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2023},
		url = {https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf},
		timestamp = {Tue, 26 Nov 2024 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zhang23.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

