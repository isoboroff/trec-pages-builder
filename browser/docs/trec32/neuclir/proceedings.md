# Proceedings - NeuCLIR 2023

#### Overview of the TREC 2023 NeuCLIR Track

_Dawn J. Lawrie,  Sean MacAvaney,  James Mayfield,  Paul McNamee,  Douglas W. Oard,  Luca Soldaini,  Eugene Yang_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_neuclir.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_neuclir.pdf)
??? abstract "Abstract"
	
	The principal goal of the TREC Neural Cross-Language Informa-tion Retrieval (NeuCLIR) track is to study the impact of neuralapproaches to cross-language information retrieval. The track hascreated four collections, large collections of Chinese, Persian, andRussian newswire and a smaller collection of Chinese scientificabstracts. The principal tasks are ranked retrieval of news in one ofthe three languages, using English topics. Results for a multilingualtask, also with English topics but with documents from all threenewswire collections, are also reported. New in this second yearof the track is a pilot technical documents CLIR task for rankedretrieval of Chinese technical documents using English topics. Atotal of 220 runs across all tasks were submitted by six participatingteams and, as baselines, by track coordinators. Task descriptionsand results are presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LawrieMMMOSY23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf](https://trec.nist.gov/pubs/trec32/papers/h2oloo.DN.pdf)
- :material-file-search: **Runs:** [fas-h2oloo-A1PND_SpladeMiraclMonoqt](./runs.md#fas-h2oloo-a1pnd_splademiraclmonoqt) | [fas-h2oloo-A1PNL_spladeqt](./runs.md#fas-h2oloo-a1pnl_spladeqt) | [fas-h2oloo-A1PND_mContrieverqt](./runs.md#fas-h2oloo-a1pnd_mcontrieverqt) | [fas-h2oloo-A1PNS_bm25qt](./runs.md#fas-h2oloo-a1pns_bm25qt) | [fas-h2oloo-AETD_RetroMAEReprodt](./runs.md#fas-h2oloo-aetd_retromaereprodt) | [fas-h2oloo-AETD_SpladeMiraclENdt](./runs.md#fas-h2oloo-aetd_splademiraclendt) | [fas-h2oloo-AETL_spladedt](./runs.md#fas-h2oloo-aetl_spladedt) | [fas-h2oloo-AETS_bm25dt](./runs.md#fas-h2oloo-aets_bm25dt) | [fas-h2oloo-A1NETSP_BM25s](./runs.md#fas-h2oloo-a1netsp_bm25s) | [fas-h2oloo-A1NETHP_BM25sSplades](./runs.md#fas-h2oloo-a1nethp_bm25ssplades) | [fas-h2oloo-A1NETHP_EverythingRun](./runs.md#fas-h2oloo-a1nethp_everythingrun) | [fas-h2oloo-A_rgpt4](./runs.md#fas-h2oloo-a_rgpt4) | [fas-h2oloo-A_frgpt4](./runs.md#fas-h2oloo-a_frgpt4) | [fas-h2oloo-A_RERANKBM25s](./runs.md#fas-h2oloo-a_rerankbm25s) | [fas-h2oloo-A_RERANKBM25sSplades](./runs.md#fas-h2oloo-a_rerankbm25ssplades) | [fas-h2oloo-A_RERANKEverythingRun](./runs.md#fas-h2oloo-a_rerankeverythingrun) | [rus-h2oloo-A_frgpt4](./runs.md#rus-h2oloo-a_frgpt4) | [rus-h2oloo-A_rgpt4](./runs.md#rus-h2oloo-a_rgpt4) | [rus-h2oloo-A_RERANKEverythingRun](./runs.md#rus-h2oloo-a_rerankeverythingrun) | [rus-h2oloo-A_RERANKBM25sSplades](./runs.md#rus-h2oloo-a_rerankbm25ssplades) | [rus-h2oloo-A_RERANKBM25s](./runs.md#rus-h2oloo-a_rerankbm25s) | [rus-h2oloo-A1NETHR_EverythingRun](./runs.md#rus-h2oloo-a1nethr_everythingrun) | [rus-h2oloo-A1NETHR_BM25sSplades](./runs.md#rus-h2oloo-a1nethr_bm25ssplades) | [rus-h2oloo-A1NETSR_BM25s](./runs.md#rus-h2oloo-a1netsr_bm25s) | [zho-h2oloo-A1NETSC_BM25s](./runs.md#zho-h2oloo-a1netsc_bm25s) | [zho-h2oloo-A1NETHC_BM25sSplades](./runs.md#zho-h2oloo-a1nethc_bm25ssplades) | [zho-h2oloo-A1NETHC_EverythingRun](./runs.md#zho-h2oloo-a1nethc_everythingrun) | [zho-h2oloo-A_RERANKBM25s](./runs.md#zho-h2oloo-a_rerankbm25s) | [zho-h2oloo-A_RERANKBM25sSplades](./runs.md#zho-h2oloo-a_rerankbm25ssplades) | [zho-h2oloo-A_RERANKEverythingRun](./runs.md#zho-h2oloo-a_rerankeverythingrun) | [zho-h2oloo-A_rgpt4](./runs.md#zho-h2oloo-a_rgpt4) | [zho-h2oloo-A_frgpt4](./runs.md#zho-h2oloo-a_frgpt4) | [mlir-h2oloo-A_frgpt4](./runs.md#mlir-h2oloo-a_frgpt4) | [mlir-h2oloo-A_rgpt4](./runs.md#mlir-h2oloo-a_rgpt4) | [mlir-h2oloo-A_RERANKEverythingRun](./runs.md#mlir-h2oloo-a_rerankeverythingrun) | [mlir-h2oloo-A_RERANKBM25sSplades](./runs.md#mlir-h2oloo-a_rerankbm25ssplades) | [mlir-h2oloo-A_RERANKBM25s](./runs.md#mlir-h2oloo-a_rerankbm25s) | [mlir-h2oloo-A_EverythingRun](./runs.md#mlir-h2oloo-a_everythingrun) | [mlir-h2oloo-A_BM25sSplades](./runs.md#mlir-h2oloo-a_bm25ssplades) | [mlir-h2oloo-A_BM25s](./runs.md#mlir-h2oloo-a_bm25s) | [rus-h2oloo-A1RND_mContrieverqt](./runs.md#rus-h2oloo-a1rnd_mcontrieverqt) | [rus-h2oloo-A1RND_SpladeMiraclMonoqt](./runs.md#rus-h2oloo-a1rnd_splademiraclmonoqt) | [rus-h2oloo-A1RNL_spladeqt](./runs.md#rus-h2oloo-a1rnl_spladeqt) | [rus-h2oloo-A1RNS_bm25qt](./runs.md#rus-h2oloo-a1rns_bm25qt) | [rus-h2oloo-AETD_RetroMAEReprodt](./runs.md#rus-h2oloo-aetd_retromaereprodt) | [rus-h2oloo-AETD_SpladeMiraclENdt](./runs.md#rus-h2oloo-aetd_splademiraclendt) | [rus-h2oloo-AETL_spladedt](./runs.md#rus-h2oloo-aetl_spladedt) | [rus-h2oloo-AETS_bm25dt](./runs.md#rus-h2oloo-aets_bm25dt) | [zho-h2oloo-AETS_bm25dt](./runs.md#zho-h2oloo-aets_bm25dt) | [zho-h2oloo-AETL_spladedt](./runs.md#zho-h2oloo-aetl_spladedt) | [zho-h2oloo-AETD_SpladeMiraclENdt](./runs.md#zho-h2oloo-aetd_splademiraclendt) | [zho-h2oloo-AETD_RetroMAEReprodt](./runs.md#zho-h2oloo-aetd_retromaereprodt) | [zho-h2oloo-A1CNS_bm25qt](./runs.md#zho-h2oloo-a1cns_bm25qt) | [zho-h2oloo-A1CNL_spladeqt](./runs.md#zho-h2oloo-a1cnl_spladeqt) | [zho-h2oloo-A1CND_SpladeMiraclMonoqt](./runs.md#zho-h2oloo-a1cnd_splademiraclmonoqt) | [zho-h2oloo-A1CND_mContrieverqt](./runs.md#zho-h2oloo-a1cnd_mcontrieverqt) | [tech-h2oloo-AETS_bm25dt](./runs.md#tech-h2oloo-aets_bm25dt) | [tech-h2oloo-A1CNS_bm25qt](./runs.md#tech-h2oloo-a1cns_bm25qt) | [tech-h2oloo-A1CND_mContrieverqt](./runs.md#tech-h2oloo-a1cnd_mcontrieverqt) | [tech-h2oloo-A1CNL_SpladeMiraclMonoqt](./runs.md#tech-h2oloo-a1cnl_splademiraclmonoqt) | [tech-h2oloo-A1CNL_SpladeNeuclirqt](./runs.md#tech-h2oloo-a1cnl_spladeneuclirqt) | [tech-h2oloo-AETD_RetroMAEReprodt](./runs.md#tech-h2oloo-aetd_retromaereprodt) | [tech-h2oloo-AETL_SpladeMiraclENdt](./runs.md#tech-h2oloo-aetl_splademiraclendt) | [tech-h2oloo-AETL_SpladePPSDdt](./runs.md#tech-h2oloo-aetl_spladeppsddt) | [tech-h2oloo-A1NETSC_BM25s](./runs.md#tech-h2oloo-a1netsc_bm25s) | [tech-h2oloo-A1NETHC_BM25sSplades](./runs.md#tech-h2oloo-a1nethc_bm25ssplades) | [tech-h2oloo-A1NETHC_EverythingRun](./runs.md#tech-h2oloo-a1nethc_everythingrun) | [tech-h2oloo-A_BM25s_RR](./runs.md#tech-h2oloo-a_bm25s_rr) | [tech-h2oloo-A_BM25s_fRR](./runs.md#tech-h2oloo-a_bm25s_frr) | [tech-h2oloo-A_BM25sSplades_fRR](./runs.md#tech-h2oloo-a_bm25ssplades_frr) | [tech-h2oloo-A_BM25sSplades_RR](./runs.md#tech-h2oloo-a_bm25ssplades_rr) | [tech-h2oloo-A_EverythingRun_RR](./runs.md#tech-h2oloo-a_everythingrun_rr) | [tech-h2oloo-A_EverythingRun_fRR](./runs.md#tech-h2oloo-a_everythingrun_frr)

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

#### ISI's SEARCHER II System for TREC's 2023 NeuCLIR Track

_Scott Miller,  Shantanu Agarwal,  Joel Barry_

- :fontawesome-solid-user-group: **Participant:** [ISI_SEARCHER](./participants.md#isi_searcher)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/ISI_SEARCHER.N.pdf](https://trec.nist.gov/pubs/trec32/papers/ISI_SEARCHER.N.pdf)
- :material-file-search: **Runs:** [zho-ISI_SEARCHER-ANE_run1](./runs.md#zho-isi_searcher-ane_run1) | [tech-ISI_SEARCHER-ANE_run_tech_base](./runs.md#tech-isi_searcher-ane_run_tech_base) | [tech-ISI_SEARCHER-ANE_run_tech_rr](./runs.md#tech-isi_searcher-ane_run_tech_rr) | [tech-ISI_SEARCHER-ANE_run_tech_rr_combine](./runs.md#tech-isi_searcher-ane_run_tech_rr_combine) | [tech-ISI_SEARCHER-ANE_run_tech_rr_combine_td](./runs.md#tech-isi_searcher-ane_run_tech_rr_combine_td)

??? abstract "Abstract"
	
	This overviews the University of Massachusetts’s efforts in cross-lingual retrieval run submissions for the TREC 2023 NeuCLIR Track. In this cross-lingual information retrieval (CLIR) task, the search queries are written in English, and three target collections are in Chinese, Persian, and Russian. We focus on building strong ensembles of initial ranking models, including dense and sparse retrievers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MillerAB23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [CIIR](./participants.md#ciir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CIIR.N.pdf](https://trec.nist.gov/pubs/trec32/papers/CIIR.N.pdf)
- :material-file-search: **Runs:** [fas-CIIR-LATE-SPLADE](./runs.md#fas-ciir-late-splade) | [zho-CIIR-LATE-SPLADE](./runs.md#zho-ciir-late-splade) | [rus-CIIR-LATE-SPLADE](./runs.md#rus-ciir-late-splade) | [mlir-CIIR-LATE-SPLADE](./runs.md#mlir-ciir-late-splade) | [fas-CIIR-ATEH-TransFuisonTrec23](./runs.md#fas-ciir-ateh-transfuisontrec23) | [rus-CIIR-ATEH-TransFuisonTrec23](./runs.md#rus-ciir-ateh-transfuisontrec23) | [zho-CIIR-ATEH-TransFuisonTrec23](./runs.md#zho-ciir-ateh-transfuisontrec23) | [mlir-CIIR-ATEH-TransFuisonTrec23](./runs.md#mlir-ciir-ateh-transfuisontrec23) | [fas-CIIR-ANEH-NativeFuisonTrec23](./runs.md#fas-ciir-aneh-nativefuisontrec23) | [zho-CIIR-ANEH-NativeFuisonTrec23](./runs.md#zho-ciir-aneh-nativefuisontrec23) | [fas-CIIR-ATEH-HybridFuisonTrec23](./runs.md#fas-ciir-ateh-hybridfuisontrec23) | [zho-CIIR-ATEH-HybridFuisonTrec23](./runs.md#zho-ciir-ateh-hybridfuisontrec23) | [rus-CIIR-ANEH-NativeFuisonTrec23](./runs.md#rus-ciir-aneh-nativefuisontrec23) | [mlir-CIIR-ANEH-NativeFuisonTrec23](./runs.md#mlir-ciir-aneh-nativefuisontrec23) | [rus-CIIR-ATEH-HybridFuisonTrec23](./runs.md#rus-ciir-ateh-hybridfuisontrec23) | [mlir-CIIR-ATEH-HybridFuisonTrec23](./runs.md#mlir-ciir-ateh-hybridfuisontrec23) | [tech-CIIR-ANEH-NativeFuisonTrec23](./runs.md#tech-ciir-aneh-nativefuisontrec23) | [tech-CIIR-ATEH-TransFuisonTrec23](./runs.md#tech-ciir-ateh-transfuisontrec23) | [tech-CIIR-ATEH-HybridFuisonTrec23](./runs.md#tech-ciir-ateh-hybridfuisontrec23)

??? abstract "Abstract"
	
	This overviews the University of Massachusetts’s efforts in cross-lingual retrieval run submissions for the TREC 2023 NeuCLIR Track. In this cross-lingual information retrieval (CLIR) task, the search queries are written in English, and three target collections are in Chinese, Persian, and Russian. We focus on building strong ensembles of initial ranking models, including dense and sparse retrievers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangYA23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/hltcoe.N.pdf](https://trec.nist.gov/pubs/trec32/papers/hltcoe.N.pdf)
- :material-file-search: **Runs:** [fas-hltcoe-SEMN-PSQ-td](./runs.md#fas-hltcoe-semn-psq-td) | [rus-hltcoe-SEMN-PSQ-td](./runs.md#rus-hltcoe-semn-psq-td) | [zho-hltcoe-SEMN-PSQ-td](./runs.md#zho-hltcoe-semn-psq-td) | [mlir-hltcoe-SEMN-PSQraw-td](./runs.md#mlir-hltcoe-semn-psqraw-td) | [mlir-hltcoe-SEMN-PSQraw-t](./runs.md#mlir-hltcoe-semn-psqraw-t) | [fas-hltcoe-SEMN-PSQ-t](./runs.md#fas-hltcoe-semn-psq-t) | [rus-hltcoe-SEMN-PSQ-t](./runs.md#rus-hltcoe-semn-psq-t) | [zho-hltcoe-SEMN-PSQ-t](./runs.md#zho-hltcoe-semn-psq-t) | [fas-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./runs.md#fas-hltcoe-demn-plaidkd-monomt5tt-td) | [rus-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./runs.md#rus-hltcoe-demn-plaidkd-monomt5tt-td) | [zho-hltcoe-DCMN-PLAID192mono-td](./runs.md#zho-hltcoe-dcmn-plaid192mono-td) | [fas-hltcoe-HEMN-PLAIDkd-mT5gt-td](./runs.md#fas-hltcoe-hemn-plaidkd-mt5gt-td) | [rus-hltcoe-HEMN-PLAIDkd-mT5gt-td](./runs.md#rus-hltcoe-hemn-plaidkd-mt5gt-td) | [zho-hltcoe-HEMN-PLAIDkd-mT5gt-dt](./runs.md#zho-hltcoe-hemn-plaidkd-mt5gt-dt) | [fas-hltcoe-DPMN-PLAID192mono-td](./runs.md#fas-hltcoe-dpmn-plaid192mono-td) | [rus-hltcoe-DRMN-PLAID192mono-td](./runs.md#rus-hltcoe-drmn-plaid192mono-td) | [fas-hltcoe-HEMN2-mT5gt-td](./runs.md#fas-hltcoe-hemn2-mt5gt-td) | [rus-hltcoe-HEMN2-mT5gt-td](./runs.md#rus-hltcoe-hemn2-mt5gt-td) | [zho-hltcoe-HEMN2-mT5gt-dt](./runs.md#zho-hltcoe-hemn2-mt5gt-dt) | [fas-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./runs.md#fas-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [rus-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./runs.md#rus-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [zho-hltcoe-MNED-PLAID_shard_by_date_1bit_v1_tt](./runs.md#zho-hltcoe-mned-plaid_shard_by_date_1bit_v1_tt) | [fas-hltcoe-MTED-plaid_v2_eng_1](./runs.md#fas-hltcoe-mted-plaid_v2_eng_1) | [rus-hltcoe-MTED-plaid_v2_eng_1](./runs.md#rus-hltcoe-mted-plaid_v2_eng_1) | [zho-hltcoe-MTED-plaid_v2_eng_1](./runs.md#zho-hltcoe-mted-plaid_v2_eng_1) | [fas-hltcoe-MNED-colbertX](./runs.md#fas-hltcoe-mned-colbertx) | [rus-hltcoe-MNED-colbertX](./runs.md#rus-hltcoe-mned-colbertx) | [zho-hltcoe-MNED-colbertX](./runs.md#zho-hltcoe-mned-colbertx) | [mlir-hltcoe-MNED-plaid_v1_mtt_1bit](./runs.md#mlir-hltcoe-mned-plaid_v1_mtt_1bit) | [mlir-hltcoe-MTED-plaid_v2_eng_1](./runs.md#mlir-hltcoe-mted-plaid_v2_eng_1) | [mlir-hltcoe-MNED-colbertX](./runs.md#mlir-hltcoe-mned-colbertx) | [fas-hltcoe-MTES-patapscoBM25RM3td](./runs.md#fas-hltcoe-mtes-patapscobm25rm3td) | [fas-hltcoe-MTES-patapscoBM25RM3title](./runs.md#fas-hltcoe-mtes-patapscobm25rm3title) | [rus-hltcoe-MTES-patapscoBM25RM3td](./runs.md#rus-hltcoe-mtes-patapscobm25rm3td) | [zho-hltcoe-MTES-patapscoBM25RM3td](./runs.md#zho-hltcoe-mtes-patapscobm25rm3td) | [rus-hltcoe-MTES-patapscoBM25RM3title](./runs.md#rus-hltcoe-mtes-patapscobm25rm3title) | [zho-hltcoe-MTES-patapscoBM25RM3title](./runs.md#zho-hltcoe-mtes-patapscobm25rm3title) | [fas-hltcoe-MTES-patapscoBM25RM3desc](./runs.md#fas-hltcoe-mtes-patapscobm25rm3desc) | [rus-hltcoe-MTES-patapscoBM25RM3desc](./runs.md#rus-hltcoe-mtes-patapscobm25rm3desc) | [zho-hltcoe-MTES-patapscoBM25RM3desc](./runs.md#zho-hltcoe-mtes-patapscobm25rm3desc) | [fas-hltcoe-MNES-patapscoBM25RM3td](./runs.md#fas-hltcoe-mnes-patapscobm25rm3td) | [rus-hltcoe-MNES-patapscoBM25RM3td](./runs.md#rus-hltcoe-mnes-patapscobm25rm3td) | [zho-hltcoe-MNES-patapscoBM25RM3td](./runs.md#zho-hltcoe-mnes-patapscobm25rm3td) | [fas-hltcoe-MNES-patapscoBM25RM3title](./runs.md#fas-hltcoe-mnes-patapscobm25rm3title) | [rus-hltcoe-MNES-patapscoBM25RM3title](./runs.md#rus-hltcoe-mnes-patapscobm25rm3title) | [zho-hltcoe-MNES-patapscoBM25RM3title](./runs.md#zho-hltcoe-mnes-patapscobm25rm3title) | [fas-hltcoe-MNES-patapscoBM25RM3desc](./runs.md#fas-hltcoe-mnes-patapscobm25rm3desc) | [rus-hltcoe-MNES-patapscoBM25RM3desc](./runs.md#rus-hltcoe-mnes-patapscobm25rm3desc) | [zho-hltcoe-MNES-patapscoBM25RM3desc](./runs.md#zho-hltcoe-mnes-patapscobm25rm3desc) | [fas-hltcoe-MNPS-patapscoBM25RM3td](./runs.md#fas-hltcoe-mnps-patapscobm25rm3td) | [rus-hltcoe-MNRS-patapscoBM25RM3td](./runs.md#rus-hltcoe-mnrs-patapscobm25rm3td) | [fas-hltcoe-MNPS-patapscoBM25RM3title](./runs.md#fas-hltcoe-mnps-patapscobm25rm3title) | [rus-hltcoe-MNRS-patapscoBM25RM3title](./runs.md#rus-hltcoe-mnrs-patapscobm25rm3title) | [fas-hltcoe-MNPS-patapscoBM25RM3desc](./runs.md#fas-hltcoe-mnps-patapscobm25rm3desc) | [rus-hltcoe-MNRS-patapscoBM25RM3desc](./runs.md#rus-hltcoe-mnrs-patapscobm25rm3desc) | [fas-hltcoe-MTES-patapscoBM25noRM3td](./runs.md#fas-hltcoe-mtes-patapscobm25norm3td) | [rus-hltcoe-MTES-patapscoBM25noRM3td](./runs.md#rus-hltcoe-mtes-patapscobm25norm3td) | [zho-hltcoe-MTES-patapscoBM25noRM3td](./runs.md#zho-hltcoe-mtes-patapscobm25norm3td) | [fas-hltcoe-MTES-patapscoBM25noRM3title](./runs.md#fas-hltcoe-mtes-patapscobm25norm3title) | [rus-hltcoe-MTES-patapscoBM25noRM3title](./runs.md#rus-hltcoe-mtes-patapscobm25norm3title) | [zho-hltcoe-MTES-patapscoBM25noRM3title](./runs.md#zho-hltcoe-mtes-patapscobm25norm3title) | [fas-hltcoe-MTES-patapscoBM25noRM3desc](./runs.md#fas-hltcoe-mtes-patapscobm25norm3desc) | [rus-hltcoe-MTES-patapscoBM25noRM3desc](./runs.md#rus-hltcoe-mtes-patapscobm25norm3desc) | [zho-hltcoe-MTES-patapscoBM25noRM3desc](./runs.md#zho-hltcoe-mtes-patapscobm25norm3desc) | [fas-hltcoe-MNES-patapscoBM25noRM3td](./runs.md#fas-hltcoe-mnes-patapscobm25norm3td) | [rus-hltcoe-MNES-patapscoBM25noRM3td](./runs.md#rus-hltcoe-mnes-patapscobm25norm3td) | [zho-hltcoe-MNES-patapscoBM25noRM3td](./runs.md#zho-hltcoe-mnes-patapscobm25norm3td) | [fas-hltcoe-MNES-patapscoBM25noRM3title](./runs.md#fas-hltcoe-mnes-patapscobm25norm3title) | [rus-hltcoe-MNES-patapscoBM25noRM3title](./runs.md#rus-hltcoe-mnes-patapscobm25norm3title) | [zho-hltcoe-MNES-patapscoBM25noRM3title](./runs.md#zho-hltcoe-mnes-patapscobm25norm3title) | [fas-hltcoe-MNES-patapscoBM25noRM3desc](./runs.md#fas-hltcoe-mnes-patapscobm25norm3desc) | [rus-hltcoe-MNES-patapscoBM25noRM3desc](./runs.md#rus-hltcoe-mnes-patapscobm25norm3desc) | [zho-hltcoe-MNES-patapscoBM25noRM3desc](./runs.md#zho-hltcoe-mnes-patapscobm25norm3desc) | [fas-hltcoe-MNPS-patapscoBM25noRM3td](./runs.md#fas-hltcoe-mnps-patapscobm25norm3td) | [rus-hltcoe-MNRS-patapscoBM25noRM3td](./runs.md#rus-hltcoe-mnrs-patapscobm25norm3td) | [fas-hltcoe-MNPS-patapscoBM25noRM3title](./runs.md#fas-hltcoe-mnps-patapscobm25norm3title) | [rus-hltcoe-MNRS-patapscoBM25noRM3title](./runs.md#rus-hltcoe-mnrs-patapscobm25norm3title) | [fas-hltcoe-MNPS-patapscoBM25noRM3desc](./runs.md#fas-hltcoe-mnps-patapscobm25norm3desc) | [rus-hltcoe-MNRS-patapscoBM25noRM3desc](./runs.md#rus-hltcoe-mnrs-patapscobm25norm3desc) | [mlir-hltcoe-MTES-patapscoBM25RM3td](./runs.md#mlir-hltcoe-mtes-patapscobm25rm3td) | [mlir-hltcoe-MTES-patapscoBM25RM3title](./runs.md#mlir-hltcoe-mtes-patapscobm25rm3title) | [mlir-hltcoe-MTES-patapscoBM25RM3desc](./runs.md#mlir-hltcoe-mtes-patapscobm25rm3desc) | [mlir-hltcoe-MTES-patapscoBM25noRM3td](./runs.md#mlir-hltcoe-mtes-patapscobm25norm3td) | [mlir-hltcoe-MTES-patapscoBM25noRM3title](./runs.md#mlir-hltcoe-mtes-patapscobm25norm3title) | [mlir-hltcoe-MTES-patapscoBM25noRM3desc](./runs.md#mlir-hltcoe-mtes-patapscobm25norm3desc) | [zho-hltcoe-DEMN-PLAIDkd-monomt5tt-td](./runs.md#zho-hltcoe-demn-plaidkd-monomt5tt-td) | [mlir-hltcoe-MNED-plaid_v1_mtt_1bit_date](./runs.md#mlir-hltcoe-mned-plaid_v1_mtt_1bit_date) | [zho-hltcoe-MNCS-patapscoBM25RM3td](./runs.md#zho-hltcoe-mncs-patapscobm25rm3td) | [zho-hltcoe-MNCS-patapscoBM25RM3title](./runs.md#zho-hltcoe-mncs-patapscobm25rm3title) | [zho-hltcoe-MNCS-patapscoBM25RM3desc](./runs.md#zho-hltcoe-mncs-patapscobm25rm3desc) | [zho-hltcoe-MNCS-patapscoBM25noRM3td](./runs.md#zho-hltcoe-mncs-patapscobm25norm3td) | [zho-hltcoe-MNCS-patapscoBM25noRM3title](./runs.md#zho-hltcoe-mncs-patapscobm25norm3title) | [zho-hltcoe-MNCS-patapscoBM25noRM3desc](./runs.md#zho-hltcoe-mncs-patapscobm25norm3desc) | [tech-hltcoe-MNES-psq_t_f32](./runs.md#tech-hltcoe-mnes-psq_t_f32) | [tech-hltcoe-MNES-psq_td_f32](./runs.md#tech-hltcoe-mnes-psq_td_f32) | [tech-hltcoe-MTES-patapsco_bm25_d_rm3](./runs.md#tech-hltcoe-mtes-patapsco_bm25_d_rm3) | [tech-hltcoe-MTES-patapsco_bm25_td_rm3](./runs.md#tech-hltcoe-mtes-patapsco_bm25_td_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_d_rm3](./runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_d_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_td_rm3](./runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_td_rm3) | [tech-hltcoe-MNES-patapsco_bm25_qt_t_rm3](./runs.md#tech-hltcoe-mnes-patapsco_bm25_qt_t_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_d_rm3](./runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_d_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_t_rm3](./runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_t_rm3) | [tech-hltcoe-MNCS-patapsco_bm25_ht_td_rm3](./runs.md#tech-hltcoe-mncs-patapsco_bm25_ht_td_rm3) | [tech-hltcoe-MNEL-blade-t](./runs.md#tech-hltcoe-mnel-blade-t) | [tech-hltcoe-MNEL-blade-d](./runs.md#tech-hltcoe-mnel-blade-d) | [tech-hltcoe-MNEL-blade-td](./runs.md#tech-hltcoe-mnel-blade-td) | [tech-hltcoe-2MNEH-rerank_mt5gt_td](./runs.md#tech-hltcoe-2mneh-rerank_mt5gt_td) | [tech-hltcoe-2MNCH-rerank_mt5ht_td](./runs.md#tech-hltcoe-2mnch-rerank_mt5ht_td) | [tech-hltcoe-MNCD-plaid_monozh_mt5ht_td](./runs.md#tech-hltcoe-mncd-plaid_monozh_mt5ht_td) | [tech-hltcoe-MNED-plaid_tt_mt5gt_td](./runs.md#tech-hltcoe-mned-plaid_tt_mt5gt_td) | [tech-hltcoe-MNED-plaid_tt_td](./runs.md#tech-hltcoe-mned-plaid_tt_td) | [tech-hltcoe-MNED-plaid_distilled_td](./runs.md#tech-hltcoe-mned-plaid_distilled_td) | [tech-hltcoe-MTED-plaid_V2model_td](./runs.md#tech-hltcoe-mted-plaid_v2model_td) | [tech-hltcoe-MNCD-plaid_mono_td](./runs.md#tech-hltcoe-mncd-plaid_mono_td) | [tech-hltcoe-MNED-plaid_jhpolo_td](./runs.md#tech-hltcoe-mned-plaid_jhpolo_td) | [tech-hltcoe-MNED-colbert_x_td](./runs.md#tech-hltcoe-mned-colbert_x_td) | [tech-hltcoe-MTES-patapsco_bm25_t_rm3](./runs.md#tech-hltcoe-mtes-patapsco_bm25_t_rm3)

??? abstract "Abstract"
	
	The HLTCOE team applied PLAID, an mT5 reranker, and docu-ment translation to the TREC 2023 NeuCLIR track. For PLAID weincluded a variety of models and training techniques – the Englishmodel released with ColBERT v2, translate-train (TT), TranslateDistill (TD) and multilingual translate-train (MTT). TT trains aColBERT model with English queries and passages automaticallytranslated into the document language from the MS-MARCO v1collection. This results in three cross-language models for the track,one per language. MTT creates a single model for all three doc-ument languages by combining the translations of MS-MARCOpassages in all three languages into mixed-language batches. Thusthe model learns about matching queries to passages simultane-ously in all languages. Distillation uses scores from the mT5 modelover non-English translated document pairs to learn how to scorequery-document pairs. The team submitted runs to all NeuCLIRtasks: the CLIR and MLIR news task as well as the technical docu-ments task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLM23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [umd_hcil](./participants.md#umd_hcil)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/umd_hcil.N.pdf](https://trec.nist.gov/pubs/trec32/papers/umd_hcil.N.pdf)
- :material-file-search: **Runs:** [fas-umd_hcil-AELN_blade](./runs.md#fas-umd_hcil-aeln_blade) | [zho-umd_hcil-AELN_blade](./runs.md#zho-umd_hcil-aeln_blade) | [rus-umd_hcil-AELN_blade](./runs.md#rus-umd_hcil-aeln_blade)

??? abstract "Abstract"
	
	The University of Maryland submitted three runs to the Ad Hoc CLIR Task of the TREC 2023NeuCLIR track. This paper describes three systems that cross the language barrier using a learnedsparse retrieval model using bilingual embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NairO23.bib) "
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

