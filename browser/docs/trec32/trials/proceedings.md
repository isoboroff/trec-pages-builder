# Proceedings - Clinical Trials 2023

#### UNIMIB at TREC 2023 Clinical Trials Track

_Georgios Peikos_

- :fontawesome-solid-user-group: **Participant:** [UNIMIB_IKR3](./participants.md#unimib_ikr3)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UNIMIB_IKR3.C.pdf](https://trec.nist.gov/pubs/trec32/papers/UNIMIB_IKR3.C.pdf)
- :material-file-search: **Runs:** [BM25RM3_single_run](./runs.md#bm25rm3_single_run) | [BM25_two_stage](./runs.md#bm25_two_stage) | [BM25RM3_gpt35_run](./runs.md#bm25rm3_gpt35_run) | [BM25RM3_gpt35_strict_run](./runs.md#bm25rm3_gpt35_strict_run)

??? abstract "Abstract"
	
	This notebook summarizes our participation as the UNIMIB team in the TREC 2023 Clinical Trials Track. Our research evaluates the efficacy of Large Language Models (LLMs) in assessing patient eligibility for clinical trials. For this purpose, we integrated GPT-3.5 as the final stage in our retrieval pipeline. The results indicate that GPT-3.5 may enhance the performance of retrieval tasks in this context. Nonetheless, comparable results may be attained with less complex retrieval systems that utilize BM25.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Peikos23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [DoSSIER](./participants.md#dossier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/DoSSIER.C.pdf](https://trec.nist.gov/pubs/trec32/papers/DoSSIER.C.pdf)
- :material-file-search: **Runs:** [DoSSIER_2](./runs.md#dossier_2) | [DoSSIER_1](./runs.md#dossier_1) | [DoSSIER_3](./runs.md#dossier_3) | [DoSSIER_4](./runs.md#dossier_4) | [DoSSIER_5](./runs.md#dossier_5)

??? abstract "Abstract"
	
	This paper describes the experimental setup and results of the DoSSIER team’s participation in the Clinical Trials Track at TREC 2023. The primary objective of this track was to identify clinical trials for which patients meet the eligibility criteria. Our approach uses pipeline-based models, including large language models (LLMs) for query expansion and entity extraction techniques to augment both queries and documents. In our pipelines, we tested two different first-stage retrieval models, followed by a neural re-ranking framework that leverages topical relevance and eligibility criteria. We add to the pipeline a GPT-3.5-based question-answering post-processing step. Our findings demonstrate that the neural re-ranking and subsequent LLM post-processing notably enhanced performance. Future research will focus on a comprehensive assess- ment of the impact of query and document representation strategies on retrieval efficacy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KusaSSMH23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [EMA3](./participants.md#ema3)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/EMA3.C.pdf](https://trec.nist.gov/pubs/trec32/papers/EMA3.C.pdf)
- :material-file-search: **Runs:** [stage1ema](./runs.md#stage1ema) | [brsema3](./runs.md#brsema3) | [nrema3](./runs.md#nrema3) | [wrsema3](./runs.md#wrsema3)

??? abstract "Abstract"
	
	This paper describes the submissions of the EMA31 team from the MALNIS2 lab to the TREC 2023 Clinical Trials Track. In our ap- proach to the TREC clinical trial matching problem, we use a two-stage process for effec- tively ranking and re-ranking clinical trials per- taining to a specific disorder. First, we identify candidate trials by matching normalized medi- cal terms and non-negated inclusion/exclusion criteria to the disorder. Then, we rank the can- didates using weighted relevance scores based on cosine similarity between contextual embed- dings of the disorder and trial criteria. We use three different weighting schemes to compute a matching score. The unique aspect of our approach lies in the innovative use of these cri- teria to filter clinical trials and in the weighted relevance scoring, which reflects the varying importance of inclusion and exclusion crite- ria. Once we have computed the weighted rel- evance score for each candidate clinical trial, we rank the clinical trials by their score. Our submission performs better in terms of Preci- sion@10 and NDCG-cut-10 than the median scores of the TREC 2023 Clinical trials track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SaeidiJDKM23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [CSIRO-UQ-ielab](./participants.md#csiro-uq-ielab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CSIRO-UQ-ielab.C.pdf](https://trec.nist.gov/pubs/trec32/papers/CSIRO-UQ-ielab.C.pdf)
- :material-file-search: **Runs:** [GPT4](./runs.md#gpt4) | [CE_weighted](./runs.md#ce_weighted) | [Hybrid](./runs.md#hybrid) | [DR](./runs.md#dr) | [SPLADEv2](./runs.md#spladev2)

??? abstract "Abstract"
	
	We describe team ielab from CSIRO and The University of Queensland’s approach to the 2023 TREC Clinical Trials Track. Our approach was to use neural rankers but to utilise Large Language Models to overcome the issue of lack of training data for such rankers. Specifically, we employ ChatGPT to generate relevant patient descriptions for randomly selected clinical trials from the corpus. This synthetic dataset, combined with human-annotated training data from previous years, is used to train both dense and sparse retrievers based on PubmedBERT. Additionally, a cross-encoder re-ranker is integrated into the system. To further enhance the effectiveness of our approach, we prompting GPT-4 as a TREC annotator to provide judgments on our run files. These judgments are subsequently employed to re-rank the results. This architecture tightly integrates strong PubmedBERT-based rankers with the aid of SOTA Large Language Models, demonstrating a new approach to clinical trial retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuangKZ23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CSIROmed.C.pdf](https://trec.nist.gov/pubs/trec32/papers/CSIROmed.C.pdf)
- :material-file-search: **Runs:** [qe_prr_ft_rf](./runs.md#qe_prr_ft_rf) | [qe_prr_zs](./runs.md#qe_prr_zs) | [qe_err](./runs.md#qe_err) | [qe](./runs.md#qe) | [bm25_bsln](./runs.md#bm25_bsln)

??? abstract "Abstract"
	
	To assist with finding eligible participants for clinical trials,the TREC 2023 Clinical Trials track sets a task where patientdata, in the form of patient questionnaires, can be used tomatch eligible patients to a relevant clinical trial. We exploreseveral query expansion and reranking methods using largelanguage models. Our best method uses query expansionwith GPT 3.5-turbo and reranking with a fine-tuned versionof the same model.CCS CONCEPTS• Information systems → Retrieval models and ranking;Language models; Decision support systems; • Applied comput-ing → Health informatics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiK23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [MU_CS](./participants.md#mu_cs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/MU_CS.C.pdf](https://trec.nist.gov/pubs/trec32/papers/MU_CS.C.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1)

??? abstract "Abstract"
	
	This paper briefly discusses our submission to the TREC 2023 Clinical Records Track.  The track challenged participants to match patient details with medical research trials based on whether the patients were believed to be a good fit. Our method utilized OpenAI’s Ada model, a market solution for finding similarity based on given strings. By using a prebuilt solution, we sought to produce a solution that gave results better than random guessing with both low design cost and low overall monetary cost.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RichmondD23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [V-TorontoMU](./participants.md#v-torontomu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/V-TorontoMU.C.pdf](https://trec.nist.gov/pubs/trec32/papers/V-TorontoMU.C.pdf)
- :material-file-search: **Runs:** [v1tmurun](./runs.md#v1tmurun) | [v4tmurun](./runs.md#v4tmurun) | [v2tmurun](./runs.md#v2tmurun) | [v3tmurun](./runs.md#v3tmurun)

??? abstract "Abstract"
	
	This paper describes Toronto Metropolitan University’s participation in the TREC Clinical Trials Track for 2023. As part of the tasks, we utilize ad- vanced natural language processing techniques and neural language models in our experiments to retrieve the most relevant clinical trials. We illustrate the overall methodology, experimental settings, and results of our implementation for the run submission as part of (Team - V-Ryerson).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LahiriHHD23.bib) "
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

