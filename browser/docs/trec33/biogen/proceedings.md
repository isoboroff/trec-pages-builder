# Proceedings - Biomedical Generative Retrieval (BioGen) Track 2024

#### Overview of TREC 2024 Biomedical Generative Retrieval (BioGen) Track

_Deepak Gupta, Dina Demner-Fushman, William Hersh, Steven Bedrick, Kirk Roberts_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_biogen.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_biogen.pdf)
??? abstract "Abstract"
	
	With the advancement of large language models (LLMs), the biomedical domain has seen significant progress and improvement in multiple tasks such as biomedical question answering, lay language summarization of the biomedical literature, clinical note summarization, etc. However, hallucinations or confabulations remain one of the key challenges when using LLMs in the biomedical and other domains. Inaccuracies may be particularly harmful in high-risk situations, such as making clinical decisions or appraising biomedical research. Studies on the evaluation of the LLMs' abilities to ground generated statements in verifiable sources have shown that models perform significantly worse on lay-user generated questions, and often fail to reference relevant sources. This can be problematic when those seeking information want evidence from studies to back up the claims from LLMs[3]. Unsupported statements are a major barrier to using LLMs in any applications that may affect health. Methods for grounding generated statements in reliable sources along with practical evaluation approaches are needed to overcome this barrier. Towards this, in our pilot task organized at TREC 2024, we introduced the task of reference attribution as a means to mitigate the generation of false statements by LLMs answering biomedical questions.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-1,
		author = {Deepak Gupta, Dina Demner-Fushman, William Hersh, Steven Bedrick, Kirk Roberts},
		title = {Overview of TREC 2024 Biomedical Generative Retrieval (BioGen) Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {coordinators},
		trec_runs = {},
		trec_tracks = {biogen},
		url = {https://trec.nist.gov/pubs/trec33/papers/Overview_biogen.pdf}
	}
	```

#### Exploring the Few-Shot Performance of Low-Cost Proprietary Models in the 2024 TREC BioGen Track

_Samy Ateia (University of Regensburg), Udo Kruschwitz (University of Regensburg)_

- :fontawesome-solid-user-group: **Participant:** [ur-iw](./participants.md#ur-iw)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/ur-iw.biogen.pdf](https://trec.nist.gov/pubs/trec33/papers/ur-iw.biogen.pdf)
- :material-file-search: **Runs:** [zero-shot-gpt4o-mini](./runs.md#zero-shot-gpt4o-mini) | [zero-shot-gemini-flash](./runs.md#zero-shot-gemini-flash) | [ten-shot-gpt4o-mini](./runs.md#ten-shot-gpt4o-mini) | [ten-shot-gemini-flash](./runs.md#ten-shot-gemini-flash) | [ten-shot-gpt4o-mini-wiki](./runs.md#ten-shot-gpt4o-mini-wiki) | [ten-shot-gemini-flash-wiki](./runs.md#ten-shot-gemini-flash-wiki)

??? abstract "Abstract"
	
	For the 2024 TREC Biomedical Generative Retrieval (BioGen) Track, we evaluated proprietary low-cost large language models (LLMs) in few-shot and zero-shot settings for biomedical question answering. Building upon our prior competitive approach from the CLEF 2024 BioASQ challenge, we adapted our methods to the BioGen task. We reused few-shot examples from BioASQ and generated additional ones from the test set for the BioGen specific answer format, by using an LLM judge to select examples. Our approach involved query expansion, BM25-based retrieval using Elasticsearch, snippet extraction, reranking, and answer generation both with and without 10-shot learning and additional relevant context from Wikipedia. The results are in line with our findings at BioASQ, indicating that additional Wikipedia context did not improve the results, while 10-shot learning did. An interactive reference implementation that showcases Google's Gemini-1.5-flash performance with 3-shot learning is available online and the source code of this demo is available on GitHub.
	

??? quote "Bibtex"
	```
	@inproceedings{ur-iw-trec2024-papers-proc-1,
		author = {Samy Ateia (University of Regensburg), Udo Kruschwitz (University of Regensburg)},
		title = {Exploring the Few-Shot Performance of Low-Cost Proprietary Models in the 2024 TREC BioGen Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {ur-iw},
		trec_runs = {zero-shot-gpt4o-mini, zero-shot-gemini-flash, ten-shot-gpt4o-mini, ten-shot-gemini-flash, ten-shot-gpt4o-mini-wiki, ten-shot-gemini-flash-wiki},
		trec_tracks = {biogen},
		url = {https://trec.nist.gov/pubs/trec33/papers/ur-iw.biogen.pdf}
	}
	```

#### Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks

_Maik Fröbe (Friedrich-Schiller-Universität), Lukas Gienapp (Leipzig University     ScaDS.AI), Harrisen Scells (Universität Kassel), Eric Oliver Schmidt (Martin-Luther-Universität Halle), Matti Wiegmann (Bauhaus-Universität Weimar), Martin Potthast, Universität Kassel (Universität Kassel     hessian.AI     ScaDS.AI), Matthias Hagen (Friedrich-Schiller-Universität Jena)_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf)
- :material-file-search: **Runs:** [webis-1](./runs.md#webis-1) | [webis-2](./runs.md#webis-2) | [webis-3](./runs.md#webis-3) | [webis-gpt-1](./runs.md#webis-gpt-1) | [webis-gpt-4](./runs.md#webis-gpt-4) | [webis-gpt-6](./runs.md#webis-gpt-6) | [webis-5](./runs.md#webis-5)

??? abstract "Abstract"
	
	In this paper, we describe the Webis Group's participation in the 2024~edition of TREC. We participated in the Biomedical Generative Retrieval track, the Retrieval-Augmented Generation track, and the Tip-of-the-Tongue track. For the biomedical track, we applied different paradigms of retrieval-augmented generation with open- and closed-source LLMs. For the Retrieval-Augmented Generation track, we aimed to contrast manual response submissions with fully-automated responses. For the Tip-of-the-Tongue track, we employed query relaxation as in our last year's submission (i.e., leaving out terms that likely reduce the retrieval effectiveness) that we combine with a new cross-encoder that we trained on an enriched version of the TOMT-KIS dataset.
	

??? quote "Bibtex"
	```
	@inproceedings{webis-trec2024-papers-proc-1,
		author = {Maik Fröbe (Friedrich-Schiller-Universität), Lukas Gienapp (Leipzig University & ScaDS.AI), Harrisen Scells (Universität Kassel), Eric Oliver Schmidt (Martin-Luther-Universität Halle), Matti Wiegmann (Bauhaus-Universität Weimar), Martin Potthast, Universität Kassel (Universität Kassel & hessian.AI & ScaDS.AI), Matthias Hagen (Friedrich-Schiller-Universität Jena)},
		title = {Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {webis},
		trec_runs = {webis-01, webis-02, webis-03, webis-04, webis-05, webis-ag-run0-taskrag, webis-ag-run1-taskrag, webis-manual, webis-rag-run0-taskrag, webis-rag-run1-taskrag, webis-rag-run3-taskrag, webis-ag-run3-reuserag, webis-rag-run4-reuserag, webis-rag-run5-reuserag, webis-ag-run2-reuserag, webis-1, webis-2, webis-3, webis-gpt-1, webis-gpt-4, webis-gpt-6, webis-5, webis-base, webis-tot-01, webis-tot-02, webis-tot-04, webis-tot-03},
		trec_tracks = {biogen.rag.tot},
		url = {https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf}
	}
	```

