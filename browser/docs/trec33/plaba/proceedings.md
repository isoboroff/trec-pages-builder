# Proceedings - Plain-Language Adaptation of Biomedical Abstracts 2024

#### SIB Text-Mining at TREC PLABA 2024

_Luc Mottin,  AnaÃs Mottaz,  Julien Knafou,  Alexandre Flament,  Julien Gobeill,  Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [SIB](./participants.md#sib)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/SIB.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/SIB.plaba.pdf)
- :material-file-search: **Runs:** [TREC2024_SIB_run1](./runs.md#trec2024_sib_run1) | [TREC2024_SIB_run3](./runs.md#trec2024_sib_run3) | [TREC2024_SIB_run4](./runs.md#trec2024_sib_run4)

??? abstract "Abstract"
	
	The comprehension of health information by patients has a real influence on the efficacy of their treatment. However, while more health resources are increasingly available to the public, the use of medical jargon and complex syntax makes them difficult to understand. Recent advances in machine translation and text simplification may help to make these resources more accessible by adapting biomedical text into plain language. In this context, the TREC 2024 Plain Language Adaptation of Biomedical Abstracts track sought to develop specialized algorithms able to adapt biomedical abstracts into plain language for the general public. The SIB Text Mining group participated in the “Complete Abstract Adaptation” subtask. Our first approach examines how a specific prompting using a state-of-the-art Large Language Model performs in the global adaptation of biomedical documents, with the intention of proposing a baseline with no technical improvements to compare more advanced strategies. The second approach investigates how the fine tuning of the transformer handles the task, and the third approach integrates a Retrieval Augmented Generation function to help generate a new document based on information from relevant sources.
	

??? quote "Bibtex"
	```
	@inproceedings{SIB-trec2024-papers-proc-7,
		title = {SIB Text-Mining at TREC PLABA 2024},
		author = {Luc Mottin and AnaÃs Mottaz and Julien Knafou and Alexandre Flament and Julien Gobeill and Patrick Ruch},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Biomedical Text Simplification Models Trained on Aligned Abstracts and Lay Summaries

_Jan Bakker,  Taiki Papandreou-Lazos,  Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/UAmsterdam.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/UAmsterdam.plaba.pdf)
- :material-file-search: **Runs:** [UAms-ConBART-Cochrane](./runs.md#uams-conbart-cochrane) | [UAms-BART-Cochrane](./runs.md#uams-bart-cochrane)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam’s participation in the TREC 2024 Plain Language Adaptation of Biomedical Abstracts (PLABA) Track. We investigated the effectiveness of text simplification models trained on aligned pairs of sentences in biomedical abstracts and plain language summaries. We participated in Task 2 on Complete Abstract Adaptation and conducted post-submission experiments in Task 1 on Term Replacement.
	

??? quote "Bibtex"
	```
	@inproceedings{UAmsterdam-trec2024-papers-proc-2,
		title = {Biomedical Text Simplification Models Trained on Aligned Abstracts and Lay Summaries},
		author = {Jan Bakker and Taiki Papandreou-Lazos and Jaap Kamps},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### MALEI at the PLABA Track of TREC 2024: RoBERTa for Term Replacement – LLaMA3.1 and GPT-4o for Complete Abstract Adaptation

_Zhidong Ling,  Zihao Li,  Pablo Romero,  Lifeng Han,  Goran Nenadic_

- :fontawesome-solid-user-group: **Participant:** [UM](./participants.md#um)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/UM.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/UM.plaba.pdf)
- :material-file-search: **Runs:** [Roberta-base](./runs.md#roberta-base) | [GPT](./runs.md#gpt) | [LLaMa 3.1 70B instruction (2nd run)](./runs.md#llama-31-70b-instruction-2nd-run)

??? abstract "Abstract"
	
	Health literacy, or the ability of individuals to comprehend and apply health information for informed decision-making, is one of the central focuses of the Healthy People 2030 framework in the US. Even though biomedical information is highly accessible online, patients and caregivers often struggle with language barriers, even when the content is presented in their native language. The shared task PLABA aims to harness advances in deep learning to empower the automatic simplification of complex scientific texts into language that is more understandable for patients and caregivers. Despite substantial obstacles to effective implementation, the goal of the PLABA track is to improve health literacy by translating biomedical abstracts into plain language, making them more accessible and understandable to the general public 1. Following our participation on the PLABA-2023 shared task using large language models (LLMs) such as ChatGPT, BioGPT, and Flan-T5, and Control Mechanisms (Li et al., 2024), in this work, we introduce our system participation to the PLABA-2024. Instead of end-to-end biomedical abstract simplification as in PLABA-2023, in this year, PLABA-2024 introduced more granular-steps, including Term Replacement for Task-1 and Complete Abstract Adaption for Task-2, which we will describe in detail for our methodologies via fine-tuning RoBERTa-Base model for Task-1 and prompting LLMs (LLaMa-3.1-70B and GPT4o) for Task-2.
	

??? quote "Bibtex"
	```
	@inproceedings{UM-trec2024-papers-proc-3,
		title = {MALEI at the PLABA Track of TREC 2024: RoBERTa for Term Replacement – LLaMA3.1 and GPT-4o for Complete Abstract Adaptation},
		author = {Zhidong Ling and Zihao Li and Pablo Romero and Lifeng Han and Goran Nenadic},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### UM_FHS at TREC 2024 PLABA: Exploration of Fine-tuning and AI agent approach for plain language adaptations of biomedical text

_Primoz Kocbek,  Leon Kopitar,  Zhihong Zhang,  Emirhan Aydın,  Maxim Topaz,  Gregor Stiglic_

- :fontawesome-solid-user-group: **Participant:** [um_fhs](./participants.md#um_fhs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/um_fhs.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/um_fhs.plaba.pdf)
- :material-file-search: **Runs:** [plaba_um_fhs_sub1](./runs.md#plaba_um_fhs_sub1) | [plaba_um_fhs_sub2](./runs.md#plaba_um_fhs_sub2) | [plaba_um_fhs_sub3](./runs.md#plaba_um_fhs_sub3)

??? abstract "Abstract"
	
	This paper describes our submissions to the TREC 2024 PLABA track with the aim to simplify biomedical abstracts for a K8-level audience (13–14 years old students). We tested three approaches using OpenAI’s gpt-4o and gpt-4o-mini models: baseline prompt engineering, a two-AI agent approach, and fine-tuning. Adaptations were evaluated using qualitative metrics (5-point Likert scales for simplicity, accuracy, completeness, and brevity) and quantitative readability scores (Flesch-Kincaid grade level, SMOG Index). Results indicated that the two-agent approach and baseline prompt engineering with gpt-4o-mini models showed superior qualitative performance, while fine-tuned models excelled in accuracy and completeness but were less simple.
	

??? quote "Bibtex"
	```
	@inproceedings{um_fhs-trec2024-papers-proc-1,
		title = {UM\_FHS at TREC 2024 PLABA: Exploration of Fine-tuning and AI agent approach for plain language adaptations of biomedical text},
		author = {Primoz Kocbek and Leon Kopitar and Zhihong Zhang and Emirhan Aydın and Maxim Topaz and Gregor Stiglic},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### MALEI at the PLABA Track of TAC-2024: RoBERTa for Task 1 – LLaMA3.1 and GPT-4o for Task 2

_Zhidong Ling,  Zihao Li,  Pablo Romero,  Lifeng Han,  Goran Nenadic_

- :fontawesome-solid-user-group: **Participant:** [UM](./participants.md#um)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/UM.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/UM.plaba.pdf)
- :material-file-search: **Runs:** [Roberta-base](./runs.md#roberta-base) | [GPT](./runs.md#gpt) | [LLaMa 3.1 70B instruction (2nd run)](./runs.md#llama-31-70b-instruction-2nd-run)

??? abstract "Abstract"
	
	Health literacy, or the ability of individuals to comprehend and apply health information for informed decision-making, is one of the central focuses of the Healthy People 2030 framework in the US. Even though biomedical information is highly accessible online, patients and caregivers often struggle with language barriers, even when the content is presented in their native language. The shared task PLABA aims to harness advances in deep learning to empower the automatic simplification of complex scientific texts into language that is more understandable for patients and caregivers. Despite substantial obstacles to effective implementation, the goal of the PLABA track is to improve health literacy by translating biomedical abstracts into plain language, making them more accessible and understandable to the general public 1. Following our participation on the PLABA-2023 shared task using large language models (LLMs) such as ChatGPT, BioGPT, and Flan-T5, and Control Mechanisms (Li et al., 2024), in this work, we introduce our system participation to the PLABA-2024. Instead of end-to-end biomedical abstract simplification as in PLABA-2023, in this year, PLABA-2024 introduced more granular-steps, including Term Replacement for Task-1 and Complete Abstract Adaption for Task-2, which we will describe in detail for our methodologies via fine-tuning RoBERTa-Base model for Task-1 and prompting LLMs (LLaMa-3.1-70B and GPT4o) for Task-2.
	

??? quote "Bibtex"
	```
	@inproceedings{UM-trec2024-papers-proc-2,
		title = {MALEI at the PLABA Track of TAC-2024: RoBERTa for Task 1 – LLaMA3.1 and GPT-4o for Task 2},
		author = {Zhidong Ling and Zihao Li and Pablo Romero and Lifeng Han and Goran Nenadic},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation

_Ting-Wei Chang,  Hen-Hsen Huang,  Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu_nlp](./participants.md#ntu_nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/ntu_nlp.plaba.pdf](https://trec.nist.gov/pubs/trec33/papers/ntu_nlp.plaba.pdf)
- :material-file-search: **Runs:** [gemini-1.5-pro_demon5_replace-demon5](./runs.md#gemini-15-pro_demon5_replace-demon5) | [gemini-1.5-flash_demon5_replace-demon5](./runs.md#gemini-15-flash_demon5_replace-demon5) | [gpt-4o-mini _demon5_replace-demon5](./runs.md#gpt-4o-mini-_demon5_replace-demon5) | [task2_moa_tier3_post](./runs.md#task2_moa_tier3_post) | [task2_moa_tier1_post](./runs.md#task2_moa_tier1_post) | [task2_moa_tier2_post](./runs.md#task2_moa_tier2_post)

??? abstract "Abstract"
	
	This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients’ reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In this work, we leverage the capabilities of LLMs such as GPT-4o-mini, Gemini-1.5-pro, and LLaMA for text simplification. Additionally, we incorporate Mixture-of-Agents (MoA) techniques to enhance adaptability and robustness in PLA tasks. Key contributions include a comparative analysis of prompting strategies, finetuning with QLoRA on different LLMs, and the integration of MoA technique. Our findings demonstrate the effectiveness of LLM-driven PLA, showcasing its potential in making healthcare information more comprehensible while preserving essential content.
	

??? quote "Bibtex"
	```
	@inproceedings{ntu_nlp-trec2024-papers-proc-1,
		title = {Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation},
		author = {Ting-Wei Chang and Hen-Hsen Huang and Hsin-Hsi Chen},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

