# Proceedings - Biomedical Generative Retrieval (BioGen) Track 2024

#### Overview of TREC 2024 Biomedical Generative Retrieval (BioGen) Track

_Deepak Gupta,  Dina Demner-Fushman,  William Hersh,  Steven Bedrick,  Kirk Roberts_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_biogen.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_biogen.pdf)
??? abstract "Abstract"
	
	With the advancement of large language models (LLMs), the biomedical domain has seen significant progress and improvement in multiple tasks such as biomedical question answering, lay language summarization of the biomedical literature, clinical note summarization, etc. However, hallucinations or confabulations remain one of the key challenges when using LLMs in the biomedical and other domains.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-1,
		title = {Overview of TREC 2024 Biomedical Generative Retrieval (BioGen) Track},
		author = {Deepak Gupta and Dina Demner-Fushman and William Hersh and Steven Bedrick and Kirk Roberts},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks

_Lukas Gienapp,  Maik Fröbe,  Jan Heinrich Merker,  Harrisen Scells,  Eric Oliver Schmidt,  Matti Wiegmann,  Martin Potthast,  Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf](https://trec.nist.gov/pubs/trec33/papers/webis.biogen.rag.tot.pdf)
- :material-file-search: **Runs:** [webis-1](./runs.md#webis-1) | [webis-2](./runs.md#webis-2) | [webis-3](./runs.md#webis-3) | [webis-gpt-1](./runs.md#webis-gpt-1) | [webis-gpt-4](./runs.md#webis-gpt-4) | [webis-gpt-6](./runs.md#webis-gpt-6) | [webis-5](./runs.md#webis-5)

??? abstract "Abstract"
	
	In this paper, we describe the Webis Group’s participation in the 2024 edition of TREC. We participated in the Biomedical Generative Retrieval track, the Retrieval-Augmented Generation track, and the Tip-of-the-Tongue track. For the biomedical track, we applied different paradigms of retrieval-augmented generation with open- and closed-source LLMs. For the Retrieval-Augmented Generation track, we aimed to contrast manual response submissions with fully-automated responses. For the Tip-of-the-Tongue track, we employed query relaxation as in our last year’s submission (i.e., leaving out terms that likely reduce the retrieval effectiveness) that we combine with a new cross-encoder that we trained on an enriched version of the TOMT-KIS dataset.
	

??? quote "Bibtex"
	```
	@inproceedings{webis-trec2024-papers-proc-1,
		title = {Webis at TREC 2024: Biomedical Generative Retrieval, Retrieval-Augmented Generation, and Tip-of-the-Tongue Tracks},
		author = {Lukas Gienapp and Maik Fröbe and Jan Heinrich Merker and Harrisen Scells and Eric Oliver Schmidt and Matti Wiegmann and Martin Potthast and Matthias Hagen},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Exploring the Few-Shot Performance of Low-Cost Proprietary Models in the 2024 TREC BioGen Track

_Samy Ateia,  Udo Kruschwitz_

- :fontawesome-solid-user-group: **Participant:** [ur-iw](./participants.md#ur-iw)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/ur-iw.biogen.pdf](https://trec.nist.gov/pubs/trec33/papers/ur-iw.biogen.pdf)
- :material-file-search: **Runs:** [zero-shot-gpt4o-mini](./runs.md#zero-shot-gpt4o-mini) | [zero-shot-gemini-flash](./runs.md#zero-shot-gemini-flash) | [ten-shot-gpt4o-mini](./runs.md#ten-shot-gpt4o-mini) | [ten-shot-gemini-flash](./runs.md#ten-shot-gemini-flash) | [ten-shot-gpt4o-mini-wiki](./runs.md#ten-shot-gpt4o-mini-wiki) | [ten-shot-gemini-flash-wiki](./runs.md#ten-shot-gemini-flash-wiki)

??? abstract "Abstract"
	
	For the 2024 TREC Biomedical Generative Retrieval (BioGen) Track, we evaluated proprietary low-cost large language models (LLMs) in few-shot and zero-shot settings for biomedical question answering. Building upon our prior competitive approach from the CLEF 2024 BioASQ challenge, we adapted our methods to the BioGen task. We reused few-shot examples from BioASQ and generated additional ones from the test set for the BioGen specific answer format, by using an LLM judge to select examples. Our approach involved query expansion, BM25-based retrieval using Elasticsearch, snippet extraction, reranking, and answer generation both with and without 10-shot learning and additional relevant context from Wikipedia. The results are in line with our findings at BioASQ, indicating that additional Wikipedia context did not improve the results, while 10-shot learning did. An interactive reference implementation that showcases Google’s Gemini-1.5-flash performance with 3-shot learning is available online and the source code of this demo is available on GitHub.
	

??? quote "Bibtex"
	```
	@inproceedings{ur-iw-trec2024-papers-proc-1,
		title = {Exploring the Few-Shot Performance of Low-Cost Proprietary Models in the 2024 TREC BioGen Track},
		author = {Samy Ateia and Udo Kruschwitz},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

