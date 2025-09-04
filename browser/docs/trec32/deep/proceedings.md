# Proceedings - Deep Learning 2023

#### Overview of the TREC 2023 Deep Learning Track

_Nick Craswell,  Bhaskar Mitra,  Emine Yilmaz,  Hossein A. Rahmani,  Daniel Campos,  Jimmy Lin,  Ellen M. Voorhees,  Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_deep.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_deep.pdf)
??? abstract "Abstract"
	
	This is the fifth year of the TREC Deep Learning track. As in previous years, we leverage the MSMARCO datasets that made hundreds of thousands of human-annotated training labels availablefor both passage and document ranking tasks. We mostly repeated last year’s design, to get anothermatching test set, based on the larger, cleaner, less-biased v2 passage and document set, with passageranking as primary and document ranking as a secondary task (using labels inferred from passage).As we did last year, we sample from MS MARCO queries that were completely held out, unusedin corpus construction, unlike the test queries in the first three years. This approach yields a moredifficult test with more headroom for improvement. Alongside the usual MS MARCO (human)queries from MS MARCO, this year we generated synthetic queries using a fine-tuned T5 modeland using a GPT-4 prompt.The new headline result this year is that runs using Large Language Model (LLM) prompting insome way outperformed runs that use the “nnlm” approach, which was the best approach in theprevious four years. Since this is the last year of the track, future iterations of prompt-based rankingcan happen in other tracks. Human relevance assessments were applied to all query types, notjust human MS MARCO queries. Evaluation using synthetic queries gave similar results to humanqueries, with system ordering agreement of τ = 0.8487. However, human effort was needed toselect a subset of the synthetic queries that were usable. We did not see clear evidence of bias,where runs using GPT-4 were favored when evaluated using synthetic GPT-4 queries, or where runsusing T5 were favored when evaluated on synthetic T5 queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellMYRCLVS23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf)
- :material-file-search: **Runs:** [agg-cocondenser](./runs.md#agg-cocondenser) | [slim-pp-0shot-uw](./runs.md#slim-pp-0shot-uw) | [naverloo_bm25_RR](./runs.md#naverloo_bm25_rr) | [naverloo-frgpt4](./runs.md#naverloo-frgpt4) | [naverloo-rgpt4](./runs.md#naverloo-rgpt4) | [splade_pp_ensemble_distil](./runs.md#splade_pp_ensemble_distil) | [splade_pp_self_distil](./runs.md#splade_pp_self_distil) | [bm25_splades](./runs.md#bm25_splades) | [naverloo_fs](./runs.md#naverloo_fs) | [naverloo_fs_RR](./runs.md#naverloo_fs_rr) | [naverloo_fs_RR_duo](./runs.md#naverloo_fs_rr_duo) | [naverloo_bm25_splades_RR](./runs.md#naverloo_bm25_splades_rr) | [D_bm25_splades](./runs.md#d_bm25_splades) | [D_naverloo-frgpt4](./runs.md#d_naverloo-frgpt4) | [D_naverloo_bm25_RR](./runs.md#d_naverloo_bm25_rr) | [D_naverloo_bm_splade_RR](./runs.md#d_naverloo_bm_splade_rr)

??? abstract "Abstract"
	
	In this notebook, we outline the architecture and evaluation of our TREC 2023submissions, which employ a sophisticated cascading multi-stage ranking frame-work comprising four distinct steps. Through experimentation across multipleconfigurations, we validate the efficacy of each stage within this hierarchy. Ourfindings demonstrate the high effectiveness of our pipeline, consistently outper-forming median benchmarks and approaching the maximal aggregate scores. No-tably, reproducibility is a key outcome of our methodology. Nevertheless, thereproducibility of the final component, termed “listo”, is contingent upon interac-tions with the proprietary and inherently non-deterministic GPT4, raising salientquestions about its consistency and reliability in a research context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassancePL23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf](https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf)
