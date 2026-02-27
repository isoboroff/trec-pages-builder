# Proceedings - Interactive Knowledge Assistance 2024

#### TREC iKAT 2024: The Interactive Knowledge Assistance Track Overview

_Mohammad Aliannejadi,  Zahra Abbasiantaeb,  Simon Lupart,  Shubham Chatterjee,  Jeffrey Dalton,  Leif Azzopardi_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/Overview_ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/Overview_ikat.pdf)
??? abstract "Abstract"
	
	Conversational information seeking has evolved rapidly in the last few years with the development of large language models (LLMs) providing the basis for interpreting and responding in a naturalistic manner to user requests. iKAT emphasizes the creation and research of conversational search agents that adapt responses based on the user’s prior interactions and present context, maintaining a long-term memory of user-system interactions. This means that the same question might yield varied answers, contingent on the user’s profile and preferences. The challenge lies in enabling conversational search agents (CSA) to incorporate personalized context to guide users through the relevant information effectively. iKAT’s second year attracted seven teams and a total of 31 runs. Most of the runs leveraged LLMs in their pipelines with some LLMs to do a single query rewrite, while others leveraged LLMs to do multiple query rewrites.
	

??? quote "Bibtex"
	```
	@inproceedings{coordinators-trec2024-papers-proc-4,
		title = {TREC iKAT 2024: The Interactive Knowledge Assistance Track Overview},
		author = {Mohammad Aliannejadi and Zahra Abbasiantaeb and Simon Lupart and Shubham Chatterjee and Jeffrey Dalton and Leif Azzopardi},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### IRLab@iKAT24: Learned Sparse Retrieval with Multi-aspect LLM Query Generation for Conversational Search

_Simon Lupart,  Zahra Abbasiantaeb,  Mohammad Aliannejadi_

- :fontawesome-solid-user-group: **Participant:** [uva](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/uva.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/uva.ikat.pdf)
- :material-file-search: **Runs:** [manual-splade-fusion](./runs.md#manual-splade-fusion) | [manual-splade-debertav3](./runs.md#manual-splade-debertav3) | [gpt4-MQ-debertav3](./runs.md#gpt4-mq-debertav3) | [gpt4-mq-rr-fusion](./runs.md#gpt4-mq-rr-fusion) | [gpt-single-QR-rr-debertav3](./runs.md#gpt-single-qr-rr-debertav3) | [qd1](./runs.md#qd1)

??? abstract "Abstract"
	
	The Interactive Knowledge Assistant Track (iKAT) 2024 focuses on advancing conversational assistants, able to adapt their interaction and responses from personalized user knowledge. The track incorporates a Personal Textual Knowledge Base (PTKB) alongside Conversational AI tasks, such as passage ranking and response generation. Query Rewrite being an effective approach for resolving conversational context, we explore Large Language Models (LLMs), as query rewriters. Specifically, our submitted runs explore multi-aspect query generation using the MQ4CS framework, which we further enhance with Learned Sparse Retrieval via the SPLADE architecture, coupled with robust cross-encoder models. We also propose an alternative to the previous interleaving strategy, aggregating multiple aspects during the reranking phase. Our findings indicate that multi-aspect query generation is effective in enhancing performance when integrated with advanced retrieval and reranking models. Our results also lead the way for better personalization in Conversational Search, relying on LLMs to integrate personalization within query rewrite, and outperforming human rewrite performance.
	

??? quote "Bibtex"
	```
	@inproceedings{uva-trec2024-papers-proc-1,
		title = {IRLab@iKAT24: Learned Sparse Retrieval with Multi-aspect LLM Query Generation for Conversational Search},
		author = {Simon Lupart and Zahra Abbasiantaeb and Mohammad Aliannejadi},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### DCU-ADAPT@TREC iKAT 2024: Incorporating Retrieved Knowledge for Enhanced Conversational Search

_Praveen Acharya,  Xiao Fu,  Noriko Kando,  Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [DCU-ADAPT](./participants.md#dcu-adapt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/DCU-ADAPT.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/DCU-ADAPT.ikat.pdf)
- :material-file-search: **Runs:** [dcu_manual_qe_summ_TopP_3](./runs.md#dcu_manual_qe_summ_topp_3) | [dcu_manual_qe_summ_ptkb_TopP_3](./runs.md#dcu_manual_qe_summ_ptkb_topp_3) | [dcu_auto_qe_key_topP-50_topK-5](./runs.md#dcu_auto_qe_key_topp-50_topk-5) | [dcu_auto_qre_sim](./runs.md#dcu_auto_qre_sim) | [dcu_auto_qe_summ_TopP_3](./runs.md#dcu_auto_qe_summ_topp_3) | [dcu_auto_qe_summ_ptkb_TopP_](./runs.md#dcu_auto_qe_summ_ptkb_topp_)

??? abstract "Abstract"
	
	Users of search applications often encounter difficulties in expressing their information needs effectively. Conversational search (CS) can potentially support users in creating effective queries by enabling a multi-turn, iterative dialogue between a User and the search Systems. These dialogues help users to refine and build their understanding of their information need through a series of query-response exchanges. However, current CS systems generally do not accumulate knowledge about the user’s information needs or the content with which they have engaged during this dialogue. This limitation can hinder the system’s ability to support users effectively. To address this issue, we propose an approach that seeks to model and utilize knowledge gained from each interaction to enhance future user queries. Our method focuses on incorporating knowledge from retrieved documents to enrich subsequent user queries, ultimately improving query comprehension and retrieval outcomes. We test the effectiveness of our proposed approach in our TREC iKAT 2024 participation.
	

??? quote "Bibtex"
	```
	@inproceedings{DCU-ADAPT-trec2024-papers-proc-1,
		title = {DCU-ADAPT@TREC iKAT 2024: Incorporating Retrieved Knowledge for Enhanced Conversational Search},
		author = {Praveen Acharya and Xiao Fu and Noriko Kando and Gareth J. F. Jones},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### IIUoT at TREC 2024 Interactive Knowledge Assistance Track

_YATING ZHANG,  HAITAO YU_

- :fontawesome-solid-user-group: **Participant:** [ii_research](./participants.md#ii_research)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/ii_research.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/ii_research.ikat.pdf)
- :material-file-search: **Runs:** [iiresearch_ikat2024_rag_top5_bge_reranker](./runs.md#iiresearch_ikat2024_rag_top5_bge_reranker) | [iiresearch_ikat2024_rag_top5_monot5_reranker](./runs.md#iiresearch_ikat2024_rag_top5_monot5_reranker)

??? abstract "Abstract"
	
	In conversational information-seeking (CIS), the ability to tailor responses to individual user contexts is essential for enhancing relevance and accuracy. The TREC Interactive Knowledge Assistance Track addresses this need by advancing research in personalized conversational agents that adapt dynamically to user-specific details and preferences. Our study aligns with this framework, which involves three core tasks: personal textual knowledge base (PTKB) statement ranking, passage ranking, and response generation. To address these tasks, we propose a comprehensive framework that incorporates user context at each stage. For PTKB statement ranking, we integrate embedding models with large language models (LLMs) to optimize relevance-based ranking precision, allowing for more nuanced alignment of user characteristics with retrieved information. In the passage ranking stage, our adaptive retrieval strategy combines BM25 with iterative contextual refinement, enhancing the relevance and accuracy of retrieved passages. Finally, our response generation module leverages a Retrieval-Augmented Generation (RAG) model that dynamically synthesizes user-specific context and external knowledge, producing responses that are both precise and contextually relevant. Experimental results demonstrate that our framework effectively addresses the complexities of personalized CIS, achieving notable improvements over traditional static retrieval methods.
	

??? quote "Bibtex"
	```
	@inproceedings{ii_research-trec2024-papers-proc-1,
		title = {IIUoT at TREC 2024 Interactive Knowledge Assistance Track},
		author = {YATING ZHANG and HAITAO YU},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### RALI@TREC iKAT 2024: Achieving Personalization via Retrieval Fusion in Conversational Search

_Yuchen Hui,  Fengran Mo,  Milan Mao,  Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [rali lab](./participants.md#rali-lab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/rali lab.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/rali lab.ikat.pdf)
- :material-file-search: **Runs:** [RALI_manual_monot5](./runs.md#rali_manual_monot5) | [RALI_manual_rankllama](./runs.md#rali_manual_rankllama) | [RALI_gpt4o_fusion_rerank](./runs.md#rali_gpt4o_fusion_rerank) | [RALI_gpt4o_no_personalize_fusion_rerank](./runs.md#rali_gpt4o_no_personalize_fusion_rerank) | [RALI_gpt4o_no_personalize_fusion_norerank](./runs.md#rali_gpt4o_no_personalize_fusion_norerank) | [RALI_gpt4o_fusion_norerank](./runs.md#rali_gpt4o_fusion_norerank)

??? abstract "Abstract"
	
	The Recherche Appliquée en Linguistique Informatique (RALI) team participated in the 2024 TREC Interactive Knowledge Assistance (iKAT) Track. In personalized conversational search, effectively capturing a user’s complex search intent requires incorporating both contextual information and key elements from the user profile into query reformulation. The user profile often contains many relevant pieces, and each could potentially complement the user’s information needs. It is difficult to disregard any of them, whereas introducing an excessive number of these pieces risks drifting from the original query and hinders search performance. This is a challenge we denote as over-personalization. In this paper, we tackle the problem via employing different strategies based on fusing ranking lists generated from the queries with different levels of personalization.
	

??? quote "Bibtex"
	```
	@inproceedings{rali lab-trec2024-papers-proc-1,
		title = {RALI@TREC iKAT 2024: Achieving Personalization via Retrieval Fusion in Conversational Search},
		author = {Yuchen Hui and Fengran Mo and Milan Mao and Jian-Yun Nie},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### NII@TREC IKAT 2024:LLM-Based Pipelines for Personalized Conversational Information Seeking

_Noriko Kando,  Praveen Acharya,  Navdeep Singh Bedi,  Xiao Fu_

- :fontawesome-solid-user-group: **Participant:** [nii](./participants.md#nii)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/nii.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/nii.ikat.pdf)
- :material-file-search: **Runs:** [nii_res_gen](./runs.md#nii_res_gen) | [nii_auto_base](./runs.md#nii_auto_base) | [nii_manu_base](./runs.md#nii_manu_base) | [nii_auto_ptkb_rr](./runs.md#nii_auto_ptkb_rr) | [nii_manu_ptkb_rr](./runs.md#nii_manu_ptkb_rr) | [NII_automatic_GeRe](./runs.md#nii_automatic_gere)

??? abstract "Abstract"
	
	In this paper, we propose two novel pipelines—Retrieve-then-Generate (RtG) and Generate-then-Retrieve (GtR)—to enhance conversational information seeking (CIS) systems, evaluated within the TREC iKAT 2023 framework. The RtG pipeline emphasizes brevity in rewriting user utterances and generates multiple query groups to maximize the retrieval of relevant documents. This approach leads to improved recall in the final results compared to the best submission in 2023. Additionally, it incorporates a chain-of-thought methodology through a two-stage response generation process. In a zero-shot setting, the GtR pipeline introduces a hybrid approach by ensembling state-of-the-art Large Language Models (LLMs), specifically GPT-4o and Claude-3-opus. By leveraging the strengths of multiple LLMs, the GtR pipeline achieves high recall while maintaining competitive precision and ranking performance in both document retrieval and Personal Task Knowledge Base (PTKB) statement classification tasks. Our experimental results demonstrate that both pipelines significantly enhance retrieval effectiveness, offering robust solutions for future CIS systems.
	

??? quote "Bibtex"
	```
	@inproceedings{nii-trec2024-papers-proc-1,
		title = {NII@TREC IKAT 2024:LLM-Based Pipelines for Personalized Conversational Information Seeking},
		author = {Noriko Kando and Praveen Acharya and Navdeep Singh Bedi and Xiao Fu},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

#### Passage Query Methods for Retrieval and Reranking in Conversational Agents

_Victor De Lima,  Grace Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [infosenselab](./participants.md#infosenselab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/infosenselab.ikat.pdf](https://trec.nist.gov/pubs/trec33/papers/infosenselab.ikat.pdf)
- :material-file-search: **Runs:** [infosense_llama_pssgqrs_wghtdrerank_2](./runs.md#infosense_llama_pssgqrs_wghtdrerank_2) | [infosense_llama_pssgqrs_wghtdrerank_1](./runs.md#infosense_llama_pssgqrs_wghtdrerank_1) | [infosense_llama_short_long_qrs_2](./runs.md#infosense_llama_short_long_qrs_2) | [infosense_llama_short_long_qrs_3](./runs.md#infosense_llama_short_long_qrs_3)

??? abstract "Abstract"
	
	This paper presents our approach to the TREC Interactive Knowledge Assistance Track (iKAT), which focuses on improving conversational information-seeking (CIS) systems. While recent advancements in CIS have improved conversational agents' ability to assist users, significant challenges remain in understanding context and retrieving relevant documents across domains and dialogue turns. To address these issues, we extend the Generate-Retrieve-Generate pipeline by developing passage queries (PQs) that align with the target document's expected format to improve query-document matching during retrieval. We propose two variations of this approach: Weighted Reranking and Short and Long Passages. Each method leverages a Meta Llama model for context understanding and generating queries and responses. Passage ranking evaluation results show that the Short and Long Passages approach outperformed the organizers' baselines, performed best among Llama-based systems in the track, and achieved results comparable to GPT-4-based systems. These results indicate that the method effectively balances efficiency and performance. Findings suggest that PQs improve semantic alignment with target documents and demonstrate their potential to improve multi-turn dialogue systems.
	

??? quote "Bibtex"
	```
	@inproceedings{infosenselab-trec2024-papers-proc-1,
		title = {Passage Query Methods for Retrieval and Reranking in Conversational Agents},
		author = {Victor De Lima and Grace Hui Yang},
		booktitle = {Proceedings of the 33th Text {REtrieval} Conference (TREC 2024)},
		year = {2024},
		address = {Gaithersburg, Maryland},
		series = {NIST SP 1329}
	}
	```

