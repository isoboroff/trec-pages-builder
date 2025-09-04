# Proceedings - Relevance Feedback 2009

#### FUB at TREC 2009 Relevance Feedback Track: Diversifying Feedback  Documents (Extended Abstract)

_Andrea Bernardini,  Claudio Carpineto,  Edgardo Ambrosi_

- :fontawesome-solid-user-group: **Participant:** [FUB](./participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf)
- :material-file-search: **Runs:** [fub.1](./runs.md#fub1) | [FUB9RF.fub.1](./runs.md#fub9rffub1) | [FUB9RF.CMU.1](./runs.md#fub9rfcmu1) | [FUB9RF.QUT.1](./runs.md#fub9rfqut1) | [FUB9RF.twen.2](./runs.md#fub9rftwen2) | [FUB9RF.ilps.2](./runs.md#fub9rfilps2) | [FUB9RF.PRIS.1](./runs.md#fub9rfpris1) | [FUB9RF.UMas.1](./runs.md#fub9rfumas1) | [FUB9RF.base](./runs.md#fub9rfbase)

??? abstract "Abstract"
	
	The focus of our participation was optimal selection and use of diverse feedback documents. Assuming that the query has a topical structure and that the user is interested only in some query topics and assuming also that only a small amount of feedback information will be made available, the goal was to select topic representatives to be used as feedback documents and then exploit the feedback information to bias the set of results towards the topics of interest. Our method consists of the following steps. The selection of topic representatives was performed by running a first-pass retrieval on the original query and extracting the most novel and relevant documents from the obtained results. Such documents were returned for manual evaluation and the provided feedback was given as an input to an improved version of the relevance feedback system that we developed at TREC 2008 Relevance Feedback track. As this system was designed for explicitly dealing with both positive and negative relevance feedback, we reckoned that in principle it would be able to use the diverse topic representatives to filter out the highly-ranked documents belonging to the unwanted topics in an effective manner. Unfortunately, due to resource and time limitations, we were not able to fully implement and test the method outlined above. We had to make a number of approximations and simplifications that did not allow us to evaluate its true potential for improving relevance feedback. Likewise, we could not test our main hypothesis that this method is suitable for dealing with multi-topic queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernardiniCA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernardiniCA09,
		author = {Andrea Bernardini and Claudio Carpineto and Edgardo Ambrosi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FUB} at {TREC} 2009 Relevance Feedback Track: Diversifying Feedback Documents (Extended Abstract)},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/fub.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernardiniCA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Padua at TREC 2009: Relevance Feedback Track