- :material-file-search: **Runs:** [WatS-LLM-Rerank](./runs.md#wats-llm-rerank) | [WatS-Augmented-BM25](./runs.md#wats-augmented-bm25)

??? abstract "Abstract"
	
	Our submissions to the TREC 2023 Deep LearningTrack and the Tip-of-the-Tongue Track utilized thepower of language models. For the Deep Learningtrack, we prompted a Large Language Model (LLM)to generate more queries for BM25 retrieval, whichdid not yield better performance than the BM25 base-line. We also tried to prompt the model to per-form passage assessments similar to human asses-sors, which effectively improved the ranking of thebaseline. For the Tip-of-the-Tongue track, we useda general-purpose text embedding model to performdense retrieval, achieving better performance thanthe dense retrieval baseline with a high recall. Whenwe instructed an LLM to assess whether a Wikipediapage matches a user’s description, the model did notseem to produce accurate assessments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zhang23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [uot-yj](./participants.md#uot-yj)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.D.pdf](https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.D.pdf)
- :material-file-search: **Runs:** [uot-yj_rankgpt35](./runs.md#uot-yj_rankgpt35) | [uot-yj_rankgpt4](./runs.md#uot-yj_rankgpt4) | [uot-yj_LLMs-blender](./runs.md#uot-yj_llms-blender)

??? abstract "Abstract"
	
	This paper describes the approaches used in three automatic submission runs for the TREC 2023 deep learning track specifically for the passage re-ranking task. We tested three different approaches using GPT-3.5-turbo, GPT-4, and a combination of multiple LLMs to explore effective methods for this task and demonstrated a variable performance of these methods, where none did better than the average results from the other participants in the track. These findings indicate a potential area for further exploration into how current LLMs re-rank search results, highlighting the need for careful prompt creation and model selection in information retrieval. Our work is an initial attempt to understand what LLMs can achieve and where they could be improved, offering some direction for future research in this area.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZYFJ23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/TREMA-UNH.D.pdf](https://trec.nist.gov/pubs/trec32/papers/TREMA-UNH.D.pdf)

??? abstract "Abstract"
	
	This notebook describes the submission from the TREMA-UNHteam to the TREC 2023 deep learning track. Conventional DPRsystems use dense vector representations from large language mod-els such as BERT to measure how similar queries are to candidatepassages. For effective open-domain question-answering, it’s cru-cial for the embedding model to grasp both high-level topics andtheir detailed subtopics. While recent DPR systems implicitly learntopic similarities, explicitly integrating topic taxonomies wouldbe beneficial. Vital article category scheme from Wikipedia is uti-lized to establish an overarching topic framework, and a hyperbolicembedding space is used to gain insights into topic hierarchies.When integrated into a DPR system, the entire topic landscape isconsidered while responding to a query. The resulting DPR systemis utilized to produce runs for the reranking task of TREC 2023deep learning track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiD23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [CIP](./participants.md#cip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CIP.D.pdf](https://trec.nist.gov/pubs/trec32/papers/CIP.D.pdf)
- :material-file-search: **Runs:** [cip_run_7](./runs.md#cip_run_7) | [cip_run_1](./runs.md#cip_run_1) | [cip_run_2](./runs.md#cip_run_2) | [cip_run_3](./runs.md#cip_run_3) | [cip_run_4](./runs.md#cip_run_4) | [cip_run_5](./runs.md#cip_run_5) | [cip_run_6](./runs.md#cip_run_6)

??? abstract "Abstract"
	
	This study presents the strategies and experimental results employed by the CIP team in the Passage Ranking task of the 2023 TREC Deep Learning Track. In the full-ranking task, we incorporated sparse retrieval methods such as Unicoil [4] and DocT5Query [6], cross- attention mechanism (MonoT5 [8]), and the recent advancements in large language models (LLM) to achieve improved sorting effectiveness. Ad- ditionally, we utilized a multi-round iterative optimization strategy for deep ranking of selected candidate documents. The experimental data suggests that by harnessing the power of existing resources, our approach has yielded favorable results in this task, without necessitating any ad- ditional training.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenHSS23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uogTr.D.pdf](https://trec.nist.gov/pubs/trec32/papers/uogTr.D.pdf)
- :material-file-search: **Runs:** [uogtr_dph](./runs.md#uogtr_dph) | [uogtr_dph_bo1](./runs.md#uogtr_dph_bo1) | [uogtr_be](./runs.md#uogtr_be) | [uogtr_se](./runs.md#uogtr_se) | [uogtr_s](./runs.md#uogtr_s) | [uogtr_se_gb](./runs.md#uogtr_se_gb) | [uogtr_be_gb](./runs.md#uogtr_be_gb) | [uogtr_qr_be_gb](./runs.md#uogtr_qr_be_gb) | [uogtr_b_grf_e](./runs.md#uogtr_b_grf_e) | [uogtr_qr_be](./runs.md#uogtr_qr_be) | [uogtr_b_grf_e_gb](./runs.md#uogtr_b_grf_e_gb)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2023 DeepLearning Track. We submitted runs that apply generative relevancefeedback from a large language model in both a zero-shot andpseudo-relevance feedback setting over two sparse retrieval ap-proaches, namely BM25 and SPLADE. We couple this first stagewith adaptive re-ranking over a BM25 corpus graph scored using amonoELECTRA cross-encoder. We investigate the efficacy of thesegenerative approaches for different query types in first-stage re-trieval. In re-ranking, we investigate operating points of adaptivere-ranking with different first stages to find the point in graphtraversal where the first stage no longer has an effect on the perfor-mance of the overall retrieval pipeline. We find some performancegains from the application of generative query reformulation. How-ever, our strongest run in terms of P@10 and nDCG@10 appliedboth adaptive re-ranking and generative pseudo-relevance feed-back, namely uogtr_b_grf_e_gb.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParryJMO23.bib) "
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

