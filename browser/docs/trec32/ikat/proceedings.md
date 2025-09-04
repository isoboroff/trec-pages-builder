# Proceedings - Interactive Knowledge Assistance 2023

#### TREC iKAT 2023: The Interactive Knowledge Assistance Track Overview

_Mohammad Aliannejadi,  Zahra Abbasiantaeb,  Shubham Chatterjee,  Jeffery Dalton,  Leif Azzopardi_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/Overview_ikat.pdf](https://trec.nist.gov/pubs/trec32/papers/Overview_ikat.pdf)
??? abstract "Abstract"
	
	Conversational Information Seeking has evolved rapidly in thelast few years with the development of Large Language Modelsproviding the basis for interpreting and responding in a natural-istic manner to user requests. iKAT emphasizes the creation andresearch of conversational search agents that adapt responses basedon the user’s prior interactions and present context. This meansthat the same question might yield varied answers, contingent onthe user’s profile and preferences. The challenge lies in enablingConversational Search Agents (CSA) to incorporate personalizedcontext to effectively guide users through the relevant informationto them. iKAT’s first year attracted seven teams and a total of 24runs. Most of the runs leveraged Large Language Models (LLMs)in their pipelines, with a few focusing on a generate-then-retrieveapproach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiACDA23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [IRLab-Amsterdam](./participants.md#irlab-amsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IRLab-Amsterdam.K.pdf](https://trec.nist.gov/pubs/trec32/papers/IRLab-Amsterdam.K.pdf)
- :material-file-search: **Runs:** [run-4-GPT-4](./runs.md#run-4-gpt-4) | [run-2-llama-fine-tuned](./runs.md#run-2-llama-fine-tuned) | [run-1-llama-zero-shot](./runs.md#run-1-llama-zero-shot) | [run-3-llama-fine-tuned-manual](./runs.md#run-3-llama-fine-tuned-manual)

??? abstract "Abstract"
	
	The interactive Knowledge Assistant Track (iKAT) aims to developpersonalized conversational assistants. In this task, the persona ofthe user is provided to the system before the conversation. iKATconsists of three main tasks including, Personal Textual KnowledgeBase (PTKB) statement ranking, passage ranking, and responsegeneration. We proposed two different pipelines to approach thetask, namely, retrieve-then-generate and generate-then-retrieve. Wesubmitted three runs based on the retrieve-then-generate pipelineusing the Llama model and one run based on the generate-then-retrieve pipeline. The automatic run based on generate-then-retrievepipeline outperformed the other automatic runs in the passageranking task. This run achieved comparable results to the manualrun based on the retrieve-then-generate pipeline. For the PTKB state-ment ranking task, we proposed two approaches including rankingPTKB statements using (MiniLM12) model and using the GPT-4model as a zero-shot learner for classifying the PTKB statements asrelevant or non-relevant. The ranking approach using (MiniLM12)model achieved better performance than the classification modelapproach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbasiantaebMRKRA23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [IITD](./participants.md#iitd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/IITD.K.pdf](https://trec.nist.gov/pubs/trec32/papers/IITD.K.pdf)
- :material-file-search: **Runs:** [run_automatic_dense_mini_LM_reranker](./runs.md#run_automatic_dense_mini_lm_reranker) | [run_automatic_llm_damo](./runs.md#run_automatic_llm_damo) | [run_automatic_dense_monot5](./runs.md#run_automatic_dense_monot5) | [run_automatic_dense_damo_canard_16000_recall](./runs.md#run_automatic_dense_damo_canard_16000_recall)

??? abstract "Abstract"
	
	Conventional information retrieval procedurestypically entail multiple stages, encompassinginformation retrieval and subsequent responsegeneration. The quality of the response derivedfrom the retrieved content significantly influ-ences the overall efficacy of the retrieval pro-cess. With the advent of large language models,it is possible to utilize larger contexts to gener-ate more cogent summaries for users. To ensurethe production of contextually grounded andpertinent responses, particularly in conversa-tional models, a good retrieval mechanism actsas a keystone. This study aims to develop a con-versational engine adept at extracting relevantdocuments and generating pertinent responsesby summarizing key passages, leveraging vari-ous types of language models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoudharyCS23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [uot-yj](./participants.md#uot-yj)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.K.pdf](https://trec.nist.gov/pubs/trec32/papers/uot-yahoo.K.pdf)
- :material-file-search: **Runs:** [uot-yj_run](./runs.md#uot-yj_run) | [uot-yj_run_llmnoptkb](./runs.md#uot-yj_run_llmnoptkb) | [uot-yj_run_rankgpt35](./runs.md#uot-yj_run_rankgpt35) | [uot-yj_run_monot5](./runs.md#uot-yj_run_monot5)

??? abstract "Abstract"
	
	In this paper, we present our approach employed in the four automatic submission runs for the TREC 2023 Interactive Knowledge Assistance Track. This track comprises three subtasks: passage ranking, response genera- tion, and Personal Text Knowledge Base (PTKB) statement ranking. Our comprehensive multi-stage pipeline for this task encompasses query rewriting, PTKB statement ranking, passage retrieval and re-ranking, and response generation. In particular, we employed fine-tuned pre-trained T5-CANARD for query rewriting, a combination of BERT, RankGPT, and MonoT5 for PTKB statement ranking, and Large Language Models (LLMs), RankGPT, and MonoT5 separately for passage re-ranking in four submission runs. For response generation, we adopted "mrm8488/t5-base-finetuned-summarize-news" from HuggingFace, which is a Text-to-Text Transfer Transformer (T5) based model that specially fine-tuned for summarization tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengYYFJ23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [InfoSense](./participants.md#infosense)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/InfoSense.K.pdf](https://trec.nist.gov/pubs/trec32/papers/InfoSense.K.pdf)
- :material-file-search: **Runs:** [georgetown_infosense_ikat_run_1](./runs.md#georgetown_infosense_ikat_run_1) | [georgetown_infosense_ikat_run_2](./runs.md#georgetown_infosense_ikat_run_2) | [georgetown_infosense_ikat_run_3](./runs.md#georgetown_infosense_ikat_run_3)

??? abstract "Abstract"
	
	The Text Retrieval Conference (TREC)’s Interactive KnowledgeAssistance (iKAT) Track has the goal of combining conversationaland personalizable elements with existing information retrieval(IR) technologies to facilitate information-seeking. To accomplishthis, an iKAT system is given two pieces of information from theuser: 1) a Personal Textual Knowledge Base (PTKB), which is apersistent set of a handful of factual statements about the user (like"I am lactose intolerant" or "I am afraid of roller coasters") thatlasts throughout a conversation, and 2) the user utterance, whichis usually written from an information-seeking standpoint. In anautomatic run, the system must find both the PTKBs relevant toeach utterance and provide relevant responses to both the currentutterance and the conversation history. Answers must be generatedbased on passages retrieved from the ClueWeb 22B Corpus.This paper contains what the Georgetown InfoSense group hasdone in regard to solving the challenges presented by TREC iKAT2023. Our submitted runs outperform the median runs by a sig-nificant margin, exhibiting superior performance in nDCG acrossvarious cut numbers and in overall success rate. Our approach uses aGenerate-Retrieve-Generate method, which we’ve found to greatlyoutpace Retrieve-Then-Generate approaches for the purposes ofiKAT. Our solution involves the use of Large Language Models(LLMs) for initial answers, answer grounding by BM25, passagequality filtering by logistic regression, and answer generation byLLMs again. We leverage several purpose-built Language Models,including BERT, Chat-based, and text-to-transfer-based models, fortext understanding, classification, generation, and summarization.The official results of the TREC evaluation contradict our initialself-evaluation, which may suggest that a decrease in the relianceon our retrieval and classification methods is better. Nonetheless,our findings suggest that the sequence of involving these differentcomponents matters, where we see an essentiality of using LLMsbefore using search engines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PatwardhanY23.bib) "
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

- :fontawesome-solid-user-group: **Participant:** [RALI](./participants.md#rali)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec32/papers/RALI.K.pdf](https://trec.nist.gov/pubs/trec32/papers/RALI.K.pdf)
- :material-file-search: **Runs:** [ConvGQR](./runs.md#convgqr) | [LLMConvGQR](./runs.md#llmconvgqr)

??? abstract "Abstract"
	
	The Recherche Appliquée en Linguistique Informatique (RALI)team has participated in the 2023 TREC Interactive KnowledgeAssistance Track (iKAT). This paper introduces our approaches andreports our results on the passage ranking task. The most challeng-ing in conversational information seeking is to reveal the user’sreal search intent. To tackle these challenges, we employ a com-bination of query rewriting and query expansion techniques torephrase conversational queries using generative language modelsin both supervised and zero-shot manner. Furthermore, to establisha connection between query reformulation and the retrieval pro-cess, we implement a knowledge infusion mechanism to enhanceboth procedures during training. The outcome of our efforts yieldsimpressive results, with an nDCG@5 score of 16.24% and an MRRof 32.75% in our best-performing experiments. Besides, we alsoexplore the impact of personal information on the search resultsbased on GPT-4, showing that not all query turns are associatedwith personalized information needs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoYN23.bib) "
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