_Emanuele Di Buccio,  Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD](./participants.md#upd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf)
- :material-file-search: **Runs:** [UPD.1](./runs.md#upd1) | [UPD9RF.base](./runs.md#upd9rfbase) | [UPD9RF.CMU.1](./runs.md#upd9rfcmu1) | [UPD9RF.PRIS.1](./runs.md#upd9rfpris1) | [UPD9RF.QUT.1](./runs.md#upd9rfqut1) | [UPD9RF.UMas.1](./runs.md#upd9rfumas1) | [UPD9RF.UPD.1](./runs.md#upd9rfupd1) | [UPD9RF.hit2.1](./runs.md#upd9rfhit21) | [UPD9RF.ilps.2](./runs.md#upd9rfilps2)

??? abstract "Abstract"
	
	In the Relevance Feedback (RF) task the user is directly involved in the search process: given an initial set of results, he specifies if they are relevant or not to the achievement of his information goal. In the TREC 2009 RF track the first five documents retrieved by the baseline systems were judged by the assessors and then used as evidence for the RF algorithms to be tested. The specific algorithm we tested is mainly based on a geometric framework which allows the latent semantic associations of terms in the feedback documents to be modeled as a vector subspace; the documents of the collection represented as vectors of TF·IDF weights were re-ranked according to their distance from the subspace. The adopted geometric framework was used in past works as a basis for Implicit Relevance Feedback (IRF) and Pseudo Relevance Feedback (PRF) algorithms; the participation to the RF track allows us to make some preliminary investigations on the effectiveness of the adopted framework when it is exploited to support explicit RF on much larger test collections, thus complementing the work carried out for the other RF strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioM09,
		author = {Emanuele Di Buccio and Massimo Melucci},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Padua at {TREC} 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/upadua.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Minimal Test Collections for Relevance Feedback

_Ben Carterette,  Praveen Chandar,  Aparna Kailasam,  Divya Muppaneni,  Sree Lekha Thota_

- :fontawesome-solid-user-group: **Participant:** [UDel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf)
- :material-file-search: **Runs:** [udel.1](./runs.md#udel1) | [udel.2](./runs.md#udel2) | [udel2.SIEL.1](./runs.md#udel2siel1) | [udel2.Sab.1](./runs.md#udel2sab1) | [udel2.UCSC.1](./runs.md#udel2ucsc1) | [udel2.WatS.1](./runs.md#udel2wats1) | [udel2.fub.1](./runs.md#udel2fub1) | [udel2.twen.1](./runs.md#udel2twen1) | [udel2.udel.1](./runs.md#udel2udel1) | [udel2.udel.2](./runs.md#udel2udel2) | [udel2.base](./runs.md#udel2base)

??? abstract "Abstract"
	
	The Information Retrieval Lab at the University of Delaware participated in the Relevance Feedback track at TREC 2009. We used only the Category B subset of the ClueWeb collection; our preprocessing and indexing steps are described in our paper on ad hoc and diversity runs [10]. The second year of the Relevance Feedback track focused on selection of documents for feedback. Our hypothesis is that documents that are good at distinguishing systems in terms of their effectiveness by mean average precision will also be good documents for relevance feedback. Thus we have applied the document selection algorithm MTC (Minimal Test Collections) developed by Carterette et al. [6, 4, 9, 5] that is used in the Million Query Track [2, 1, 8] for selecting documents to be judged to find the right ranking of systems. Our approach can therefore be described as “MTC for Relevance Feedback”.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteCKMT09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteCKMT09,
		author = {Ben Carterette and Praveen Chandar and Aparna Kailasam and Divya Muppaneni and Sree Lekha Thota},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Minimal Test Collections for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-ben.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteCKMT09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Amherst and UT Austin @ the TREC 2009 Relevance Feedback  Track

_Marc-Allen Cartright,  Jangwon Seo,  Matthew Lease_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf)
- :material-file-search: **Runs:** [UMas.1](./runs.md#umas1) | [UMas.2](./runs.md#umas2) | [UMa9RF.base](./runs.md#uma9rfbase) | [UMa9RF.PRIS.1](./runs.md#uma9rfpris1) | [UMa9RF.UCSC.2](./runs.md#uma9rfucsc2) | [UMa9RF.UMas.1](./runs.md#uma9rfumas1) | [UMa9RF.UMas.2](./runs.md#uma9rfumas2) | [UMa9RF.YUIR.2](./runs.md#uma9rfyuir2) | [UMa9RF.ilps.1](./runs.md#uma9rfilps1) | [UMa9RF.ugTr.1](./runs.md#uma9rfugtr1)

??? abstract "Abstract"
	
	We present a new supervised method for estimating term-based retrieval models and apply it to weight expansion terms from relevance feedback. While previous work on supervised feedback [Cao et al., 2008] demonstrated significantly improved retrieval accuracy over standard unsupervised approaches [Lavrenko and Croft, 2001, Zhai and Lafferty, 2001], feedback terms were assumed to be independent in order to reduce training time. In contrast, we adapt the AdaRank learning algorithm [Xu and Li, 2007] to simultaneously estimate parameterization of all feedback terms. While not evaluated here, the method can be more generally applied for joint estimation of both query and feedback terms. To apply our method to a large web collection, we also investigate use of sampling to reduce feature extraction time while maintaining robust learning.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CartrightSL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CartrightSL09,
		author = {Marc{-}Allen Cartright and Jangwon Seo and Matthew Lease},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Amherst and {UT} Austin @ the {TREC} 2009 Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/umass-amhearst.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CartrightSL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack,  Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [WAT2.base](./runs.md#wat2base) | [WAT2.CMIC.2](./runs.md#wat2cmic2) | [WAT2.MSRC.2](./runs.md#wat2msrc2) | [WAT2.UCSC.1](./runs.md#wat2ucsc1) | [WAT2.UPD.1](./runs.md#wat2upd1) | [WAT2.WatS.2](./runs.md#wat2wats2) | [WAT2.YUIR.1](./runs.md#wat2yuir1) | [WAT2.hit2.2](./runs.md#wat2hit22) | [WAT2.udel.1](./runs.md#wat2udel1)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2009: Web and Relevance Feedback Track

_Nick Craswell,  Dennis Fetterly,  Marc Najork,  Stephen Robertson,  Emine Yilmaz_

- :fontawesome-solid-user-group: **Participant:** [msrc](./participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf)
- :material-file-search: **Runs:** [MSRC.2](./runs.md#msrc2) | [MSRC.1](./runs.md#msrc1) | [MSRC.CMU.1](./runs.md#msrccmu1)

??? abstract "Abstract"
	
	We took part in the Web and Relevance Feedback tracks, using the ClueWeb09 corpus. To process the corpus, we developed a parallel processing pipeline which avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline and how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellFNRY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellFNRY09,
		author = {Nick Craswell and Dennis Fetterly and Marc Najork and Stephen Robertson and Emine Yilmaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2009: Web and Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/microsoft.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellFNRY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMIC@TREC 2009: Relevance Feedback Track

_Kareem Darwish,  Ahmed El-Deeb_

- :fontawesome-solid-user-group: **Participant:** [CMIC](./participants.md#cmic)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf)
- :material-file-search: **Runs:** [CMIC.1](./runs.md#cmic1) | [CMIC.2](./runs.md#cmic2) | [CMIC.base](./runs.md#cmicbase) | [CMIC.CMIC.1](./runs.md#cmiccmic1) | [CMIC.CMIC.2](./runs.md#cmiccmic2) | [CMIC.MSRC.1](./runs.md#cmicmsrc1) | [CMIC.UMas.2](./runs.md#cmicumas2) | [CMIC.ilps.1](./runs.md#cmicilps1) | [CMIC.udel.1](./runs.md#cmicudel1) | [CMIC.udel.2](./runs.md#cmicudel2) | [CMIC.ugTr.2](./runs.md#cmicugtr2)

??? abstract "Abstract"
	
	This paper describes CMIC's submissions to the TREC'09 relevance feedback track. In the phase 1 runs we submitted, we experimented with two different techniques to produce 5 documents to be judged by the user in the initial feedback step, namely using knowledge bases and clustering. Both techniques attempt to topically diversify these 5 documents as much as possible in an effort to maximize the probability that they contain at least 1 relevant document. The basic premise is that if a query has n diverse interpretations, then diversifying results and picking the top 5 most likely interpretations would maximize the probability that a user would be interested in at least one interpretation. In phase 2 runs, which involved the use of the feedback attained from phase 1 judgments, we attempted to use positive and negative judgments in weighing the terms to be used for subsequent feedback. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishE09.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishE09,
		author = {Kareem Darwish and Ahmed El{-}Deeb},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {CMIC@TREC 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmic.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishE09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pairwise Document Classification for Relevance Feedback

_Jonathan L. Elsas,  Pinar Donmez,  Jamie Callan,  Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf)
- :material-file-search: **Runs:** [CMU.1](./runs.md#cmu1) | [CMU.base](./runs.md#cmubase) | [CMU.CMIC.1](./runs.md#cmucmic1) | [CMU.CMIC.2](./runs.md#cmucmic2) | [CMU.CMU.1](./runs.md#cmucmu1) | [CMU.FDU.1](./runs.md#cmufdu1) | [CMU.MSRC.1](./runs.md#cmumsrc1) | [CMU.UMas.2](./runs.md#cmuumas2) | [CMU.YUIR.2](./runs.md#cmuyuir2)

??? abstract "Abstract"
	
	In this paper we present Carnegie Mellon University's submission to the TREC 2009 Relevance Feedback Track. In this submission we take a classification approach on document pairs to using relevance feedback information. We explore using textual and non-textual document-pair features to classify unjudged documents as relevant or non-relevant, and use this prediction to re-rank a baseline document retrieval. These features include co-citation measures, URL similarities, as well as features often used in machine learning systems for document ranking such as the difference in scores assigned by the baseline retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ElsasDCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ElsasDCC09,
		author = {Jonathan L. Elsas and Pinar Donmez and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pairwise Document Classification for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/cmu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ElsasDCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Twente @ TREC 2009: Indexing Half a Million Web Pages

_Claudia Hauff,  Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf)
- :material-file-search: **Runs:** [twen.1](./runs.md#twen1) | [twen.2](./runs.md#twen2) | [twen.base](./runs.md#twenbase) | [twen.FDU.1](./runs.md#twenfdu1) | [twen.ilps.1](./runs.md#twenilps1) | [twen.UCSC.2](./runs.md#twenucsc2) | [twen.twen.1](./runs.md#twentwen1) | [twen.YUIR.2](./runs.md#twenyuir2) | [twen.ugTr.1](./runs.md#twenugtr1) | [twen.twen.2](./runs.md#twentwen2)

??? abstract "Abstract"
	
	The University of Twente participated in three tasks of TREC 2009: the adhoc task, the diversity task and the relevance feedback task. All experiments are performed on the English part of ClueWeb09. We describe our approach to tuning our retrieval system in absence of training data in Section 3. We describe the use of categories and a query log for diversifying search results in Section 4. Section 5 describes preliminary results for the relevance feedback task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauffH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauffH09,
		author = {Claudia Hauff and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Twente @ {TREC} 2009: Indexing Half a Million Web Pages},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/utwente.WEB.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauffH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at 2009 Relevance Feedback Track: Experiments in Language Model  for Relevance Feedback

_Si Li,  Xinsheng Li,  Hao Zhang,  Sanyuan Gao,  Guang Chen,  Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf)
- :material-file-search: **Runs:** [PRIS.1](./runs.md#pris1) | [PRIS.base](./runs.md#prisbase) | [PRIS.ilps.1](./runs.md#prisilps1) | [PRIS.PRIS.1](./runs.md#prispris1) | [PRIS.Sab.1](./runs.md#prissab1) | [PRIS.SIEL.1](./runs.md#prissiel1) | [PRIS.UCSC.1](./runs.md#prisucsc1) | [PRIS.hit2.2](./runs.md#prishit22) | [PRIS.twen.1](./runs.md#pristwen1)

??? abstract "Abstract"
	
	This paper describes BUPT (pris) participation in Relevance Feedback Track 2009. The track has two phrases. In the first phrase, 5 documents are submitted based on the results of the k-means. In the second phrase, language model is used to relevance feedback for query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiLZGCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiLZGCG09,
		author = {Si Li and Xinsheng Li and Hao Zhang and Sanyuan Gao and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at 2009 Relevance Feedback Track: Experiments in Language Model for Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pris.RF.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiLZGCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mining Specific and General Features in Both Positive and Negative  Relevance Feedback

_Yuefeng Li,  Xiaohui Tao,  Abdulmohsen Algarni,  Sheng-Tang Wu_

- :fontawesome-solid-user-group: **Participant:** [QUT_ED_Lab](./participants.md#qut_ed_lab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf)
- :material-file-search: **Runs:** [QUT.1](./runs.md#qut1) | [QUT.base](./runs.md#qutbase) | [QUT.CMIC.1](./runs.md#qutcmic1) | [QUT.MSRC.2](./runs.md#qutmsrc2) | [QUT.QUT.1](./runs.md#qutqut1) | [QUT.SIEL.1](./runs.md#qutsiel1) | [QUT.UPD.1](./runs.md#qutupd1) | [QUT.WatS.1](./runs.md#qutwats1) | [QUT.YUIR.2](./runs.md#qutyuir2) | [QUT.hit2.1](./runs.md#quthit21)

??? abstract "Abstract"
	
	User relevance feedback is usually utilized by Web systems to interpret user information needs and retrieve effective results for users. However, how to discover useful knowledge in user relevance feedback and how to wisely use the discovery knowledge are two critical problems. In TREC 2009, we participated in the Relevance Feedback Track and experimented a model consisting of two innovative stages: one for subject-based query expansion to extract pseudo-relevance feedback; one for relevance feature discovery to find useful patterns and terms in relevance judgements to rank documents. In this paper, the detailed description of our model is given, as well as the related discussions for the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiTAW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiTAW09,
		author = {Yuefeng Li and Xiaohui Tao and Abdulmohsen Algarni and Sheng{-}Tang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mining Specific and General Features in Both Positive and Negative Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/queenslandu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiTAW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie,  Craig Macdonald,  Iadh Ounis,  Jie Peng,  Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [ugTr.1](./runs.md#ugtr1) | [ugTr.2](./runs.md#ugtr2) | [ugTr.base](./runs.md#ugtrbase) | [ugTr.CMU.1](./runs.md#ugtrcmu1) | [ugTr.hit2.1](./runs.md#ugtrhit21) | [ugTr.ilps.2](./runs.md#ugtrilps2) | [ugTr.ugTr.1](./runs.md#ugtrugtr1) | [ugTr.ugTr.2](./runs.md#ugtrugtr2) | [ugTr.UMas.1](./runs.md#ugtrumas1) | [ugTr.UPD.1](./runs.md#ugtrupd1) | [ugTr.YUIR.1](./runs.md#ugtryuir1)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topical Diversity and Relevance Feedback

_Edgar Meij,  Jiyin He,  Wouter Weerkamp,  Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf)
- :material-file-search: **Runs:** [ilps.2](./runs.md#ilps2) | [ilps.1](./runs.md#ilps1) | [IlpsRF.base](./runs.md#ilpsrfbase) | [IlpsRF.QUT.1](./runs.md#ilpsrfqut1) | [IlpsRF.Sab.1](./runs.md#ilpsrfsab1) | [IlpsRF.WatS.1](./runs.md#ilpsrfwats1) | [IlpsRF.fub.1](./runs.md#ilpsrffub1) | [IlpsRF.ilps.1](./runs.md#ilpsrfilps1) | [IlpsRF.ilps.2](./runs.md#ilpsrfilps2) | [IlpsRF.twen.1](./runs.md#ilpsrftwen1) | [IlpsRF.twen.2](./runs.md#ilpsrftwen2)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's Intelligent Systems Lab in the relevance feedback track at TREC 2009. Our main conclusion for the relevance feedback track is that a topical diversity approach provides good feedback documents. Further, we find that our relevance feedback algorithm seems to help most when there are sufficient relevant documents available.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijHWR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijHWR09,
		author = {Edgar Meij and Jiyin He and Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topical Diversity and Relevance Feedback},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijHWR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with ClueWeb09: Relevance Feedback and Web Tracks

_Mark D. Smucker,  Charles L. A. Clarke,  Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf)
- :material-file-search: **Runs:** [WatS.1](./runs.md#wats1) | [WatS.2](./runs.md#wats2) | [WatS.base](./runs.md#watsbase) | [WatS.SIEL.1](./runs.md#watssiel1) | [WatS.Sab.1](./runs.md#watssab1) | [WatS.UCSC.1](./runs.md#watsucsc1) | [WatS.WatS.1](./runs.md#watswats1) | [WatS.WatS.2](./runs.md#watswats2) | [WatS.fub.1](./runs.md#watsfub1) | [WatS.twen.1](./runs.md#watstwen1) | [WatS.twen.2](./runs.md#watstwen2)

??? abstract "Abstract"
	
	In this paper, we report on our TREC experiments with the ClueWeb09 document collection. We participated in the relevance feedback and web tracks. While our phase 1 relevance feedback run's performance was good, our other relevance feedback and web track submissions' performances were lacking. We suspect this performance difference is caused by the Category B document subset of the ClueWeb09 collection having a higher prior probability of relevance than the rest of the collection. Future work will involve a more detailed error analysis of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCC09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCC09,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with ClueWeb09: Relevance Feedback and Web Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCC09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Feedback Based on Constrained Clustering: FDU at TREC  09

_Bingqing Wang,  Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [FDU_MEDLAB](./participants.md#fdu_medlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf)
- :material-file-search: **Runs:** [FDU.1](./runs.md#fdu1) | [FDURFN.base](./runs.md#fdurfnbase) | [FDURFN.PRIS.1](./runs.md#fdurfnpris1) | [FDURFN.QUT.1](./runs.md#fdurfnqut1) | [FDURFN.UMas.1](./runs.md#fdurfnumas1) | [FDURFN.fub.1](./runs.md#fdurfnfub1) | [FDURFN.twen.2](./runs.md#fdurfntwen2) | [FDURFN.WatS.1](./runs.md#fdurfnwats1) | [FDURFN.FDU.1](./runs.md#fdurfnfdu1)

??? abstract "Abstract"
	
	We introduce our participation of the TREC Relevance Feedback(RF) TRACK in 2009. The RF09 TRACK is focused on the explicit relevant feedback, where a few relevant and irrelevant documents are available to each query. Our system is implemented under the framework of probabilistic language model. We apply the constrained clustering on the top returned documents and extract the expanded words to reform the query. We also extract the named entities from the explicit relevant documents to expand the query. The experiment was conducted on the ClueWeb09 TREC Category B, which is a new and huge test collection for the TREC TRACKs. The evaluation result shows the performance of the constrained clustering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangH09,
		author = {Bingqing Wang and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback Based on Constrained Clustering: {FDU} at {TREC} 09},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/fudanu.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2009: Relevance Feedback Track

_Zheng Ye,  Xiangji Huang,  Ben He,  Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [york09](./participants.md#york09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf)
- :material-file-search: **Runs:** [YUIR.1](./runs.md#yuir1) | [YUIR.2](./runs.md#yuir2) | [YUIR.base](./runs.md#yuirbase) | [YUIR.YUIR.1](./runs.md#yuiryuir1) | [YUIR.ugTr.1](./runs.md#yuirugtr1) | [YUIR.UMas.2](./runs.md#yuirumas2) | [YUIR.FDU.1](./runs.md#yuirfdu1) | [YUIR.YUIR.2](./runs.md#yuiryuir2) | [YUIR.CMIC.1](./runs.md#yuircmic1) | [YUIR.UCSC.2](./runs.md#yuirucsc2)

??? abstract "Abstract"
	
	We describe a series of experiments conducted in our participation in the Relevance Feedback Track. We evaluate two traditional weighting models (BM25 and DFR) for the phase 1 task, which are widely used in text retrieval domain. We also evaluate a statistics-based feedback model and our proposed feedback model for the phase 2 task. Currently, we are waiting for the overview paper to facilitate further analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YeHHYL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YeHHYL09,
		author = {Zheng Ye and Xiangji Huang and Ben He and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2009: Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/yorku.RF.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YeHHYL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCSC at Relevance Feedback Track

_Lanbo Zhang,  Jadiel de Arma,  Kai Yu_

- :fontawesome-solid-user-group: **Participant:** [UCSCIRKM](./participants.md#ucscirkm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf](http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf)
- :material-file-search: **Runs:** [UCSC.1](./runs.md#ucsc1) | [UCSC.2](./runs.md#ucsc2) | [UCSC.base](./runs.md#ucscbase) | [UCSC.CMIC.1](./runs.md#ucsccmic1) | [UCSC.FDU.1](./runs.md#ucscfdu1) | [UCSC.UMas.2](./runs.md#ucscumas2) | [UCSC.ugTr.2](./runs.md#ucscugtr2) | [UCSC.udel.2](./runs.md#ucscudel2) | [UCSC.UCSC.2](./runs.md#ucscucsc2) | [UCSC.UCSC.1](./runs.md#ucscucsc1) | [UCSC.MSRC.1](./runs.md#ucscmsrc1)

??? abstract "Abstract"
	
	The relevance feedback track in TREC 2009 focuses on two sub tasks: actively selecting good documents for users to provide relevance feedback and retrieving documents based on user relevance feedback. For the first task, we tried a clustering based method and the Transductive Experimental Design (TED) method proposed by Yu et al. [5]. For clustering based method, we use the K-means algorithm to cluster the top retrieved documents and choose the most representative document of each cluster. The TED method aims to find documents that are hard-to-predict and representative of the unlabeled documents. For the second task, we did query expansion based on a relevance model learned on the relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangAY09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangAY09,
		author = {Lanbo Zhang and Jadiel de Arma and Kai Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCSC} at Relevance Feedback Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uc-santa.cruz.RF.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangAY09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

