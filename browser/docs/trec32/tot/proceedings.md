# Proceedings - Tip-of-the-Tongue 2023

#### Overview of the TREC 2023 Tip-of-the-Tongue Track

_Jaime Arguello,  Samarth Bhargav,  Fernando Diaz,  Evangelos Kanoulas,  Bhaskar Mitra_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_tot.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_tot.pdf)
??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves supporting searchers interested in refindinga previously encountered item for which they are unable to reliably recall an identifier. ToT requeststend to be verbose and include several complex phenomena, making them especially difficult for ex-isting information retrieval systems. The TREC 2023 ToT track focused on a single ad-hoc retrievaltask in the movie domain. Requests were sampled from an existing ToT dataset and the documentcorpus consisted of a subset of Wikipedia pages associated with the “audiovisual works” category.This year 11 groups submitted a total of 33 runs. Consistent with earlier findings, there is a negativecorrelation between query length and retrieval performance. We found that successful teams wereable to leverage large external datasets to substantially improve performance. While a closed largelanguage model managed to beat 26 participant runs, it did so with much lower recall.Track website: https://trec-tot.github.io
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArguelloBDKM23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI](./participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf](https://trec.nist.gov/pubs/trec32/papers/CMU-LTI.T.pdf)
- :material-file-search: **Runs:** [dpr-100-rerank](./runs.md#dpr-100-rerank) | [dpr-1000-rerank-robin](./runs.md#dpr-1000-rerank-robin) | [dpr-abstract-100-rerank](./runs.md#dpr-abstract-100-rerank) | [dpr-abstract-1000-robin](./runs.md#dpr-abstract-1000-robin)

??? abstract "Abstract"
	
	This paper describes our submissions to the 2023 TREC Tip- of-the-Tongue (ToT) track. We opted for the common retrieval method- ology of a Recall oriented first-stage retrieval, followed by the use of a more accurate re-ranker model. For first-stage retrieval, we considered a DPR retriever either aggregating the passages from the documents, or matching different parts of the queries against the abstract sections of the Wikipedia articles that describe the movies. Re-ranking was dele- gated to a Large Language Model (LLM) in a zero-shot setting, taking as input the movie titles from the first stage of retrieval. Results attest to the effectiveness of the proposed approach with the best run achieving an NDCG@1000 of 0.55.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorgesCM23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Webis.T.pdf](https://trec.nist.gov/pubs/trec32/papers/Webis.T.pdf)
- :material-file-search: **Runs:** [webis-t5-01](./runs.md#webis-t5-01) | [webis-t5-f](./runs.md#webis-t5-f) | [webis-fus-01](./runs.md#webis-fus-01) | [webis-bm25r-1](./runs.md#webis-bm25r-1) | [webis-t53b-01](./runs.md#webis-t53b-01)

??? abstract "Abstract"
	
	In this paper, we describe the Webis Group’s participation in theTREC 2023 Tip-of-the-Tongue track. Our runs focus on improvingthe retrieval effectiveness via query relaxation (i.e., leaving outterms that likely reduce the retrieval effectiveness). We combineBERT- or ChatGPT-based query relaxation with BM25- or monoT5-based retrieval and also experiment with reciprocal rank fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrobeBKSH23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [RSLTOT](./participants.md#rsltot)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/RSLTOT.T.pdf](https://trec.nist.gov/pubs/trec32/papers/RSLTOT.T.pdf)
- :material-file-search: **Runs:** [RSLTOTY](./runs.md#rsltoty)

??? abstract "Abstract"
	
	In this study, we focused on the situation that a user can recall only the movie’s synopsis, character features, etc., but not the movie’s title. In our experiment, we introduced systems based on TF– IDF and BERT. The results showed that our TF–IDF vectorizer is better than our BERT model if they are used individually. In addition, as each system showed different tendencies in the results, we tried a hybrid model combining these two systems. The results showed that combining these models outperformed the two component models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YoshikoshiS23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [endicott-unc](./participants.md#endicott-unc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/endicott-unc.T.pdf](https://trec.nist.gov/pubs/trec32/papers/endicott-unc.T.pdf)
- :material-file-search: **Runs:** [endicott_unc_baseline](./runs.md#endicott_unc_baseline) | [endicott_unc_boost_oracle](./runs.md#endicott_unc_boost_oracle) | [endicott_unc_boost_pred](./runs.md#endicott_unc_boost_pred) | [endicott_unc_boost_conf](./runs.md#endicott_unc_boost_conf)

??? abstract "Abstract"
	
	Tip-of-the-tongue (ToT) known-item retrieval involves retrievinga previously encountered item for which the searcher is unableto reliably recall an identifier. The TREC 2023 ToT track focusedon an ad-hoc retrieval task in the movie identification domain.The Endicott and UNC team submitted four runs to the track. Ourbaseline run used BM25, while our three experimental runs used a“boosted” version of BM25 that weighed query-terms differently. AllToT queries used in the track had sentence-level annotations basedon the topics and language phenomena found in the sentence. Ourthree experimental runs weighed query-terms depending on thesentence-level categories associated with the sentence from whicheach query-term originated. One experimental run weighed query-terms using gold-standard sentence-level categories. The other twoused predicted categories. Across all metrics considered, our threeexperimental runs outperformed our baseline run by a statisticallysignificant margin. Differences between experimental runs werenot statistically significant across metrics. Our results suggest thatsentence-level categories were predicted with sufficient accuracyto inform the re-weighing of query-terms to improve retrievalperformance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FeildA23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [ufmg](./participants.md#ufmg)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/ufmg.T.pdf](https://trec.nist.gov/pubs/trec32/papers/ufmg.T.pdf)
- :material-file-search: **Runs:** [ufmgDBmBQD](./runs.md#ufmgdbmbqd) | [ufmgDBmBdTQD](./runs.md#ufmgdbmbdtqd) | [ufmgG4mBQD](./runs.md#ufmgg4mbqd) | [ufmgG4dTQD](./runs.md#ufmgg4dtqd) | [ufmgDBmBQ](./runs.md#ufmgdbmbq)

??? abstract "Abstract"
	
	In the TREC 2023 Tip of the Tongue (ToT)track, we address the challenge of movieretrieval from queries laden with impre-cise or incorrect natural language. In par-ticular, the Movie Identification Task aimsto produce a well-ranked list of movies,identified by Wikipedia page IDs, in re-sponse to a set of queries in Tip of theTongue (TOT) format. In our participa-tion, we experiment with reranking tech-niques, leveraging both sparse and denseretrieval approaches to refine the returnedresults. Additionally, we incorporate termfiltering heuristics for both queries anddocuments, enhancing the overall effec-tiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimaS23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [snuldilab](./participants.md#snuldilab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/snuldilab.T.pdf](https://trec.nist.gov/pubs/trec32/papers/snuldilab.T.pdf)
- :material-file-search: **Runs:** [pre_aug_vat](./runs.md#pre_aug_vat) | [pre_aug_vat_max4_origin](./runs.md#pre_aug_vat_max4_origin) | [pre_aug_vat_max4](./runs.md#pre_aug_vat_max4)

??? abstract "Abstract"
	
	This paper describes our participation in theTREC 2023 Tip-of-the-Tongue (ToT) Track.Our first contribution involves formulating theproblem as a retrieval, of finding a relevantdocument with a much shorter query. Inspiredby a self-supervised learning approach, we ex-tract ToT query surrogates from the corpus andpair them with the document. These pairs areused for self-supervised training and then en-riching document representations to handle in-sufficiency. Second, we augment ToT querieswith cropping and adversarial perturbation. Ourresults in the ToT benchmark show that ourmodel outperforms state-of-the-art methods in-cluding GPT-4 and performs competitively inthe TREC-ToT competition.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimHH23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf](https://trec.nist.gov/pubs/trec32/papers/UWaterlooMDS.DT.pdf)
- :material-file-search: **Runs:** [WatS-DR](./runs.md#wats-dr) | [WatS-TDR](./runs.md#wats-tdr) | [WatS-TDR-RR](./runs.md#wats-tdr-rr)

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

